#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ (W.., ?HB..,
                             ?L.., QApplication)
____ ?.QtGui ______ QPixmap
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        hbox _ ?HB..(
        pixmap _ QPixmap("redrock.png")

        lbl _ ?L..(
        lbl.setPixmap(pixmap)

        hbox.aW..(lbl)
        sL..(hbox)

        m..(300, 200)
        sWT__('Red Rock')
        show


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())