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
        painter.setPen(QtGui.QPen(red, 4, style=QtCore.Qt.SolidLine))
        painter.drawLine(20, 50, 280, 50)
        painter.setPen(QtGui.QPen(red, 4, style=QtCore.Qt.DashLine))
        painter.drawLine(20, 100, 280, 100)
        painter.setPen(QtGui.QPen(red, 4, style=QtCore.Qt.DotLine))
        painter.drawLine(20, 150, 280, 150)
        painter.setPen(QtGui.QPen(red, 4, style=QtCore.Qt.DashDotLine))
        painter.drawLine(20, 200, 280, 200)
        painter.setPen(QtGui.QPen(red, 4, style=QtCore.Qt.DashDotDotLine))
        painter.drawLine(20, 250, 280, 250)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPen")
    window.show()
    sys.exit(app.exec_())