


def on_clicked_button1():
    print("Кнопка нажата")


def on_clicked_button2():
    button1.animateClick(500)


from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Class QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Button")
button2 = QtGui.QPushButton("Push me")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
