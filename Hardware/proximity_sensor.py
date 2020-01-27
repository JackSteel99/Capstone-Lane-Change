"""
TY01 Proximity Sensor
This script defines the basic functions needed to control the three ultrasonic
sensors used for this project.

The RPi4B uses the HC-SR04 Ultrasonic sensor modules in order to determine the
robot's proximity to other objects in its surroundings. The sensors are
powered by the RPi4B's 5V GPIO pin(s). Make sure to employ a voltage regulator
when RPi4 is recieving input from the sensors, as the GPIO pins can only handle
3.3V, not the 5V the sensors output which will kill the pins/Pi.

When the car is aligned to face forward and observed from the back, sensors on
left, front, and right sides have been referenced as lds, fds, and rds respectively.

Authors: Deshan Silva, Ben Marini, Elias Abatneh, Soheil Vaez
EDP Group: TY01, 2019-2020
EDP FLC: Dr. Truman Yang
"""

import RPi.GPIO as GPIO
import time

'''
How HC-SR04 Ultra Sonic Sensor works:
https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/
https://www.youtube.com/watch?v=xACy8l3LsXI
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pin assignments
fdsTrig = 29
fdsEcho = 31
'''
to be set up after installing HW
ldsTrig =
ldsEcho =
rdsTrig =
rdsEcho = 
'''

GPIO.setup(fdsTrig, GPIO.OUT)
GPIO.setup(fdsEcho, GPIO.IN)
'''
GPIO.setup(ldsTrig, GPIO.OUT)
GPIO.setup(ldsEcho, GPIO.IN)
GPIO.setup(rdsTrig, GPIO.OUT)
GPIO.setup(rdsEcho, GPIO.IN)
'''

#Letting sensors setup  for 50ms per specs
GPIO.output(fdsTrig, 0)
# GPIO.output(ldsTrig, 0)
# GPIO.output(rdsTrig, 0)
time.sleep(0.06)


#Function to get Front Proximity sensor distance data
def fdsDistance():
    #Initial 10us burst
    GPIO.output(fdsTrig, 1)
    time.sleep(0.00001)
    GPIO.output(fdsTrig, 0)
    #Record times to send/recieve sonic pulse
    while GPIO.input(fdsEcho) == 0:
        pass
    fdsStart = time.time()
    while GPIO.input(fdsEcho) == 1:
        pass
    fdsStop = time.time()
    #Calculate distance in cm
    fdsDist = (fdsStop - fdsStart)*17150
    return fdsDist

'''
#Function to get Left Proximity sensor distance data
def ldsDistance():
    #Initial 10us burst
    GPIO.output(ldsTrig, 1)
    time.sleep(0.00001)
    GPIO.output(ldsTrig, 0)
    #Record times to send/recieve sonic pulse
    while GPIO.input(ldsEcho) == 0:
        pass
    ldsStart = time.time()
    while GPIO.input(ldsEcho) == 1:
        pass
    ldsStop = time.time()
    #Calculate distance in cm
    ldsDist = (ldsStop - ldsStart)*17150
    return ldsDist

#Function to get Right Proximity sensor distance data
def rdsDistance():
    #Initial 10us burst
    GPIO.output(rdsTrig, 1)
    time.sleep(0.00001)
    GPIO.output(rdsTrig, 0)
    #Record times to send/recieve sonic pulse
    while GPIO.input(rdsEcho) == 0:
        pass
    rdsStart = time.time()
    while GPIO.input(rdsEcho) == 1:
        pass
    rdsStop = time.time()
    #Calculate distance in cm
    rdsDist = (rdsStop - rdsStart)*17150
    return rdsDist
'''

#Proximity Sensor test
while True:
    distance = fdsDistance()
    print(distance)
    if distance > 30.0:
        print("Safe to lane change")
    else:
        print("Unsafe to lane change")
    time.sleep(0.1)
    
GPIO.cleanup()
