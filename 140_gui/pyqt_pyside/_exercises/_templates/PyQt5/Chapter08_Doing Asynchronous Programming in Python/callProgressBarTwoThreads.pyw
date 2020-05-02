_____ ___
_____ threading
_____ time

____ ?.?W.. _____ ?D.., ?A..

____ demoTwoProgressBars _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        s..
       
c_ myThread (threading.Thread
   counter=0
   ___  -  , w, ProgressBar
      threading.Thread. - 
      w=w
      counter=0
      progreassBar=ProgressBar
      
   ___ run 
      print ("Starting " + name+"\n")
      while counter <=100:
          time.sleep(1)
          progreassBar.setValue(counter)
          counter+=10
      print ("Exiting " + name+"\n")

      
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    thread1 = myThread(w, w.ui.progressBarFileDownload)
    thread2 = myThread(w, w.ui.progressBarVirusScan)
    thread1.start()
    thread2.start()
    w.exec()
    thread1.join()
    thread2.join()
    ___.e..(app.exec_())


