#!/usr/bin/python


#Python multithreading example to print current date.
#1. Define a subclass using ? class.
#2. Instantiate the subclass and trigger the thread. 


______ _
______ datetime


class myThread (_.?):
    ___ __init__(self, name, counter):
        _.?.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    ___ run(self):
        print "Starting " + self.name
        print_date(self.name, self.counter)
        print "Exiting " + self.name

___ print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print "%s[%d]: %s" % ( threadName, counter, datefields[0] )


# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)


# Start new Threads
thread1.s..
thread2.s..
thread1.join()
thread2.join()
print "Exiting the Program!!!"
