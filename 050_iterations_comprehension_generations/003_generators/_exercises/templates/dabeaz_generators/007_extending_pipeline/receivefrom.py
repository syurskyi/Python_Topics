# receivefrom.py
#
# Receive objects from a different machine

______ s__
f.. genpickle ______ gen_unpickle

___ receivefrom(addr):
    s = s__.s__(s__.AF_INET,s__.SOCK_STREAM)
    s.setsockopt(s__.SOL_SOCKET,s__.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    c, a = s.accept()
    ___ item __ gen_unpickle(c.makefile('rb')):
        y... item
    c.close()

# Example use:
__ __name__ __ '__main__':
    ___ r __ receivefrom(("",15000)):
        print(r['host'], r['request'])
