# Import libraries
import RPi.GPIO as GPIO
import time
import random
import numpy as np

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(36,GPIO.OUT)
servo1 = GPIO.PWM(36,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty
pre_duty = 2
while True:
    duty = random.randint(2, 12)
    #print("pre_duty",pre_duty)
    #print("duty",duty)
    if(duty < pre_duty):
        for i in np.arange(pre_duty, duty,-0.1):
            print(i)
            servo1.ChangeDutyCycle(i)
            time.sleep(0.02)
            servo1.ChangeDutyCycle(0)
    else:
        for i in np.arange(pre_duty, duty,0.1):
            print(i)
            servo1.ChangeDutyCycle(i)
            time.sleep(0.02)
            servo1.ChangeDutyCycle(0)
    pre_duty = duty
    

# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
#servo1.ChangeDutyCycle(7)
#time.sleep(0.5)
#servo1.ChangeDutyCycle(0)
#time.sleep(1.5)

#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")
