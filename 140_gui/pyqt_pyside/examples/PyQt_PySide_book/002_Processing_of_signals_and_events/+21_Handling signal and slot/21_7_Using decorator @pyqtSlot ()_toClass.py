from PySide import QtCore, QtGui
import sys

class MyClass(QtGui.QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.button = QtGui.QPushButton("Click me", self)

        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"),
                               self, QtCore.SLOT("on_clicked()"))
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked(bool)"),
                               self, QtCore.SLOT("myslot(bool)"))

    @QtCore.Slot()
    def on_clicked(self):
        print("Кнопка нажата. Слот on_clicked()")

    @QtCore.Slot(bool, name="myslot")
    def on_clicked2(self, status):
        print("Кнопка нажата. Слот myslot(bool)", status)



def main():
    main.panel = MyClass()
    main.panel.show()

main()