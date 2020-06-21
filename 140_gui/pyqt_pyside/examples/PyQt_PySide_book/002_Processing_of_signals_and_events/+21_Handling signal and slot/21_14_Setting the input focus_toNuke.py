from PySide import QtGui


class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, id, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, e):
        print("Receive focus field", self.id)
        QtGui.QLineEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        print("Lost focus field", self.id)
        QtGui.QLineEdit.focusOutEvent(self, e)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)
        self.button = QtGui.QPushButton("Receive focus field 2")
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

        QtGui.QWidget.setTabOrder(self.line1, self.line2)
        QtGui.QWidget.setTabOrder(self.line2, self.button)

    def on_clicked(self):
        self.line2.setFocus()

def main():
    main.panel = MyWindow()
    main.panel.show()

main()
