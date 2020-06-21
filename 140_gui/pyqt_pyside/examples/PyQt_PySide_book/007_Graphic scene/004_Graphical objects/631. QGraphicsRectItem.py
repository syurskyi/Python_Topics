# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsRectItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

item = QtGui.QGraphicsRectItem(0, 0, 450, 450)
item.setPos(QtCore.QPointF(10.0, 10.0))
item.setPen(QtGui.QPen(QtCore.Qt.darkBlue, 3))
item.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
item.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
item.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
scene.addItem(item)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())