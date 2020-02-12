import sys
sys.path.insert(0, '../hardware/')

from line_tracker import isInLane

while True:
    """isInLane(): returns two variables depending on IR sensor readings
    inLane: boolean, True if both sensors are high / False if either are low
    turnDir: l or r chars for which direction the car should turn

    """
    inLane, turnDir = isInLane()

    if(turnDir == r):
        pass # turn right
    elif(turnDir == l):
        pass # turn left
    else:
        continue

