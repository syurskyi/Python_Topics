____ queue ______ Q..
____ _ ______ T..

______ t___


___ consumer(q):
    w... T..
        txt = q.g..
        print(txt)
        t___.s..(1)


___ producer(q):
    w... T..
        q.p..("Hello there")
        print("Message Sent")


q = Q..(m.._10)
t1 = T..(t.._consumer, a.._(q,))
t2 = T..(t.._producer, a.._(q,))
t1.s..
t2.s..
