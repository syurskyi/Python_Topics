#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.?C.. ______ __
____ ?.?W.. ______ (W.., QLCDNumber, ?S..,
                             ?VB.., QApplication)


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        lcd _ QLCDNumber(
        sld _ ?S..(__.H..,

        vbox _ ?VB..
        vbox.aW..(lcd)
        vbox.aW..(sld)

        sL..(vbox)
        sld.vC__.c..(lcd.display)

        sG__(300, 300, 250, 150)
        sWT__('Signal and slot')
        show


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())