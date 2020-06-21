from PySide2 import QtCore, QtGui, QtWidgets
import sys

class QtDialog(QtGui.QWidget):
    def __init__(self):
        super(QtDialog, self).__init__()
        self.btn = QtGui.QPushButton("Close Window")
        self.btn.setGeometry(50, 10, 200, 30)

        QtCore.QObject.connect(self.btn, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)



def main():
    main.panel = QtDialog()
    # main.panel.setWindowFlags(QtCore.Qt.Dialog)
    # main.panel.setWindowTitle("Name Window")
    # main.panel.resize(300, 50)
    # desktop = QtGui.QApplication.desktop()
    # x = (desktop.width() - main.panel.width()) // 2
    # y = (desktop.height() - main.panel.height()) // 2
    # main.panel.move(x, y)
    main.panel.show
