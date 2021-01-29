import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Open File", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QFileDialog.getOpenFileNames(self, "Open File", "/Users/lstomsl", "JPG File (*.jpg);;PNG Files (*.png)")
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
