#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., QCheckBox, ?A..
____ ?.?C.. ______ __
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        cb _ QCheckBox('Show title',
        cb.m..(20, 20)
        cb.toggle
        cb.stateChanged.c..(changeTitle)

        sG__(300, 300, 250, 150)
        sWT__('QCheckBox')
        show

    ___ changeTitle(self, state):

        __ state __ __.Checked:
            sWT__('QCheckBox')
        else:
            sWT__(' ')


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())