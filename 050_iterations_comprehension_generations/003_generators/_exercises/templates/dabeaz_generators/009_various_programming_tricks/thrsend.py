# thrsend.py
#
# Send items to consumer threads

______ queue, threading
class ConsumerThread(threading.Thread):
    ___ __init__(self, target):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.in_queue = queue.Queue()
        self.target = target

    ___ s..(self,item):
        self.in_queue.put(item)

    ___ generate(self):
        w____ T..
            item = self.in_queue.get()
            y... item

    ___ run(self):
        self.target(self.generate())

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
    c1.start()
    c2 = ConsumerThread(bytes_transferred)
    c2.start()
    
    lines = follow(o..("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[c1,c2])


