from PySide.QtCore import *
from PySide.QtGui import *

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage2)

    def showMessage2(self):
        i = QInputDialog.getItem(self, 'Enter text', 'Name:',  # Tak kak eto staticheskij metod, mu mozem vuzvat' ne sozdavaja ekzempljar klassa
                                 [str(x) for x in range(10)])
        print i

    def showMessage(self):
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detail text')
        ret = msgBox.exec_()
        print ret == QMessageBox.Save




def main():
    global c
    c = simpleWindow()
    c.raise_()
    c.show()

main()