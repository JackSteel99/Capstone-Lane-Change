import sys
sys.path.insert(0, 'hardware/')

import time                 # TEMP only for demo
t_end = time.time() + 10# TEMP only for demo

from motor_lib import Motor #includes all functions to control the motor

motor = Motor()

# mode = 0 : No Movement
# mode = 1 : Backwards
# mode = 2 : Forwards
# mode = 3 : Left
# mode = 4 : Right

v = 90  # Percentage of power to motors during normal operation
motor.startFWD(v,v)

while time.time() < t_end:
    """isInLane(): returns two variables depending on IR sensor readings
    inLane: boolean, True if both sensors are high / False if either are low
    turnDir: l or r chars for which direction the car should turn

    """
    inLane, turnDir = motor.isInLane()
    #time.sleep(.001)

    if not inLane:
        if turnDir == 'r':    # turn right
            print("Turn Right")
            motor.startRT(v, (v-10))

        elif turnDir == 'l':  # turn left
            print("Turn Left")
            motor.startLT((v-10), v)

    else: # Go forward
        print("All Good")
        motor.startFWD(v, v)
#end while

motor.stopFWD()
motor.exit()
