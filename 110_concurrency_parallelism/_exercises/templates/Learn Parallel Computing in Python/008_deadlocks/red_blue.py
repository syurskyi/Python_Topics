____ _ ______ T.., L...
______ t___


___ red_robot(lock1, lock2):
    w... T..
        print("Red: Acquiring lock 1...")
        lock1.a...
        print("Red: Acquiring lock 2...")
        lock2.a...
        print("Red: Locks acquired...")
        lock1.r..
        lock2.r..
        print("Red: Locks released")
        t___.s..(0.5)

___ blue_robot(lock1, lock2):
    w... T..
        print("Blue: Acquiring lock 2...")
        lock2.a...
        print("Blue: Acquiring lock 1...")
        lock1.a...
        print("Blue: Locks acquired...")
        lock1.r..
        lock2.r..
        print("Blue: Locks released")
        t___.s..(0.5)


mutex1 = L...()
mutex2 = L...()
red = T..(t.._red_robot, a.._(mutex1, mutex2))
blue = T..(t.._blue_robot, a.._(mutex1, mutex2))
red.s..
blue.s..



