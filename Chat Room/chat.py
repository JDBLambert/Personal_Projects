# github.com/JDBLambert
# 4/16/2021
# chat program
# Not yet fully tested across internet as that requires both parties opening a port.

import socket
import threading
from time import sleep

port = 56789

class Server(threading.Thread):
    def run(self):
        print("Starting server")
        ip = "0.0.0.0"
        addr = (ip, port)
        self.listening_server = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.listening_server.bind(addr)
        self.listening_server.listen(1)
        print("Server started")
        (listening_socket, sending_addr) = self.listening_server.accept()
        print(f"connection established with {sending_addr}")
        while(1):
            chunk = listening_socket.recv(4096).decode()
            print(f"{addr}>>{chunk}")


class Client(threading.Thread):
    def run(self):
        print("Starting client")
        self.sending_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while(1):
            try:
                self.sending_client = socket.create_connection(
                    (peer_address, port))
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
    print("If you don't know your IPv4 address, please go to: www.whatismyip.com")
    peer_address = input("Address shared with you:")
    srv = Server()
    srv.daemon = True
    srv.start()
    sleep(1)
    cli = Client()
    cli.start()
