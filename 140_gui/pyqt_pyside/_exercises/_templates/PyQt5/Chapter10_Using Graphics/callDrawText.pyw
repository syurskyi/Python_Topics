_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ QPainter, QColor, ?F..
____ ?.?C.. _____ Qt

____ demoDrawText _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ui.sU..
        ui.pushButtonDrawText.c___.c..(dispText)
        textToDraw_""
        fontName_"Courier New"
        fontSize_5
        s..

    ___ paintEvent , event
        qp _ QPainter()
        qp.begin  
        qp.setPen(QColor(168, 34, 3))
        qp.sF..(?F..(fontName, fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, textToDraw)
        qp.end()  

    ___ dispText
        fontName_ui.listWidgetFont.cI__).t..()
        fontSize_int(ui.comboBoxFontSize.iT..(ui.comboBoxFontSize.cI..()))
        textToDraw_ui.tE__.toPlainText()
        update()

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
