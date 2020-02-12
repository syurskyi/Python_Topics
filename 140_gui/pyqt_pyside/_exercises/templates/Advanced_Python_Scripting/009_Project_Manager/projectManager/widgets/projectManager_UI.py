# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
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

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName(_fromUtf8("projectManager"))
        projectManager.resize(508, 384)
        self.centralwidget = QtGui.QWidget(projectManager)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.projectList_ly = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.projectList_ly.setMargin(0)
        self.projectList_ly.setObjectName(_fromUtf8("projectList_ly"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.create_btn = QtGui.QPushButton(self.widget)
        self.create_btn.setObjectName(_fromUtf8("create_btn"))
        self.verticalLayout.addWidget(self.create_btn)
        self.templateEditor_btn = QtGui.QPushButton(self.widget)
        self.templateEditor_btn.setObjectName(_fromUtf8("templateEditor_btn"))
        self.verticalLayout.addWidget(self.templateEditor_btn)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.info_lb = QtGui.QLabel(self.groupBox)
        self.info_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_lb.setObjectName(_fromUtf8("info_lb"))
        self.verticalLayout_3.addWidget(self.info_lb)
        self.verticalLayout.addWidget(self.groupBox)
        self.settings_btn = QtGui.QPushButton(self.widget)
        self.settings_btn.setObjectName(_fromUtf8("settings_btn"))
        self.verticalLayout.addWidget(self.settings_btn)
        self.verticalLayout_2.addWidget(self.splitter)
        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(_translate("projectManager", "Project Manager", None))
        self.create_btn.setText(_translate("projectManager", "Create Project", None))
        self.templateEditor_btn.setText(_translate("projectManager", "Template Editor", None))
        self.groupBox.setTitle(_translate("projectManager", "Info", None))
        self.info_lb.setText(_translate("projectManager", "TextLabel", None))
        self.settings_btn.setText(_translate("projectManager", "Settings", None))

