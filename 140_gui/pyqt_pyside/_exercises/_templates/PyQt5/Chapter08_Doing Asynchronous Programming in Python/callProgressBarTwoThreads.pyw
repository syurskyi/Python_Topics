_____ ___
_____ threading
_____ time

____ ?.?W.. _____ ?D.., ?A..

____ demoTwoProgressBars _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        s..
       
c_ myThread (threading.Thread
   counter_0
   ___  -  , w, ProgressBar
      threading.Thread. - 
      w_w
      counter_0
      progreassBar_ProgressBar
      
   ___ run 
      print ("Starting " + name+"\n")
      while counter <_100:
          time.sleep(1)
          progreassBar.setValue(counter)
          counter+_10
      print ("Exiting " + name+"\n")

      
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    thread1 _ myThread(w, w.ui.progressBarFileDownload)
    thread2 _ myThread(w, w.ui.progressBarVirusScan)
    thread1.start()
    thread2.start()
    w.exec()
    thread1.join()
    thread2.join()
    ___.e..(app.exec_())


