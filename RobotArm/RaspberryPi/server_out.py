from time import sleep
import RPi.GPIO as GPIO
import numpy as np
class server_out:
    def __init__(self, port, pre_duty):
        self.stageList = {16:True, 20:True, 21:True, 26:True}
        self.port=port
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.OUT)
        self.pwm=GPIO.PWM(self.port, 50)
        self.pwm.start(0)
        GPIO.output(self.port, False)
        self.val_que = [0, 0, 0]
        self.pre_duty = pre_duty
     
    def GiveOutput(self, arrayofoutput):

        OutputArray = [int(i) for i in arrayofoutput.split(' ')[0]][::-1]
        val = 0
        for i in range(len(OutputArray)):
            val = val + 2**i * OutputArray[i]
        self.val_que.pop(0)
        self.val_que.append(val)
        print("val: ",self.val_que[1])
        if(self.val_que[2]-self.val_que[1] != self.val_que[1]-self.val_que[0]):
            duty = 10.5/20*self.val_que[1]
            if (self.val_que[1]-self.val_que[0] == 1):
                for i in np.arange(self.pre_duty, duty,0.1):
                    self.pwm.ChangeDutyCycle(i)
                    sleep(0.02)
                    self.pwm.ChangeDutyCycle(0)
                    #time.sleep(0.07)
            elif (self.val_que[1]-self.val_que[0] == -1):
                for i in np.arange(self.pre_duty, duty,-0.1):
                    self.pwm.ChangeDutyCycle(i)
                    sleep(0.02)
                    self.pwm.ChangeDutyCycle(0)
                    #time.sleep(0.07)
            elif(self.val_que[1]-self.val_que[0] == 0) and self.stageList[self.port]:
                self.stageList[self.port] = False
                print("DDFDDFDFDFDFDFDFDFDFDFDDFDFD")
                print("pre_duty: ", self.pre_duty)
                self.pwm.ChangeDutyCycle(self.pre_duty)
                sleep(0.5)
                self.pwm.ChangeDutyCycle(0)
            self.pre_duty = duty 
    