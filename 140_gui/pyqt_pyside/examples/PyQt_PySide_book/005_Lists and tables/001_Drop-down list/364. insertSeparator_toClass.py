# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


class InsertSeparator(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

def on_clicked():
    print("Текст:", comboBox.currentText())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i))
comboBox.insertSeparator(5)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = InsertSeparator()
    sys.exit(app.exec_())