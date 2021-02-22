# sendto.py
#
# Send items to a remote machine

______ socket
f.. genpickle ______ gen_pickle

___ sendto(source,addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    ___ pitem __ gen_pickle(source):
        s.sendall(pitem)
    s.close()

# Example use.   This requires you to run receivefrom.py
# in a different process/window

__ __name__ __ '__main__':
    f.. apachelog ______ apache_log
    f.. follow ______ follow

    lines = follow(o..("run/foo/access-log"))
    log = apache_log(lines)
    sendto(log,("",15000))

