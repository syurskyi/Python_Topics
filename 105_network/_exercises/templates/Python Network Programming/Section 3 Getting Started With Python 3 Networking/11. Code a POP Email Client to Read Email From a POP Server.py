import poplib
from email.message import EmailMessage

server = "127.0.0.1"
user = "phil"
passwd = "pythoncode"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print (msg.decode())