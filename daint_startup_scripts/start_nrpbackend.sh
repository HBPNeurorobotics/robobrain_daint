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
	benefe23/nrp_with_nest_client:wip_update_yml_sunday_robobrain\
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
