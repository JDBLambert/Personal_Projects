import socket
from time import sleep

print("Starting server")
ip = "127.0.0.1"
listening_port = 10001
addr = (ip, listening_port)
listening_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listening_server.bind(addr)
listening_server.listen(1)
print("done listening")
(listening_socket, sending_addr) = listening_server.accept()
print(f"connection established with {sending_addr}")
#print(sending_addr)
while(1):
    # chunk = listening_socket.recv(4096)            
    # print(f"{addr}{chunk}")
    pass