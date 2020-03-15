# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


def on_clicked():
    wizard = QtGui.QWizard(window)
    wizard.setWindowTitle("Мой мастер")

    page1 = QtGui.QWizardPage()
    page1.setTitle("Название страницы 1")
    label1 = QtGui.QLabel("Содержимое страницы 1")
    line1 = QtGui.QLineEdit()
    box1 = QtGui.QVBoxLayout()
    box1.addWidget(label1)
    box1.addWidget(line1)
    page1.setLayout(box1)
    page1.registerField("line1*", line1)

    page2 = QtGui.QWizardPage()
    page2.setTitle("Название страницы 2")
    page2.setSubTitle("Подзаголовок на странице 2")
    label2 = QtGui.QLabel("Содержимое страницы 2")
    line2 = QtGui.QLineEdit()
    box2 = QtGui.QVBoxLayout()
    box2.addWidget(label2)
    box2.addWidget(line2)
    page2.setLayout(box2)
    page2.registerField("line2*", line2)

    wizard.addPage(page1)
    wizard.setPage(1, page2)

    result = wizard.exec_()
    if result == QtGui.QDialog.Accepted:
        print("Нажата кнопка Finish")
        print(line1.text(), wizard.field("line1"))
        print(line2.text(), wizard.field("line2"))
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>",
              result)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QWizard")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())