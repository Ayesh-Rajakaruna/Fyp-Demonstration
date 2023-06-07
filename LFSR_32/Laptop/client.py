import requests
from writefile import WriteFile
from test import Test
from data import Data
import time

class Main:

    def __init__(self):
        self._url_start_transmition = 'http://192.168.100.106:8000/start_transmition'
        self._url_get_line = 'http://192.168.100.106:8000/get_line'
        self._url_ask_input = 'http://192.168.100.106:8000/ask_input'
        self._url_send_data = 'http://192.168.100.106:8000/send_data'

        self.predict = Test()
        self.data = Data()
        self.openfile =  WriteFile()

    def run(self):
        response = requests.get(self._url_start_transmition)
        print(response.text)
        if response.text== "ReadyToTransmit":
            self.openfile.start("Counter")
            accuracy = 0
            while accuracy<self.data.get_accuracy():
                response = requests.post(self._url_get_line)
                print(response.text)
                if response.text == "No element":
                    pass
                else:
                    accuracy = self.openfile.write(response.text)
        self.askInput()
        
    def askInput(self):
        print("Ready to predict")
        self.predict.makeIntialzationList()
        LisOfResult = self.openfile.getListOfInitialization()
        while True:
            response = requests.get(self._url_ask_input)
            predict_result = self.predict.predictresult(response.text.split("\n")[0])
            LisOfResult.append(predict_result)
            ResultOfData = LisOfResult.pop(0)
            ResultofData = LisOfResult[0]
            print(ResultOfData)
            response = requests.post(self._url_send_data, data=ResultOfData)
if __name__ == '__main__':
    Main = Main()
    Main.run()