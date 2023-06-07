from http.server import BaseHTTPRequestHandler, HTTPServer
from Data_rx import DataRx
from SevenSegment import SevenSegment 
from Led import Led
from multiprocessing import Manager
import threading
import RPi.GPIO as GPIO 

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    manager = Manager()
    List_Data = manager.list() # initialize List_Data as a class attribute
    Stage_Data = manager.list()
    SevenSegment = SevenSegment()
    LedArray = [Led(13),Led(19)]
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
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            inputdata = "1"
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
            MyHTTPRequestHandler.LedArray[0].High()
            MyHTTPRequestHandler.LedArray[1].Low()

        elif self.path == '/send_data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            content_length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(content_length).decode('utf-8').split()
            MyHTTPRequestHandler.SevenSegment.PinAssing(data)
            MyHTTPRequestHandler.LedArray[1].High()
            MyHTTPRequestHandler.LedArray[0].Low()
            
        else:
            self.send_error(404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    t2 = threading.Thread(target=run)
    t2.start()