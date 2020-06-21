
def insert_tab():
    tab.setUpdatesEnabled(False) # Для предотвращения мерцания
    ind = tab.insertTab(0, QtGui.QLabel("Содержимое вкладки 3"),
                        "Вкладка &3")
    tab.setCurrentIndex(ind)
    tab.setUpdatesEnabled(True) # Устанавливаем обратно
    button.setEnabled(False)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QTabWidget")
        self.resize(400, 150)
        tab = QtGui.QTabWidget()
        button = QtGui.QPushButton("Добавить вкладку")
        button.clicked.connect(insert_tab)
        tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        vbox.addWidget(button)
        self.setLayout(vbox)
