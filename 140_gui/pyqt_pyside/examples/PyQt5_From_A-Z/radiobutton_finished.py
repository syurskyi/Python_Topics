import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lbl = QLabel("My Label", self)
        self.lbl.setStyleSheet("color:red; font-size:15px")
        self.lbl.move(50, 30)

        #####   Color Button Group
        self.btgColor = QButtonGroup()

        self.rbtRed = QRadioButton("Red", self)
        self.rbtRed.move(50, 60)
        self.rbtRed.setChecked(True)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtRed)

        self.rbtBlue = QRadioButton("Blue", self)
        self.rbtBlue.move(50, 90)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtBlue)

        self.rbtGreen = QRadioButton("Green", self)
        self.rbtGreen.move(50, 120)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtGreen)

        #####   Text Size button
        self.btgSize = QButtonGroup()
        self.rbtSmall = QRadioButton("Small Text", self)
        self.rbtSmall.move(50, 150)
        self.btgSize.addButton(self.rbtSmall, 10)
        self.rbtSmall.clicked.connect(self.evt_rbt_clicked)

        self.rbtMedium = QRadioButton("Medium Text", self)
        self.rbtMedium.setChecked(True)
        self.rbtMedium.move(50, 180)
        self.btgSize.addButton(self.rbtMedium, 15)
        self.rbtMedium.clicked.connect(self.evt_rbt_clicked)

        self.rbtLarge = QRadioButton("Large Text", self)
        self.rbtLarge.move(50, 210)
        self.btgSize.addButton(self.rbtLarge, 20)
        self.rbtLarge.clicked.connect(self.evt_rbt_clicked)

    def evt_rbt_clicked(self):
        clr = self.btgColor.checkedButton()
        size = self.btgSize.checkedId()
        ss = "color:"+clr.text()+"; font-size:"+str(size)+"px"
        print(ss)
        self.lbl.setStyleSheet(ss)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
