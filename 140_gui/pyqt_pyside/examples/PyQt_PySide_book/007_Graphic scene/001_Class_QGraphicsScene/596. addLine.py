# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtGui.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.white)

scene.addLine(50.0, 50.0, 450.0, 50.0, pen=QtGui.QPen(QtCore.Qt.red, 3))
scene.addLine(QtCore.QLineF(50.0, 150.0, 450.0, 150.0),
              pen=QtGui.QPen(QtCore.Qt.blue, 3))

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())