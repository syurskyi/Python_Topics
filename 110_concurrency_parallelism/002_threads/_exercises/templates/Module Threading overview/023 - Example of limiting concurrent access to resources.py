import threading, random, time


class ActivePool:
    """Воображаемый пул соединений"""

    start = time.time()

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')


def worker(sem, pool):
    with sem:
        th_name = threading.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeActive(th_name)
        time.sleep(0.5)
        pool.makeInactive(th_name)


# переменная семафора
sem = threading.Semaphore(2)

# воображаемый пул соединений
pool = ActivePool()
# запускаем потоки
for i in range(4):
    t = threading.Thread(
        target=worker,
        args=(sem, pool),
    )
    t.start()

# Thread-1 ожидает присоединения к пулу
# Время: 0.0 Running: ['Thread-1']
# Thread-2 ожидает присоединения к пулу
# Время: 0.0 Running: ['Thread-1', 'Thread-2']
# Время: 0.501 Running: ['Thread-2']
# Thread-3 ожидает присоединения к пулу
# Время: 0.501 Running: []
# Время: 0.502 Running: ['Thread-3']
# Thread-4 ожидает присоединения к пулу
# Время: 0.502 Running: ['Thread-3', 'Thread-4']
# Время: 1.003 Running: ['Thread-4']
# Время: 1.003 Running: []