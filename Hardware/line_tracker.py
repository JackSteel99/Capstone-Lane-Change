"""
TY01 Line Tracker
This script defines the basic functions needed to control the two infrared (IR)
sensors used for line tracking of the robot car used for this project.

The two TCRT5000 IR sensors are powered by the 5V supply of the RPi4B, and
the two digital outputs of the sensors  connect as inputs on the RPi4B GPIO as
inputs. Make sure to use a voltage regulator when connecting the outputs to the
Pi as the operating voltage of the TCRT5000 module is 5V, and the Pi can only
handle 3.3V. The 3.3V input of the Pi can also  be used to power the TCRT5000,
but some online sources suggested for best operation use 5V. Finally make sure 
the sensor is <=2.0cm away from the track. The potentiometer at the back of the
controller for each IR sensor is used to tweak the IR receiver sensitivity as it
depends on environmental factors

When the car is aligned to face forward and observed from the back, sensors on
left and right sides have been referenced as is.

Authors: Deshan Silva, Ben Marini, Elias Abatneh, Soheil Vaez
EDP Group: TY01, 2019-2020
EDP FLC: Dr. Truman Yang
"""

import RPi.GPIO as GPIO
import time

'''
How TCRT5000 works IR Sensor module works;
The IR emmitter of the TCRT5000 will continously emit an IR beam. Depending on
the surface in front of it, the IR receiver will either pickup the reflected beam
(white board) or not pick it up if the surface is not reflective (black tape).
The output will then turn HIGH (reflected), or turn LOW (non-refelcted).

To actually code the robot to stay in between the lines, follow this example;
If your robot strays to the left, the right sensor will move over the black line.
Knowing that the right sensor has gone low, means we can move our robot slightly right,
bringing the line back in between the sensors.

https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-use-the-tcrt5000-ir-line-follower-sensor-with-the-raspberry-pi
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pin assignments
leftIR = 
rightIR = 

GPIO.setup(leftIR, GPIO.IN)
GPIO.setup(rightIR, GPIO.IN)

#Check status of left IR sensor
def leftIRstatus():
    return GPIO.input(leftIR)

#Check status of right IR sensor
def rightIRstatus():
    return GPIO.input(rightIR)

#Return if robot is in lane or not and where to turn
def isInLane():
    leftStatus = GPIO.input(leftIR)
    rightStatus = GPIO.input(rightIR)
    inLane = True
    turnDir = n
    if (leftStatus==True) || (rightStatus==True):
        if leftStatus==True:
		inLane = False
		turnDir = r
	elif rightStatus==True:
		inLane = False
		turnDir = l
    return inLane, turnDir

#Test
try:
	while True:
		if not leftIRstatus():
			print("Robot is straying off to the right, move left!")
		elif not rightIRstatus():
			print("Robot is straying off to the left, move right!")
		else:
			print("Following the line!")
		sleep(0.2)
except:
	GPIO.cleanup()
