#!/usr/bin/python


##1. Calculate factorial using recursion.
##2. Call factorial function using thread. 


from thread ______ start_new_thread

threadId = 1


___ factorial(n):
   global threadId
   if n < 1:   # base case
       print "@: %d" @ ("Thread", threadId )
       threadId += 1
       r_ 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(s..(n) + '! = ' + s..(returnNumber))
       r_ returnNumber

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

c = raw_input("Waiting for threads to return...\n")
