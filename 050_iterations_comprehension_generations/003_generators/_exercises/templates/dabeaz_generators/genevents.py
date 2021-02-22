# genevents.py
#
# A very simplistic example of generating events on a set of sockets

import select
def gen_events(socks):
    while True:
        rdr,wrt,err = select.select(socks,socks,socks,0.1)
        ___ r __ rdr:
            yield "read",r
        ___ w __ wrt:
            yield "write",w
        ___ e __ err:
            yield "error",e

# Example use
# Use telnet to port 12000 to test this

__ __name__ == '__main__':
    import socket
    from genreceive import *

    addr = ("",12000)
    clientset = []
    def acceptor(sockset,addr):
        ___ c,a __ receive_connections(addr):
            clientset.append(c)

    import threading
    acc_thr = threading.Thread(target=acceptor,
                               args = (clientset, addr))
    acc_thr.daemon = True
    acc_thr.start()
    
    ___ evt, s __ gen_events(clientset):
        __ evt == 'read':
            data = s.recv(1024)
            __ not data:
                print("Closing", s)
                s.close()
                clientset.remove(s)
            else:
                print(s,data)




