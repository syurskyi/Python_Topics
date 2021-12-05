____ _ ______ T.., Lock
______ t___


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
        t___.s..(0.5)

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
        t___.s..(0.5)


mutex1 = Lock()
mutex2 = Lock()
red = T..(t.._red_robot, a.._(mutex1, mutex2))
blue = T..(t.._blue_robot, a.._(mutex1, mutex2))
red.s..
blue.s..



