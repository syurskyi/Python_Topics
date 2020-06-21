# example 1 (UDP server socket)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8888))
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
sock.close()
