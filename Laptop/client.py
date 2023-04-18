import requests
from writefile import WriteFile
from test import Test
from data import Data

class Main:

    def __init__(self):
        self._url_start_transmition = 'http://192.168.8.189:8000/start_transmition'
        self._url_get_line = 'http://192.168.8.189:8000/get_line'
        self._url_ask_input = 'http://192.168.8.189:8000/ask_input'
        self._url_send_data = 'http://192.168.8.189:8000/send_data'

        self.predict = Test()
        self.data = Data()

    def run(self):
        response = requests.get(self._url_start_transmition)
        print(response.text)
        if response.text== "ReadyToTransmit":
            openfile =  WriteFile()
            openfile.start("Counter")
            count = 0
            while count<self.data.get_number_of_data_point():
                response = requests.post(self._url_get_line)
                print(response.text)
                if response.text == "No element":
                    pass
                else:
                    count = count + 1
            del openfile
        self.askInput()
    def askInput(self):
        print("Read to predct")
        self.predict.makeIntialzationList()
        while True:
            response = requests.get(self._url_ask_input)
            predict_result = self.predict.predictresult(response.text.split("\n")[-1].strip())
            response = requests.post(self._url_send_data, data=predict_result)

if __name__ == '__main__':
    Main = Main()
    Main.run()