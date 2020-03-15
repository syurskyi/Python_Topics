
from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtGui.QTabWidget()
tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setTabToolTip(0, "Это текст подсказки для вкладки 1")
tab.setTabToolTip(1, "Это текст подсказки для вкладки 2")
tab.setTabWhatsThis(0, "Это текст справки для вкладки 1")
tab.setTabWhatsThis(1, "Это текст справки для вкладки 2")
tab.setCurrentIndex(0)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())