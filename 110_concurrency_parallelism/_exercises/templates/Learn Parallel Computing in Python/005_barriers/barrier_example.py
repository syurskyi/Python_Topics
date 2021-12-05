______ t___
____ _ ______ Barrier, T..

barrier = Barrier(2)


___ wait_on_barrier(name, time_to_sleep):
    ___ i __ r...(10):
        print(name, "running")
        t___.s..(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.w..
    print(name, "is finished")


red = T..(t.._wait_on_barrier, a.._["red", 4])
blue = T..(t.._wait_on_barrier, a.._["blue", 10])
red.s..
blue.s..
# time.sleep(8)
# print("Aborting barrier")
# barrier.abort()
# barrier.reset()
