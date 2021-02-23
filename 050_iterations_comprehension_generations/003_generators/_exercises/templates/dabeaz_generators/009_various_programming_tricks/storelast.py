# storelast.py
#
# An iterator that stores the last value returned.  

c_ storelast(object):
    ___ __init__(,source):
        .source = source
    ___ __next__():
        item = .source.__next__()
        .last = item
        r_ item
    ___ __iter__():
        r_

# Example
__ __name__ __ '__main__':
    f.. follow ______ follow
    f.. apachelog ______ apache_log

    lines = storelast(follow(o..("run/foo/access-log")))
    log   = apache_log(lines)

    ___ r __ log:
        print(r)
        print(lines.last)
