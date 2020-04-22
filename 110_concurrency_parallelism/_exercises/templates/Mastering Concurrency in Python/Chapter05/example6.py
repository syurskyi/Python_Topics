# ch05/example6.py

______ th..
______ req..
______ ti..

UPDATE_INTERVAL _ 0.01

c_ MyThread(?.T..):
    ___  - (self, url):
        ?.T... - (self)
        self.url _ url
        self.result _ f'{self.url}: Custom timeout'

    ___ run(self):
        res _ ?.get(self.url)
        self.result _ f'{self.url}: {res.text}'

___ process_requests(threads, timeout_5):
    ___ alive_count():
        alive _ [1 __ thread.isAlive() else 0 ___ thread __ threads]
        r_ su.(alive)

    w__ alive_count() > 0 and timeout > 0:
        timeout -_ UPDATE_INTERVAL
        t__.s..(UPDATE_INTERVAL)
    ___ thread __ threads:
        print(thread.result)

urls _ [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=4000',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
]

start _ t__.t__()

threads _ [MyThread(url) ___ url __ urls]
___ thread __ threads:
    thread.setDaemon(T..)
    thread.s..
process_requests(threads)

print(f'Took {t__.t__() - start : .2f} seconds')

print('Done.')
