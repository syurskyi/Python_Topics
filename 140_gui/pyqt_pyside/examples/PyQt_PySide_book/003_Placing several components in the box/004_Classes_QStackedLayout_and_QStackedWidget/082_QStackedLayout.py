# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

def on_clicked_button1():
    stack.setCurrentIndex(id1)      # Изменение по индексу

def on_clicked_button2():
    stack.setCurrentWidget(label2)  # Изменение по ссылке

def on_current_changed(index):      # Вызывается при изменении компонента
    print(index)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QStackedLayout")
window.resize(300, 250)
label1 = QtWidgets.QLabel("Страница 1")
label2 = QtWidgets.QLabel("Страница 2")
label1.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
button1 = QtWidgets.QPushButton("Отобразить страницу 1")
button2 = QtWidgets.QPushButton("Отобразить страницу 2")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)

vbox = QtWidgets.QVBoxLayout()
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
vbox.addLayout(hbox)

stack = QtWidgets.QStackedLayout()
id1 = stack.addWidget(label1)
id2 = stack.addWidget(label2)
vbox.addLayout(stack)

# Назначение обработчика смены компонента
stack.currentChanged["int"].connect(on_current_changed)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())