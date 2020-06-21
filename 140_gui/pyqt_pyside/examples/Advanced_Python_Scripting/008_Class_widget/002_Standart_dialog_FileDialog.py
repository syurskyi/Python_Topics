from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from PyQt4.QtGui import *

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn  = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300,200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        # _filter = '*.py'
        # _filter = '*.py;;*.txt'
        # _filter = '*.py *.txt'
        # _filter = '*.py *.txt;;cmd.exe'
        # _filter = 'Python File(*.py);; All(*.*)'
        d = QFileDialog.getExistingDirectory(self, 'Set folder', 'c:/Users') # staticheskaja peremenaja getExistingDirectory
                                                                             # vozvrachaet pyt' k direktorii
        # d = QFileDialog.getOpenFileName(self, 'Set folder', 'c:/tmp', _filter)
        # d = QFileDialog.getOpenFileNames(self, 'Set folder', 'c:/Users', _filter)
        print(d, type(d))

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()