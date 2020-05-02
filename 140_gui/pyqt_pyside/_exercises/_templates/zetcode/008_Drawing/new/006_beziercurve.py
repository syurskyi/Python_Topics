#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., QApplication
____ ?.QtGui ______ QPainter, QPainterPath
____ ?.QtCore ______ Qt
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 380, 250)
        sWT__('Bézier curve')
        show

    ___ paintEvent(self, e):
        qp _ QPainter
        qp.begin(
        qp.setRenderHint(QPainter.Antialiasing)
        drawBezierCurve(qp)
        qp.end

    ___ drawBezierCurve(self, qp):
        path _ QPainterPath
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())