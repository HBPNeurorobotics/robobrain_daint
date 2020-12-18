## Changes to containers
- nrp container:
	- docker cp nest_client_rest.py 6be3b849e160:/home_daint/bbpnrsoa/.opt/platform_venv/lib/python2.7/site-packages/cscs_nest_nrp/benchmarks/nest_clien_rest.py
    - docker cp robobrain_mouse_with_joystick/ 6be3b849e160:/home_daint/bbpnrsoa/nrp/src/Models/robobrain_mouse_with_joystick
    - ./create_symlinks.sh


ssh -A bp000231@ela.cscs.ch
ssh -A daint


salloc -N1 -C 'mc&startx' -A ich004m --time=02:00:00 --mem=120GB
scontrol show jobid <JOBID> | grep NodeList


benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain
christopherbignamini/nrp_with_nest_client:wip_update_yml_sunday


## start nrp backend
module load sarus 
sarus pull christopherbignamini/nrp_with_nest_client:wip_update_yml_sunday
srun -v --account ich004m -C mc -N1 -n1 /apps/daint/system/opt/sarus/1.1.0/bin/sarus run \
--mount=type=bind,source=/etc/opt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf \
--mount=type=bind,source=/var/run/munge/munge.socket.2,dst=/var/run/munge/munge.socket.2 \
--mount=type=bind,source=/scratch/snx3000/$USER,dst=/scratch/snx3000/$USER \
--mount=type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
--mount=type=bind,source=$HOME,dst=$HOME \
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
sleep 1800; \
ps uxa | grep python; \
netstat -tulpen | grep 8080; \
cat /var/log/supervisor/supervisord.log; \
cat /var/log/supervisor/nrp-services_app/**; \
cat /var/log/supervisor/ros-simulation-factory_app/**;"



## start nest server
ssh -A nidXXX
module load sarus
sarus pull christopherbignamini/nestsim:benedikt_restricted_python
sarus run --tty --mount=type=bind,source=$HOME,dst=$HOME \
      christopherbignamini/nestsim:benedikt_restricted_python \
      /bin/bash
ln -s $HOME/robobrain_nrp/nrp_experiment/robobrain_mouse_exp/resources /opt/data
. /opt/nest/bin/nest_vars.sh
nest-server start -o





## start tunnel
ssh -A nidXXX
ssh -i key-tunneluser -o StrictHostKeyChecking=no -R 0.0.0.0:8080:localhost:8080 -R 0.0.0.0:5000:localhost:5000 -TN tunneluser@148.187.97.12
oder tunneluser@148.187.96.206

## DEBUG nrp backend interactive mode
srun -v --account ich004m -C mc -N1 -n1 --pty /apps/daint/system/opt/sarus/1.1.0/bin/sarus run --tty \
--mount=type=bind,source=/etc/opt/slurm/slurm.conf,dst=/usr/local/etc/slurm.conf \
--mount=type=bind,source=/var/run/munge/munge.socket.2,dst=/var/run/munge/munge.socket.2 \
--mount=type=bind,source=/scratch/snx3000/$USER,dst=/scratch/snx3000/$USER \
--mount=type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
--mount=type=bind,source=$HOME,dst=$HOME \
benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain \
bash


## Debug backend container locally
docker run -it --entrypoint /bin/bash benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain 


## Start frontend
http://148.187.96.212/#/esv-private?dev

--- more output logs with Virtual Coach!