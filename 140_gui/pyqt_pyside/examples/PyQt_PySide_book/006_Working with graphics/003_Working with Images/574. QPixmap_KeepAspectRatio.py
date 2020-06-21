# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.pix = QtGui.QPixmap("foto.jpg", "JPG")
        self.pix = self.pix.scaled(250, 300,
                                   aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                   transformMode=QtCore.Qt.FastTransformation)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPixmap")
    window.show()
    sys.exit(app.exec_())