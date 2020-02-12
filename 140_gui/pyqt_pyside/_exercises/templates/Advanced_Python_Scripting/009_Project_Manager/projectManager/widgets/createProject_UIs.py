# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\009_Project_Manager\projectManager\widgets\createProject.ui'
#
# Created: Tue Dec 27 17:41:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(432, 298)
        self.verticalLayout = QtGui.QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(createDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_lb = QtGui.QLineEdit(createDialog)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(createDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comment_te = QtGui.QPlainTextEdit(createDialog)
        self.comment_te.setObjectName("comment_te")
        self.gridLayout.addWidget(self.comment_te, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtGui.QPushButton(createDialog)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.cancel_btn = QtGui.QPushButton(createDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QtGui.QApplication.translate("createDialog", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("createDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("createDialog", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("createDialog", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("createDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

