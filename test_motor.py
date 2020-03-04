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
mA1 = 33  #Mot A IN1
mA2 = 35 #Mot A IN2
mB1 = 37 #Mot B IN1
mB2 = 36 #Mot B IN2
mAePin = 38 #Mot A PWM Enable Pin
mBePin = 40 #Mot B PWM Enable Pin
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
def startFWD():
    GPIO.output(mA2, True)
    GPIO.output(mB2, True)
    return;

#Stop going Forward
def stopFWD():
    GPIO.output(mA2, False)
    GPIO.output(mB2, False)
    return;

#Start going Backward
def startBWD():
    GPIO.output(mA1, True)
    GPIO.output(mB1, True)
    return;

#Stop going Forward
def stopBWD():
    GPIO.output(mA1, False)
    GPIO.output(mB1, False)
    return;

#Start Left turn
def startLT():
    GPIO.output(mA1, True)
    GPIO.output(mB2, True)
    return;

#Stop Left turn
def stopLT():
    GPIO.output(mA1, False)
    GPIO.output(mB2, False)
    return;

#Start Right turn
def startRT():
    GPIO.output(mA2, True)
    GPIO.output(mB1, True)
    return;

#Stop Right turn
def stopRT():
    GPIO.output(mA2, False)
    GPIO.output(mB1, False)
    return;


#Test (Comment out lines 89-135 when importing to another .py)
mAspeed.start(0)#Enable speed control and set speed to 0
mBspeed.start(0)#-----------------''--------------------
#Forward at 90% speed
mAspeed.ChangeDutyCycle(40)
mBspeed.ChangeDutyCycle(40)
startFWD()
time.sleep(2)
stopFWD()
time.sleep(1)
#Backward at 45% speed
mAspeed.ChangeDutyCycle(45)
mBspeed.ChangeDutyCycle(45)
startBWD()
time.sleep(2)
stopBWD()
time.sleep(1)
#Sharp turns at 90% speed
mAspeed.ChangeDutyCycle(45)
mBspeed.ChangeDutyCycle(45)
startLT()
time.sleep(1)
stopLT()
time.sleep(1)
startRT()
time.sleep(1)
stopRT()
time.sleep(1)
#Wide right turn going FWD(MotA @ 80%, MotB @ 40%)
mAspeed.ChangeDutyCycle(90)
mBspeed.ChangeDutyCycle(40)
startFWD()
time.sleep(1)
stopFWD()
time.sleep(1)
#FWD at 70% speed
mAspeed.ChangeDutyCycle(100)
mBspeed.ChangeDutyCycle(100)
startFWD()
time.sleep(5)
stopFWD()
#Disable speed control
mAspeed.stop()
mBspeed.stop()

GPIO.cleanup()
