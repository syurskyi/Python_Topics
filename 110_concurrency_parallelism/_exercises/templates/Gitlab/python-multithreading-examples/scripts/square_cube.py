

# Python program to illustrate the concept
# of _
# importing the _ module
______ _
 
___ print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
 
___ print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
 
__ ____ __ ______:
    # creating thread
    t1 = _.? ?_print_square,  ?_(10,))
    t2 = _.? ?_print_cube,  ?_(10,))
 
    # starting thread 1
    t1.s..
    # starting thread 2
    t2.s..
 
    # wait until thread 1 is completely executed
    t1.j..
    # wait until thread 2 is completely executed
    t2.j..
 
    # both threads completely executed
    print("Done!")
