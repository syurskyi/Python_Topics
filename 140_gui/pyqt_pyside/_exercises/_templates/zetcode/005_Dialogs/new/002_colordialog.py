#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?P.., QFrame,
                             QColorDialog, QApplication)
____ ?.QtGui ______ QColor
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        col _ QColor(0, 0, 0)

        btn _ ?P..('Dialog',
        btn.m..(20, 20)

        btn.clicked.connect(showDialog)

        frm _ QFrame(
        frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        frm.sG__(130, 22, 100, 100)

        sG__(300, 300, 250, 180)
        sWT__('Color dialog')
        show

    ___ showDialog
        col _ QColorDialog.getColor

        __ col.isValid :
            frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())