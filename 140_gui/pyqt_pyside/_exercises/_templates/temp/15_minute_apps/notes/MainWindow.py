# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow(object):
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 279)
        MainWindow.setAutoFillBackground(True)
        centralWidget _ ?W...QWidget(MainWindow)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Maximum, ?W...QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centralWidget.sizePolicy().hasHeightForWidth())
        centralWidget.sSP..(sizePolicy)
        centralWidget.setObjectName("centralWidget")
        verticalLayout_2 _ ?W...QVBoxLayout(centralWidget)
        verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        verticalLayout_2.setSpacing(6)
        verticalLayout_2.setObjectName("verticalLayout_2")
        verticalLayout _ ?W...?VBL..
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout _ ?W...QHBoxLayout()
        horizontalLayout.setSpacing(6)
        horizontalLayout.setObjectName("horizontalLayout")
        closeButton _ ?W...?PB..(centralWidget)
        closeButton.setMinimumSize(?C...QSize(25, 20))
        closeButton.setMaximumSize(?C...QSize(25, 20))
        closeButton.setBaseSize(?C...QSize(2, 0))
        font _ ?G...QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        closeButton.setFont(font)
        closeButton.setLayoutDirection(?C...__.LeftToRight)
        closeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        closeButton.setObjectName("closeButton")
        horizontalLayout.aW..(closeButton)
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        moreButton _ ?W...?PB..(centralWidget)
        moreButton.setMinimumSize(?C...QSize(25, 25))
        moreButton.setMaximumSize(?C...QSize(25, 25))
        font _ ?G...QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        moreButton.setFont(font)
        moreButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        moreButton.setObjectName("moreButton")
        horizontalLayout.aW..(moreButton)
        verticalLayout.aL..(horizontalLayout)
        textEdit _ ?W...QTextEdit(centralWidget)
        font _ ?G...QFont()
        font.setPointSize(18)
        textEdit.setFont(font)
        textEdit.setFrameShape(?W...QFrame.NoFrame)
        textEdit.setFrameShadow(?W...QFrame.Plain)
        textEdit.setLineWidth(0)
        textEdit.setObjectName("textEdit")
        verticalLayout.aW..(textEdit)
        verticalLayout_2.aL..(verticalLayout)
        MainWindow.sCW..(centralWidget)

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C...QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Failamp"))
        closeButton.sT..(_translate("MainWindow", "×"))
        moreButton.sT..(_translate("MainWindow", "＋"))

