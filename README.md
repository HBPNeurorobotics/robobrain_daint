# robobrain_nrp
This repository contains the NRP experiment to integrate the robobrain in a mouse closed-loop experiment. It consists of the experiment files and the model description. 
A short video demo of the experiment setup is located in the media folder.

To run the experiment:
- create a symbolic link in $HBP/Models to the model\
        ```
        ln -s /ABS_PATH/robobrain_nrp/model/robobrain_mouse_with_joystick  $HBP/Models/robobrain_mouse_with_joystick
        ```
        
- Create symlinks for your NRP models with \
        ```
        $HBP/Models/create-symlinks.sh
        ```
        
- create a symbolic link in your NRP workspace to the experiment\
        ```
        ln -s /ABS_PATH/robobrain_nrp/nrp_experiment/robobrain_mouse_exp $HOME/.opt/nrpStorage/robobrain_mouse_exp
        ```
        
Start the NRP and you will find the experiment in your experiments list with the name "Robobrain Holodeck NRP Experiment"
        
        
