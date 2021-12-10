#!/usr/bin/python


______ _
______ t__ 


tLock = _.?


___ timer(name, delay, repeat):
  print ("Timer: " + name + " Started")
  
  tLock.a..
  print name + " has acquired lock"
  w___ repeat > 0:
    t__.s..(delay)
    print (name + ":" + s..(t__.c..(t__.t__())))
    repeat -= 1
  print name + "is releasing the lock"
  tLock.r..
  print ("Timer: " + name + "Completed")

  
___ Main():
  thread1 = _.?(
    target=timer, 
     ?_("Timer1", 1, 5)
  )
  thread2 = _.?(
    target=timer, 
     ?_("Timer2", 2, 5)
  )
  thread1.s..
  thread2.s..

  print ("Main function completed")


__ _____ __ ______
  Main()
