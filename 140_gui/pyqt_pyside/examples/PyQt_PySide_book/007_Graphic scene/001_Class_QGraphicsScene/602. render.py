# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    r = scene.sceneRect()
    img = QtGui.QImage(int(r.width()), int(r.height()),
                       QtGui.QImage.Format_ARGB32_Premultiplied)
    img.fill(QtGui.QColor("#ffffff").rgb())
    painter = QtGui.QPainter()
    painter.begin(img)
    scene.render(painter)
    painter.end()
    img.save("scene.png", "PNG")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

w = QtGui.QWidget()
w.move(50, 50)
w.resize(300, 50)
btn = QtGui.QPushButton("Командная кнопка")
b = QtGui.QVBoxLayout()
b.addWidget(btn)
w.setLayout(b)
widget1 = scene.addWidget(w, QtCore.Qt.Window)
widget1.setWindowTitle("Заголовок окна 1")

w2 = QtGui.QWidget()
w2.move(50, 250)
w2.resize(300, 50)
widget2 = scene.addWidget(w2, QtCore.Qt.Window)
widget2.setWindowTitle("Заголовок окна 2")

view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Сохранить")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())