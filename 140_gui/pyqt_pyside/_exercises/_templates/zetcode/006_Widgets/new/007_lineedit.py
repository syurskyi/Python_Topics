#!/usr/bin/python3
# -*- coding: utf-8 -*-


______ ___
____ ?.?W.. ______ (W.., ?L..,
                             QLineEdit, QApplication)


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        lbl _ ?L..(
        qle _ QLineEdit(

        qle.m..(60, 100)
        lbl.m..(60, 40)

        qle.textChanged[str].connect(onChanged)

        sG__(300, 300, 280, 170)
        sWT__('QLineEdit')
        show

    ___ onChanged(self, text):
        lbl.setText(text)
        lbl.adjustSize


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())