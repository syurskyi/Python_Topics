______ t___
____ _ ______ T.., Lock


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
T..(t.._ss.stingy, a.._()).s..
T..(t.._ss.spendy, a.._()).s..
t___.s..(5)
print("Money in the end", ss.money)
