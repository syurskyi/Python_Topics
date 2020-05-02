_____ ___
_____ threading
_____ time

____ PyQt5.?W.. _____ ?D.., ?A..

____ demoProgressBarThread _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        s..
       
c_ myThread (threading.Thread
   counter=0
   ___  -  , w
      threading.Thread. - 
      w=w
      counter=0
      
   ___ run 
      print ("Starting " + name)
      while counter <=100:
          time.sleep(1)
          w.ui.progressBar.setValue(counter)
          counter+=10
      print ("Exiting " + name)

      
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    thread1 = myThread(w)
    thread1.start()
    w.exec()
    ___.e..(app.exec_())


