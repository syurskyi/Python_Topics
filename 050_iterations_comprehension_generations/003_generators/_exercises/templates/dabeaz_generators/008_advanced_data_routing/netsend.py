# netsend.py
#
# Consume items and send them to a remote machine

______ socket, pickle

class NetConsumer(object):
    ___ __init__(self,addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(addr)
    ___ send(self,item):
        pitem = pickle.dumps(item)
        self.s.sendall(pitem)
    ___ close(self):
        self.s.close()

# Example use.  This requires you to run receivefrom.py first.

__ __name__ == '__main__':
    f.. broadcast ______ broadcast
    f.. follow ______ follow
    f.. apachelog ______ apache_log

    # A class that sends 404 requests to another host
    class Stat404(NetConsumer):
        ___ send(self,item):
            __ item['status'] == 404:
                NetConsumer.send(self,item)
    
    stat404 = Stat404(("",15000))
    
    lines = follow(o..("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[stat404])


    
    
    
