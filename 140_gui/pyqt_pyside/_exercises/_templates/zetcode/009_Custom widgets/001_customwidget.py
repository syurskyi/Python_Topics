#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?S.., ?A..,
                             ?HB.., ?VB..)
____ ?.?C.. ______ QObject, __, pyqtSignal
____ ?.?G__ ______ ?P.., QFont, ?C.., ?P..
______ ___


c_ Communicate(QObject):
    updateBW _ pyqtSignal(int)


c_ BurningWidget(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        setMinimumSize(1, 30)
        value _ 75
        num _ [75, 150, 225, 300, 375, 450, 525, 600, 675]

    ___ sV..(self, value):

        value _ value

    ___ paintEvent(self, e):

        qp _ ?P..
        qp.b..(
        drawWidget(qp)
        qp.end

    ___ drawWidget(self, qp):

        MAX_CAPACITY _ 700
        OVER_CAPACITY _ 750

        font _ QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size _ size
        w _ size.width
        h _ size.height

        step _ int(round(w / 10))

        till _ int(((w / OVER_CAPACITY) * value))
        full _ int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        __ value >= MAX_CAPACITY:

            qp.setPen(?C..(255, 255, 255))
            qp.setBrush(?C..(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(?C..(255, 175, 175))
            qp.setBrush(?C..(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        ____

            qp.setPen(?C..(255, 255, 255))
            qp.setBrush(?C..(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen _ ?P..(?C..(20, 20, 20), 1,
                   __.SolidLine)

        qp.setPen(pen)
        qp.setBrush(__.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j _ 0

        ___ i __ ra..(step, 10 * step, step):
            qp.dL..(i, 0, i, 5)
            metrics _ qp.fontMetrics
            fw _ metrics.width(st.(num[j]))
            qp.drawText(i - fw / 2, h / 2, st.(num[j]))
            j _ j + 1


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI
        OVER_CAPACITY _ 750

        sld _ ?S..(__.H..,
        sld.sFP..(__.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.sV..(75)
        sld.sG__(30, 40, 150, 30)

        c _ Communicate
        wid _ BurningWidget
        c.updateBW[int].c..(wid.sV..)

        sld.vC__[int].c..(changeValue)
        hbox _ ?HB..
        hbox.aW..(wid)
        vbox _ ?VB..
        vbox.aS..(1)
        vbox.aL..(hbox)
        sL..(vbox)

        sG__(300, 300, 390, 210)
        sWT__('Burning widget')
        s..

    ___ changeValue(self, value):
        c.updateBW.emit(value)
        wid.repaint


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())