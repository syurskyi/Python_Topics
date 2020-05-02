#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., ?S..,
                             ?L.., ?A..)
____ ?.?C.. ______ __
____ ?.?G__ ______ QPixmap
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        sld _ ?S..(__.H..,
        sld.setFocusPolicy(__.NoFocus)
        sld.sG__(30, 40, 100, 30)
        sld.vC__[int].c..(changeValue)

        label _ ?L..(
        label.setPixmap(QPixmap('mute.png'))
        label.sG__(160, 40, 80, 30)

        sG__(300, 300, 280, 170)
        sWT__('?S..')
        show

    ___ changeValue(self, value):

        __ value __ 0:
            label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            label.setPixmap(QPixmap('med.png'))
        ____
            label.setPixmap(QPixmap('max.png'))


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())