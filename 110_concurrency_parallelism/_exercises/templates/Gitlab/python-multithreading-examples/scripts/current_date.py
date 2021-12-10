#!/usr/bin/python


#Python multithreading example to print current date.
#1. Define a subclass using ? class.
#2. Instantiate the subclass and trigger the thread. 


______ _
______ datetime


c_ myThread (_.?):
    ___ -  name, counter):
        _.?.- (self)
        threadID = counter
        name = name
        counter = counter

    ___ run
        print "Starting " + name
        print_date(name, counter)
        print "Exiting " + name

___ print_date(threadName, counter):
    datefields   # list
    today = datetime.date.today()
    datefields.a.. (today)
    print "@[%d]: @" @ ( threadName, counter, datefields[0] )


# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)


# Start new Threads
thread1.s..
thread2.s..
thread1.j..
thread2.j..
print "Exiting the Program!!!"
