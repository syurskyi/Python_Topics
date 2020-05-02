#!/usr/bin/python3
# -*- coding: utf-8 -*-


______ ___
____ ?.QtCore ______ Qt
____ ?.?W.. ______ W.., QApplication, ?G.., ?L..


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        grid _ ?G..

        x _ 0
        y _ 0

        text _ "x: {0},  y: {1}".format(x, y)

        label _ ?L..(text,
        grid.aW..(label, 0, 0, Qt.AlignTop)

        setMouseTracking(True)

        sL..(grid)

        sG__(300, 300, 350, 200)
        sWT__('Event object')
        show

    ___ mouseMoveEvent(self, e):
        x _ e.x
        y _ e.y

        text _ "x: {0},  y: {1}".format(x, y)
        label.setText(text)


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())