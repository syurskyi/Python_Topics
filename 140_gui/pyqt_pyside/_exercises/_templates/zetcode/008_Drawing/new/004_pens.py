#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., QApplication
____ ?.QtGui ______ QPainter, QPen
____ ?.QtCore ______ Qt
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 280, 270)
        sWT__('Pen styles')
        show

    ___ paintEvent(self, e):
        qp _ QPainter
        qp.begin(
        drawLines(qp)
        qp.end

    ___ drawLines(self, qp):
        pen _ QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())