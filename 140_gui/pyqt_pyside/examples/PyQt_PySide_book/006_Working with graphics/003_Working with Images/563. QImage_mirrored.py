# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 700)
        self.img = QtGui.QImage("foto.jpg", "JPG")
        self.img2 = self.img.mirrored(horizontal=False, vertical=True)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.img)
        painter.drawImage(0, 335, self.img2)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QImage")
    window.show()
    sys.exit(app.exec_())