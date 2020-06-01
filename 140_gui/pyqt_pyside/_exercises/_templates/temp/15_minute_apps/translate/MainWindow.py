# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 333)
        centralwidget = QtWidgets.QWidget(MainWindow)
        centralwidget.setObjectName("centralwidget")
        horizontalLayout = QtWidgets.QHBoxLayout(centralwidget)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        srcLanguage = QtWidgets.QComboBox(centralwidget)
        srcLanguage.setObjectName("srcLanguage")
        verticalLayout.addWidget(srcLanguage)
        srcTextEdit = QtWidgets.QTextEdit(centralwidget)
        srcTextEdit.setObjectName("srcTextEdit")
        verticalLayout.addWidget(srcTextEdit)
        horizontalLayout.aL..(verticalLayout)
        verticalLayout_3 = QtWidgets.QVBoxLayout()
        verticalLayout_3.setObjectName("verticalLayout_3")
        translateButton = QtWidgets.QPushButton(centralwidget)
        translateButton.setMinimumSize(QtCore.QSize(75, 50))
        translateButton.setMaximumSize(QtCore.QSize(75, 50))
        translateButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/flag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        translateButton.setIcon(icon)
        translateButton.setIconSize(QtCore.QSize(75, 50))
        translateButton.setObjectName("translateButton")
        verticalLayout_3.addWidget(translateButton)
        horizontalLayout.aL..(verticalLayout_3)
        verticalLayout_2 = QtWidgets.QVBoxLayout()
        verticalLayout_2.setObjectName("verticalLayout_2")
        destTextEdit = QtWidgets.QTextEdit(centralwidget)
        destTextEdit.setObjectName("destTextEdit")
        verticalLayout_2.addWidget(destTextEdit)
        horizontalLayout.aL..(verticalLayout_2)
        MainWindow.setCentralWidget(centralwidget)
        menubar = QtWidgets.QMenuBar(MainWindow)
        menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        menubar.setObjectName("menubar")
        MainWindow.setMenuBar(menubar)

        retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translataarrr"))
        translateButton.setToolTip(_translate("MainWindow", "Translate"))

