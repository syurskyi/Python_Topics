______ p_l_
____ email.message ______ EmailMessage

server _ "127.0.0.1"
user _ "phil"
p__swd _ "pythoncode"

server _ p_l_.POP3(server)
server.user(user)
server.p__s_(p__swd)

msgNum _ le.(server.list[1])

___ i __ ra.. msgNum
    ___ msg __ server.retr(i+1)[1]:
        print (msg.d..)