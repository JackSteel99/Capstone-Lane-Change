import sys
sys.path.insert(0, '../hardware/')

import time                 # TEMP only for demo
t_end = time.time() + 5     # TEMP only for demo

import motor_lib #includes all functions to control the motor
from line_tracker import isInLane


while time.time() < t_end:
    """isInLane(): returns two variables depending on IR sensor readings
    inLane: boolean, True if both sensors are high / False if either are low
    turnDir: l or r chars for which direction the car should turn

    """
    inLane, turnDir = isInLane()
    v = 80 # Percentage of power to motors during normal operation

    if not inLane:
        if turnDir == r:    # turn right
            startFWD(v, v-10)
        elif turnDir == l:  # turn left
            startFWD(v-10, v)
        else:
            startFWD(v, v)
#end while

stopFWD()

GPIO.cleanup()
