from http.server import BaseHTTPRequestHandler, HTTPServer
from Data_rx import DataRx
from multiprocessing import Manager
import threading

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    manager = Manager()
    List_Data = manager.list() # initialize List_Data as a class attribute
    def do_GET(self):     
        if self.path == '/start_transmition':
            print("Start")
            self.DataGenerator = DataRx()
            print("Make DataRx")
            print("Start")
            t1 = threading.Thread(target=self.DataGenerator.PutData, args=(MyHTTPRequestHandler.List_Data,))
            t1.start()
            print("Stop")
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("ReadyToTransmit".encode()) # Ready to transmit
            print("send result")


        elif self.path == '/ask_input':
            inputdata = input("Prease enter input line: ")
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
                self.wfile.write("No element") 

        elif self.path == '/send_data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            content_length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(content_length).decode('utf-8')
            print(data)
            
        else:
            self.send_error(404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    t2 = threading.Thread(target=run)
    t2.start()