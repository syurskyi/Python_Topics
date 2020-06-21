# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.img = QtGui.QImage("foto.jpg", "JPG")
        self.img.save("foto.png", "PNG")

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