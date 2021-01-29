import sys
from PyQt5.QtWidgets import *


class FunnyButton(QPushButton):
    def __init__(self, txt, parent):
        QPushButton.__init__(self, txt, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, evt):
        #print('Mouse moved!')
        if evt.y()<self.height()/2:
            self.move(self.pos().x()+evt.x(), self.pos().y()+evt.y())
        else:
            self.move(self.pos().x()+evt.x(), self.pos().y()-self.height()+evt.y())


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.btn = FunnyButton("Click Me If You Are Smart", self)
        self.btn.move(100, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())