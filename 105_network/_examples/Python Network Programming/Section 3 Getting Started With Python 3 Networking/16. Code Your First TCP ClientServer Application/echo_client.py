import socket

host = '127.0.0.1'
port = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Hello world')
    data = s.recv(1024)

print('Received', repr(data.decode()))