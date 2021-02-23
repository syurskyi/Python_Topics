# genmulti.py
#
# Generate items from multiple generators (multiplex)
#

______ qu___, t___
f.. genqueue ______ genfrom_queue, sendto_queue
f.. gencat ______ gen_cat

___ multiplex(sources):
    in_q = qu___.Queue()
    consumers = []
    ___ src __ sources:
        thr = t___.T...(t.._sendto_queue,
                               args=(src, in_q))
        thr.s..
        consumers.append(genfrom_queue(in_q))
    r_ gen_cat(consumers)

___ gen_multiplex(genlist):
    item_q = qu___.Queue()
    ___ run_one(source):
        ___ item __ source:
            item_q.p..(item)

    ___ run_all():
        thrlist = []
        ___ source __ genlist:
            t = t___.T...(t.._run_one, args=(source,))
            t.s..
            thrlist.append(t)
        ___ t __ thrlist:
            t.join()
        item_q.p..(StopIteration)

    t___.T...(t.._run_all).s..
    w____ T..
        item = item_q.g..
        __ item __ S_I_
            r_
        y... item


# Example use
#
# This example requires you to perform these setup steps:
#
# 1.  Go to run/foo and run logsim.py
# 2.  Go to run/bar and run logsim.py
#
# These two steps will start writing two different Apache log files.
# Now, we're going to read from both at the same time.

__ __name__ __ '__main__':
    f.. follow ______ follow
    
    log1 = follow(o..("run/foo/access-log"))
    log2 = follow(o..("run/bar/access-log"))
    
    log = multiplex([log1,log2])
    
    ___ line __ log:
        print(line, e.._'')
