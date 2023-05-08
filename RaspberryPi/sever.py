from http.server import BaseHTTPRequestHandler, HTTPServer
from Data_rx import DataRx
from server_out import server_out
from multiprocessing import Manager
import threading
import RPi.GPIO as GPIO 


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    manager = Manager()
    List_Data = manager.list() # initialize List_Data as a class attribute
    Stage_Data = manager.list()
    serverOut = [server_out(25), server_out(8)]
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(20, GPIO.IN)
    # GPIO.setup(16, GPIO.IN)
    # GPIO.setup(16, GPIO.IN)

    Stage_Data.append("Runing")
    def do_GET(self):     
        if self.path == '/start_transmition':
            self.DataGenerator = DataRx()
            t1 = threading.Thread(target=self.DataGenerator.PutData, args=(MyHTTPRequestHandler.List_Data, MyHTTPRequestHandler.Stage_Data,))
            t1.start()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("ReadyToTransmit".encode()) # Ready to transmit

        elif self.path == '/ask_input':
            MyHTTPRequestHandler.Stage_Data[0] = "Stop"
            # inputdata = input("Prease enter input line: ")
            inputdata = ""
            inputdata += str(GPIO.input(16))
            inputdata += str(GPIO.input(20))
            # inputdata += str(GPIO.input(16))
            # inputdata += str(GPIO.input(16))
            # print(inputdata)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(inputdata.encode())

        else:
            self.send_error(404)

    def do_POST(self): 
        if self.path == '/get_line':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            if MyHTTPRequestHandler.List_Data:
                self.wfile.write(MyHTTPRequestHandler.List_Data.pop(0).encode())  # remove and sent the first element of the list
            else:
                self.wfile.write("No element".encode()) 

        elif self.path == '/send_data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            content_length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(content_length).decode('utf-8').split()
            print(data)
            for i,j in zip(data, MyHTTPRequestHandler.serverOut):
                j.GiveOutput(i)
            
        else:
            self.send_error(404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    t2 = threading.Thread(target=run)
    t2.start()