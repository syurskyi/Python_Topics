
def on_clicked():
    print("Кнопка нажата")


from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()


window.setWindowTitle("Класс QPushButton")
window.resize(300, 80)
button = QtGui.QPushButton("Кнопка")
button.clicked.connect(on_clicked)
button.setAutoRepeat(True)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
