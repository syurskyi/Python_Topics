# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 400)
        self.pix = QtGui.QPixmap("foto.jpg", "JPG")
        mask = QtGui.QBitmap(self.pix.size())
        mask.clear()
        painter = QtGui.QPainter()
        painter.begin(mask)
        painter.setPen(QtCore.Qt.color1)
        painter.setBrush(QtCore.Qt.color1)
        painter.setFont(QtGui.QFont("Tahoma", 26, weight=75))
        painter.setRenderHint(QtGui.QPainter.TextAntialiasing)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawText(0, 0, 500, 50,
                         QtCore.Qt.AlignCenter, "Камеронова галерея")
        painter.drawEllipse(50, 50, 400, 250)
        painter.end()
        self.pix.setMask(mask)

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