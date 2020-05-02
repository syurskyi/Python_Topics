_____ ___

____ ?.?W.. _____ ?D.., ?A.., QColorDialog
____ ?.?G.. _____ QColor

____ demoColorDialog _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        col _ QColor(0, 0, 0) 
        ui _ Ui_Dialog()
        ui.sU..
        ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
        ui.pushButtonColor.c___.c..(dispcolor)
        s..

    ___ dispcolor 
        col _ QColorDialog.getColor()
        __ col.isValid(
            ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
            ui.labelColor.sT..("You have selected the color with code: " + st.(col.name()))

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e

