from std_msgs.msg import Float64

@nrp.MapVariable("muscle_actuation", initial_value=8*[0.], scope=nrp.GLOBAL)
@nrp.MapVariable("muscle_positions", initial_value=None, scope=nrp.GLOBAL)

@nrp.MapRobotPublisher("joystick_forward", Topic("/robobrain_mouse/joystick_helper_joint/cmd_pos", Float64))
@nrp.MapRobotPublisher("joystick_sideways", Topic("/robobrain_mouse/joystick_world_joint/cmd_pos", Float64))


@nrp.Robot2Neuron()
def controller (t,
               muscle_positions, muscle_actuation,
                joystick_forward, joystick_sideways
               ):
    
    #log the first timestep (20ms), each couple of seconds
    if t % 2 < 0.02:
        clientLogger.info('Time: ', t)
        
        
    ## Send actuation values to muscle
    muscle_actuation.value = [0.3, 0.5, 0.4, 0.4, 0.6, 0.2, 0.2, 0.6]
        
        
    ## Add force to joystick
    # forward
    joystick_forward.send_message(1.0)
    
    # sideways
    joystick_sideways.send_message(-1.0)