_____ _, r__, t__

class Counter(

    ___ __init__(self, start=0
        self.lock = _.Lock()
        self.value = start

    ___ increment(self
        th_name = _.current_thread().n..
        print(f'Th: {th_name} - ждет блокировку')
        self.lock.acquire()
        try:
            print(f'Th: {th_name} - получил блокировку')
            self.value = self.value + 1
        finally:
            self.lock.release()


___ worker(c
    ___ i __ r..(2
        pause = r__.r__()
        th_name = _.current_thread().n..
        print(f'Th: {th_name} - заснул на {pause:0.02f}')
        t__.s..(pause)
        c.increment()
    print(f'Th: {th_name} - сделано.')


counter = Counter()
___ i __ r..(2
    t = _.?(t.. worker, a.. (counter,))
    t.start()

print('Ожидание рабочих потоков')
main_thread = _.main_thread()
___ t __ _.enumerate(
    __ t is n__ main_thread:
        t.j..
print(f'Счетчик: {counter.value}')


# Th: Thread-1 - заснул на 0.34
# Th: Thread-2 - заснул на 0.26
# Ожидание рабочих потоков
# Th: Thread-2 - ждет блокировку
# Th: Thread-2 - получил блокировку
# Th: Thread-2 - заснул на 0.34
# Th: Thread-1 - ждет блокировку
# Th: Thread-1 - получил блокировку
# Th: Thread-1 - заснул на 0.33
# Th: Thread-2 - ждет блокировку
# Th: Thread-2 - получил блокировку
# Th: Thread-2 - сделано.
# Th: Thread-1 - ждет блокировку
# Th: Thread-1 - получил блокировку
# Th: Thread-1 - сделано.
# Счетчик: 4