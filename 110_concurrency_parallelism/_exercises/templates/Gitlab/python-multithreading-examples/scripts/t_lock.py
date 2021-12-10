#!/usr/bin/python


import threading
import time 


tLock = threading.Lock()


def timer(name, delay, repeat):
  print ("Timer: " + name + " Started")
  
  tLock.acquire()
  print name + " has acquired lock"
  while repeat > 0:
    time.sleep(delay)
    print (name + ":" + str(time.ctime(time.time())))
    repeat -= 1
  print name + "is releasing the lock"
  tLock.release()
  print ("Timer: " + name + "Completed")

  
def Main():
  thread1 = threading.Thread(
    target=timer, 
    args=("Timer1", 1, 5)
  )
  thread2 = threading.Thread(
    target=timer, 
    args=("Timer2", 2, 5)
  )
  thread1.start()
  thread2.start()

  print ("Main function completed")


if __name__ == '__main__':
  Main()
