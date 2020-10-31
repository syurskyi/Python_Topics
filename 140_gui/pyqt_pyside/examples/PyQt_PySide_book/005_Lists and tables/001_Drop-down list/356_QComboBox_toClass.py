# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class QComboBox(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i), i)
        self.button = QtWidgets.QPushButton("Получить значение")
        self.button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(self.button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print("Текст:", self.comboBox.currentText())
        print("Данные:", self.comboBox.itemData(self.comboBox.currentIndex()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = QComboBox()
    sys.exit(app.exec_())