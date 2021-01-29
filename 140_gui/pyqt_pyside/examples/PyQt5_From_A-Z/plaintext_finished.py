import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.ted = QPlainTextEdit('This nest was surveyed for 4 consecutive years without any fledgelings')

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.ted)

        self.setLayout(self.lytMain)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
