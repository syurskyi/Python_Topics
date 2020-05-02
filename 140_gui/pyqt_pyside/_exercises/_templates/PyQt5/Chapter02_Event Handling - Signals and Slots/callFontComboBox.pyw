_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoFontComboBox _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        myFont_QtGui.QFont(ui.fontComboBox.itemText(ui.fontComboBox.currentIndex()),15)
        ui.textEdit.setFont(myFont)
        ui.fontComboBox.currentFontChanged.c..(changeFont)
        s..

    ___ changeFont
        myFont_QtGui.QFont(ui.fontComboBox.itemText(ui.fontComboBox.currentIndex()),15)
        ui.textEdit.setFont(myFont)
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
