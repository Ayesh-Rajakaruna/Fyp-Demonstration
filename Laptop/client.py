import requests
from writefile import WriteFile
from test import Test

class Main:

    def __init__(self):
        self._url_start_transmition = 'http://192.168.8.189:8000/start_transmition'
        self._url_get_line = 'http://192.168.8.189:8000/get_line'
        self._url_ask_input = 'http://192.168.8.189:8000/ask_input'
        self._url_send_data = 'http://192.168.8.189:8000/send_data'

        self.predict = Test()

    def run(self):
        response = requests.get(self._url_start_transmition)
        if response.text== "ReadyToTransmit":
            openfile =  WriteFile()
            openfile.start("Counter")
            count = 0
            while count>1000:
                response = requests.post(self._url_get_line)
                if response.text == "No element":
                    pass
                else:
                    openfile.write(response.text)
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