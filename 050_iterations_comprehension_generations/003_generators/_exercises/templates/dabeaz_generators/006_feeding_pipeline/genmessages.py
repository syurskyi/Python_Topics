# genmessages.py
#
# A generator that yields messages on a UDP socket

______ s__
___ receive_messages(addr,maxsize):
    s = s__.s__(s__.AF_INET,s__.SOCK_DGRAM)
    s.bind(addr)
    w____ T..
        msg = s.recvfrom(maxsize)
        y... msg

# Example use
# To send a message to this generator, use the code "msgtest.py"

__ __name__ __ '__main__':
    ___ msg, addr __ receive_messages(("",10000),1024):
        print(msg, "from", addr)


    
