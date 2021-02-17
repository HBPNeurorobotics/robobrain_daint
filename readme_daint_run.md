# Resources
Jochen documentation:       https://demo.hedgedoc.org/gz8U5lJsSVSAIeufTd5vAA
script christopher:         https://gitlab.humanbrainproject.org/uptona/cscs-nest-nrp/-/blob/master/container_launcher/run_nrp_daint.sh
sarus workflow user guide:  https://sarus.readthedocs.io/en/stable/user/user_guide.html#loading-images-from-tar-archives
another sarus docu:         https://user.cscs.ch/tools/containers/sarus/
SLURM docu:                 https://slurm.schedmd.com/scancel.html
Jochen documentation:       



# Changes to containers
- nrp container:
    - robobrain model:
        - ```docker cp nrp_model/robobrain_mouse_with_joystick/ 6be3b849e160:/home_daint/bbpnrsoa/nrp/src/Models/robobrain_mouse_with_joystick```
	    - ```docker cp nest_client_rest.py 6be3b849e160:/home_daint/bbpnrsoa/.opt/platform_venv/lib/python2.7/site-packages/cscs_nest_nrp/benchmarks/nest_client_rest.py```
    - nest client patch for brain dictionary
        - ```docker cp NestPythonBrainLoader.py 6be3b849e160:/home_daint/bbpnrsoa/nrp/src/CLE/hbp_nrp_cle/hbp_nrp_cle/brainsim/nest_client/NestPythonBrainLoader.py```
        - ```./create_symlinks.sh```
    - .local/etc/nginx/nginx.conf und .local/etc/nginx/conf.d/....conf increased timeouts + same on frontend
    - /etc/nginx/nginx.conf und /etc/nginx/conf.d/....conf increased timeouts + same on frontend
- upload experiment via frontend

# Start screen session
--> necessary to keep the keep the containers and tunneling machine running while ssh connection closes

docu: https://linuxize.com/post/how-to-use-linux-screen/
- screen help: CTRL + A, ?
- create named session
- create windows for every session: CTRL+A, C
- close active window: CTRL+d
- and rename : CTRLL+A SHIFT+A
- resize screen window: CTRL+A, resize
- show screen windows: CTRL+A, "
- split screen horizontally: CTRL+a, S
- split screen vertically: CTRL+a, |
- close actual region: CTRL+a, X
- go to next region: CTRL+a, TAB

# HTOP
Reorganize HTOP: F2



# Start Daint setup
## log in and get new node
```
ssh -A bp000231@ela.cscs.ch
ssh -A daint
```

```
salloc -N1 -C 'mc&startx' -A ich004m --time=10:00:00 --mem=120GB
scontrol show jobid <JOBID> | grep NodeList
```

benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain
christopherbignamini/nrp_with_nest_client:wip_update_yml_sunday    --- outdated
hbpneurorobotics/nrp_with_nest_client:wip_spike_plot_fix            -- newest with spike plot fix

