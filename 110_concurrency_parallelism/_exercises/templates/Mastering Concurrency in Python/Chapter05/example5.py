# ch05/example5.py

______ th..
______ req..
______ ti..

c_ MyThread(?.T..):
    ___  - (self, url):
        ?.T... - (self)
        self.url _ url
        self.result _ N..

    ___ run(self):
        res _ ?.get(self.url)
        self.result _ f'{self.url}: {res.text}'

urls _ [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
]

start _ t__.t__()

threads _ [MyThread(url) ___ url __ urls]
___ thread __ threads:
    thread.s..
___ thread __ threads:
    thread.j..
___ thread __ threads:
    print(thread.result)

print(f'Took {t__.t__() - start : .2f} seconds')

print('Done.')
