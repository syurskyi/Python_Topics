#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., QProgressBar,
                             ?P.., QApplication)
____ ?.QtCore ______ QBasicTimer
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
        btn.clicked.connect(doAction)

        timer _ QBasicTimer
        step _ 0

        sG__(300, 300, 280, 170)
        sWT__('QProgressBar')
        show

    ___ timerEvent(self, e):

        __ step >= 100:
            timer.stop
            btn.setText('Finished')
            return

        step _ step + 1
        pbar.setValue(step)

    ___ doAction

        __ timer.isActive :
            timer.stop
            btn.setText('Start')
        else:
            timer.start(100,
            btn.setText('Stop')


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())