#! /usr/bin/env python2.7
import rospy
import time
import numpy as np
import manualcontrol

rospy.init_node('muscle_length_sampling', anonymous=False)

muscle_control = manualcontrol.MuscleControl('mouse_and_sled')
muscle_names = muscle_control.get_muscle_names()
try:
  lengths = []
  while not rospy.is_shutdown():
    states = muscle_control.get_muscle_states()
    l = [ m.length for m in states ]
    lengths.append(l)
    time.sleep(0.1)
except KeyboardInterrupt:
  pass
lengths = np.asarray(lengths)
min_lengths = np.amin(lengths, axis = 0)
max_lengths = np.amax(lengths, axis = 0)
print "\nlength_bounds = {"
for name, min, max in zip(muscle_names, min_lengths, max_lengths):
  print "'%s': (%f, %f)," % (name, min ,max)
print "}"