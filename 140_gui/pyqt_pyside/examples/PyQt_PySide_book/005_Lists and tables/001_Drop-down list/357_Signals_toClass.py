# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

class Signals(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        self.comboBox.setEditable(True)
        self.comboBox.activated[int].connect(self.on_activated)
        self.comboBox.activated[str].connect(self.on_activated)
        self.comboBox.currentIndexChanged[int].connect(self.on_index_changed)
        self.comboBox.currentIndexChanged[str].connect(self.on_index_changed)
        self.comboBox.editTextChanged[str].connect(self.on_text_changed)
        self.comboBox.highlighted[int].connect(self.on_highlighted)
        self.comboBox.highlighted[str].connect(self.on_highlighted)
        self.button = QtWidgets.QPushButton("Выбрать элемент с индексом 3")
        self.button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(self.button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.comboBox.setCurrentIndex(3)

    def on_activated(self, v):
        print("on_activated", v)

    def on_index_changed(self, v):
        print("on_index_changed", v)

    def on_text_changed(self, s):
        print("on_text_changed", s)

    def on_highlighted(self, v):
        print("on_highlighted", v)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Signals()
    sys.exit(app.exec_())