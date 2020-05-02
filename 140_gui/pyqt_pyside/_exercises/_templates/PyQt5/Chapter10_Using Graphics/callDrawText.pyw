_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter, QColor, QFont
____ ?.?C.. _____ Qt

____ demoDrawText _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonDrawText.c___.c..(dispText)
        textToDraw_""
        fontName_"Courier New"
        fontSize_5
        s..

    ___ paintEvent , event
        qp _ QPainter()
        qp.begin  
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont(fontName, fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, textToDraw)
        qp.end()  

    ___ dispText
        fontName_ui.listWidgetFont.currentItem().t..()
        fontSize_int(ui.comboBoxFontSize.itemText(ui.comboBoxFontSize.currentIndex()))
        textToDraw_ui.textEdit.toPlainText()
        update()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
