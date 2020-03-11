from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        layout = QVBoxLayout(self)
        button = QPushButton('Print')
        layout.addWidget(button)
        button.clicked.connect(self.action)
        line = QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.text)
        # self.connect(button, SIGNAL('clicked()'),
        #              self, SLOT('action()'))

        @button.clicked.connect
        def click():
            self.action()

    def action(self):
        print 'ACTION'

    def text(self, arg):
        print arg


app = QApplication([])
window = MyWidget()
window.show()
app.exec_()
