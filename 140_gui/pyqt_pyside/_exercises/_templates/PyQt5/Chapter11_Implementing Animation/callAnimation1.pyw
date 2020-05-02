_____ ___

____ PyQt5.?W.. _____ ?D.., ?A..
____ PyQt5.?C.. _____ QRect, QPropertyAnimation

____ demoAnimation1 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonMoveDown.clicked.c..(startAnimation)
        s..

    ___ startAnimation 
        anim = QPropertyAnimation(ui.labelPic, b"geometry")
        anim.setDuration(10000)
        anim.setStartValue(QRect(160, 70, 80, 80))
        anim.setEndValue(QRect(160, 70, 220, 220))
        anim.start()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
