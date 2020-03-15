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
        painter.setPen(QtGui.QPen(red, 15, join=QtCore.Qt.MiterJoin))
        painter.drawPolygon(
            QtCore.QPoint(20, 20),
            QtCore.QPoint(120, 20),
            QtCore.QPoint(20, 120)
        )
        painter.setPen(QtGui.QPen(red, 15, join=QtCore.Qt.BevelJoin))
        painter.drawPolygon(
            QtCore.QPoint(180, 20),
            QtCore.QPoint(280, 20),
            QtCore.QPoint(280, 120)
        )
        painter.setPen(QtGui.QPen(red, 15, join=QtCore.Qt.RoundJoin))
        painter.drawPolygon(
            QtCore.QPoint(20, 180),
            QtCore.QPoint(20, 280),
            QtCore.QPoint(120, 280)
        )
        painter.setPen(QtGui.QPen(red, 15, join=QtCore.Qt.SvgMiterJoin))
        painter.drawPolygon(
            QtCore.QPoint(280, 180),
            QtCore.QPoint(280, 280),
            QtCore.QPoint(180, 280)
        )


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPen")
    window.show()
    sys.exit(app.exec_())