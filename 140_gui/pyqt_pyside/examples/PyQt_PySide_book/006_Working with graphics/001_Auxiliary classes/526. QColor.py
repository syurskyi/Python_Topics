# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 300)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.black
        yellow = QtGui.QColor(255, 255, 0)
        darkBlue = QtGui.QColor("#000080")
        red = QtGui.QColor("#f00")
        white = QtGui.QColor("white")
        painter.setPen(black)
        painter.setBrush(QtGui.QBrush(red))
        painter.drawRect(3, 3, 294, 294)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QColor")
    window.show()
    print(QtGui.QColor.colorNames())
    print(QtGui.QColor.isValidColor("lightcyan"))
    print(QtGui.QColor.isValidColor("lightcyan2"))
    print(QtGui.QColor(255, 255, 0).isValid())
    print(QtGui.QColor().isValid())
    print(QtGui.QColor.isValidColor("#FFF"))
    sys.exit(app.exec_())