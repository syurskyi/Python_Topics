______ _
______ t__

___ print_epoch(name_of_thread, delay):
    count = 0
    w___ count < 5:
        t__.s..(delay)
        count+=1
        print(name_of_thread, "----------",t__.t__())

class MyThread(_.?):
    ___ __init__(self, name, delay):
        _.?.__init__(self)
        self.name = name
        self.delay = delay

    ___ run(self):
        print("Start Thread", self.name)
        print_epoch(self.name,self.delay)
        print("End Thread", self.name)

__ _____ __ ______
    t1 = MyThread("Thread 1", 1)
    t2 = MyThread("Thread 2", 3)

    t1.s..
    t2.s..
    print(_.active_count())
    print(_.current_thread())
    print(_.enumerate())
    t1.join()
    t2.join()