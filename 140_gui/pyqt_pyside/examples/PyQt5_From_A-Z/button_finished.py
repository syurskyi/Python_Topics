import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Disable Label", self)
        self.btn.setIcon(QIcon(QPixmap("fotos/search.png")))
        self.btn.setFlat(False)
        self.btn.move(40, 40)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100, 100)
        font = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.lbl.repaint()
            self.btn.setText("Enable Label")
            self.btn.repaint()
        else:
            self.lbl.setDisabled(False)
            self.lbl.repaint()
            self.btn.setText("Disable Label")
            self.btn.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
