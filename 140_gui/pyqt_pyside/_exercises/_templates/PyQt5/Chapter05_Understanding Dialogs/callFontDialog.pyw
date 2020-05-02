_____ ___

____ ?.?W.. _____ ?D.., ?A.., QFontDialog


____ demoFontDialog _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonFont.c___.c..(changefont)
        s..

    ___ changefont
        font, ok _ QFontDialog.getFont()
        __ ok:
            ui.textEdit.setFont(font)

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())

