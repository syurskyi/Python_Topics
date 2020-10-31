# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys


class Find(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
       
        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i), i)
        self.comboBox.addItem("Пункт".format(i), 11)
        button = QtWidgets.QPushButton("Найти элементы")
        button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print(self.comboBox.findText("пункт 3",
                            flags=QtCore.Qt.MatchFixedString))
        print(self.comboBox.findText("[а-яёА-ЯЁ]+",
                                 flags=QtCore.Qt.MatchRegExp))
        print(self.comboBox.findText("Пункт 80"))
        print(self.comboBox.findData(10))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Find()
    sys.exit(app.exec_())