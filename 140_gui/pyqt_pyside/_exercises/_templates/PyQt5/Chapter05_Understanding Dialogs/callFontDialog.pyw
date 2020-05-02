_____ ___

____ ?.?W.. _____ ?D.., ?A.., QFontDialog


____ demoFontDialog _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonFont.clicked.c..(changefont)
        s..

    ___ changefont
        font, ok = QFontDialog.getFont()
        __ ok:
            ui.textEdit.setFont(font)

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())

