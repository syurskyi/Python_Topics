____ _ ______ C...


c_ WaitGroup:
    wait_count=0
    cv = C...()

    ___ add(self, count):
        cv.a...
        wait_count += count
        cv.r..

    ___ done
        cv.a...
        __ wait_count > 0:
            wait_count -= 1
        __ wait_count == 0:
            cv.notify_all()
        cv.r..

    ___ wait
        cv.a...
        w... wait_count > 0:
            cv.w..
        cv.r..