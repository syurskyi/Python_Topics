# thrsend.py
#
# Send items to consumer threads

______ qu___, t___
c_ ConsumerThread(t___.T...):
    ___ __init__(, target):
        t___.T....__init__()
        .setDaemon(True)
        .in_queue = qu___.Q..
        .target = target

    ___ s..(,item):
        .in_queue.p..(item)

    ___ generate():
        w____ T..
            item = .in_queue.g..
            y... item

    ___ run():
        .target(.generate())

# Example Use

__ __name__ __ '__main__':
    f.. follow ______ follow
    f.. apachelog ______ apache_log
    f.. broadcast ______ broadcast
    
    ___ find_404(log):
        r404 = (r ___ r __ log __ r['status'] __ 404)
        ___ r __ r404:
            print(r['status'],r['datetime'],r['request'])

    ___ bytes_transferred(log):
        total = 0
        ___ r __ log:
            total += r['bytes']
            print("Total bytes", total)
            
    c1 = ConsumerThread(find_404)
    c1.s..
    c2 = ConsumerThread(bytes_transferred)
    c2.s..
    
    lines = follow(o..("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[c1,c2])


