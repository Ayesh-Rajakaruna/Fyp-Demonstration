import RPi.GPIO as GPIO
class SevenSegment:
    def __init__(self):
        self.portList=[12,13] #Add the GPIO 16 Port for this array.
        GPIO.setmode(GPIO.BCM)
        for port in self.portList:
            GPIO.setup(port, GPIO.OUT)
        
    def PinAssing(self, pinsString):
        print(pinsString)
        for i,j in zip(pinsString,self.portList):
            if i == "1":
                GPIO.output(j, GPIO.HIGH)
            else:
                GPIO.output(j, GPIO.LOW)