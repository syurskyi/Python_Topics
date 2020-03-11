# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week4\imageConverter\widgets\imageConverter.ui'
#
# Created: Tue Oct 21 17:49:06 2014
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

class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        imageConverter.setObjectName(_fromUtf8("imageConverter"))
        imageConverter.resize(339, 379)
        self.centralwidget = QtGui.QWidget(imageConverter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.iconvert_lb = QtGui.QLabel(self.centralwidget)
        self.iconvert_lb.setObjectName(_fromUtf8("iconvert_lb"))
        self.horizontalLayout.addWidget(self.iconvert_lb)
        self.browseIconvert_btn = QtGui.QPushButton(self.centralwidget)
        self.browseIconvert_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseIconvert_btn.setObjectName(_fromUtf8("browseIconvert_btn"))
        self.horizontalLayout.addWidget(self.browseIconvert_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.files_ly = QtGui.QVBoxLayout()
        self.files_ly.setObjectName(_fromUtf8("files_ly"))
        self.verticalLayout.addLayout(self.files_ly)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.out_le = QtGui.QLineEdit(self.centralwidget)
        self.out_le.setObjectName(_fromUtf8("out_le"))
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtGui.QPushButton(self.centralwidget)
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseOut_btn.setObjectName(_fromUtf8("browseOut_btn"))
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_btn = QtGui.QPushButton(self.centralwidget)
        self.start_btn.setObjectName(_fromUtf8("start_btn"))
        self.verticalLayout.addWidget(self.start_btn)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)
        QtCore.QMetaObject.connectSlotsByName(imageConverter)

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(_translate("imageConverter", "MainWindow", None))
        self.iconvert_lb.setText(_translate("imageConverter", "Path", None))
        self.browseIconvert_btn.setText(_translate("imageConverter", "...", None))
        self.browseOut_btn.setText(_translate("imageConverter", "...", None))
        self.start_btn.setText(_translate("imageConverter", "Strat", None))

