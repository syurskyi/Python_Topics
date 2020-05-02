_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoLCD _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        timer = ?C...QTimer
        timer.timeout.c..(showlcd)
        timer.start(1000)
        showlcd()
  
    ___ showlcd
        time = ?C...QTime.currentTime()
        text = time.toString('hh:mm')
        ui.lcdNumber.display(text)
 
__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
