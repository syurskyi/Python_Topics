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
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)

        painter.fillRect(10, 10, 50, 50, QtCore.Qt.red)
        painter.save()
        matrix = QtGui.QMatrix()
        matrix.translate(105, 105)
        matrix.rotate(45.0)
        painter.setMatrix(matrix)
        painter.fillRect(-25, -25, 50, 50, QtCore.Qt.green)
        painter.restore()
        painter.fillRect(150, 150, 50, 50, QtCore.Qt.blue)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec_())