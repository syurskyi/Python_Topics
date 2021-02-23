# genreceive.py
#
# A generator that yields connections to a TCP socket

______ s__
___ receive_connections(addr):
    s = s__.s__(s__.AF_INET,s__.SOCK_STREAM)
    s.setsockopt(s__.SOL_SOCKET,s__.SO_REUSEADDR,1)
    s.bind(addr)
    s.listen(5)
    w____ T..
        client = s.accept()
        y... client

# Example use

__ __name__ __ '__main__':
    ___ c, a __ receive_connections(("",9000)):
        print("Got connection from", a)
        c.send(b"Hello World\n")
        c.close()

    
