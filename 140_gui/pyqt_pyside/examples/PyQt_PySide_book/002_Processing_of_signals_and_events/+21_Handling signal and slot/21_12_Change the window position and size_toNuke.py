from PySide import QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def moveEvent(self, e):
        print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
        QtGui.QWidget.moveEvent(self, e)   # Отправляем дальше

    def resizeEvent(self, e):
        print("w = {0}; h = {1}".format(e.size().width(),
                                        e.size().height()))
        QtGui.QWidget.resizeEvent(self, e) # Отправляем дальше

def main():
    main.panel = MyWindow()
    main.panel.show()

main()