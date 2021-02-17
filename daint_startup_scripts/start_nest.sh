
module load sarus
sarus run --tty --mount=type=bind,source=$HOME,dst=$HOME \
	christopherbignamini/nestsim:benedikt_restricted_python \
	/bin/bash -c \
		"ln -s $HOME/robobrain_nrp/nrp_experiment/robobrain_mouse_exp/resources /opt/data; \
		. /opt/nest/bin/nest_vars.sh; \
		nest-server start -o; bash"
