from threading ______ Condition


class WaitGroup:
    wait_count=0
    cv = Condition()

    ___ add(self, count):
        self.cv.acquire()
        self.wait_count += count
        self.cv.release()

    ___ done(self):
        self.cv.acquire()
        if self.wait_count > 0:
            self.wait_count -= 1
        if self.wait_count == 0:
            self.cv.notify_all()
        self.cv.release()

    ___ wait(self):
        self.cv.acquire()
        while self.wait_count > 0:
            self.cv.wait()
        self.cv.release()