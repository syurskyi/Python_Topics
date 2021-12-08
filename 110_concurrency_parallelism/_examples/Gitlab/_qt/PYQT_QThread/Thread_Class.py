import threading
import time

def print_epoch(name_of_thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print(name_of_thread, "----------",time.time())

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Start Thread", self.name)
        print_epoch(self.name,self.delay)
        print("End Thread", self.name)

if __name__ == '__main__':
    t1 = MyThread("Thread 1", 1)
    t2 = MyThread("Thread 2", 3)

    t1.start()
    t2.start()
    print(threading.active_count())
    print(threading.current_thread())
    print(threading.enumerate())
    t1.join()
    t2.join()