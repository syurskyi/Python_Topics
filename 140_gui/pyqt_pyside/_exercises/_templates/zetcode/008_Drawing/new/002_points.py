#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., QApplication
____ ?.QtGui ______ QPainter
____ ?.QtCore ______ Qt
______ ___, random


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 300, 190)
        sWT__('Points')
        show

    ___ paintEvent(self, e):
        qp _ QPainter
        qp.begin(
        drawPoints(qp)
        qp.end

    ___ drawPoints(self, qp):
        qp.setPen(Qt.red)
        size _ size

        ___ i __ ra..(1000):
            x _ random.randint(1, size.width  - 1)
            y _ random.randint(1, size.height  - 1)
            qp.drawPoint(x, y)


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())