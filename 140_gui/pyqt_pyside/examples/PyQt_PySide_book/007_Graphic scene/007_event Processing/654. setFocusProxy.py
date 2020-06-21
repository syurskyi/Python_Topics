# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

    def focusInEvent(self, e):
        self.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        QtGui.QGraphicsRectItem.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        QtGui.QGraphicsRectItem.focusOutEvent(self, e)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Up:
            self.moveBy(0, -5)
        elif e.key() == QtCore.Qt.Key_Down:
            self.moveBy(0, 5)
        elif e.key() == QtCore.Qt.Key_Left:
            self.moveBy(-5, 0)
        elif e.key() == QtCore.Qt.Key_Right:
            self.moveBy(5, 0)
        e.ignore()
        QtGui.QGraphicsRectItem.keyPressEvent(self, e)

    def keyReleaseEvent(self, e):
        QtGui.QGraphicsRectItem.keyReleaseEvent(self, e)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Обработка событий клавиатуры")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0))
rect.setPos(QtCore.QPointF(50.0, 150.0))
scene.addItem(rect)

rect2 = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 50.0))
rect2.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect2)
rect.setFocusProxy(rect2)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())