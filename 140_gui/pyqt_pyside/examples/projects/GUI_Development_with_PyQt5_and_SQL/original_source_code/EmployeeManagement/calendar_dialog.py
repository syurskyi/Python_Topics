

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 270)
        Dialog.setMinimumSize(QtCore.QSize(322, 270))
        Dialog.setMaximumSize(QtCore.QSize(322, 270))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        Dialog.setStyleSheet("""
            QDialog {
                background-color: #ced3e0;
            }

            QPushButton {
                border-radius: 5px;
                padding-left: 10px;
                padding-right: 10px;
                padding-top:4px;
                padding-bottom:4px;
                font-size: 8pt;
                font-family: Verdana;
                border: 1px solid rgb(45,52,71);
                color:white;
                background-color: rgb(94,109,148);
            }

            QPushButton:hover {
                background-color: rgb(112, 126, 164);
            }

            QPushButton:hover:pressed {
                background-color: rgb(129, 141, 175);
            }
            """)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Birthday Picker"))
        self.saveButton.setText(_translate("Dialog", "Save"))


class CalendarDialog(QtWidgets.QDialog):


    def __init__(self):
        super(CalendarDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.date = None

        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        self.date = self.ui.calendarWidget.selectedDate()
        self.done(QtWidgets.QDialog.Accepted)
