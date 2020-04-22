# ch05/example3.py

______ th..
______ req..
______ ti..

___ ping(url
    res _ ?.get(url)
    print(f'{url}: {res.text}')

urls _ [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524'
]

start _ t__.t__()
___ url __ urls:
    ping(url)
print(f'Sequential: {t__.t__() - start : .2f} seconds')

print()

start _ t__.t__()
threads _    # list
___ url __ urls:
    thread _ ?.T..(target_ping, args_(url,))
    threads.ap..(thread)
    thread.s..
___ thread __ threads:
    thread.j..

print(f'Threading: {t__.t__() - start : .2f} seconds')
