# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtGui.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.white)

ellipse = QtGui.QGraphicsEllipseItem(0.0, 0.0, 300.0, 100.0)
ellipse.setPen(QtGui.QPen(QtCore.Qt.red, 3))
ellipse.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
ellipse.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(ellipse)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())