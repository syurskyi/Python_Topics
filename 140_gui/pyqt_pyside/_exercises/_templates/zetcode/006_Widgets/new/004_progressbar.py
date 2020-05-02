#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., QProgressBar,
                             ?P.., ?A..)
____ ?.?C.. ______ QBasicTimer
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        pbar _ QProgressBar(
        pbar.sG__(30, 40, 200, 25)

        btn _ ?P..('Start',
        btn.m..(40, 80)
        btn.c__.c..(doAction)

        timer _ QBasicTimer
        step _ 0

        sG__(300, 300, 280, 170)
        sWT__('QProgressBar')
        show

    ___ timerEvent(self, e):

        __ step >= 100:
            timer.stop
            btn.sT..('Finished')
            return

        step _ step + 1
        pbar.setValue(step)

    ___ doAction

        __ timer.isActive :
            timer.stop
            btn.sT..('Start')
        ____
            timer.start(100,
            btn.sT..('Stop')


__ _____ __ _______
    app _ ?A..(___.argv)
    ex _ Example
    ___.e..(app.e..())