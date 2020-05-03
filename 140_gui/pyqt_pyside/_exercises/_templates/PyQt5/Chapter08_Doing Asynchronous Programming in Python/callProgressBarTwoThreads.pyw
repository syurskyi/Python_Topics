_____ ___
_____ th..
_____ t___

____ ?.?W.. _____ ?D.., ?A..

____ demoTwoProgressBars _____ _

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
      w__ counter <_100:
          t___.s..(1)
          progreassBar.sV..(counter)
          counter+_10
      print ("Exiting " + name+"\n")

      
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    thread1 _ myThread(w, w.?.progressBarFileDownload)
    thread2 _ myThread(w, w.?.progressBarVirusScan)
    thread1.s..
    thread2.s..
    w.exec
    thread1.join
    thread2.join
    ___.e.. ?.e


