


def on_clicked():
    print("Кнопка нажата")

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button = QtGui.QPushButton("Выполнить операцию")
button.setShortcut("Alt+В")
button.clicked.connect(on_clicked)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button)
window.setLayout(vbox)
