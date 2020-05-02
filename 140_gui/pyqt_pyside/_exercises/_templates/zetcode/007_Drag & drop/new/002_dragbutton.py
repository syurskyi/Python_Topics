#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ ?P.., W.., ?A..
____ ?.?C.. ______ __, QMimeData
____ ?.?G__ ______ QDrag
______ ___


c_ Button(?P..):

    ___ - (self, title, parent):
        s__ .- (title, parent)

    ___ mouseMoveEvent(self, e):

        __ e.buttons  != __.RightButton:
            r_

        mD__ _ QMimeData

        drag _ QDrag(
        drag.setMimeData(mD__)
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
        sAD..(T..)

        button _ Button('Button',
        button.m..(100, 65)

        sWT__('Click or Move')
        sG__(300, 300, 280, 150)

    ___ dragEnterEvent(self, e):
        e.a...

    ___ dropEvent(self, e):
        position _ e.pos
        button.m..(position)

        e.setDropAction(__.MoveAction)
        e.a...


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ex.show
    app.e..