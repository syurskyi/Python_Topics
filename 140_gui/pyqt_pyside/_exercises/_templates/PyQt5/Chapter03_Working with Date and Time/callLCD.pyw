_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoLCD _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        timer _ ?C...QTimer
        timer.timeout.c..(showlcd)
        timer.start(1000)
        showlcd()
  
    ___ showlcd
        time _ ?C...QTime.currentTime()
        t.. _ time.toString('hh:mm')
        ui.lcdNumber.display(t..)
 
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
