from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QLabel")
window.resize(500, 350)
label = QtGui.QLabel()
picture = QtGui.QPicture()
painter = QtGui.QPainter()
painter.begin(picture)
painter.fillRect(10, 10, 480, 330, QtGui.QBrush(QtCore.Qt.white))
painter.end()
label.setPicture(picture)
label.setAutoFillBackground(True)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
