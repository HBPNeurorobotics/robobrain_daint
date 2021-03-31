import requests
import json
import time
import os
requests.packages.urllib3.disable_warnings()

"""
Helper methods for using UNICORE's REST API

For a full API reference and examples, have a look at
https://sourceforge.net/p/unicore/wiki/REST_API
https://sourceforge.net/p/unicore/wiki/REST_API_Examples
"""

def get_sites():
    """ get info about the known sites in the HPC Platform """
    sites = {}
    sites['JURECA'] = {'name': 'JURECA (JSC)', 'id': 'JURECA',
                       'url': "https://hbp-unic.fz-juelich.de:7112/FZJ_JURECA/rest/core" }
    sites['DAINT-CSCS'] = {'name': 'PIZ DAINT (CSCS)', 'id': 'VIS',
                         'url': "https://unicoregw.cscs.ch:8080/DAINT-CSCS/rest/core" }
    sites['MARE_NOSTRUM'] = {'name': 'Mare Nostrum (BSC)', 'id': 'MN',
                             'url': "https://unicore-hbp.bsc.es:8080/BSC-MareNostrum/rest/core" }
    sites['MARCONI'] = {'name': 'MARCONI (CINECA)', 'id': 'MARCONI',
                      'url': "https://grid.hpc.cineca.it:9111/CINECA-MARCONI/rest/core" }
    return sites


def get_site(name):
    return get_sites().get(name, None)


def get_properties(resource, headers={}):
    """ get JSON properties of a resource """
    my_headers = headers.copy()
    my_headers['Accept']="application/json"
    r = requests.get(resource, headers=my_headers, verify=False)
    if r.status_code!=200:
        raise RuntimeError("Error getting properties: %s" % r.status_code)
    else:
        return r.json()


def get_working_directory(job, headers={}, properties=None):
    """ returns the URL of the working directory resource of a job """
    if properties is None:
        properties = get_properties(job,headers)
    return properties['_links']['workingDirectory']['href']


def invoke_action(resource, action, headers, data={}):
    my_headers = headers.copy()
    my_headers['Content-Type']="application/json"
    my_headers['Accept']="application/json"
    action_url = get_properties(resource, headers)['_links']['action:'+action]['href']
    r = requests.post(action_url,data=json.dumps(data), headers=my_headers, verify=False)
    if r.status_code!=200:
        raise Runtimeinvoke_actionError("Error invoking action: %s" % r.status_code)
    return r.json()


def upload(destination, file_desc, headers):
    my_headers = headers.copy()
    my_headers['Content-Type']="application/octet-stream"
    name = file_desc['To']
    data = file_desc['Data']
    # TODO file_desc could refer to local file
    r = requests.put(destination+"/"+name, data=data, headers=my_headers, verify=False)
    if r.status_code!=204:
        raise RuntimeError("Error uploading data: %s" % r.status_code)


def submit(url, job, headers, inputs=[]):
    """
    Submits a job to the given URL, which can be the ".../jobs" URL
    or a ".../sites/site_name/" URL
    If inputs is not empty, the listed input data files are
    uploaded to the job's working directory, and a "start" command is sent
    to the job.
    """
    my_headers = headers.copy()
    my_headers['Content-Type']="application/json"
    if len(inputs)>0:
        # make sure UNICORE does not start the job
        # before we have uploaded data
        job['haveClientStageIn']='true'

    r = requests.post(url,data=json.dumps(job), headers=my_headers, verify=False)
    if r.status_code!=201:
        raise RuntimeError("Error submitting job: %s" % r.status_code)
    else:
        jobURL = r.headers['Location']

    #  upload input data and explicitely start job
    if len(inputs)>0:
        working_directory = get_working_directory(jobURL, headers)
        for input in inputs:
            upload(working_directory+"/files", input, headers)
        invoke_action(jobURL, "start", headers)

    return jobURL


def is_running(job, headers={}):
    """ check status for a job """
    properties = get_properties(job,headers)
    status = properties['status']
    return ("SUCCESSFUL"!=status) and ("FAILED"!=status)


