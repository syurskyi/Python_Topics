# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\013_ImageConverter\imageConverter\widgets\imageConverter.ui'
#
# Created: Wed Nov 29 22:31:01 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        imageConverter.setObjectName("imageConverter")
        imageConverter.resize(456, 399)
        self.centralwidget = QtWidgets.QWidget(imageConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconver_lb = QtWidgets.QLabel(self.centralwidget)
        self.iconver_lb.setObjectName("iconver_lb")
        self.horizontalLayout.addWidget(self.iconver_lb)
        self.browseIconvert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browseIconvert_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseIconvert_btn.setObjectName("browseIconvert_btn")
        self.horizontalLayout.addWidget(self.browseIconvert_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.files_ly = QtWidgets.QVBoxLayout()
        self.files_ly.setObjectName("files_ly")
        self.verticalLayout.addLayout(self.files_ly)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.out_le = QtWidgets.QLineEdit(self.centralwidget)
        self.out_le.setObjectName("out_le")
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseOut_btn.setObjectName("browseOut_btn")
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)
        QtCore.QMetaObject.connectSlotsByName(imageConverter)

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(QtWidgets.QApplication.translate("imageConverter", "MainWindow", None))
        self.iconver_lb.setText(QtWidgets.QApplication.translate("imageConverter", "Path", None))
        self.browseIconvert_btn.setText(QtWidgets.QApplication.translate("imageConverter", "...", None))
        self.browseOut_btn.setText(QtWidgets.QApplication.translate("imageConverter", "...", None))
        self.start_btn.setText(QtWidgets.QApplication.translate("imageConverter", "Start", None))

