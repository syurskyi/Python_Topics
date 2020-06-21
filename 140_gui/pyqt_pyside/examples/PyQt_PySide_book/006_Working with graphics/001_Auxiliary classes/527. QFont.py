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
        painter.setPen(QtGui.QPen(red, 5))

        font = QtGui.QFont("Tahoma", 16)
        fm = QtGui.QFontMetrics(font)
        print(fm.width("Строка"))  # 67
        print(fm.height())  # 25
        print(fm.boundingRect("Строка"))  # PyQt4.QtCore.QRect(0, -21, 65, 25)

        painter.setFont(font)
        painter.drawText(50, 50, "Строка")


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QFont")
    window.show()
    sys.exit(app.exec_())