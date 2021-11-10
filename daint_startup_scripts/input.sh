#!/bin/sh
# This script holds functions and procedure to start NRP jobs on PizDaint.
# It is implemented to be submitted via Unicore to start up the NRP and distributed Nest server, and can be executed manually on a node for debugging. For manual execution uncomment the 'set_env_variables' function, you may also want to make use of the debugging functions.

##############################################################################
# LOCAL EXECUTION FUNCTIONS
##############################################################################

#######################################
# Sets the environment variables for debugging on PizDaint only.
# Usually these variables are set by unicore directly
#######################################
function set_env_variables {
/bin/echo -e "\n\n == Setting Environment Variables"

export TUNNEL_HOST=148.187.96.206
export TARGET_PORT=8080
export RUNTIME=5000  # 500 to just start and stop the NRP
}


##############################################################################
# DEBUG FUNCTIONS
##############################################################################

#######################################
# Echoes environment variables set by unicore
# job description to be checked by user
#######################################
function check_env_variables {
/bin/echo -e "\n\n == Checking Environment Variables"

# check runtime
/bin/echo -e "\n - runtime is [/bin/echo Runtime $RUNTIME]"
/bin/echo Runtime $RUNTIME

# check tunnel settings
/bin/echo -e "\n - Tunnel environment variables"
/bin/echo TUNNEL_HOST $TUNNEL_HOST
/bin/echo TARGET_PORT $TARGET_PORT
}


#######################################
# Get current working directory and output file contents
# of relevant directories
#######################################
function check_working_dirs {
/bin/echo -e "\n\n == Check Directories"

# get working directory
/bin/echo -e "\n - Current working directory [pwd]"
pwd

# check working/home/user directories content
/bin/echo -e "\n\n == Directories content"
/bin/echo -e "\n - Available Files in working directory [ls -lah]"
ls -lah
/bin/echo -e "\n - Available Files in home directory [ls -lah $HOME]"
ls -lah $HOME
/bin/echo -e "\n - Available Files in user directory [ls -lah /scratch/snx3000/${USER}]"
ls -lah /scratch/snx3000/${USER}
}



##############################################################################
# WORKSPACE PREPARATION FUNCTIONS
##############################################################################

#######################################
# Export additional environment variables // NOT USED
#######################################
function export_envs {
/bin/echo -e "\n\n == Export Environment Variables"

## export envs
#BFecho "Overriding SLURM_NTASKS=$SLURM_NTASKS with 1"
#BFexport SLURM_NTASKS=1
#BFecho "Overriding SLURM_NPROCS=$SLURM_NPROCS with 1"
#BFexport SLURM_NPROCS=1
}


#######################################
# Loads the sarus module and outputs the available images.
#######################################
function load_sarus {
/bin/echo -e "\n\n == Checking / Loading Sarus images"

# Load sarus module
/bin/echo -e "\n - Load sarus module [module load sarus]"
module load sarus

# Output available sarus images
/bin/echo -e "\n - Sarus available images are [sarus images]"
sarus images
}


#######################################
# Pulls the NRP image using sarus pull.
#######################################
function pull_image_nrp {
/bin/echo -e "\n\n == Pull NRP image"

# Pull image
/bin/echo -e "\n - Sarus pull NRP image [sarus pull hbpneurorobotics/nrp_with_nest_client:wip_spike_plot_fix]"
sarus pull hbpneurorobotics/nrp_with_nest_client:wip_spike_plot_fix

}

#######################################
# Pulls the Nest Server image using sarus pull.
#######################################
function pull_image_nest {
/bin/echo -e "\n\n == Pull Nest Server image"

# ull image
/bin/echo -e "\n - Sarus pull Nest-Server image [sarus pull christopherbignamini/nestsim:benedikt_restricted_python]"
sarus pull christopherbignamini/nestsim:benedikt_restricted_python

}


##############################################################################
# NRP STARTUP FUNCTIONS
##############################################################################

#######################################
# Creates the ssh tunnel to the tunneling machine
#######################################
function create_tunnel {
/bin/echo -e "\n\n == Creating tunnel"

# Instantiate tunnel
# -TNf option sends the ssh process into background, and $! gives a pid that's not the tunnel
# use -v for verbose output below
ssh -i key-tunneluser -o StrictHostKeyChecking=no -R 0.0.0.0:$TARGET_PORT:localhost:8080 -R 0.0.0.0:5000:localhost:5000 -TNf tunneluser@$TUNNEL_HOST
#BF ssh -v -i key-tunneluser -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -R 0.0.0.0:${TARGET_PORT}:localhost:8080 -TN tunneluser@${TUNNEL_HOST} &
tunnelpid=$!	# $! is PID of last job running in background.
retval=$?  	# $? is assigning the status of the last executed command to the RETVAL variable.

# Save results
/bin/echo -e "\n - Tunnelpid [/bin/echo $tunnelpid]"
/bin/echo $tunnelpid

/bin/echo -e "\n ssh tunnel command status [/bin/echo $retval]"
/bin/echo $retval

# Check if tunnel is running
if [ $retval -eq 0 ]; then
echo -e "\n o=====o Tunnel created"
else
echo -e "\n o==/==o Tunnel creation FAILED"
fi
}



