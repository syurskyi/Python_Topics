#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSlider, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__

        self.initUI()

    def initUI(self)
        hbox _ ?HB..

        topleft _ ?F.
        ?.sFS.. ?F..aS..

        topright _ ?F.
        ?.sFS.. ?F..aS..

        bottom _ ?F.
        ?.sFS.. ?F..aS..

        splitter1 _ ?S.. __.H..
        ?.aW.. t_l..
        ?.aW.. t_r..

        splitter2 _ ?S.. __.V..
        ?.aW.. _1
        ?.aW.. b..

        h__.aW.. _2
        sL.. h..

        sG__ 300 300 300 200
        sWT__('QSplitter')
        s..


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())