## start nrp backend
```module load sarus 
sarus pull benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain

srun -v --account ich004m -C mc -N1 -n1 /apps/daint/system/opt/sarus/1.1.0/bin/sarus run \
--mount=type=bind,source=/etc/opt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf \
--mount=type=bind,source=/var/run/munge/munge.socket.2,dst=/var/run/munge/munge.socket.2 \
--mount=type=bind,source=/scratch/snx3000/$USER,dst=/scratch/snx3000/$USER \
--mount=type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
--mount=type=bind,source=$HOME,dst=$HOME \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/nginx,dst=/var/log/supervisor/nginx \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/nrp-services_app,dst=/var/log/supervisor/nrp-services_app \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/ros-simulation-factory_app,dst=/var/log/supervisor/ros-simulation-factory_app \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/rosbridge,dst=/var/log/supervisor/rosbridge \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/roscore,dst=/var/log/supervisor/roscore \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/rosvideoserver,dst=/var/log/supervisor/rosvideoserver \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/virtualcoach,dst=/var/log/supervisor/virtualcoach \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/uwsgi,dst=/var/log/supervisor/uwsgi \
--mount=type=bind,source=/scratch/snx3000/$USER/nrp_logs/nginx_home,dst=/home_daint/bbpnrsoa/nginx \
benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain \
bash -c "\
unset LD_PRELOAD; rm /usr/lib/libmpi.so.12; rm /usr/lib/libmpi.so.12.0.2; ln -s /usr/lib/libmpi.so.12.0.5 /usr/lib/libmpi.so.12; \
export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH; \
export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH; \
\
export LC_ALL=C; unset LANGUAGE; \
source /home_daint/bbpnrsoa/nrp/src/user-scripts/nrp_variables; \
\
sed -i 's|<STORAGE_ADDR>|148.187.96.212|' /home_daint/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
sed -i 's|= MPILauncher|= DaintLauncher|' /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
sed -i 's|sys.executable|\\\"/home_daint/bbpnrsoa/.opt/platform_venv/bin/python\\\"|' /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
sed -i 's|$VGLRUN|xvfb-run -a --server-args=\\\"-screen 0 1280x1024x24\\\"|' /home_daint/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
sed -i 's|--pause|--pause --software_only_rendering|' /home_daint/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
grep -n 'URI' /home_daint/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
grep -n 'socket' /home_daint/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
grep -n 'auth' /home_daint/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
grep -n 'socket' /home_daint/bbpnrsoa/.local/etc/nginx/uwsgi-nrp.ini; \
grep -n 'DaintLauncher' /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
which srun; \
cat /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/DaintLauncher.py; \
\
/etc/init.d/supervisor start; \
sleep 50000000; \
ps uxa | grep python; \
netstat -tulpen | grep 8080; \
cat /var/log/supervisor/supervisord.log; \
cat /var/log/supervisor/nrp-services_app/**; \
cat /var/log/supervisor/ros-simulation-factory_app/**;"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## start tunnel
```
ssh -A nidXXX
ssh -i key-tunneluser -o StrictHostKeyChecking=no -R 0.0.0.0:8080:localhost:8080 -R 0.0.0.0:5000:localhost:5000 -TN tunneluser@148.187.97.12
oder tunneluser@148.187.96.206
```

## start nest server
drop your nest brain modules in $HOME and mount them to /opt/data with ln -s
```
ssh -A nidXXX
module load sarus
sarus run --tty --mount=type=bind,source=$HOME,dst=$HOME \
      christopherbignamini/nestsim:benedikt_restricted_python \
      /bin/bash -c \
      "ln -s $HOME/robobrain_nrp/nrp_experiment/robobrain_mouse_exp/resources /opt/data; \
        . /opt/nest/bin/nest_vars.sh; \
        nest-server start -o; \
        bash"
```






## Start frontend
http://148.187.96.212/#/esv-private?dev


## Start Virtual Coach
--- more output logs with Virtual Coach!



# DEBUG

## 
ssh to frontend
```
ssh -i /etc/ansible/keys/test-key.pem centos@148.187.96.212
sudo docker exec -it nrp_frontend bash
``

## Slurm commands
###Show current jobs
```
squeue -u bp000231
```

### list past jobIDs
```
sacct -S year-month-day will print the past job
```
### cancel job
```
scancel jobID
```


## Inspect NRP logs
```
cd /scratch/snx3000/$USER/nrp_logs
```

## get logs from backend
on ela
scp daint:/scratch/snx3000/$USER/nrp_logs . 

## DEBUG nrp backend interactive mode
```
srun -v --account ich004m -C mc -N1 -n1 --pty /apps/daint/system/opt/sarus/1.1.0/bin/sarus run --tty \
--mount=type=bind,source=/var/run/munge/munge.socket.2,dst=/var/run/munge/munge.socket.2 \
--mount=type=bind,source=/scratch/snx3000/$USER,dst=/scratch/snx3000/$USER \
--mount=type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
--mount=type=bind,source=$HOME,dst=$HOME \
benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain \
bash
```

--mount=type=bind,source=/etc/dopt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf \


## start htop container 
```
ssh -A nidXXX
module load sarus
sarus pull benefe23/ubuntu_htop
sarus run --tty benefe23/ubuntu_htop /bin/bash
htop
```

## Debug backend container locally
```
docker run -it benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain bash
```



rm /scratch/snx3000/$USER/nrp_logs/nginx/*
rm /scratch/snx3000/$USER/nrp_logs/nrp-services_app/*
rm /scratch/snx3000/$USER/nrp_logs/ros-simulation-factory_app/*
rm /scratch/snx3000/$USER/nrp_logs/rosbridge/*
rm /scratch/snx3000/$USER/nrp_logs/roscore/*
rm /scratch/snx3000/$USER/nrp_logs/rosvideoserver/*
rm /scratch/snx3000/$USER/nrp_logs/virtualcoach/*





# nginx settings
settings are both in frontend AND backend

/etc/nginx/nginx.conf
    keepalive_timeout 65000000s;
    proxy_connect_timeout       3000000s;
    proxy_send_timeout          3000000s;
    proxy_read_timeout          3000000s;
    send_timeout                3000000s;

    uwsgi_read_timeout 36000000s;
    uwsgi_connect_timeout 3600000s;
    uwsgi_send_timeout 36000000s;
    uwsgi_ignore_client_abort on;
    uwsgi_max_temp_file_size 10000M;
    client_max_body_size 10000M;
    
/.local/etc/nginx/nginx.conf