#######################################
# Starts the NRP via sarus run
#######################################
function start_nrp {
/bin/echo -e "\n - Sarus run NRP image [sarus run $sarus_command]"

# Start NRP with sarus run
# seds are to be replaced programatically in the backend
# greps can be removed once everything works smoothly
sarus run --mount=type=bind,source=/etc/opt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf \
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
hbpneurorobotics/nrp_with_nest_client:wip_spike_plot_fix \
bash -c "\
unset LD_PRELOAD; rm /usr/lib/libmpi.so.12; rm /usr/lib/libmpi.so.12.0.2; ln -s /usr/lib/libmpi.so.12.0.5 /usr/lib/libmpi.so.12; \
export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH; \
\
export LC_ALL=C;     unset LANGUAGE ; \
\
source /home_daint/bbpnrsoa/nrp/src/user-scripts/nrp_variables; \
sed -i 's|<STORAGE_ADDR>|148.187.96.212|' /home_daint/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
cat /home_daint/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
sed -i 's|= MPILauncher|= DaintLauncher|' /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
sed -i 's|sys.executable|\\\"/home_daint/bbpnrsoa/.opt/platform_venv/bin/python\\\"|' /home_daint/bbpnrsoa/nrp/src/BrainSimulation/hbp_nrp_distributed_nest/hbp_nrp_distributed_nest/launch/NestLauncher.py; \
sed -i 's|$VGLRUN|xvfb-run -a --server-args=\\\"-screen 0 1280x1024x24\\\"|' /home_daint/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
sed -i 's|--pause|--pause --software_only_rendering|' /home_daint/bbpnrsoa/.opt/bbp/nrp-services/gzserver; \
grep -n 'URI' /home_daint/bbpnrsoa/nrp/src/ExDBackend/hbp_nrp_commons/hbp_nrp_commons/workspace/Settings.py; \
grep -n 'socket' /home_daint/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
grep -n 'auth' /home_daint/bbpnrsoa/.local/etc/nginx/conf.d/nrp-services.conf; \
grep -n 'socket' /home_daint/bbpnrsoa/.local/etc/nginx/uwsgi-nrp.ini; \
which srun; \
\
/etc/init.d/supervisor start; \
sleep $(($RUNTIME - 300)); \
ps uxa | grep python; \
netstat -tulpen | grep 8080; \
cat /var/log/supervisor/supervisord.log; \
cat /var/log/supervisor/nrp-services_app/**; \
cat /var/log/supervisor/ros-simulation-factory_app/**;"

# Save output
nrppid=$! # NRP process PID
retval=$? # NRP process status

# Check if NRP is running
if [ $retval -eq 0 ]; then
echo "Supervisor launched"
else
echo "Supervisor launch FAILED"
fi
}


function start_nestserver {
sarus run --mount=type=bind,source=$HOME,dst=$HOME \
christopherbignamini/nestsim:benedikt_restricted_python \
/bin/bash -c \
". /opt/nest/bin/nest_vars.sh; \
nest-server start -o; \
sleep $(($RUNTIME - 300))" &

# Save output
nestpid=$! # nestserver process PID
retval=$? # nestserver process status

# Check if NRP is running
if [ $retval -eq 0 ]; then
echo "NEST Server launched"
else
echo "NEST Server launch FAILED"
fi
}




##############################################################################
# MAIN SCRIPT
##############################################################################

## Welcome
/bin/echo -e "== == == == == == == == == == =="
/bin/echo -e "== Starting NRP Startup Script =="
/bin/echo -e "== == == == == == == == == == =="


## RUN MANUALLY ON A DAINT NODE
# set_env_variables


## DEBUG
check_env_variables
check_working_dirs


## WORKSPACE PREPARATION
# export_envs
load_sarus
# pull_image_nrp
# pull_image_nest


## STARTUP FUNCTIONS
create_tunnel
start_nestserver
start_nrp


## All done
/bin/echo
/bin/echo -e "== == == == == == == == == == =="
/bin/echo -e "== Ending NRP Startup Script =="
/bin/echo -e "== == == == == == == == == == =="
