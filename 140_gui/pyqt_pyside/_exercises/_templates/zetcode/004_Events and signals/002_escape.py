#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.QtCore ______ Qt
____ ?.?W.. ______ W.., QApplication


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 250, 150)
        sWT__('Event handler')
        show

    ___ keyPressEvent(self, e):
        __ e.key  __ Qt.Key_Escape:
            close


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())