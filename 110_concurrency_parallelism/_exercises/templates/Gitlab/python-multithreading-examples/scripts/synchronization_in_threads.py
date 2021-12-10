

______ _
______ t__ 
# global variable x
x = 0
 
___ Tfunc(i,lock):
 lock.a..
 print('from thread %d' @i)
 lock.r..
 
 
 # creating a lock
lock = _.?
 
 # creating threads
t1 = _.? ?_Tfunc,  ?_(1,lock,))
t2 = _.? ?_Tfunc,  ?_(2,lock,))
 
 # start threads
t1.s..
t2.s..
 
 # wait until threads finish their job
t1.j..
t__.s..(5)
t2.j..

