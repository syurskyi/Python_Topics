#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.QtCore ______ Qt
____ ?.?W.. ______ (W.., QLCDNumber, QSlider,
                             ?VB.., QApplication)


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        lcd _ QLCDNumber(
        sld _ QSlider(Qt.Horizontal,

        vbox _ ?VB..
        vbox.aW..(lcd)
        vbox.aW..(sld)

        sL..(vbox)
        sld.valueChanged.connect(lcd.display)

        sG__(300, 300, 250, 150)
        sWT__('Signal and slot')
        show


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())