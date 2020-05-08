from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class simpleWidget(QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.label = QLabel('OUT')
        ly.addWidget(self.label)
        self.e = eventFilterClass()
        self.installEventFlter()

    def eventFilter(self, obj, event):
        # print event
        # print event.type()
        if event.type() == QEvent.Enter:
            self.label.setText('IN')
            return True
        elif event.type() == QEvent.Leave:
            self.label.setText('OUT')
            return True
        return False

if __name__ == '__main':
    app = QApplication([])
    w = simpleWidget()
    w.show()
    app.exec_()