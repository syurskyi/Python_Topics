# udp client
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Test Message', 'unix.sock')
