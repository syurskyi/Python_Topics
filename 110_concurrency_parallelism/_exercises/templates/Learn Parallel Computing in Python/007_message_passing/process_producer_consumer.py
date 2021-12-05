from _ ______ P.., Queue

______ time


___ consumer(q):
    while (True):
        txt = q.get()
        print(txt)
        time.sleep(1)


___ producer(q):
    while (True):
        q.put("Hello there")
        print("Message Sent")


__ _____ __ _____
    q = Queue(maxsize=10)
    p1 = P..(t.._consumer, a.._(q,))
    p2 = P..(t.._producer, a.._(q,))
    p1.start()
    p2.start()
