from PySide.QtGui import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()


        self.btn = QtGui.QPushButton('Get Name', self)
        self.line2 = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.line2)
        self.setLayout(layout)

        self.btn.clicked.connect(self.action)

    def action(self):
        num = nuke.selectedNode().getNumKnobs()
        self.btn.setText(str(num))

def main():
    global c
    c = Panel()
    c.show()

main()

