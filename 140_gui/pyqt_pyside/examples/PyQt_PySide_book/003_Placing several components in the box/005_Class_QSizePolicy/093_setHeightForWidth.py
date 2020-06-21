# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


class MyLabel(QtGui.QLabel):
    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)

    def heightForWidth(self, w):
        return w // 2


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("QSizePolicy")
window.resize(300, 250)
label = MyLabel("Минимальная высота компонента зависит от ширины")
button = QtGui.QPushButton("1")

label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                           QtGui.QSizePolicy.Expanding)
policy.setHeightForWidth(True)
label.setSizePolicy(policy)

vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())