# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


class SetCurrentIndex(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        button = QtWidgets.QPushButton("Сделать элемент с индексом 5 текущим")
        button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.comboBox.setCurrentIndex(5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetCurrentIndex()
    sys.exit(app.exec_())