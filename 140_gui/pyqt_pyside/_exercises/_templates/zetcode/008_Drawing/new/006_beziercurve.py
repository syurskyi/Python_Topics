#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., ?A..
____ ?.?G__ ______ ?P.., QPainterPath
____ ?.?C.. ______ __
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 380, 250)
        sWT__('Bézier curve')
        s..

    ___ paintEvent(self, e):
        qp _ ?P..
        qp.begin(
        qp.setRenderHint(?P...Antialiasing)
        drawBezierCurve(qp)
        qp.end

    ___ drawBezierCurve(self, qp):
        path _ QPainterPath
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())