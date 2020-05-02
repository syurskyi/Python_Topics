_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.QtGui _____ QPainter, QColor, QFont
____ ?.?C.. _____ Qt

____ demoDrawText _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonDrawText.clicked.c..(dispText)
        textToDraw=""
        fontName="Courier New"
        fontSize=5
        s..

    ___ paintEvent , event
        qp = QPainter()
        qp.begin  
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont(fontName, fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, textToDraw)
        qp.end()  

    ___ dispText
        fontName=ui.listWidgetFont.currentItem().text()
        fontSize=int(ui.comboBoxFontSize.itemText(ui.comboBoxFontSize.currentIndex()))
        textToDraw=ui.textEdit.toPlainText()
        update()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
