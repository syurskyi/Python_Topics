# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys


class SetIconSize(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setIconSize(QtCore.QSize(32, 32))
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        ico = self.style().standardIcon(
            QtWidgets.QStyle.SP_MessageBoxCritical)
        self.comboBox.insertItem(0, ico, "Пункт 11")
        button = QtWidgets.QPushButton("Получить индекс")
        button.clicked.connect(on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()
        sys.exit(app.exec_())


    def on_clicked():
        print(self.comboBox.currentIndex())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetIconSize()
    sys.exit(app.exec_())