def wait_for_completion(job, headers={}, refresh_function=None, refresh_interval=360):
    """ wait until job is done
        if refresh_function is not none, it will be called to refresh
        the "Authorization" header
        refresh_interval is in seconds
    """
    sleep_interval = 10
    do_refresh = refresh_function is not None
    # refresh every N iterations
    refresh = int(1 + refresh_interval / sleep_interval)
    count = 0;
    status = get_properties(job,headers)['status']
    print "Status is " + status
    while ("SUCCESSFUL"!=status) and ("FAILED"!=status):
        time.sleep(sleep_interval)
        count += 1
        if do_refresh and count == refresh:
            headers['Authorization'] = refresh_function()
            count=0

        prev_status = status
        status = get_properties(job,headers)['status']
        if prev_status != status:
            print "\nStatus changed to " + status
        else:
            print str(count),



def file_exists(wd, name, headers):
    """ check if a file with the given name exists
        if yes, return its URL
        of no, return None
    """
    files_url = get_properties(wd, headers)['_links']['files']['href']
    children = get_properties(files_url, headers)['children']
    return name in children or "/"+name in children


def get_file_content(file_url, headers, check_size_limit=True, MAX_SIZE=2048000):
    """ download binary file data """
    if check_size_limit:
        size = get_properties(file_url, headers)['size']
        if size>MAX_SIZE:
            raise RuntimeError("File size too large!")
    my_headers = headers.copy()
    my_headers['Accept']="application/octet-stream"
    r = requests.get(file_url, headers=my_headers, verify=False)
    if r.status_code!=200:
        raise RuntimeError("Error getting file data: %s" % r.status_code)
    else:
        return r.content


def list_files(dir_url, auth, path="/"):
    return get_properties(dir_url+"/files"+path, auth)['children']

