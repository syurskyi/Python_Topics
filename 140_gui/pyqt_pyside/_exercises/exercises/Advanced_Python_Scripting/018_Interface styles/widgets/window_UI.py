# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\compileUI\window.ui'
#
# Created: Fri Dec 15 07:08:59 2017
#      by: PyQt4 UI code generator 4.10.1
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
        MainWindow.r..(478, 496)
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
        horizontalSlider.setOrientation(?C...__.Horizontal)
        horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        verticalLayout.addWidget(horizontalSlider)
        checkBox _ ?G...QCheckBox(centralwidget)
        checkBox.setObjectName(_fromUtf8("checkBox"))
        verticalLayout.addWidget(checkBox)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        radioButton _ ?G...QRadioButton(centralwidget)
        radioButton.setObjectName(_fromUtf8("radioButton"))
        horizontalLayout_2.addWidget(radioButton)
        radioButton_2 _ ?G...QRadioButton(centralwidget)
        radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        horizontalLayout_2.addWidget(radioButton_2)
        verticalLayout.addLayout(horizontalLayout_2)
        treeWidget _ ?G...QTreeWidget(centralwidget)
        treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_2 _ ?G...QTreeWidgetItem(item_1)
        item_3 _ ?G...QTreeWidgetItem(item_2)
        item_3 _ ?G...QTreeWidgetItem(item_2)
        item_3 _ ?G...QTreeWidgetItem(item_2)
        item_2 _ ?G...QTreeWidgetItem(item_1)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_1 _ ?G...QTreeWidgetItem(item_0)
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
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        cB__.aI..(_fromUtf8(""))
        verticalLayout.addWidget(cB__)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spinBox _ ?G...QSpinBox(centralwidget)
        sP__.setObjectName(_fromUtf8("spinBox"))
        horizontalLayout.addWidget(sP__)
        progressBar _ ?G...QProgressBar(centralwidget)
        pB__.setProperty("value", 24)
        pB__.setObjectName(_fromUtf8("progressBar"))
        horizontalLayout.addWidget(pB__)
        verticalLayout.addLayout(horizontalLayout)
        MainWindow.setCentralWidget(centralwidget)
        menubar _ ?G...QMenuBar(MainWindow)
        menubar.setGeometry(?C...?R..(0, 0, 478, 21))
        menubar.setObjectName(_fromUtf8("menubar"))
        menuFile _ ?G...QMenu(menubar)
        menuFile.setObjectName(_fromUtf8("menuFile"))
        menuHelp _ ?G...QMenu(menubar)
        menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(menubar)
        actionOpen _ ?G...?assert(MainWindow)
        aO__.setObjectName(_fromUtf8("actionOpen"))
        actionClose _ ?G...?assert(MainWindow)
        actionClose.setObjectName(_fromUtf8("actionClose"))
        actionExit _ ?G...?assert(MainWindow)
        actionExit.setObjectName(_fromUtf8("actionExit"))
        actionAbout _ ?G...?assert(MainWindow)
        actionAbout.setObjectName(_fromUtf8("actionAbout"))
        menuFile.addAction(aO__)
        menuFile.addAction(actionClose)
        menuFile.addAction(actionExit)
        menuHelp.addAction(actionAbout)
        menubar.addAction(menuFile.menuAction())
        menubar.addAction(menuHelp.menuAction())

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", N..))
        pB__.sT..(_translate("MainWindow", "PushButton", N..))
        checkBox.sT..(_translate("MainWindow", "Show", N..))
        radioButton.sT..(_translate("MainWindow", "Enable", N..))
        radioButton_2.sT..(_translate("MainWindow", "Disable", N..))
        treeWidget.headerItem.sT..(0, _translate("MainWindow", "1", N..))
        __sortingEnabled _ treeWidget.isSortingEnabled
        treeWidget.setSortingEnabled(F..)
        treeWidget.topLevelItem(0).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(0).child(0).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(0).child(0).child(1).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(0).child(0).child(0).child(2).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(0).child(0).child(1).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(1).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(0).child(2).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.topLevelItem(1).sT..(0, _translate("MainWindow", "New Item", N..))
        treeWidget.topLevelItem(1).child(0).sT..(0, _translate("MainWindow", "New Subitem", N..))
        treeWidget.setSortingEnabled(__sortingEnabled)
        cB__.setItemText(0, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(1, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(2, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(3, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(4, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(5, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(6, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(7, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(8, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(9, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(10, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(11, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(12, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(13, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(14, _translate("MainWindow", "New Item", N..))
        cB__.setItemText(15, _translate("MainWindow", "New Item", N..))
        menuFile.setTitle(_translate("MainWindow", "File", N..))
        menuHelp.setTitle(_translate("MainWindow", "Help", N..))
        aO__.sT..(_translate("MainWindow", "Open", N..))
        actionClose.sT..(_translate("MainWindow", "Close", N..))
        actionExit.sT..(_translate("MainWindow", "Exit", N..))
        actionAbout.sT..(_translate("MainWindow", "About", N..))

