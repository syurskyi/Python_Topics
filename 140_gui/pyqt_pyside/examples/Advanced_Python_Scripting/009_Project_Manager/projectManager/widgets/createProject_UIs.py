# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\createProject.ui'
#
# Created: Thu Oct 09 13:31:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(240, 219)
        self.verticalLayout = QtWidgets.QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(createDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_lb = QtWidgets.QLineEdit(createDialog)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(createDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comment_te = QtWidgets.QPlainTextEdit(createDialog)
        self.comment_te.setObjectName("comment_te")
        self.gridLayout.addWidget(self.comment_te, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtWidgets.QPushButton(createDialog)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.cancel_btn = QtWidgets.QPushButton(createDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QtWidgets.QApplication.translate("createDialog", "Dialog", None))
        self.label.setText(QtWidgets.QApplication.translate("createDialog", "Name", None))
        self.label_2.setText(QtWidgets.QApplication.translate("createDialog", "Comment", None))
        self.create_btn.setText(QtWidgets.QApplication.translate("createDialog", "Create", None))
        self.cancel_btn.setText(QtWidgets.QApplication.translate("createDialog", "Cancel", None))

