#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., QCheckBox, QApplication
____ ?.QtCore ______ Qt
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        cb _ QCheckBox('Show title',
        cb.m..(20, 20)
        cb.toggle
        cb.stateChanged.connect(changeTitle)

        sG__(300, 300, 250, 150)
        sWT__('QCheckBox')
        show

    ___ changeTitle(self, state):

        __ state __ Qt.Checked:
            sWT__('QCheckBox')
        else:
            sWT__(' ')


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())