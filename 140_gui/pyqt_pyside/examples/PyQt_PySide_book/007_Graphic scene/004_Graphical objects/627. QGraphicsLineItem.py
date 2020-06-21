# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsLineItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

line = QtGui.QGraphicsLineItem(50, 50, 450, 450)
line.setPen(QtGui.QPen(QtCore.Qt.darkBlue, 3))
line.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
line.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
line.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
scene.addItem(line)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())