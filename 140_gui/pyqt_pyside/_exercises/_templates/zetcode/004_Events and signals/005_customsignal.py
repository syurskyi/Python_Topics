#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.?C.. ______ pyqtSignal, QObject
____ ?.?W.. ______ QMainWindow, ?A..


c_ Communicate(QObject):
    closeApp _ pyqtSignal


c_ Example(QMainWindow):

    ___ -
        s__ .-

        ?

    ___ initUI
        c _ Communicate
        c.closeApp.c..(close)

        sG__(300, 300, 290, 150)
        sWT__('Emit signal')
        show

    ___ mousePressEvent(self, event):
        c.closeApp.emit


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())