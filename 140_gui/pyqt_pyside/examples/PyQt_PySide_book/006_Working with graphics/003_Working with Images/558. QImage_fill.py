# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.img = QtGui.QImage(300, 300,
                                QtGui.QImage.Format_ARGB32_Premultiplied)
        self.img.fill(QtGui.QColor("#ffffff").rgb())
        painter = QtGui.QPainter()
        painter.begin(self.img)
        black = QtCore.Qt.black
        white = QtCore.Qt.white
        red = QtCore.Qt.red
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)

        painter.setPen(QtGui.QPen(red, 2, style=QtCore.Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green,
                                      style=QtCore.Qt.Dense5Pattern))
        painter.drawRect(50, 50, 80, 80)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green,
                                      style=QtCore.Qt.CrossPattern))
        painter.drawRect(QtCore.QRect(150, 50, 80, 80))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green,
                                      style=QtCore.Qt.DiagCrossPattern))
        painter.drawRect(QtCore.QRectF(50., 150., 80., 80.))
        painter.setPen(QtGui.QPen(red, 0, style=QtCore.Qt.NoPen))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green,
                                      style=QtCore.Qt.SolidPattern))
        painter.drawRect(QtCore.QRect(150, 150, 80, 80))
        painter.end()

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.img)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QImage")
    window.show()
    sys.exit(app.exec_())