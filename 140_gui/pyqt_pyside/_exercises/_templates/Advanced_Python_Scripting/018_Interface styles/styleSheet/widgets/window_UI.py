# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week7\styleSheet\widgets\window.ui'
#
# Created: Wed Nov 12 22:08:44 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., ?G..

___
    _fromUtf8 _ ?C...QString.fromUtf8
_____ AttributeError:
    ___ _fromUtf8(s
        r_ s

___
    _encoding _ ?G...?A...UnicodeUTF8
    ___ _translate(context, t.., disambig
        r_ ?G...?A...translate(context, t.., disambig, _encoding)
_____ AttributeError:
    ___ _translate(context, t.., disambig
        r_ ?G...?A...translate(context, t.., disambig)

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.r..(356, 411)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout _ ?G...QVBoxLayout(centralwidget)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        lineEdit _ ?G...QLineEdit(centralwidget)
        lE...setObjectName(_fromUtf8("lineEdit"))
        verticalLayout.addWidget(lE..)
        pB__ _ ?G...?PB..(centralwidget)
        pB__.setObjectName(_fromUtf8("pushButton"))
        verticalLayout.addWidget(pB__)
        horizontalSlider _ ?G...QSlider(centralwidget)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setOrientation(?C...__.Horizontal)
        horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        verticalLayout.addWidget(horizontalSlider)
        checkBox _ ?G...QCheckBox(centralwidget)
        checkBox.setObjectName(_fromUtf8("checkBox"))
        verticalLayout.addWidget(checkBox)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        radioButton_2 _ ?G...QRadioButton(centralwidget)
        radioButton_2.setChecked(T..)
        radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        horizontalLayout_2.addWidget(radioButton_2)
        radioButton _ ?G...QRadioButton(centralwidget)
        radioButton.setObjectName(_fromUtf8("radioButton"))
        horizontalLayout_2.addWidget(radioButton)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        treeWidget _ ?G...QTreeWidget(centralwidget)
        treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_2 _ ?G...QTreeWidgetItem(item_1)
        item_3 _ ?G...QTreeWidgetItem(item_2)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        verticalLayout.addWidget(treeWidget)
        cB__ _ ?G...QComboBox(centralwidget)
        cB__.setObjectName(_fromUtf8("comboBox"))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        verticalLayout.addWidget(cB__)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spinBox _ ?G...QSpinBox(centralwidget)
        sP__.setMaximum(100)
        sP__.setObjectName(_fromUtf8("spinBox"))
        horizontalLayout.addWidget(sP__)
        progressBar _ ?G...QProgressBar(centralwidget)
        pB__.setProperty("value", 24)
        pB__.setObjectName(_fromUtf8("progressBar"))
        horizontalLayout.addWidget(pB__)
        verticalLayout.addLayout(horizontalLayout)
        MainWindow.setCentralWidget(centralwidget)
        menubar _ ?G...QMenuBar(MainWindow)
        menubar.setGeometry(?C...?R..(0, 0, 356, 21))
        menubar.setObjectName(_fromUtf8("menubar"))
        menuFile _ ?G...QMenu(menubar)
        menuFile.setObjectName(_fromUtf8("menuFile"))
        menuOpen _ ?G...QMenu(menuFile)
        menuOpen.setObjectName(_fromUtf8("menuOpen"))
        menuHelop _ ?G...QMenu(menubar)
        menuHelop.setObjectName(_fromUtf8("menuHelop"))
        MainWindow.setMenuBar(menubar)
        actionClose _ ?G...?A__(MainWindow)
        actionClose.setObjectName(_fromUtf8("actionClose"))
        actionExit _ ?G...?A__(MainWindow)
        actionExit.setObjectName(_fromUtf8("actionExit"))
        actionAbout _ ?G...?A__(MainWindow)
        actionAbout.setObjectName(_fromUtf8("actionAbout"))
        actionFile _ ?G...?A__(MainWindow)
        actionFile.setObjectName(_fromUtf8("actionFile"))
        actionProject _ ?G...?A__(MainWindow)
        actionProject.setObjectName(_fromUtf8("actionProject"))
        menuOpen.addAction(actionFile)
        menuOpen.addAction(actionProject)
        menuFile.addAction(menuOpen.menuAction())
        menuFile.addAction(actionClose)
        menuFile.addAction(actionExit)
        menuHelop.addAction(actionAbout)
        menubar.addAction(menuFile.menuAction())
        menubar.addAction(menuHelop.menuAction())

        retranslateUi(MainWindow)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), pB__.sV..)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), sP__.sV..)
        ?C...QObject.c..(sP__, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), horizontalSlider.sV..)
        ?C...QObject.c..(sP__, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), pB__.sV..)
        ?C...QObject.c..(radioButton_2, ?C...SIGNAL(_fromUtf8("toggled(bool)")), treeWidget.setEnabled)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", N..))
        pB__.sT..(_translate("MainWindow", "Start", N..))
        checkBox.sT..(_translate("MainWindow", "Show", N..))
        radioButton_2.sT..(_translate("MainWindow", "Enable", N..))
        radioButton.sT..(_translate("MainWindow", "Disable", N..))
        treeWidget.headerItem.sT..(0, _translate("MainWindow", "1", N..))
        __sortingEnabled _ treeWidget.isSortingEnabled
        treeWidget.setSortingEnabled(F..)
        treeWidget.topLevelItem(0).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(0).child(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(1).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(2).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(1).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(2).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(3).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(3).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.setSortingEnabled(__sortingEnabled)
        cB__.setItemText(0, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(1, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(2, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(3, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(4, _translate("MainWindow", "New Item", N..))
        menuFile.setTitle(_translate("MainWindow", "File", N..))
        menuOpen.setTitle(_translate("MainWindow", "Open", N..))
        menuHelop.setTitle(_translate("MainWindow", "Help", N..))
        actionClose.sT..(_translate("MainWindow", "Close", N..))
        actionExit.sT..(_translate("MainWindow", "Exit", N..))
        actionAbout.sT..(_translate("MainWindow", "About", N..))
        actionFile.sT..(_translate("MainWindow", "File", N..))
        actionProject.sT..(_translate("MainWindow", "Project", N..))

