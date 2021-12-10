#Python multithreading example to demonstrate locking.
#1. Define a subclass using ? class.
#2. Instantiate the subclass and trigger the thread. 
#3. Implement locks __ thread's run method. 

______ _
______ datetime

exitFlag = 0

class myThread (_.?):
    ___ __init__(self, name, counter):
        _.?.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    ___ run(self):
        print "Starting " + self.name
        # Acquire lock to synchronize thread
        threadLock.a..
        print_date(self.name, self.counter)
        # Release lock ___ the next thread
        threadLock.r..
        print "Exiting " + self.name

___ print_date(threadName, counter):
    datefields   # list
    today = datetime.date.today()
    datefields.a.. (today)
    print "@[%d]: @" @ ( threadName, counter, datefields[0] )

threadLock = _.?
threads   # list

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.s..
thread2.s..

# Add threads to thread list
threads.a.. (thread1)
threads.a.. (thread2)

# Wait ___ all threads to complete
___ t __ threads:
    t.join()
print "Exiting the Program!!!"
