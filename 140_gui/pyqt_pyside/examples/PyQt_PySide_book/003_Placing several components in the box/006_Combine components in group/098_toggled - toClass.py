
def on_clicked_button():
    box.setChecked(False if box.isChecked() else True)


def on_clicked(flag):
    print("on_clicked", flag)


def on_toggled(flag):
    print("on_toggled", flag)


from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QGroupBox")
        self.resize(300, 80)
        radio1 = QtGui.QRadioButton("&Да")
        radio2 = QtGui.QRadioButton("&Нет")
        button = QtGui.QPushButton("&Переключить флажок")
        mainbox = QtGui.QVBoxLayout()
        box = QtGui.QGroupBox()
        box.setTitle("&Вы знаете язык Python?")
        box.setCheckable(True)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        box.setLayout(hbox)
        mainbox.addWidget(box)
        mainbox.addWidget(button)
        self.setLayout(mainbox)
        radio1.setChecked(True)
        box.clicked["bool"].connect(on_clicked)
        box.toggled["bool"].connect(on_toggled)
        button.clicked.connect(on_clicked_button)
