# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        img = QtGui.QImage("NukeApp128", "PNG")
        self.pix = QtGui.QBitmap.fromImage(img)
        m = QtGui.QMatrix()
        m.rotate(90.0)
        self.pix = self.pix.transformed(m)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QBitmap")
    window.show()
    sys.exit(app.exec_())