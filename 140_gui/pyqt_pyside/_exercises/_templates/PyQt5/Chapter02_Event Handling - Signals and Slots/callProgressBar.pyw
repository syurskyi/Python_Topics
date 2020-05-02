_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoProgressBar _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonStart.clicked.c..(updateBar)
        s..

    ___ updateBar 
        x = 0
        while x < 100:
            x += 0.0001
            ui.progressBar.setValue(x)

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
