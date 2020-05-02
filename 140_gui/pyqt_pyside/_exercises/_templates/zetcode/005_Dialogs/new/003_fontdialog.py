#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ (W.., ?VB.., ?P..,
                             QSizePolicy, ?L.., QFontDialog, QApplication)
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        vbox _ ?VB..

        btn _ ?P..('Dialog',
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.m..(20, 20)

        vbox.aW..(btn)

        btn.clicked.c..(showDialog)

        lbl _ ?L..('Knowledge only matters',
        lbl.m..(130, 20)

        vbox.aW..(lbl)
        sL..(vbox)

        sG__(300, 300, 250, 180)
        sWT__('Font dialog')
        show

    ___ showDialog
        font, ok _ QFontDialog.getFont
        __ ok:
            lbl.setFont(font)


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())