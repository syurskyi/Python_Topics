#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


c_ Button ?P..

    ___ -  title parent
        s__ .- ? ?

    ___ mouseMoveEvent e

        __ e.b..  != __.RB..
            r_

        mD__ _ ?MD..

        drag _ ?D..
        ?.sMD.. mD__
        ?.sHS.. e.p..  - rect .tL..

        dropAction _ ?.e.. __.MA..

    ___ mousePressEvent e

        s__ .mPE.. ?

        __ e.b..  __ __.LB..
            print('press')


c_ Example W..

    ___ -
        s__ .-

        ?

    ___ initUI
        sAD.. T..

        button _ ? 'Button'
        ?.m.. 100 65

        sWT__ 'Click or Move'
        sG__ 300 300 280 150

    ___ dragEnterEvent( e
        ?.a...

    ___ dropEvent e
        position _ ?.p..
        b__.m.. ?

        ?.sDA.. __.MA..
        ?.a...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()