"""
TY01 Motor Control
This script defines the basic functions needed to control the two  motors
of the robot car used for this project.

The RPi4B sends the control signals to the L298N Motor Driver Controller
and it handles the proper power relaying to the motors. The motor driver is
powered by 4x1.5V AA batteries to supply 4V(6V-2V(L298N drop)) to the motors.

When the car is aligned to face forward and observed from the back, motors on
left and right sides have been referenced as A and B respectively for easier
reference.

Authors: Deshan Silva, Ben Marini, Elias Abatneh, Soheil Vaez
EDP Group: TY01, 2019-2020
EDP FLC: Dr. Truman Yang
"""

import RPi.GPIO as GPIO
import time

'''
How L298N motor driver works;
-H-Bridge (for turning wheels in a certain direction)
--For a motor to drive forward, IN1=LO & IN2=HI
--For a motor to drive bckward, IN1=HI & IN2=LO
--For a left turn, MotA turns FWD and MotB turns BWD
--For a right turn, MotA turns BWD and MotB turns FWD
--Turn degree depends on how long left and right turns are activated for

-PWM (for speed control)
--Using SW PWM with GPIO.PWM for now to save HW PWM pins for sensors that need
HW PWM pins for higher resolution/frequency. Jitter won't be noticeable as the
car will be running ata relatively low speed.

Full info about L298N:
https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
'''

#Pin Assignments
mA1 = 7  #Mot A IN1
mA2 = 11 #Mot A IN2
mB1 = 13 #Mot B IN1
mB2 = 15 #Mot B IN2
mAePin = 16 #Mot A PWM Enable Pin
mBePin = 18 #Mot B PWM Enable Pin
pwmFreq = 100 #PWM Frequency = 80Hz

GPIO.setmode(GPIO.BOARD)
#Motor init
GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mAePin, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.setup(mBePin, GPIO.OUT)

mAspeed = GPIO.PWM(mAePin, pwmFreq) #Mot A speed control variable
mBspeed = GPIO.PWM(mBePin, pwmFreq) #Mot A speed control variable

#Motor control functions
#Start going Forward
def startFWD(LW, RW):
    mAspeed.ChangeDutyCycle(LW)
    mBspeed.ChangeDutyCycle(RW)
    GPIO.output(mA2, True)
    GPIO.output(mB2, True)
    return(1)

#Stop going Forward
def stopFWD():
    GPIO.output(mA2, False)
    GPIO.output(mB2, False)
    return(0)

#Start going Backward
def startBWD(LW, RW):
    mAspeed.ChangeDutyCycle(LW)
    mBspeed.ChangeDutyCycle(RW)
    GPIO.output(mA1, True)
    GPIO.output(mB1, True)
    return(1)

#Stop going Forward
def stopBWD():
    GPIO.output(mA1, False)
    GPIO.output(mB1, False)
    return(0)

#Start Left turn
def startLT(LW, RW):
    mAspeed.ChangeDutyCycle(LW)
    mBspeed.ChangeDutyCycle(RW)
    GPIO.output(mA1, True)
    GPIO.output(mB2, True)
    return(1)

#Stop Left turn
def stopLT():
    GPIO.output(mA1, False)
    GPIO.output(mB2, False)
    return(0)

#Start Right turn
def startRT(LW, RW):
    mAspeed.ChangeDutyCycle(LW)
    mBspeed.ChangeDutyCycle(RW)
    GPIO.output(mA2, True)
    GPIO.output(mB1, True)
    return(1)

#Stop Right turn
def stopRT():
    GPIO.output(mA2, False)
    GPIO.output(mB1, False)
    return(0)

##Disable speed control
#mAspeed.stop()
#mBspeed.stop()
#
#GPIO.cleanup()
