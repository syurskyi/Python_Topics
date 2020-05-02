#!/usr/bin/python3
# -*- coding: utf-8 -*-

______ ___
____ ?.?W.. ______ W.., ?A..
____ ?.QtGui ______ QPainter, QColor, QFont
____ ?.?C.. ______ __


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        text _ "Leo Nikolaevich Tolstoy \n Anna Karenina"

        sG__(300, 300, 280, 170)
        sWT__('Drawing text')
        show

    ___ paintEvent(self, event):
        qp _ QPainter
        qp.begin(
        drawText(event, qp)
        qp.end

    ___ drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect , __.AlignCenter, text)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())