import sys
sys.path.insert(0, 'hardware/')

import time                 # TEMP only for demo
t_end = time.time() + 10    # TEMP only for demo

import threading
from motor_lib import Motor
motor = Motor()


# GLOBAL VARIABLES
choice = None
wait = None

def changeLane(v, direction):
    if direction == 'right':
        motor.startRT(v, v-10)
        time.wait(0.5)
        motor.startFWD(v, v)
        time.wait(0.3)
        while not motor.getRightIR():   # Wait for the right sensor to see new lane
            pass
        while motor.getRightIR():       # Wait for the right sensor to pass over new lane 
            pass
        return(0)
    elif direction == 'left':
        motor.startLT(v-10, v)
        time.wait(0.5)
        motor.startFWD(v, v)
        time.wait(0.3)
        while not motor.getLeftIR():   # Wait for the left sensor to see new lane
            pass
        while motor.getLeftIR():       # Wait for the left sensor to pass over new lane 
            pass
        return(0)
    else:
        print("Error in lane change direction")
        return(1)
# End changeLane

def lineFollow(v):
    # mode = 0 : No Movement
    # mode = 1 : Backwards
    # mode = 2 : Forwards
    # mode = 3 : Left
    # mode = 4 : Right
    motor.startFWD(v,v)
    mode = 2
    global wait
    """ isInLane():
        returns two variables depending on IR sensor readings
        inLane: boolean, True if both sensors are low and False if either are high
        turnDir: l or r chars for which direction the car should turn
    """
    inLane, turnDir = motor.isInLane()
    while True:
        if not wait:
            if not inLane:
                if turnDir == 'r' and mode != 4:
                    print("Turn Right")
                    mode = motor.startRT(v, (v-10))

                elif turnDir == 'l' and mode != 3:
                    print("Turn Left")
                    mode = motor.startLT((v-10), v)

            elif mode != 2 :
                print("All Good")
                mode = motor.startFWD(v, v)
# End lineFollow
lineFollow_thread = threading.Thread(target=lineFollow, args=(90), daemon=True) # Thread which constantly waits for user input
lineFollow_thread.start()

def askInput():
    global choice
    global wait
    while time.time() < t_end:
        choice = input("test message 1 in askInput")
        if choice == 'l':
            print("choice was left")
            wait = True
            changeLane(90, l)
            wait = False
        elif choice == 'r':
            print("choice was right")
            wait = True
            changeLane(90, r)
            wait = False
        else:
            print("you selected ", choice)
# End askInput

try:
    askInput()
except KeyboardInterrupt:
    print("keyboard interrupt")
except:
    print("Error in program")
finally:
    motor.stopFWD()
    motor.exit()



