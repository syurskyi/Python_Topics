_____ _, r__, t__


class ActivePool:
    """Воображаемый пул соединений"""

    start = t__.t__()

    ___ __init__(self
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = _.Lock()

    ___ makeActive(self, name
        with self.lock:
            self.active.append(name)
            tm = t__.t__() - self.start
            print(f'Время: {r..(tm, 3)} Running: {self.active}')

    ___ makeInactive(self, name
        with self.lock:
            self.active.remove(name)
            tm = t__.t__() - self.start
            print(f'Время: {r..(tm, 3)} Running: {self.active}')


___ worker(sem, pool
    with sem:
        th_name = _.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeActive(th_name)
        t__.s..(0.5)
        pool.makeInactive(th_name)


# переменная семафора
sem = _.Semaphore(2)

# воображаемый пул соединений
pool = ActivePool()
# запускаем потоки
___ i __ r..(4
    t = _.?(
        t.. worker,
        a.. (sem, pool),
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