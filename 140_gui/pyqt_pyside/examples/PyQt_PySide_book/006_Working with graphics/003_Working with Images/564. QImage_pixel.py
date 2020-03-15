# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.img = QtGui.QImage(300, 300,
                         QtGui.QImage.Format_ARGB32_Premultiplied)
        self.img.fill(QtGui.QColor("#ff0000").rgb())
        color = QtGui.QColor(self.img.pixel(1, 1))
        print(color.name(), color.getRgb())

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