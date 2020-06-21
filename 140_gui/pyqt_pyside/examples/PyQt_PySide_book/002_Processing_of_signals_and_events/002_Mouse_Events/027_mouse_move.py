# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # Обрабатываем любые перемещения мыши
        self.setMouseTracking(True)
        # в пределах всего окна, а не комопонета
        self.grabMouse()

    def mouseMoveEvent(self, e):
        self.setText(
             "X: {0}, Y: {1}, globalX: {2}, globalY: {3}".format(
             e.x(), e.y(), e.globalX(), e.globalY()))
        e.ignore()
        QtWidgets.QLabel.mouseMoveEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Переместите мышь")
        self.label.setFrameStyle(QtWidgets.QFrame.Box |
                                 QtWidgets.QFrame.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())