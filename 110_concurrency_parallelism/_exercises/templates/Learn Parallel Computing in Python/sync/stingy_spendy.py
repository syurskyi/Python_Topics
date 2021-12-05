______ time
from threading ______ Thread, Lock


class StingySpendy:
    money = 100
    mutex = Lock()

    ___ stingy(self):
        ___ i __ r...(1000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy Done")

    ___ spendy(self):
        ___ i __ r...(1000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(t.._ss.stingy, a.._()).start()
Thread(t.._ss.spendy, a.._()).start()
time.sleep(5)
print("Money in the end", ss.money)
