#chat program
import socket
from time import sleep
import threading
peer_address = "127.0.0.1"      

class Server(threading.Thread):
    def run(self):
        print("Starting server")
        ip = "127.0.0.1"
        listening_port = 10002
        addr = (ip, listening_port)
        self.listening_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.listening_server.bind(addr)
        self.listening_server.listen(1)
        (listening_socket, sending_addr) = self.listening_server.accept()
        print("Server started")
        print(f"connection established with {sending_addr}")
        while(1):
            chunk = listening_socket.recv(4096).decode()           
            print(f"{addr}>>{chunk}")

class Client(threading.Thread):
    def run(self):
        print("Starting client")
        peer_address = "127.0.0.1"
        sending_port = 10001
        self.sending_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while(1):
            try:
                self.sending_client.connect((peer_address, sending_port))
                print("Connection established")
                break
            except:
                print("Failed. Trying again soon...")
                sleep(1)        
        print("Client Started")
        while(1):
            sending_data = input(">>").encode()
            self.sending_client.sendall(sending_data)
 
 
if __name__ == "__main__":
    srv = Server()
    srv.daemon = True
    srv.start()
    sleep(1)
    cli = Client()
    cli.start()