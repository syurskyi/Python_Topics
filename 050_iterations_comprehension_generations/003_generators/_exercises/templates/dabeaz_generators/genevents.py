# genevents.py
#
# A very simplistic example of generating events on a set of sockets

______ select
___ gen_events(socks):
    while True:
        rdr,wrt,err = select.select(socks,socks,socks,0.1)
        ___ r __ rdr:
            y... "read",r
        ___ w __ wrt:
            y... "write",w
        ___ e __ err:
            y... "error",e

# Example use
# Use telnet to port 12000 to test this

__ __name__ == '__main__':
    ______ socket
    f.. genreceive ______ *

    addr = ("",12000)
    clientset = []
    ___ acceptor(sockset,addr):
        ___ c,a __ receive_connections(addr):
            clientset.append(c)

    ______ threading
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