def setup_job(N, n, alloc_time, props, storage_addr='148.187.97.13', tunnel_address='148.187.97.12'):
    ''' setup the job - please refer to
    http://unicore.eu/documentation/manuals/unicore/files/ucc/ucc-manual.html
    for more options '''
    job = {}

    # we directly use a shell script,
    # often it is better to setup a server-side "Application"
    # for a simulation code and invoke that\
    # set UC_PREFER_INTERACTIVE_EXECUTION to 'true' to run on login-nodes
    job['ApplicationName'] = 'Bash shell'
    job['Parameters'] = {
        'SOURCE' : 'input.sh',
        'UC_PREFER_INTERACTIVE_EXECUTION': 'false'
    }
    # Request resources nodes etc
    # set how long the supervisor processes should stay alive
    ESTIMATED_REQUIRED_SETUP_TIME = 60.0
    reservation = alloc_time * 60.0
    uptime = reservation - ESTIMATED_REQUIRED_SETUP_TIME

    # Resources "NodeConstraints" : "gpu,startx" or "mc",

    job['Resources'] = {
        "NodeConstraints" : "gpu,startx",
        "Nodes" : str(N+1),
        "Queue" : "debug",
        "Runtime" : str(reservation),
    }

    # data stage in
    #job['Imports'] = []

    # data stage out
    #job['Exports'] = []

    # watch out for the single and double quotes combinations during chaining
    # also those semicolons :@

    # sed 212 is for the old daint image
    # sed storage_addr is for the new image
    # sed mpirun is to add -launcher option
    supervisor_command = "unset LD_PRELOAD; rm /usr/lib/libmpi.so.12;  rm /usr/lib/libmpi.so.12.0.2; ln -s /usr/lib/libmpi.so.12.0.5 /usr/lib/libmpi.so.12; \
        export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH; \
        \
        export LC_ALL=C;     unset LANGUAGE ; \
        source /home2/bbpnrsoa/nrp/src/user-scripts/nrp_variables; \
        \
        sed -i 's|<STORAGE_ADDR>|{storage_addr}|' /home2/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
        sed -i 's|= MPILauncher|= DaintLauncher|' /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
        sed -i 's|sys.executable|\\\"/home2/bbpnrsoa/.opt/platform_venv/bin/python\\\"|' /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
        sed -i 's|$VGLRUN|xvfb-run -a --server-args=\\\"-screen 0 1280x1024x24\\\"|' /home2/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
        sed -i 's|--pause|--pause --software_only_rendering|' /home2/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
        grep -n 'URI' /home2/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
        grep -n 'socket' /home2/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
        grep -n 'auth' /home2/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
        grep -n 'socket' /home2/bbpnrsoa/.local/etc/nginx/uwsgi-nrp.ini; \
        grep -n 'DaintLauncher' /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
        cp $HOME/DaintLauncher.py /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/DaintLauncher.py; \
        sed -i 's|-N 2 -n 4|-N {N} -n {n}|' /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/DaintLauncher.py; \
        cat /home2/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/DaintLauncher.py; \
        which srun; \
        \
        /etc/init.d/supervisor start; \
        sleep {t}; \
        ps uxa | grep python; \
        netstat -tulpen | grep 8080; \
        cat /var/log/supervisor/supervisord.log; \
        cat /var/log/supervisor/nrp-services_app/**; \
        cat /var/log/supervisor/ros-simulation-factory_app/**;".format(storage_addr=storage_addr, t=uptime, N=N, n=n)

    sarus_command = '{HACK}sarus run \
        --mount=source=/etc/opt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf,type=bind \
        --mount=source=/var/run/munge/munge.socket.2,dst=/var/run/munge/munge.socket.2,type=bind \
        --mount=source=/scratch/snx3000/$USER,dst=/scratch/snx3000/$USER,type=bind \
        --mount=type=bind,source=$HOME,dst=$HOME     hbpneurorobotics/nrp:daint_update \
        bash -c "{command}"'.format(command=supervisor_command, HACK='/apps/daint/system/opt/sarus/1.0.1/bin/')

    #srun_command = "srun -v -C gpu -N1 -n1 {sarus}".format(sarus=sarus_command)

    tunnel_key = os.path.join("/users/", props['client']['xlogin']['UID'], "key-tunneluser")

    # the 'input.sh' script that will be uploaded
    input_sh_content = """
    #!/bin/bash

    # export envs
    export TARGET_PORT=8080
    export TUNNEL_HOST=%s
    export _XLOGIN_=%s
    echo "overriding SLURM_NTASKS=$SLURM_NTASKS with 1"
    export SLURM_NTASKS=1
    echo "overriding SLURM_NPROCS=$SLURM_NPROCS with 1"
    export SLURM_NPROCS=1

    # checks
    pwd
    ls -lah
    # no access to /users/${_XLOGIN_} ???
    #ls -lah /users/${_XLOGIN_}
    ls -lah /scratch/snx3000/${_XLOGIN_}

    # open a server
    # custom nc doesn't allow listening on ports in daint :-/
    #nc -v -l -k -p 8080 &

    # create the tunnel
    # -TNf option sends the ssh process into background, and $! gives a pid that's not the tunnel
    # with -f and & it's works! Also had to move the key into scratch folder ans /users not available
    ssh -i %s -o StrictHostKeyChecking=no -R 0.0.0.0:${TARGET_PORT}:localhost:8080 -TN tunneluser@${TUNNEL_HOST} &
    tunnelpid=$!
    retval=$?
    if [ $retval -eq 0 ]; then
        echo "Tunnel created o===o"
    else
        echo "Tunnel creation FAILED o=/=o"
    fi

    export DAINT_SHARED_DIRECTORY=/scratch/snx3000/$USER

    # apparently module is bash specific command, needs to be imported manually in unicore
    # this might change. I looked up using 'find'
    ls -lah /opt/cray/pe/modules/3.2.11.1/etc/modules.sh
    . /opt/cray/pe/modules/3.2.10.6/etc/modules.sh

    # load shifter
    #module load shifter-ng
    # run nrp container
    %s

    superpid=$!
    retval=$?
    if [ $retval -eq 0 ]; then
        echo "Supervisor launched"
    else
        echo "Supervisor launch FAILED"
    fi

    # free resources
    kill -9 ${tunnelpid}
    kill -9 ${superpid}
    """ % (tunnel_address, props['client']['xlogin']['UID'], tunnel_key, sarus_command)

    # list of files to be uploaded
    # NOTE files can also be staged-in from remote locations
    # or can be already present on the HPC filesystem

    input_sh = {'To': 'input.sh', 'Data': input_sh_content }
    inputs = [input_sh]
    input_sh_content

    return job, inputs
