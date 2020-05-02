#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., ?A..
____ ?.?G__ ______ ?P.., ?C.., QBrush
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 350, 100)
        sWT__('Colours')
        show

    ___ paintEvent(self, e):
        qp _ ?P..
        qp.begin(
        drawRectangles(qp)
        qp.end

    ___ drawRectangles(self, qp):
        col _ ?C..(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(?C..(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(?C..(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(?C..(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())