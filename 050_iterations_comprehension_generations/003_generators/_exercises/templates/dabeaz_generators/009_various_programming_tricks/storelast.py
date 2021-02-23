# storelast.py
#
# An iterator that stores the last value returned.  

c_ storelast(object):
    ___ __init__(self,source):
        self.source = source
    ___ __next__(self):
        item = self.source.__next__()
        self.last = item
        r_ item
    ___ __iter__(self):
        r_ self

# Example
__ __name__ __ '__main__':
    f.. follow ______ follow
    f.. apachelog ______ apache_log

    lines = storelast(follow(o..("run/foo/access-log")))
    log   = apache_log(lines)

    ___ r __ log:
        print(r)
        print(lines.last)
