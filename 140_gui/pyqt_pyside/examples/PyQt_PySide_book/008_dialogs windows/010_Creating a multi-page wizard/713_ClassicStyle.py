# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys


class MyPage1(QtGui.QWizardPage):
    def __init__(self, parent=None):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 1")
        self.label1 = QtGui.QLabel("Содержимое страницы 1")
        self.line1 = QtGui.QLineEdit()
        self.box1 = QtGui.QVBoxLayout()
        self.box1.addWidget(self.label1)
        self.box1.addWidget(self.line1)
        self.setLayout(self.box1)
        self.registerField("line1*", self.line1)


class MyPage2(QtGui.QWizardPage):
    def __init__(self, parent=None):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 2")
        self.setSubTitle("Текст подзаголовка")
        self.label2 = QtGui.QLabel("Содержимое страницы 2")
        self.line2 = QtGui.QLineEdit()
        self.box2 = QtGui.QVBoxLayout()
        self.box2.addWidget(self.label2)
        self.box2.addWidget(self.line2)
        self.setLayout(self.box2)
        self.registerField("line2*", self.line2)


class MyPage3(QtGui.QWizardPage):
    def __init__(self, parent=None):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 3")
        self.setSubTitle("Текст подзаголовка")
        self.label3 = QtGui.QLabel("Содержимое страницы 3")
        self.line3 = QtGui.QLineEdit()
        self.box3 = QtGui.QVBoxLayout()
        self.box3.addWidget(self.label3)
        self.box3.addWidget(self.line3)
        self.setLayout(self.box3)
        self.registerField("line3*", self.line3)


class MyWizard(QtGui.QWizard):
    def __init__(self, parent=None):
        QtGui.QWizard.__init__(self, parent)
        self.setWindowTitle("Мой мастер")
        self.setWizardStyle(QtGui.QWizard.ClassicStyle)

        self.page1 = MyPage1()
        self.page2 = MyPage2()
        self.page3 = MyPage3()
        self.idPage1 = self.addPage(self.page1)
        self.idPage2 = self.addPage(self.page2)
        self.idPage3 = self.addPage(self.page3)


def on_clicked():
    wizard = MyWizard(window)
    result = wizard.exec_()
    if result == QtGui.QDialog.Accepted:
        print("Нажата кнопка Finish")
        print(wizard.field("line1"))
        print(wizard.field("line2"))
        print(wizard.field("line3"))
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