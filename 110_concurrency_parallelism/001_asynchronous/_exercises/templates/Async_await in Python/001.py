import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("All Threads are queued, let's see when they finish!")

# $ python thread_test.py
# All Threads are queued, let's see when they finish!
# I am Worker 1, I slept for 1 seconds
# I am Worker 3, I slept for 4 seconds
# I am Worker 4, I slept for 5 seconds
# I am Worker 2, I slept for 7 seconds
# I am Worker 0, I slept for 9 seconds

