import sys
from PyQt5.QtWidgets import *
import second

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = second.DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())