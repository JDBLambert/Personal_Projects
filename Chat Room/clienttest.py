import socket
from time import sleep

print("Starting client")
peer_address = "127.0.0.1"
sending_port = 10001
sending_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("client socket init")

while(1):
    try:
        sending_client.connect((peer_address, sending_port))
        print("Connection established")
        break
    except:
        print("Failed. Trying again soon...")
        sleep(1)        
print("Client Started")