____ _ ______ Condition


class WaitGroup:
    wait_count=0
    cv = Condition()

    ___ add(self, count):
        self.cv.a...
        self.wait_count += count
        self.cv.r..

    ___ done(self):
        self.cv.a...
        __ self.wait_count > 0:
            self.wait_count -= 1
        __ self.wait_count == 0:
            self.cv.notify_all()
        self.cv.r..

    ___ wait(self):
        self.cv.a...
        w... self.wait_count > 0:
            self.cv.wait()
        self.cv.r..