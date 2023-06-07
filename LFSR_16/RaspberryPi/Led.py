import RPi.GPIO as GPIO
class Led:
    def __init__(self, port):
        self.port=port
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.OUT)
        
    def High(self):
        GPIO.output(self.port, GPIO.HIGH)
     
    def Low(self):
        GPIO.output(self.port, GPIO.LOW)