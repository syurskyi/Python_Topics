import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        ######   Create Widgets
        self.lbl1 = QLabel("First Label")
        self.btn2 = QPushButton("Button 2")
        self.led3 = QLineEdit("Line Edit 3")
        self.cmb4 = QComboBox()
        self.cmb4.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

        ###### Setup layout
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.lbl1, 2)
        self.mainLayout.addWidget(self.btn2, 4)
        self.mainLayout.addWidget(self.led3, 4)
        self.mainLayout.addWidget(self.cmb4, 2)
        self.mainLayout.addStretch(4)

        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
