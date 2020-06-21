# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 333)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(Dialog)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameValueLabel = QtWidgets.QLabel(Dialog)
        self.firstNameValueLabel.setObjectName("firstNameValueLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameValueLabel)
        self.lastNameLabel = QtWidgets.QLabel(Dialog)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameValueLabel = QtWidgets.QLabel(Dialog)
        self.lastNameValueLabel.setObjectName("lastNameValueLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameValueLabel)
        self.currentSalaryLabel = QtWidgets.QLabel(Dialog)
        self.currentSalaryLabel.setObjectName("currentSalaryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentSalaryLabel)
        self.currentSalaryValueLabel = QtWidgets.QLabel(Dialog)
        self.currentSalaryValueLabel.setObjectName("currentSalaryValueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentSalaryValueLabel)
        self.newSalaryLabel = QtWidgets.QLabel(Dialog)
        self.newSalaryLabel.setObjectName("newSalaryLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newSalaryLabel)
        self.newSalaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.newSalaryLineEdit.setObjectName("newSalaryLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newSalaryLineEdit)
        self.reasonLabel = QtWidgets.QLabel(Dialog)
        self.reasonLabel.setObjectName("reasonLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reasonLabel)
        self.reasonLineEdit = QtWidgets.QLineEdit(Dialog)
        self.reasonLineEdit.setObjectName("reasonLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reasonLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(122, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(121, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name"))
        self.firstNameValueLabel.setText(_translate("Dialog", "Grey"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name"))
        self.lastNameValueLabel.setText(_translate("Dialog", "Yurskyi"))
        self.currentSalaryLabel.setText(_translate("Dialog", "Current Salary"))
        self.currentSalaryValueLabel.setText(_translate("Dialog", "20"))
        self.newSalaryLabel.setText(_translate("Dialog", "New Salary"))
        self.reasonLabel.setText(_translate("Dialog", "Reason"))
        self.reasonLineEdit.setPlaceholderText(_translate("Dialog", "Optional"))
        self.saveButton.setText(_translate("Dialog", "Save"))

class SalaryDialog(QtWidgets.QDialog):

    def __init__(self, first_name, last_name, current_salary):
        super(SalaryDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.firstNameValueLabel.setText(first_name)
        self.ui.lastNameValueLabel.setText(last_name)
        self.ui.currentSalaryValueLabel.setText(current_salary)

        
        
        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        self.new_salary = self.ui.newSalaryLineEdit.text()
        self.reason = self.ui.reasonLineEdit.text()

        self.accept()
