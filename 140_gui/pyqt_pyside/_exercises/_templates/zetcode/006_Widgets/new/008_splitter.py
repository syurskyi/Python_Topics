#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?HB.., ?F.,
                             QSplitter, QStyleFactory, ?A..)
____ ?.?C.. ______ __
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        hbox _ ?HB..(

        topleft _ ?F.(
        topleft.setFrameShape(?F..StyledPanel)

        topright _ ?F.(
        topright.setFrameShape(?F..StyledPanel)

        bottom _ ?F.(
        bottom.setFrameShape(?F..StyledPanel)

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
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())