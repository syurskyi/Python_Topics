

def on_tab_close(index):
    print("on_tab_close", index)


def on_current_changed(index):
    print("on_current_changed", index)


from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowTitle("Класс QTabWidget")
        self.resize(400, 350)
        tab = QtGui.QTabWidget()
        tab.currentChanged["int"].connect(on_current_changed)
        tab.tabCloseRequested["int"].connect(on_tab_close)
        tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        tab.setTabsClosable(True)
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
