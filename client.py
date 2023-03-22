# client.py

import socket

HOST = "127.0.0.1"
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # forwarded string : 'computer networks'
    s.sendall('computer networks'.encode())
    data = s.recv(1024)

print("Received from the Server : ",data.decode())
