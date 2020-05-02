_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoFontComboBox _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        myFont=QtGui.QFont(ui.fontComboBox.itemText(ui.fontComboBox.currentIndex()),15)
        ui.textEdit.setFont(myFont)
        ui.fontComboBox.currentFontChanged.c..(changeFont)
        s..

    ___ changeFont
        myFont=QtGui.QFont(ui.fontComboBox.itemText(ui.fontComboBox.currentIndex()),15)
        ui.textEdit.setFont(myFont)
__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
