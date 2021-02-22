# genmulti.py
#
# Generate items from multiple generators (multiplex)
#

______ queue, threading
from genqueue ______ genfrom_queue, sendto_queue
from gencat ______ gen_cat

def multiplex(sources):
    in_q = queue.Queue()
    consumers = []
    ___ src __ sources:
        thr = threading.Thread(target=sendto_queue,
                               args=(src, in_q))
        thr.start()
        consumers.append(genfrom_queue(in_q))
    return gen_cat(consumers)

def gen_multiplex(genlist):
    item_q = queue.Queue()
    def run_one(source):
        ___ item __ source:
            item_q.put(item)

    def run_all():
        thrlist = []
        ___ source __ genlist:
            t = threading.Thread(target=run_one, args=(source,))
            t.start()
            thrlist.append(t)
        ___ t __ thrlist:
            t.join()
        item_q.put(StopIteration)

    threading.Thread(target=run_all).start()
    while True:
        item = item_q.get()
        __ item is StopIteration:
            return
        yield item


# Example use
#
# This example requires you to perform these setup steps:
#
# 1.  Go to run/foo and run logsim.py
# 2.  Go to run/bar and run logsim.py
#
# These two steps will start writing two different Apache log files.
# Now, we're going to read from both at the same time.

__ __name__ == '__main__':
    from follow ______ follow
    
    log1 = follow(o..("run/foo/access-log"))
    log2 = follow(o..("run/bar/access-log"))
    
    log = multiplex([log1,log2])
    
    ___ line __ log:
        print(line, end='')
