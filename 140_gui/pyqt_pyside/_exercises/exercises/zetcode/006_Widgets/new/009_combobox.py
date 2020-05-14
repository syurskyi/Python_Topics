#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl _ ?L.. "Ubuntu",

        combo _ ?CB..
        ?.aI.. "Ubuntu"
        ?.aI.. "Mandriva"
        ?.aI.. "Fedora"
        ?.aI.. "Arch"
        ?.aI.. "Gentoo"

        ?.m.. 50 50
        l__.m.. 50 150

        ?.ac..|st. .c.. ?

        sG__ 300 300 300 200
        sWT__ '?CB..'
        s..

    def onActivated(self, text):
        l__.sT.. ?
        l__.aS..


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
