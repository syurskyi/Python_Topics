# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, QtGui, ?W..

class Ui_MainWindow(object):
    ___ setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 279)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget _ ?W...QWidget(MainWindow)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Maximum, ?W...QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 _ ?W...QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout _ ?W...QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout _ ?W...QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton _ ?W...?PB..(self.centralWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(25, 20))
        self.closeButton.setMaximumSize(QtCore.QSize(25, 20))
        self.closeButton.setBaseSize(QtCore.QSize(2, 0))
        font _ QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moreButton _ ?W...?PB..(self.centralWidget)
        self.moreButton.setMinimumSize(QtCore.QSize(25, 25))
        self.moreButton.setMaximumSize(QtCore.QSize(25, 25))
        font _ QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.moreButton.setFont(font)
        self.moreButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        self.moreButton.setObjectName("moreButton")
        self.horizontalLayout.addWidget(self.moreButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit _ ?W...QTextEdit(self.centralWidget)
        font _ QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(?W...QFrame.NoFrame)
        self.textEdit.setFrameShadow(?W...QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi(self, MainWindow):
        _translate _ QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Failamp"))
        self.closeButton.sT..(_translate("MainWindow", "×"))
        self.moreButton.sT..(_translate("MainWindow", "＋"))

