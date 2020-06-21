# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 300)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.black
        white = QtCore.Qt.white
        red = QtCore.Qt.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)
        painter.drawLine(20, 20, 20, 280)
        painter.drawLine(280, 20, 280, 280)
        painter.setPen(QtGui.QPen(red, 15, cap=QtCore.Qt.FlatCap))
        painter.drawLine(20, 50, 280, 50)
        painter.setPen(QtGui.QPen(red, 15, cap=QtCore.Qt.SquareCap))
        painter.drawLine(20, 100, 280, 100)
        painter.setPen(QtGui.QPen(red, 15, cap=QtCore.Qt.RoundCap))
        painter.drawLine(20, 150, 280, 150)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPen")
    window.show()
    sys.exit(app.exec_())