______ time
from threading ______ Thread, Condition


class StingySpendy:
    money = 100
    cv = Condition()

    ___ stingy(self):
        ___ i __ r...(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy Done")

    ___ spendy(self):
        ___ i __ r...(500000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            if self.money < 0:
                print("Money in bank", self.money)
            self.cv.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(t.._ss.stingy, a.._()).start()
Thread(t.._ss.spendy, a.._()).start()
time.sleep(5)
print("Money in the end", ss.money)
