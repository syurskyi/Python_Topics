# msgtest.py
#
# A program that sends a message to the sample server in genmessages.py

______ socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
___ send_msg(msg):
    s.sendto(msg, ("",10000))

send_msg(b"Hello World")

    
