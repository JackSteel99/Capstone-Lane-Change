"""
Line tracker V2
Consolidated all methods into one. Can be split up after testing and confirming functionality.
For now I'll only be using go FWD, turn Left/Right. Speed control by PWM to be added later.
Author: Deshan
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pin Assignments and variables
mA1 = 7  #Mot A IN1
mA2 = 11 #Mot A IN2
mB1 = 13 #Mot B IN1
mB2 = 15 #Mot B IN2
mAePin = 16 #Mot A PWM Enable Pin
mBePin = 18 #Mot B PWM Enable Pin
pwmFreq = 100 #PWM Frequency = 80Hz
leftIR = 23
rightIR = 24

#Pin setup
GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mAePin, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.setup(mBePin, GPIO.OUT)
GPIO.setup(leftIR, GPIO.IN)
GPIO.setup(rightIR, GPIO.IN)

#For a motor to drive forward, IN1=LO & IN2=HI
#For a motor to drive bckward, IN1=HI & IN2=LO
try:
  while true:
    if rightIR
      print("Car straying left, turning right: Wheel A")
      GPIO.output(mA1, False)
      GPIO.output(mA2, True)
    else
      print("Car straying right, turning left: Wheel A")
      GPIO.output(mA1, True)
      GPIO.output(mA2, False)
    
    if leftIR
      print("Car straying right, turning left: Wheel B")
      GPIO.output(mB1, False)
      GPIO.output(mB2, True)
    else
      print("Car straying left, turning right: Wheel B")
      GPIO.output(mB1, True)
      GPIO.output(mB2, False)
    
    """
    #If above doesn't work, another promising route
    if(leftIR==False and rightIR==False): #both while move forward     
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    elif(leftIR==True and rightIR==False): #turn right  
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    elif(leftIR==False and rightIR==True): #turn left
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,True) #2B-

    else:  #stay still
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-
        IO.output(17,True) #2A+
        IO.output(18,True) #2B-
    """

finally:
  GPIO.cleanup()
