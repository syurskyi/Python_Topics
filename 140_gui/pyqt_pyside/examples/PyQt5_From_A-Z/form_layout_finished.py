import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        #######  Create Widgets
        self.ledFname = QLineEdit("Joe")
        self.ledLname = QLineEdit("Smith")
        self.dteStarted = QDateTimeEdit()
        self.spbAge = QSpinBox()
        self.btnSubmit = QPushButton("Submit")

        #######   Setup Layout

        self.mainLayout = QFormLayout()
        self.mainLayout.setLabelAlignment(Qt.AlignLeft)
        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.mainLayout.addRow("First Name:", self.ledFname)
        self.mainLayout.addRow("Lasst Name:", self.ledLname)
        self.mainLayout.addRow("Date started:", self.dteStarted)
        self.mainLayout.addRow("Age:", self.spbAge)
        self.mainLayout.addRow("", self.btnSubmit)

        self.setLayout(self.mainLayout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
