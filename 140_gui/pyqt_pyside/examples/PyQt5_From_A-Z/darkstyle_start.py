import sys
from PyQt5.QtWidgets import *
import qdarkstyle
import styles_finished as qss

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Come on over to the darkstyle")

        self.gbxDarkStyle = QGroupBox("Dark style")
        self.gbxDarkStyle.setCheckable(True)

        self.optNormal = QRadioButton("Normal")
        self.optNormal.setChecked(True)

        self.optDark = QRadioButton("Dark style")

        self.txtStyle = QPlainTextEdit()

        self.lytBtns = QVBoxLayout()
        self.lytBtns.addWidget(self.optNormal)
        self.lytBtns.addWidget(self.optDark)

        self.lytGBox = QHBoxLayout()
        self.lytGBox.addLayout(self.lytBtns)
        self.lytGBox.addWidget(self.txtStyle)

        self.gbxDarkStyle.setLayout(self.lytGBox)

        self.lytMain = QHBoxLayout()
        self.lytMain.addWidget(self.gbxDarkStyle)

        self.setLayout(self.lytMain)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())