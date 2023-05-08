from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep

class server_out:
    def __init__(self, port):
        self.port=port
        self.servo = AngularServo(self.port, min_pulse_width=0.0006, max_pulse_width=0.0023)
        self.servo.angle = -90
    
    def GiveOutput(self, arrayofoutput):
        OutputArray = [int(i) for i in arrayofoutput.split(' ')[0]][::-1]
        val = 0
        for i in range(len(OutputArray)):
              val = val + 2**i * OutputArray[i]
        print(self.port,val)
        val = ((val-55)*90.0)/55
        self.servo.angle = val