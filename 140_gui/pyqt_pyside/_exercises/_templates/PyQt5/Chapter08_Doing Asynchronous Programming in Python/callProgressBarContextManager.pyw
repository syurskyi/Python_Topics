_____ ___
_____ threading
_____ time

____ ?.?W.. _____ ?D.., ?A..

____ demoTwoProgressBarsContextManager _____ *

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
      with threadLock:
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
    threadLock _ threading.Lock()
    threads _ []
    thread1.start()
    thread2.start()
    w.exec()
    threads.append(thread1)
    threads.append(thread2)
    for t in threads:
        t.join()
    ___.e..(app.exec_())


