import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Show Message", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        msgDiskFull = QMessageBox()
        msgDiskFull.setText("Your hard drive is almost full")
        msgDiskFull.setDetailedText("Please make some room on your disk")
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle("Full Drive")
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
