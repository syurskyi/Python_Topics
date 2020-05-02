#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ ?P.., W.., QApplication
____ ?.?C.. ______ __, QMimeData
____ ?.QtGui ______ QDrag
______ ___


c_ Button(?P..):

    ___ - (self, title, parent):
        s__ .- (title, parent)

    ___ mouseMoveEvent(self, e):

        __ e.buttons  != __.RightButton:
            return

        mimeData _ QMimeData

        drag _ QDrag(
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos  - rect .topLeft())

        dropAction _ drag.e..(__.MoveAction)

    ___ mousePressEvent(self, e):

        s__ .mousePressEvent(e)

        __ e.button  __ __.LeftButton:
            print('press')


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        setAcceptDrops(True)

        button _ Button('Button',
        button.m..(100, 65)

        sWT__('Click or Move')
        sG__(300, 300, 280, 150)

    ___ dragEnterEvent(self, e):
        e.accept

    ___ dropEvent(self, e):
        position _ e.pos
        button.m..(position)

        e.setDropAction(__.MoveAction)
        e.accept


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ex.show
    app.e..