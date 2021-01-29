import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.dteDt = QDateTimeEdit(QDate().currentDate(), self)
        self.dteDt.setCalendarPopup(True)
        self.dteDt.move(50, 50)

        self.dteTm = QDateTimeEdit(QTime().currentTime(), self)
        self.dteTm.move(50, 80)

        self.dteDtTm = QDateTimeEdit(QDateTime(QDate.currentDate(), QTime().currentTime()), self)
        self.dteDtTm.move(50, 110)

        self.btn = QPushButton("Elapsed Time", self)
        self.btn.move(50, 140)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        seconds = QDateTime().currentDateTime().secsTo(self.dteDtTm.dateTime())
        QMessageBox.information(self, "Elapsed Time", "{} seconds have elapsed since {}".format(seconds, self.dteDtTm.dateTime().toString()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
