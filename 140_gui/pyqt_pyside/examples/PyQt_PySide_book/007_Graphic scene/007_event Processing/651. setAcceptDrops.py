# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyRect(QtGui.QGraphicsRectItem):
    def __init__(self, r):
        QtGui.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            txt.setText(str(e.mimeData().data("text/plain"), "utf-8"))
            e.accept()
        else:
            e.ignore()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("События перетаскивания и сброса")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0))
rect.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect)

txt = scene.addSimpleText("Перетащите сюда текст",
                          QtGui.QFont("Verdana", 16))
txt.setPen(QtGui.QPen(QtCore.Qt.white, 1))
txt.setBrush(QtGui.QBrush(QtCore.Qt.white))
txt.setParentItem(rect)
txt.setPos(20.0, 80.0)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())