# storelast.py
#
# An iterator that stores the last value returned.  

class storelast(object):
    def __init__(self,source):
        self.source = source
    def __next__(self):
        item = self.source.__next__()
        self.last = item
        return item
    def __iter__(self):
        return self

# Example
__ __name__ == '__main__':
    from follow import follow
    from apachelog import apache_log

    lines = storelast(follow(o..("run/foo/access-log")))
    log   = apache_log(lines)

    ___ r __ log:
        print(r)
        print(lines.last)
