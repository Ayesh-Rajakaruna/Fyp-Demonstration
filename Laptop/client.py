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
        if response.text == "ReadyToTransmit":
            openfile =  WriteFile()
            openfile.start("Counter")
            while True:
                response = requests.post(self._url_get_line)
                if response.text == "Finsh":
                    self.askInput()
                else:
                    openfile.write(response.text,self.Instanses)
            del openfile
    def askInput(self):
        while True:
            response = requests.get(self._url_ask_input)
            predict_result = self.predict.predictresult(self.predict, response.text.strip())
            response = requests.post(self._url_send_data, data=predict_result.strip())


                
if __name__ == '__main__':
    Main = Main()
    Main.run()


