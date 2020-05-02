#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?P.., ?L..,
                             QInputDialog, ?A..)
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        btn _ ?P..('Dialog',
        btn.m..(20, 20)
        btn.c__.c..(showDialog)

        le _ ?L..(
        le.m..(130, 22)

        sG__(300, 300, 290, 150)
        sWT__('Input dialog')
        show

    ___ showDialog
        text, ok _ QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        __ ok:
            le.setText(st.(text))


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())