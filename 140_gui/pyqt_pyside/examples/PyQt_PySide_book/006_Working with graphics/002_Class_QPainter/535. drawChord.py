# - * - coding: utf - 8 -*-

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
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)

        painter.setPen(QtGui.QPen(red, 2))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green))
        painter.drawChord(50, 50, 80, 80, 0, 16 * 90)
        painter.drawChord(QtCore.QRect(150, 50, 80, 80), 16 * 90, 16 * 180)
        painter.drawChord(QtCore.QRectF(50., 150., 80., 80.), 0, -16 * 90)
        painter.drawChord(150, 150, 80, 80, -16 * 90, -16 * 90)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec_())