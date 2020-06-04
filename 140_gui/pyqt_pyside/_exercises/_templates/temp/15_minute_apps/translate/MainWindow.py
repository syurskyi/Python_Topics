# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., QtWidgets

c_ Ui_MainWindow o..
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(721, 333)
        centralwidget _ QtWidgets.?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        horizontalLayout _ QtWidgets.QHBoxLayout(centralwidget)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout _ QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        srcLanguage _ QtWidgets.?CB(centralwidget)
        srcLanguage.setObjectName("srcLanguage")
        verticalLayout.addWidget(srcLanguage)
        srcTextEdit _ QtWidgets.?TE..(centralwidget)
        srcTextEdit.setObjectName("srcTextEdit")
        verticalLayout.addWidget(srcTextEdit)
        horizontalLayout.aL..(verticalLayout)
        verticalLayout_3 _ QtWidgets.QVBoxLayout()
        verticalLayout_3.setObjectName("verticalLayout_3")
        translateButton _ QtWidgets.QPushButton(centralwidget)
        translateButton.sMS..(?C...?S..(75, 50))
        translateButton.sMS..(?C...?S..(75, 50))
        translateButton.sT..("")
        icon _ ?G...?I..
        icon.aP..(?G...?P..("images/flag.png"), ?G...?I...Normal, ?G...?I...Off)
        translateButton.sI..(icon)
        translateButton.setIconSize(?C...?S..(75, 50))
        translateButton.setObjectName("translateButton")
        verticalLayout_3.addWidget(translateButton)
        horizontalLayout.aL..(verticalLayout_3)
        verticalLayout_2 _ QtWidgets.QVBoxLayout()
        verticalLayout_2.setObjectName("verticalLayout_2")
        destTextEdit _ QtWidgets.?TE..(centralwidget)
        destTextEdit.setObjectName("destTextEdit")
        verticalLayout_2.addWidget(destTextEdit)
        horizontalLayout.aL..(verticalLayout_2)
        MainWindow.setCentralWidget(centralwidget)
        menubar _ QtWidgets.QMenuBar(MainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 721, 22))
        menubar.setObjectName("menubar")
        MainWindow.setMenuBar(menubar)

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Translataarrr"))
        translateButton.sTT..(_translate("MainWindow", "Translate"))

