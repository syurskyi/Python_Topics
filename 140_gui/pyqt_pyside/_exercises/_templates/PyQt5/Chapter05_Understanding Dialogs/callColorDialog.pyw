_____ ___

____ ?.?W.. _____ ?D.., ?A.., QColorDialog
____ ?.?G.. _____ ?C..

____ demoColorDialog _____ _

c_ MyForm ?D..
    ___  -  
        s__. -
        col _ ?C.. 0, 0, 0
        ui _ ?
        ?.sU..
        ?.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
        ?.pushButtonColor.c___.c..(dispcolor)
        s..

    ___ dispcolor 
        col _ QColorDialog.getColor()
        __ col.isValid(
            ?.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())
            ?.labelColor.sT..("You have selected the color with code: " + st.(col.name()))

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e

