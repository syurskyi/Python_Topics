# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(508, 384)
        self.centralwidget = QtGui.QWidget(projectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.projectList_ly = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.projectList_ly.setContentsMargins(0, 0, 0, 0)
        self.projectList_ly.setObjectName("projectList_ly")
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_btn = QtGui.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.templateEditor_btn = QtGui.QPushButton(self.widget)
        self.templateEditor_btn.setObjectName("templateEditor_btn")
        self.verticalLayout.addWidget(self.templateEditor_btn)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_lb = QtGui.QLabel(self.groupBox)
        self.info_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_lb.setObjectName("info_lb")
        self.verticalLayout_3.addWidget(self.info_lb)
        self.verticalLayout.addWidget(self.groupBox)
        self.settings_btn = QtGui.QPushButton(self.widget)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.verticalLayout_2.addWidget(self.splitter)
        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QtGui.QApplication.translate("projectManager", "Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("projectManager", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.templateEditor_btn.setText(QtGui.QApplication.translate("projectManager", "Template Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("projectManager", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.info_lb.setText(QtGui.QApplication.translate("projectManager", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_btn.setText(QtGui.QApplication.translate("projectManager", "Settings", None, QtGui.QApplication.UnicodeUTF8))

