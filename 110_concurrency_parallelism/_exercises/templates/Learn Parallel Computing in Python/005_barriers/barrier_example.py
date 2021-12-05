______ time
from threading ______ Barrier, Thread

barrier = Barrier(2)


___ wait_on_barrier(name, time_to_sleep):
    ___ i __ r...(10):
        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.wait()
    print(name, "is finished")


red = Thread(t.._wait_on_barrier, a.._["red", 4])
blue = Thread(t.._wait_on_barrier, a.._["blue", 10])
red.start()
blue.start()
# time.sleep(8)
# print("Aborting barrier")
# barrier.abort()
# barrier.reset()
