from PySide import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Generating a signal from the program")
        self.resize(300, 100)
        self.button1 = QtGui.QPushButton("Click me")
        self.button2 = QtGui.QPushButton("Button 2")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.connect(self.button1, QtCore.SIGNAL("clicked()"),
                     self.on_clicked_button1)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"),
                     self.on_clicked_button2)
        self.connect(self.button2, QtCore.SIGNAL("mysignal"),
                     self.on_mysignal)

    def on_clicked_button1(self):
        print("Button1 pressed")
        # Генерируем сигналы
        self.button2.emit(QtCore.SIGNAL("clicked(bool)"), False)
        self.button2.emit(QtCore.SIGNAL("on_mysignal"), 10, 20)

    def on_clicked_button2(self):
        print("Button2 pressed")

    def on_mysignal(self, x, y):
        print("The user signal mysignal ()")
        print("x =", x, "y =", y)


def main():
    main.panel = MyWindow()
    main.panel.show()


main()