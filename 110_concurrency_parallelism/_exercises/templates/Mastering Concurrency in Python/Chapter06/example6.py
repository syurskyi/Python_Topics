# ch6/example6.py

______ m..

c_ MyWorker():
    ___  - (self, x):
        self.x _ x

    ___ process(self):
        pname _ ?.current_process().name
        print('Starting process %s for number %i...' % (pname, self.x))

___ work(q):
    worker _ q.g..
    worker.process()

__ _______ __ _______
    my_queue _ ?.Queue()

    p _ ?.P..(target_work, args_(my_queue,))
    p.s..

    my_queue.put(MyWorker(10))

    my_queue.close()
    my_queue.join_thread()
    p.j..

    print('Done.')
