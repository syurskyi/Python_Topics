# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 297)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(35)
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
        self.currentPositionLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionLabel.setObjectName("currentPositionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentPositionLabel)
        self.currentPositionValueLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionValueLabel.setObjectName("currentPositionValueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentPositionValueLabel)
        self.newPositionLabel = QtWidgets.QLabel(Dialog)
        self.newPositionLabel.setObjectName("newPositionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newPositionLabel)
        self.newPositionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.newPositionLineEdit.setPlaceholderText("")
        self.newPositionLineEdit.setObjectName("newPositionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newPositionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(105, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.currentPositionLabel.setText(_translate("Dialog", "Current Position"))
        self.currentPositionValueLabel.setText(_translate("Dialog", "TextLabel"))
        self.newPositionLabel.setText(_translate("Dialog", "New Position"))
        self.saveButton.setText(_translate("Dialog", "Save"))


class PositionDialog(QtWidgets.QDialog):

    def __init__(self, first_name, last_name, current_position):
        super(PositionDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.firstNameValueLabel.setText(first_name)
        self.ui.lastNameValueLabel.setText(last_name)
        self.ui.currentPositionValueLabel.setText(current_position)

        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        self.new_position = self.ui.newPositionLineEdit.text()

        self.accept()