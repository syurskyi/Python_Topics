# DEAD LOCK
import threading


def produce():
    print('Set locking')
    with lock:
        with lock:
            print("It's great")
    print('Locking release!')


lock = threading.RLock()

task1 = threading.Thread(target=produce)
task2 = threading.Thread(target=produce)

task1.start()
task2.start()

task1.join()
task2.join()
