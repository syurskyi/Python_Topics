#!/usr/bin/python


## This multithreading program prints output 
## of square and cube of a series of numbers


______ t__
______ _


___ PrintSquare(numbers):
  print("Print squares")
  ___ n __ numbers:
    t__.s..(0.2)
    print("Square", n*n)


___ PrintCube(numbers):
  print("Print cubes")
  ___ n __ numbers:
    t__.s..(0.2)
    print("Cube", n*n*n)


___ Main():
	arr = [2,3,4,5]
	t = t__.t__()
	PrintSquare(arr)
	PrintCube(arr)
	t1=_.?(Target=PrintSquare,  ?_(arr,))
	t2=_.?(Target=PrintCube,  ?_(arr,))
	t1.s..
	t2.s..
	t1.join()
	t2.join()
	print("Program took", t__.t__()-t)


__ _____ __ ______
	Main()


###################################################
###################################################
###################################################


## Above program has been written using multithreading module 
## and the following one has been written __ conventional 
## way where _ module hasnot been used.
## A comparison between the above and folling program 
## would help the readers understand the difference 
## a normal program and a thread program.


# ______ t__


# ___ PrintSquare(num):
#   print("Print squares of the given numbers")
#   ___ n __ numbers:
#     t__.s..(0.2)
#     print("Square", n*n)


# ___ PrintCube(num):
#   print("Print cubes of the given numbers")
#   ___ n __ numbers:
#     t__.s..(0.2)
#     print("Cube", n*n*n)


# arr = [2,3,4,5]
# t = t__.t__()
# PrintSquare(arr)
# PrintCube(arr)
# print("Program took", t__.t__()-t)
