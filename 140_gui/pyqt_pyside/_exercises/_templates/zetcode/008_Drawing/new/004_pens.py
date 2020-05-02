#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., ?A..
____ ?.?G__ ______ QPainter, QPen
____ ?.?C.. ______ __
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
        pen _ QPen(__.black, 2, __.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(__.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(__.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(__.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(__.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(__.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())