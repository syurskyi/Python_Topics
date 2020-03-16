from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        layout = QVBoxLayout(self)
        button = QPushButton('Print')
        layout.addWidget(button)
        line = QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.text)
        # first version
        # button.clicked.connect(self.action)
        # second version
        # self.connect(button, SIGNAL('clicked()'), self, SLOT('action()'))
        # third version
        @button.clicked.connect
        def click():
            self.action()

    # @SLOT()
    def action(self):
        print('ACTION')

    def text(self, arg):
        print(arg)



def start():
    #global form
    start.form = myWidget()
    start.form.show()

start()