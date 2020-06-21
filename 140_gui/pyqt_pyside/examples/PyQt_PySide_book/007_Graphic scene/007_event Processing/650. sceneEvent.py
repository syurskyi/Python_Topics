# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r, n):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)
        self.n = n

    def mousePressEvent(self, e):
        print("mousePressEvent", self.n)
        e.accept()

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent", self.n)
        QtGui.QGraphicsRectItem.mouseReleaseEvent(self, e)

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent", self.n)
        QtGui.QGraphicsRectItem.mouseMoveEvent(self, e)

    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClickEvent", self.n)
        QtGui.QGraphicsRectItem.mouseDoubleClickEvent(self, e)

    def sceneEvent(self, e):
        print("sceneEvent", self.n)
        return QtGui.QGraphicsRectItem.sceneEvent(self, e)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Перехват всех событий")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0), 1)
rect.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect)

rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

rect2 = MyRect(QtCore.QRectF(0.0, 0.0, 300.0, 100.0), 2)
rect2.setPos(QtCore.QPointF(10.0, 10.0))
rect2.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
rect2.setParentItem(rect)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())