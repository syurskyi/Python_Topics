# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys


def on_tab_close(index):
    print("on_tab_close", index)


def on_current_changed(index):
    print("on_current_changed", index)


app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 350)
tab = QtGui.QTabWidget()
tab.currentChanged["int"].connect(on_current_changed)
tab.tabCloseRequested["int"].connect(on_tab_close)
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setTabsClosable(True)
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())