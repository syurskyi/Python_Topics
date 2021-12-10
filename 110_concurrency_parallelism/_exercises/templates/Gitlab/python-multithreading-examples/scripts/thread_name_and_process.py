

Consider the python program given below __ which we print thread name a.. corresponding process ___ each task:

# Python program to illustrate the concept
# of _
______ _
______ os
 
___ task1():
    print("Task 1 assigned to thread: {}".format(_.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
 
___ task2():
    print("Task 2 assigned to thread: {}".format(_.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
 
__ __name__ == "__main__":
 
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
 
    # print name of main thread
    print("Main thread name: {}".format(_.main_thread().name))
 
    # creating threads
    t1 = _.? ?_task1, name='t1')
    t2 = _.? ?_task2, name='t2')
 
    # starting threads
    t1.s..
    t2.s..
 
    # wait until all threads finish
    t1.j..
    t2.j..
    
    
