____ queue ______ Queue
____ _ ______ T..

______ t___


___ consumer(q):
    while (True):
        txt = q.get()
        print(txt)
        t___.s..(1)


___ producer(q):
    while (True):
        q.put("Hello there")
        print("Message Sent")


q = Queue(maxsize=10)
t1 = T..(t.._consumer, a.._(q,))
t2 = T..(t.._producer, a.._(q,))
t1.s..
t2.s..
