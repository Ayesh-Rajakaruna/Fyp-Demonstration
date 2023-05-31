from http.server import BaseHTTPRequestHandler, HTTPServer
from Data_rx import DataRx
from server_out import server_out
from Led import Led 
from ReadFile import ReadFile
from multiprocessing import Manager
import threading
import RPi.GPIO as GPIO 
import time

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    manager = Manager()
    List_Data = manager.list() # initialize List_Data as a class attribute
    ReadFile = ReadFile()
    Stage_Data = manager.list()
    serverOut = [server_out(16,2), server_out(20,4.725), server_out(21,3.15), server_out(26,7.35)]
    LedOutput = [Led(13),Led(19)]
    Dataque  = ReadFile.Read()
    DataqueIndex = 0
    lengthofdataque = len(Dataque)
    stage = True
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(17, GPIO.IN) 

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
            while not(GPIO.input(17)):
                pass
            MyHTTPRequestHandler.Stage_Data[0] = "Stop"
            inputdata = MyHTTPRequestHandler.Dataque[MyHTTPRequestHandler.DataqueIndex % MyHTTPRequestHandler.lengthofdataque]
            MyHTTPRequestHandler.DataqueIndex += 1
            print(inputdata)
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
            MyHTTPRequestHandler.LedOutput[0].High()
            MyHTTPRequestHandler.LedOutput[1].Low()

        elif self.path == '/send_data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            content_length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(content_length).decode('utf-8').split()
            #print(data)
            for i,j in zip(data, MyHTTPRequestHandler.serverOut):
                j.GiveOutput(i)
            MyHTTPRequestHandler.LedOutput[1].High()
            MyHTTPRequestHandler.LedOutput[0].Low()
            
        else:
            self.send_error(404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    t2 = threading.Thread(target=run)
    t2.start()