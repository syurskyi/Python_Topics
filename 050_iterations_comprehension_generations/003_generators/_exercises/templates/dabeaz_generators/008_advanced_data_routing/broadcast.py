# broadcast.py
#
# Broadcast a generator source to a collection of consumers

___ broadcast(source, consumers):
    ___ item __ source:
        ___ c __ consumers:
            c.s..(item)


# Example
__ __name__ __ '__main__':

    class Consumer(object):
        ___ s..(self,item):
            print(self, "got", item)

    c1 = Consumer()
    c2 = Consumer()
    c3 = Consumer()

    f.. follow ______ follow
    lines = follow(o..("run/foo/access-log"))
    broadcast(lines,[c1,c2,c3])

