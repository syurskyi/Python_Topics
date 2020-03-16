import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Get Amounts of Knobs", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Get Name of Node", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.button1Clicked)
        btn2.clicked.connect(self.button2Clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def button1Clicked(self):

        num = nuke.selectedNode().getNumKnobs()
        self.statusBar().showMessage('Number of knobs in Selected node is: ' + str(num))

    def button2Clicked(self):

        name = nuke.selectedNode().knob('name').getValue()
        self.statusBar().showMessage('Name of the Selected node is: ' + str(name))


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = Example()
    main.show()

    if app is not None:
        app.exec_()