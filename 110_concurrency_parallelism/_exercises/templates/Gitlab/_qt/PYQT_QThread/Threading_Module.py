______ _
______ t__

___ print_epoch(name_of_thread, delay):
    count = 0
    w___ count < 5:
        t__.s..(delay)
        count+=1
        print(name_of_thread, "----------",t__.t__())

___ print_Cube(thread,num):
    print("Cube = {}".format(num*num*num))

___ print_Square(thread, num):
    print("Square = {}".format(num*num))

__ _____ __ ______
    #creating an instance of the ? Class
    #target= the function print_epoch, args = (name_of_thread, delay) [arguments from the print_epoch function]
    t1 = _.? ?_print_epoch,  ?_("Thread 1", 1))
    t2 = _.? ?_print_epoch,  ?_("Thread 2", 2))
    t3 = _.? ?_print_Square,  ?_("Thread 3", 2))
    t4 = _.? ?_print_Cube,  ?_("Thread 4", 2))

    #Initiate the threads
    t1.s..
    t2.s..
    t3.s..
    t4.s..
    #join threads back to main
    t1.j..
    t2.j..
    t3.j..
    t4.j..

    print("All threads Complete")