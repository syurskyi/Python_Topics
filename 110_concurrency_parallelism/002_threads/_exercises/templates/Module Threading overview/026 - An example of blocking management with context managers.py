_____ _

___ worker_with(lock
    w__ lock:
        th_name = _.c...n..
        print(f'{th_name}: блокировка ставится через `with`')

___ worker_finally(lock
    lock.acquire()
    try:
        th_name = _.c...n..
        print(f'{th_name}: блокировка ставится явно')
    finally:
        lock.release()


lock = _.Lock()

wh = _.?(t.. worker_with, a.. (lock,))
fin = _.?(t.. worker_finally, a.. (lock,))

wh.s..
fin.s..

# Thread-1: блокировка ставится через `with`
# Thread-2: блокировка ставится явно