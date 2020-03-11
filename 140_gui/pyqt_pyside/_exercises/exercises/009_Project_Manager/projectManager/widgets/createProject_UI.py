# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\createProject.ui'
#
# Created: Thu Oct 09 13:31:13 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName(_fromUtf8("createDialog"))
        createDialog.resize(240, 219)
        self.verticalLayout = QtGui.QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(createDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_lb = QtGui.QLineEdit(createDialog)
        self.name_lb.setObjectName(_fromUtf8("name_lb"))
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(createDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comment_te = QtGui.QPlainTextEdit(createDialog)
        self.comment_te.setObjectName(_fromUtf8("comment_te"))
        self.gridLayout.addWidget(self.comment_te, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.create_btn = QtGui.QPushButton(createDialog)
        self.create_btn.setObjectName(_fromUtf8("create_btn"))
        self.horizontalLayout.addWidget(self.create_btn)
        self.cancel_btn = QtGui.QPushButton(createDialog)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(_translate("createDialog", "Dialog", None))
        self.label.setText(_translate("createDialog", "Name", None))
        self.label_2.setText(_translate("createDialog", "Comment", None))
        self.create_btn.setText(_translate("createDialog", "Create", None))
        self.cancel_btn.setText(_translate("createDialog", "Cancel", None))

