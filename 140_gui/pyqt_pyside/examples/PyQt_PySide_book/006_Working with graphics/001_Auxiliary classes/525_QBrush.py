# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 410)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.black
        white = QtCore.Qt.white
        red = QtCore.Qt.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 404)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.SolidPattern))
        painter.drawRect(10, 10, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense1Pattern))
        painter.drawRect(10, 50, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense2Pattern))
        painter.drawRect(10, 90, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense3Pattern))
        painter.drawRect(10, 130, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense4Pattern))
        painter.drawRect(10, 170, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense5Pattern))
        painter.drawRect(10, 210, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense6Pattern))
        painter.drawRect(10, 250, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.Dense7Pattern))
        painter.drawRect(10, 290, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.CrossPattern))
        painter.drawRect(10, 330, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.HorPattern))
        painter.drawRect(10, 370, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.VerPattern))
        painter.drawRect(190, 10, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.BDiagPattern))
        painter.drawRect(190, 50, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.FDiagPattern))
        painter.drawRect(190, 90, 100, 30)
        painter.setBrush(QtGui.QBrush(red, style=QtCore.Qt.DiagCrossPattern))
        painter.drawRect(190, 130, 100, 30)
        gradient1 = QtGui.QLinearGradient(190, 185, 290, 185)
        gradient1.setColorAt(0, QtCore.Qt.black)
        gradient1.setColorAt(0.5, QtCore.Qt.white)
        gradient1.setColorAt(1, QtCore.Qt.black)
        painter.setBrush(QtGui.QBrush(gradient1))
        painter.drawRect(190, 170, 100, 30)
        gradient2 = QtGui.QConicalGradient(240, 225, 0)
        gradient2.setColorAt(0, QtCore.Qt.black)
        gradient2.setColorAt(0.5, QtCore.Qt.white)
        gradient2.setColorAt(1, QtCore.Qt.red)
        painter.setBrush(QtGui.QBrush(gradient2))
        painter.drawRect(190, 210, 100, 30)
        gradient3 = QtGui.QRadialGradient(240, 265, 70)
        gradient3.setColorAt(0, QtCore.Qt.white)
        gradient3.setColorAt(1, QtCore.Qt.red)
        painter.setBrush(QtGui.QBrush(gradient3))
        painter.drawRect(190, 250, 100, 30)
        ico = self.style().standardIcon(
            QtGui.QStyle.SP_MessageBoxCritical)
        painter.setBrush(QtGui.QBrush(ico.pixmap(QtCore.QSize(32, 32))))
        painter.drawRect(190, 290, 100, 30)
        brush = QtGui.QBrush(black)
        brush.setTexture(ico.pixmap(QtCore.QSize(16, 16)).mask())
        painter.setBrush(brush)
        painter.drawRect(190, 330, 100, 30)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QBrush")
    window.show()
    sys.exit(app.exec_())