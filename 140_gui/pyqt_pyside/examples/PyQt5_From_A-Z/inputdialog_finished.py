import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Show Input", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        lstColor = ["Red", "Green", "Blue"]
        sColor, bOk = QInputDialog.getItem(self, "Text", "Enter your favorite color: ", lstColor, editable=False)
        if bOk:
            QMessageBox.information(self, "Name", "Your favorite color is "+sColor)
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
