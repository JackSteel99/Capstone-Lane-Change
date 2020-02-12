import sys
sys.path.insert(0, '../Hardware/')

from line_tracker import isInLane

while True:
    inLane, turnDir = isInLane()
    if(inLane == r):
        pass # turn right
    elif(inLane == l):
        pass # turn left
    else:
        continue

