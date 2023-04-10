from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    List_Data = []  # initialize List_Data as a class attribute

    def do_GET(self):     
        if self.path == '/start_transmition':
            MyHTTPRequestHandler.List_Data=[]
            try:
                with open('file.txt', 'r') as f:
                    for line in f:
                        line = line.strip()
                        MyHTTPRequestHandler.List_Data.append(line)  # use class attribute
                    f.close()
            except IOError:
                self.send_response(500)
                self.end_headers()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("ReadyToTransmit".encode()) # Ready to transmit
        
        elif self.path == '/ask_input':
            inputdata = input("Prease enter input line: ")
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(inputdata.encode())

        elif self.path == '/send_data':
            self.send_response(200)
            content_length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(content_length).decode('utf-8')
            print(data)

        else:
            self.send_error(404)

        
            

    def do_POST(self): 
        if self.path == '/get_line':
            print(MyHTTPRequestHandler.List_Data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            if MyHTTPRequestHandler.List_Data:
                self.wfile.write(MyHTTPRequestHandler.List_Data[0].encode())  # use class attribute
                MyHTTPRequestHandler.List_Data.pop(0)  # remove the sent element from the list
            else:
                self.wfile.write("Finsh".encode())  # send an empty response if List_Data is empty
        else:
            self.send_error(404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
