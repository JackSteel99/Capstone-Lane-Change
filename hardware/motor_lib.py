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
class Motor:

    def __init__(self):
    #Motor Init
        #Pin Assignments
        self.mA1 = 33  #Mot A IN1
        self.mA2 = 35 #Mot A IN2
        self.mB1 = 37 #Mot B IN1
        self.mB2 = 36 #Mot B IN2
        self.mAePin = 38 #Mot A PWM Enable Pin
        self.mBePin = 40 #Mot B PWM Enable Pin
        self.pwmFreq = 100 #PWM Frequency = 80Hz
        GPIO.setmode(GPIO.BOARD)
        #Motor init
        GPIO.setup(self.mA1, GPIO.OUT)
        GPIO.setup(self.mA2, GPIO.OUT)
        GPIO.setup(self.mAePin, GPIO.OUT)
        GPIO.setup(self.mB1, GPIO.OUT)
        GPIO.setup(self.mB2, GPIO.OUT)
        GPIO.setup(self.mBePin, GPIO.OUT)
        self.mAspeed = GPIO.PWM(self.mAePin, self.pwmFreq) #Mot A speed control variable
        self.mBspeed = GPIO.PWM(self.mBePin, self.pwmFreq) #Mot A speed control variable
        self.mAspeed.start(0)
        self.mBspeed.start(0)

    #Line Tracker Init
        #Pin assignments
        self.leftIR = 23
        self.rightIR = 24
        GPIO.setup(self.leftIR, GPIO.IN)
        GPIO.setup(self.rightIR, GPIO.IN)

    """ Motor control functions
    #       Functions that control the direction each motor is turning, speed is determened by the
    #       parameters given to them.

    """
    #Start going Forward
    def startFWD(self, LW, RW):
        GPIO.output(self.mA1, False)
        GPIO.output(self.mB1, False)
        self.mAspeed.ChangeDutyCycle(LW)
        self.mBspeed.ChangeDutyCycle(RW)
        GPIO.output(self.mA2, True)
        GPIO.output(self.mB2, True)
        return(2);

    #Stop going Forward
    def stopFWD(self):
        GPIO.output(self.mA2, False)
        GPIO.output(self.mB2, False)
        return(0)

    #Start going Backward
    def startBWD(self, LW, RW):
        self.mAspeed.ChangeDutyCycle(LW)
        self.mBspeed.ChangeDutyCycle(RW)
        GPIO.output(self.mA1, True)
        GPIO.output(self.mB1, True)
        return(1)

    #Stop going Forward
    def stopBWD(self):
        GPIO.output(self.mA1, False)
        GPIO.output(self.mB1, False)
        return(0)

    #Start Left turn
    def startLT(self, LW, RW):
        GPIO.output(self.mA2, False)
        GPIO.output(self.mB1, False)
        self.mAspeed.ChangeDutyCycle(LW)
        self.mBspeed.ChangeDutyCycle(RW)
        GPIO.output(self.mA1, True)
        GPIO.output(self.mB2, True)
        return(3)

    #Stop Left turn
    def stopLT(self):
        GPIO.output(self.mA1, False)
        GPIO.output(self.mB2, False)
        return(0)

    #Start Right turn
    def startRT(self, LW, RW):
        GPIO.output(self.mA1, False)
        GPIO.output(self.mB2, False)
        self.mAspeed.ChangeDutyCycle(LW)
        self.mBspeed.ChangeDutyCycle(RW)
        GPIO.output(self.mA2, True)
        GPIO.output(self.mB1, True)
        return(4)

    #Stop Right turn
    def stopRT(self):
        GPIO.output(self.mA2, False)
        GPIO.output(self.mB1, False)
        return(0)

    #Return if robot is in lane or not and where to turn
    def isInLane(self):
        leftStatus = GPIO.input(self.leftIR)
        rightStatus = GPIO.input(self.rightIR)
        inLane = True
        turnDir = 'n'
        #print(leftStatus, rightStatus) # For debugging
        if (leftStatus==True) or (rightStatus==True):
            if leftStatus==True:
                inLane = False
                turnDir = 'r'
            elif rightStatus==True:
                inLane = False
                turnDir = 'l'
        return inLane, turnDir


    def exit(self):
        self.mAspeed.stop()
        self.mBspeed.stop()
        GPIO.cleanup()
        return(0)

