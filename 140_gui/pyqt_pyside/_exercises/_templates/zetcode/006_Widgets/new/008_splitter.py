#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?HB.., QFrame,
                             QSplitter, QStyleFactory, QApplication)
____ ?.?C.. ______ __
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        hbox _ ?HB..(

        topleft _ QFrame(
        topleft.setFrameShape(QFrame.StyledPanel)

        topright _ QFrame(
        topright.setFrameShape(QFrame.StyledPanel)

        bottom _ QFrame(
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 _ QSplitter(__.H..)
        splitter1.aW..(topleft)
        splitter1.aW..(topright)

        splitter2 _ QSplitter(__.Vertical)
        splitter2.aW..(splitter1)
        splitter2.aW..(bottom)

        hbox.aW..(splitter2)
        sL..(hbox)

        sG__(300, 300, 300, 200)
        sWT__('QSplitter')
        show


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())