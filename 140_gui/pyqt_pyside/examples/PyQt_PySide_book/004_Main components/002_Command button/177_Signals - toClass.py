
def on_clicked():
    print("Сигнал clicked")

def on_pressed():
    print("Сигнал pressed")

def on_released():
    print("Сигнал released")

def on_toggled(status):
    print("Сигнал toggled", status)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Class QPushButton")
window.resize(300, 50)
button1 = QtGui.QPushButton("Обычная кнопка")
button2 = QtGui.QPushButton("Кнопка-переключатель")
button2.setCheckable(True)
button1.clicked.connect(on_clicked)
button1.pressed.connect(on_pressed)
button1.released.connect(on_released)
button2.toggled["bool"].connect(on_toggled)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())