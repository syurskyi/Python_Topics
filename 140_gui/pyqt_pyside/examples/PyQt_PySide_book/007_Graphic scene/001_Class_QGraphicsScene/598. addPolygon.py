# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtGui.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.white)

scene.addPolygon(QtGui.QPolygonF([
                    QtCore.QPointF(50.0, 50.0),
                    QtCore.QPointF(450.0, 50.0),
                    QtCore.QPointF(250.0, 250.0)
                 ]),
                 pen=QtGui.QPen(QtCore.Qt.red, 3),
                 brush=QtGui.QBrush(QtCore.Qt.yellow))

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())