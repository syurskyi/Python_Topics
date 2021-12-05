____ _ ______ C..., Value, P..

______ t___


# note this is the equivalent of a waitgroup for a process instead of a thread
c_ WaitGroupProcess:
    ___ __init__(self, cv, wait_count):
        cv = cv
        wait_count = wait_count

    ___ add(self, count):
        cv.a...
        wait_count.value += count
        cv.r..

    ___ done
        cv.a...
        __ wait_count.value > 0:
            wait_count.value -= 1
        __ wait_count.value == 0:
            cv.notify_all()
        cv.r..

    ___ wait
        cv.a...
        w... wait_count.value > 0:
            cv.w..
        cv.r..


___ sleep_and_done(condC, wc, time_to_sleep):
    wg = WaitGroupProcess(condC, wc)
    t___.s..(time_to_sleep)
    wg.done()
    print("Process called done")


__ _____ __ _____
    wait_count = Value('i', 0, lock=False)
    cv = C...()
    wait_group_process = WaitGroupProcess(cv, wait_count)
    wait_group_process.add(3)
    P..(t.._sleep_and_done, a.._(cv, wait_count, 2)).s..
    P..(t.._sleep_and_done, a.._(cv, wait_count, 5)).s..
    P..(t.._sleep_and_done, a.._(cv, wait_count, 7)).s..
    wait_group_process.w..
    print("All processes complete")
