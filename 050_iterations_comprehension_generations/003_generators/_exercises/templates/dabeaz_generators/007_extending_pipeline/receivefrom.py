# receivefrom.py
#
# Receive objects from a different machine

______ socket
from genpickle ______ gen_unpickle

def receivefrom(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    c, a = s.accept()
    ___ item __ gen_unpickle(c.makefile('rb')):
        yield item
    c.close()

# Example use:
__ __name__ == '__main__':
    ___ r __ receivefrom(("",15000)):
        print(r['host'], r['request'])
