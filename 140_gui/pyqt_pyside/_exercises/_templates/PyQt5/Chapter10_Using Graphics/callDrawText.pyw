_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?G.. _____ QPainter, ?C.., ?F..
____ ?.?C.. _____ Qt

____ demoDrawText _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ?.sU..
        ?.pushButtonDrawText.c___.c..(dispText)
        textToDraw_""
        fontName_"Courier New"
        fontSize_5
        s..

    ___ paintEvent , event
        qp _ QPainter()
        qp.begin  
        qp.setPen(?C..(168, 34, 3))
        qp.sF..(?F..(fontName, fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, textToDraw)
        qp.end()  

    ___ dispText
        fontName_ui.listWidgetFont.cI__).t..()
        fontSize_int(?.comboBoxFontSize.iT..(?.comboBoxFontSize.cI..()))
        textToDraw_ui.tE__.toPlainText()
        update()

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
