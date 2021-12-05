from threading ______ Thread, Lock
______ time


___ red_robot(lock1, lock2):
    while True:
        print("Red: Acquiring lock 1...")
        lock1.acquire()
        print("Red: Acquiring lock 2...")
        lock2.acquire()
        print("Red: Locks acquired...")
        lock1.release()
        lock2.release()
        print("Red: Locks released")
        time.sleep(0.5)

___ blue_robot(lock1, lock2):
    while True:
        print("Blue: Acquiring lock 2...")
        lock2.acquire()
        print("Blue: Acquiring lock 1...")
        lock1.acquire()
        print("Blue: Locks acquired...")
        lock1.release()
        lock2.release()
        print("Blue: Locks released")
        time.sleep(0.5)


mutex1 = Lock()
mutex2 = Lock()
red = Thread(t.._red_robot, a.._(mutex1, mutex2))
blue = Thread(t.._blue_robot, a.._(mutex1, mutex2))
red.start()
blue.start()



