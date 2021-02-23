# netsend.py
#
# Consume items and send them to a remote machine

______ s__, pickle

class NetConsumer(object):
    ___ __init__(self,addr):
        self.s = s__.s__(s__.A_I_, s__.S_S_)
        self.s.c..(addr)
    ___ s..(self,item):
        pitem = pickle.d..(item)
        self.s.sendall(pitem)
    ___ close(self):
        self.s.c..

# Example use.  This requires you to run receivefrom.py first.

__ __name__ __ '__main__':
    f.. broadcast ______ broadcast
    f.. follow ______ follow
    f.. apachelog ______ apache_log

    # A class that sends 404 requests to another host
    class Stat404(NetConsumer):
        ___ s..(self,item):
            __ item['status'] __ 404:
                NetConsumer.s..(self,item)
    
    stat404 = Stat404(("",15000))
    
    lines = follow(o..("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[stat404])


    
    
    
