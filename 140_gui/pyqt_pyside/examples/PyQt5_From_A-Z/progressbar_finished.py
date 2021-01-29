import sys, time
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.prg = QProgressBar()
        self.prg.setStyle(QStyleFactory.create("Windows"))
        self.prg.setTextVisible(True)

        self.btnStart = QPushButton("Start")
        self.btnStart.clicked.connect(self.evt_btnStart_clicked)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.prg)
        self.lytMain.addWidget(self.btnStart)
        self.setLayout(self.lytMain)

    def evt_btnStart_clicked(self):
        for x in range(100):
            print(x)
            time.sleep(0.1)
            self.prg.setValue(x)
            app.processEvents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
