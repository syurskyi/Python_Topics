# sendto.py
#
# Send items to a remote machine

______ socket
from genpickle ______ gen_pickle

def sendto(source,addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    ___ pitem __ gen_pickle(source):
        s.sendall(pitem)
    s.close()

# Example use.   This requires you to run receivefrom.py
# in a different process/window

__ __name__ == '__main__':
    from apachelog ______ apache_log
    from follow ______ follow

    lines = follow(o..("run/foo/access-log"))
    log = apache_log(lines)
    sendto(log,("",15000))

