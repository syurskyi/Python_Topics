#!/usr/bin/python3
# -*- coding: utf-8 -*-


____ ?.?W.. ______ (W.., QSlider,
                             ?L.., QApplication)
____ ?.QtCore ______ Qt
____ ?.QtGui ______ QPixmap
______ ___


c_ Example(W..):

    ___ -
        s__ .-

        ?

    ___ initUI

        sld _ QSlider(Qt.Horizontal,
        sld.setFocusPolicy(Qt.NoFocus)
        sld.sG__(30, 40, 100, 30)
        sld.valueChanged[int].connect(changeValue)

        label _ ?L..(
        label.setPixmap(QPixmap('mute.png'))
        label.sG__(160, 40, 80, 30)

        sG__(300, 300, 280, 170)
        sWT__('QSlider')
        show

    ___ changeValue(self, value):

        __ value __ 0:
            label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            label.setPixmap(QPixmap('med.png'))
        else:
            label.setPixmap(QPixmap('max.png'))


__ _____ __ _______
    app _ QApplication(___.argv)
    ex _ Example
    ___.exit(app.e..())