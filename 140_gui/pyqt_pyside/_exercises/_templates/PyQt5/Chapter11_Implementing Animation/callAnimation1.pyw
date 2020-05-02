_____ ___

____ PyQt5.?W.. _____ ?D.., ?A..
____ PyQt5.?C.. _____ QRect, QPropertyAnimation

____ demoAnimation1 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonMoveDown.c___.c..(startAnimation)
        s..

    ___ startAnimation 
        anim _ QPropertyAnimation(ui.labelPic, b"geometry")
        anim.setDuration(10000)
        anim.setStartValue(QRect(160, 70, 80, 80))
        anim.setEndValue(QRect(160, 70, 220, 220))
        anim.start()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
