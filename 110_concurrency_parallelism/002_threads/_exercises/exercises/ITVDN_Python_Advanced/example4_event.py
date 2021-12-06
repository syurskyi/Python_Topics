import threading
import time


def producer():
    time.sleep(10)
    print('Product found!')
    product.set()
    product.clear()


def consumer():
    print('product wait')
    product.wait()
    print('Product exists!')


product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()
