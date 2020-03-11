# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\templateEditor.ui'
#
# Created: Thu Oct 09 13:59:10 2014
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

class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        templateEditor.setObjectName(_fromUtf8("templateEditor"))
        templateEditor.resize(357, 461)
        self.verticalLayout = QtGui.QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add_btn = QtGui.QPushButton(templateEditor)
        self.add_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.remove_btn = QtGui.QPushButton(templateEditor)
        self.remove_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName(_fromUtf8("remove_btn"))
        self.horizontalLayout_2.addWidget(self.remove_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tree = QtGui.QTreeWidget(templateEditor)
        self.tree.setObjectName(_fromUtf8("tree"))
        self.tree.headerItem().setText(0, _fromUtf8("1"))
        self.tree.header().setVisible(False)
        self.verticalLayout.addWidget(self.tree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.save_btn = QtGui.QPushButton(templateEditor)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout.addWidget(self.save_btn)
        self.close_btn = QtGui.QPushButton(templateEditor)
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(templateEditor)
        QtCore.QMetaObject.connectSlotsByName(templateEditor)

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(_translate("templateEditor", "Form", None))
        self.add_btn.setText(_translate("templateEditor", "+", None))
        self.remove_btn.setText(_translate("templateEditor", "-", None))
        self.save_btn.setText(_translate("templateEditor", "Save", None))
        self.close_btn.setText(_translate("templateEditor", "Close", None))

