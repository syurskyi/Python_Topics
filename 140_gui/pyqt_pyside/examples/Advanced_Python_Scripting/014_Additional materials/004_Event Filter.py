from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class simpleWidget(QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.e = eventFilterClass()
        self.installEventFlter()

class eventFilterClass(QObject):
    def __init__(self):
        super(eventFilterClass, self).__init__()

    def eventFilter(self, obj, event):
        # print event
        # print event.type()
        if event.type() == QEvent.Enter:
            print('ender')
            return True
        elif event.type() == QEvent.Leave:
            print('leave')
            return True
        return False

if __name__ == '__main':
    app = QApplication([])
    w = simpleWidget()
    w.show()
    app.exec_()