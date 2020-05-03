_____ ___
_____ th..
_____ t___

____ ?.?W.. _____ ?D.., ?A..

____ demoTwoProgressBarsLocks _____ _

c_ MyForm(?D..
    ___  -
        s__. - 
        ui _ ?
        ?.sU..
        s..
       
c_ myThread (?.T..
   counter_0
   ___  -  , w, ProgressBar
      ?.T... -
      w_w
      counter_0
      progreassBar_ProgressBar
      
   ___ run
      print ("Starting " + name+"\n")
      threadLock.acquire
      w__ counter <_100:
          t___.s..(1)
          progreassBar.sV..(counter)
          counter+_10
      threadLock.release
      print ("Exiting " + name+"\n")

      
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    thread1 _ myThread(w, w.?.progressBarFileDownload)
    thread2 _ myThread(w, w.?.progressBarVirusScan)
    threadLock _ ?.Lock
    threads _ []
    thread1.s..
    thread2.s..
    w.exec
    threads.ap..(thread1)
    threads.ap..(thread2)
    ___ t in threads:
        t.join
    ___.e.. ?.e


