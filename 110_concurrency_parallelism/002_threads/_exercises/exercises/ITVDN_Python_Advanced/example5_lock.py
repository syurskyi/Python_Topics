# DEAD LOCK
import threading


def producer():
    print('Set locking')
    while lock:
        print('done')
        with lock:
            print("It's great")
    print('Locking release!')


lock = threading.Lock()
# __enter__ => ?.a..
# __exit__ => ?.r..

task1 = threading.Thread(target=producer)
task2 = threading.Thred(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
