def on_clicked_button1():
    stack.setCurrentIndex(id1)      # Изменение по индексу

def on_clicked_button2():
    stack.setCurrentWidget(label2)  # Изменение по ссылке

def on_current_changed(index):      # Вызывается при изменении компонента
    print(index)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("QStackedLayout")
        self.resize(300, 250)
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

        stack = QtGui.QStackedLayout()
        id1 = stack.addWidget(label1)
        id2 = stack.addWidget(label2)
        vbox.addLayout(stack)

        # Назначение обработчика смены компонента
        stack.currentChanged["int"].connect(on_current_changed)

        self.setLayout(vbox)
