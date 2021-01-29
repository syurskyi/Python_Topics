import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(400, 400)
        self.btn = QPushButton("Get Font", self)
        self.btn.move(130, 180)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        font, bOk = QFontDialog.getFont()
        if bOk:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn.setFont(font)
        else:
            font = QFont("Times New Roman", 24, 81, True)
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn.setFont(font)

        font = QFont("Arial", 24, 81, True)
        print(font.family())
        print(font.italic())
        print(font.bold())
        print(font.weight())
        print(font.pointSize())
        self.btn.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())