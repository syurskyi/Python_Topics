_____ ___

____ ?.?W.. _____ ?D.., ?A.., QColorDialog
____ ?.QtGui _____ QColor

____ demoColorDialog _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        col = QColor(0, 0, 0) 
        ui = Ui_Dialog()
        ui.setupUi
        ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
        ui.pushButtonColor.clicked.c..(dispcolor)
        s..

    ___ dispcolor 
        col = QColorDialog.getColor()
        __ col.isValid(
            ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
            ui.labelColor.sT..("You have selected the color with code: " + st.(col.name()))

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())

