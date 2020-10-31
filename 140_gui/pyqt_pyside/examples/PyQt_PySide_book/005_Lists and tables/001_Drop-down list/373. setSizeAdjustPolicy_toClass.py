# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


class SetSizeAdjustPolicy(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setMinimumContentsLength(30)
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
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
    ex = SetSizeAdjustPolicy()
    sys.exit(app.exec_())