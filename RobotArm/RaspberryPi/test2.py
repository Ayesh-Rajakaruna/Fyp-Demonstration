import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)

delay = 0.1  # Delay in seconds between readings
count = 0
prev_data = ""
while True:
    # Read data from GPIO
    data1 = GPIO.input(2)
    data2 = GPIO.input(3)

    # Process the data or perform any desired operations
    # ...

    # Wait for the specified delay
    time.sleep(delay)
    data = str(data1)+str(data2)
    if data == prev_data:
        count+= 1
    else:
        count = 0
    prev_data = data
    print(count)
