

def on_clicked():
    toolBox.setUpdatesEnabled(False) # Для предотвращения мерцания
    index = toolBox.insertItem(0, QtGui.QLabel("Содержимое вкладки 3"),
                               "Вкладка &3")
    toolBox.setCurrentIndex(index)
    toolBox.setUpdatesEnabled(True) # Устанавливаем обратно
    button.setEnabled(False)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QToolBox")
        self.resize(300, 250)
        toolBox = QtGui.QToolBox()
        button = QtGui.QPushButton("Добавить вкладку")
        button.clicked.connect(on_clicked)
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        toolBox.addItem(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        toolBox.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(toolBox)
        vbox.addWidget(button)
        self.setLayout(vbox)
