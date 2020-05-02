#!/usr/bin/python3
# -*- coding: utf-8 -*-

____ ?.?W.. ______ W.., ?A..
____ ?.?G__ ______ QPainter, QBrush
____ ?.?C.. ______ __
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        sG__(300, 300, 355, 280)
        sWT__('Brushes')
        show

    ___ paintEvent(self, e):
        qp _ QPainter
        qp.begin(
        drawBrushes(qp)
        qp.end

    ___ drawBrushes(self, qp):
        brush _ QBrush(__.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(__.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(__.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(__.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(__.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(__.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(__.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(__.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(__.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())