from _ ______ Condition, Value, P..

______ time


# note this is the equivalent of a waitgroup for a process instead of a thread
class WaitGroupProcess:
    ___ __init__(self, cv, wait_count):
        self.cv = cv
        self.wait_count = wait_count

    ___ add(self, count):
        self.cv.acquire()
        self.wait_count.value += count
        self.cv.release()

    ___ done(self):
        self.cv.acquire()
        if self.wait_count.value > 0:
            self.wait_count.value -= 1
        if self.wait_count.value == 0:
            self.cv.notify_all()
        self.cv.release()

    ___ wait(self):
        self.cv.acquire()
        while self.wait_count.value > 0:
            self.cv.wait()
        self.cv.release()


___ sleep_and_done(condC, wc, time_to_sleep):
    wg = WaitGroupProcess(condC, wc)
    time.sleep(time_to_sleep)
    wg.done()
    print("Process called done")


__ _____ __ _____
    wait_count = Value('i', 0, lock=False)
    cv = Condition()
    wait_group_process = WaitGroupProcess(cv, wait_count)
    wait_group_process.add(3)
    P..(t.._sleep_and_done, a.._(cv, wait_count, 2)).start()
    P..(t.._sleep_and_done, a.._(cv, wait_count, 5)).start()
    P..(t.._sleep_and_done, a.._(cv, wait_count, 7)).start()
    wait_group_process.wait()
    print("All processes complete")
