____ _ ______ P.., Queue

______ t___


___ consumer(q):
    w... T..
        txt = q.get()
        print(txt)
        t___.s..(1)


___ producer(q):
    w... T..
        q.put("Hello there")
        print("Message Sent")


__ _____ __ _____
    q = Queue(maxsize=10)
    p1 = P..(t.._consumer, a.._(q,))
    p2 = P..(t.._producer, a.._(q,))
    p1.s..
    p2.s..
