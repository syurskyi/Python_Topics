import threading

def worker_with(lock):
    with lock:
        th_name = threading.current_thread().name
        print(f'{th_name}: блокировка ставится через `with`')

def worker_finally(lock):
    lock.acquire()
    try:
        th_name = threading.current_thread().name
        print(f'{th_name}: блокировка ставится явно')
    finally:
        lock.release()


lock = threading.Lock()

wh = threading.Thread(target=worker_with, args=(lock,))
fin = threading.Thread(target=worker_finally, args=(lock,))

wh.start()
fin.start()

# Thread-1: блокировка ставится через `with`
# Thread-2: блокировка ставится явно