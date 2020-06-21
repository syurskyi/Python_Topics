# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from employee_full_info import EmployeeFullInfo
from ui_calendar_dialog import CalendarDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 429)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(Dialog)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(Dialog)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(Dialog)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayToolButton = QtWidgets.QToolButton(Dialog)
        self.birthdayToolButton.setText("")
        self.birthdayToolButton.setObjectName("birthdayToolButton")

        self.birthdayToolButton.setIcon(QtGui.QIcon(":/resources/ic-calendar.png"))

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.birthdayToolButton)
        self.departmentLabel = QtWidgets.QLabel(Dialog)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(Dialog)
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.salaryLabel = QtWidgets.QLabel(Dialog)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(Dialog)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Empoyee"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name"))
        self.birthdayLabel.setText(_translate("Dialog", "Birthday"))
        self.departmentLabel.setText(_translate("Dialog", "Department"))
        self.salaryLabel.setText(_translate("Dialog", "Salary"))
        self.positionLabel.setText(_translate("Dialog", "Position"))
        self.saveButton.setText(_translate("Dialog", "Save"))


class EmployeeDialog(QtWidgets.QDialog):

    def __init__(self):
        super(EmployeeDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.employeeInfo = None

        self.ui.saveButton.clicked.connect(self.save_button_clicked)
        self.ui.birthdayToolButton.clicked.connect(self.birthday_button_clicked)

    def save_button_clicked(self):
        self.employeeInfo = EmployeeFullInfo(
            self.ui.firstNameLineEdit.text(),
            self.ui.lastNameLineEdit.text(),
            self.birthday,
            self.ui.departmentLineEdit.text(),
            self.ui.salaryLineEdit.text(),
            self.ui.positionLineEdit.text())

        self.accept()

    def birthday_button_clicked(self):
        self.calendarDialog = CalendarDialog()
        result = self.calendarDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.birthday = self.calendarDialog.date

