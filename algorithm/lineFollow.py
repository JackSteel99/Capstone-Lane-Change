import sys
sys.path.insert(0, '../hardware/')

import time                 # TEMP only for demo
t_end = time.time() + 5     # TEMP only for demo

from motor_lib import Motor #includes all functions to control the motor
from line_tracker import isInLane

motor = Motor()

while time.time() < t_end:
    """isInLane(): returns two variables depending on IR sensor readings
    inLane: boolean, True if both sensors are high / False if either are low
    turnDir: l or r chars for which direction the car should turn

    """
    print("running isInLane()")
    inLane, turnDir = isInLane()
    v = 80 # Percentage of power to motors during normal operation

    if not inLane:
        if turnDir == r:    # turn right
            print("Turn Right")
            motor.startFWD(v, v-10)
        elif turnDir == l:  # turn left
            print("Turn Left")
            motor.startFWD(v-10, v)
        else:
            print("All Good")
            motor.startFWD(v, v)
#end while

motor.stopFWD()

mAspeed.stop()
mBspeed.stop()
GPIO.cleanup()
