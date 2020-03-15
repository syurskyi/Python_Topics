# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)

    def mousePressEvent(self, e):
        print("mousePressEvent")
        e.accept()

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent")
        QtGui.QGraphicsRectItem.mouseReleaseEvent(self, e)

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent")
        QtGui.QGraphicsRectItem.mouseMoveEvent(self, e)

    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClickEvent")
        QtGui.QGraphicsRectItem.mouseDoubleClickEvent(self, e)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("События мыши")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0))
rect.setPos(QtCore.QPointF(50.0, 150.0))
scene.addItem(rect)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())