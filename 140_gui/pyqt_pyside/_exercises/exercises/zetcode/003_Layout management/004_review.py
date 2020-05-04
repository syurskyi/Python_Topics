#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd _ ?LCDN..
        sld _ ?S.. __.H..

        vbox _ ?VB..
        ?.aW.. l..
        ?.aW.. s..

        sL.. ?
        s__.vC__.c.. l__.d..

        sG__ 300, 300, 250, 150
        sWT__('Signal and slot')
        s..


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())