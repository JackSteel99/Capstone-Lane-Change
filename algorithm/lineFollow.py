import sys
sys.path.insert(0, 'hardware/')

import time                 # TEMP only for demo
t_end = time.time() + 10     # TEMP only for demo

from motor_lib import Motor #includes all functions to control the motor

motor = Motor()

#           mode = 0 : No Movement
#           mode = 1 : Backwards
#           mode = 2 : Forwards
#           mode = 3 : Left
#           mode = 4 : Right
mode = 0 # Tracks the current mode of the vehicle (explained above)

v = 40  # Percentage of power to motors during normal operation

while time.time() < t_end:
    """isInLane(): returns two variables depending on IR sensor readings
    inLane: boolean, True if both sensors are high / False if either are low
    turnDir: l or r chars for which direction the car should turn

    """
    inLane, turnDir = motor.isInLane()

    if not inLane:
        if turnDir == 'r' and mode != 4:    # turn right
            print("Turn Right")
            motor.startFWD(v, (v-10))
            mode = 4

        elif turnDir == 'l' and mode != 3:  # turn left
            print("Turn Left")
            motor.startFWD((v-10), v)
            mode = 3

    elif mode != 2: # Go forward
        print("All Good")
        motor.startFWD(v, v)
        mode = 2
#end while

motor.stopFWD()
motor.exit()
