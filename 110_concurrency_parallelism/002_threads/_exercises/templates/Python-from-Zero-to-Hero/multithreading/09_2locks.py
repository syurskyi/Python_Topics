_______ _
_______ t___

a = 5
b = 5

a_lock = _.L..
b_lock = _.L..


___ thread1calc
    g___ a
    g___ b

    print('Thread1 acquiring lock a')
    ?.a..
    t___.s 5

    print('Thread1 acquiring lock b')
    ?.a..
    t___.s(5)

    a += 5
    b += 5

    print('Thread1 releasing both locks')
    a_lock.r..)
    b_lock.r..)


___ thread2calc():
    g___ a
    g___ b

    print('Thread2 acquiring lock b')
    b_lock.a..
    t___.s(5)

    print('Thread2 acquiring lock a')
    a_lock.a..
    t___.s(5)

    a += 10
    b += 10

    print('Thread2 releasing both locks')
    b_lock.r..)
    a_lock.r..)


__ _____ __ _____
    t1 = _.T..(t.._thread1calc)
    t1.s..

    t2 = _.T..(t.._thread2calc)
    t2.s..