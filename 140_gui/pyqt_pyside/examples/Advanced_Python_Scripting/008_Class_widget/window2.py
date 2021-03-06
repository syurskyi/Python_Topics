from PySide2.QtGui import *
# from PyQt4.QtGui import *
from PySide2.QtWidgets import *

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn  = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300,200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        _filter = 'Python File(*.py);; All(*.*)'
        d = QFileDialog.getOpenFileName(self, 'Set folder', 'c:/tmp', _filter)
        print(d)

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()