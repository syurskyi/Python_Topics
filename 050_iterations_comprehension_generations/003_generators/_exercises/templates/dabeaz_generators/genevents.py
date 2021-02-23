# genevents.py
#
# A very simplistic example of generating events on a set of sockets

______ select
___ gen_events(socks):
    w____ T..
        rdr,wrt,err = select.select(socks,socks,socks,0.1)
        ___ r __ rdr:
            y... "read",r
        ___ w __ wrt:
            y... "write",w
        ___ e __ err:
            y... "error",e

# Example use
# Use telnet to port 12000 to test this

__ __name__ __ '__main__':
    ______ s__
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
        __ evt __ 'read':
            data = s.recv(1024)
            __ no. data:
                print("Closing", s)
                s.c..
                clientset.remove(s)
            ____
                print(s,data)




