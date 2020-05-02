_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?C.. _____ QRect, QPropertyAnimation

____ demoAnimation3 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonBounce.clicked.c..(startAnimation)
        s..

    ___ startAnimation 
        anim = QPropertyAnimation(ui.labelPic, b"geometry")
        anim.setDuration(10000)
        anim.setKeyValueAt(0, QRect(0, 0, 100, 80));
        anim.setKeyValueAt(0.8, QRect(160, 160, 200, 180));
        anim.setKeyValueAt(1, QRect(400, 0, 100, 80));
        anim.start()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
