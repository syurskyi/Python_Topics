# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked_button1():
    stack.setCurrentIndex(id1)      # Изменение по индексу

def on_clicked_button2():
    stack.setCurrentWidget(label2)  # Изменение по ссылке

def on_current_changed(index):      # Вызывается при изменении компонента
    print(index)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("QStackedWidget")
window.resize(300, 250)
label1 = QtGui.QLabel("Страница 1")
label2 = QtGui.QLabel("Страница 2")
label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
button1 = QtGui.QPushButton("Отобразить страницу 1")
button2 = QtGui.QPushButton("Отобразить страницу 2")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)

vbox = QtGui.QVBoxLayout()
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)

vbox.addLayout(hbox)

stack = QtGui.QStackedWidget()
id1 = stack.addWidget(label1)
id2 = stack.addWidget(label2)
vbox.addWidget(stack)

# Назначение обработчика смены компонента
stack.currentChanged["int"].connect(on_current_changed)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())