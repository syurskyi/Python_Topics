from queue ______ Queue
from threading ______ Thread

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


q = Queue(maxsize=10)
t1 = Thread(t.._consumer, a.._(q,))
t2 = Thread(t.._producer, a.._(q,))
t1.start()
t2.start()
