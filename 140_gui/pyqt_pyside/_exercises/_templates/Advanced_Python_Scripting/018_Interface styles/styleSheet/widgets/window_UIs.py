# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week7\styleSheet\widgets\window.ui'
#
# Created: Wed Nov 12 22:08:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., ?G..

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 411)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        verticalLayout _ ?G...QVBoxLayout(centralwidget)
        verticalLayout.setObjectName("verticalLayout")
        lineEdit _ ?G...QLineEdit(centralwidget)
        lE...setObjectName("lineEdit")
        verticalLayout.addWidget(lE..)
        pB__ _ ?G...?PB..(centralwidget)
        pB__.setObjectName("pushButton")
        verticalLayout.addWidget(pB__)
        horizontalSlider _ ?G...QSlider(centralwidget)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setOrientation(?C...__.Horizontal)
        horizontalSlider.setObjectName("horizontalSlider")
        verticalLayout.addWidget(horizontalSlider)
        checkBox _ ?G...QCheckBox(centralwidget)
        checkBox.setObjectName("checkBox")
        verticalLayout.addWidget(checkBox)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        radioButton_2 _ ?G...QRadioButton(centralwidget)
        radioButton_2.setChecked(T..)
        radioButton_2.setObjectName("radioButton_2")
        horizontalLayout_2.addWidget(radioButton_2)
        radioButton _ ?G...QRadioButton(centralwidget)
        radioButton.setObjectName("radioButton")
        horizontalLayout_2.addWidget(radioButton)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        treeWidget _ ?G...QTreeWidget(centralwidget)
        treeWidget.setObjectName("treeWidget")
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
        cB__.setObjectName("comboBox")
        cB__.aI..("")
        cB__.aI..("")
        cB__.aI..("")
        cB__.aI..("")
        cB__.aI..("")
        verticalLayout.addWidget(cB__)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        spinBox _ ?G...QSpinBox(centralwidget)
        sP__.setMaximum(100)
        sP__.setObjectName("spinBox")
        horizontalLayout.addWidget(sP__)
        progressBar _ ?G...QProgressBar(centralwidget)
        pB__.setProperty("value", 24)
        pB__.setObjectName("progressBar")
        horizontalLayout.addWidget(pB__)
        verticalLayout.addLayout(horizontalLayout)
        MainWindow.setCentralWidget(centralwidget)
        menubar _ ?G...QMenuBar(MainWindow)
        menubar.setGeometry(?C...?R..(0, 0, 356, 21))
        menubar.setObjectName("menubar")
        menuFile _ ?G...QMenu(menubar)
        menuFile.setObjectName("menuFile")
        menuOpen _ ?G...QMenu(menuFile)
        menuOpen.setObjectName("menuOpen")
        menuHelop _ ?G...QMenu(menubar)
        menuHelop.setObjectName("menuHelop")
        MainWindow.setMenuBar(menubar)
        actionClose _ ?G...?A__(MainWindow)
        actionClose.setObjectName("actionClose")
        actionExit _ ?G...?A__(MainWindow)
        actionExit.setObjectName("actionExit")
        actionAbout _ ?G...?A__(MainWindow)
        actionAbout.setObjectName("actionAbout")
        actionFile _ ?G...?A__(MainWindow)
        actionFile.setObjectName("actionFile")
        actionProject _ ?G...?A__(MainWindow)
        actionProject.setObjectName("actionProject")
        menuOpen.addAction(actionFile)
        menuOpen.addAction(actionProject)
        menuFile.addAction(menuOpen.menuAction())
        menuFile.addAction(actionClose)
        menuFile.addAction(actionExit)
        menuHelop.addAction(actionAbout)
        menubar.addAction(menuFile.menuAction())
        menubar.addAction(menuHelop.menuAction())

        retranslateUi(MainWindow)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL("valueChanged(int)"), pB__.sV..)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL("valueChanged(int)"), sP__.sV..)
        ?C...QObject.c..(sP__, ?C...SIGNAL("valueChanged(int)"), horizontalSlider.sV..)
        ?C...QObject.c..(sP__, ?C...SIGNAL("valueChanged(int)"), pB__.sV..)
        ?C...QObject.c..(radioButton_2, ?C...SIGNAL("toggled(bool)"), treeWidget.setEnabled)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(?G...?A...translate("MainWindow", "MainWindow", None, ?G...?A...UnicodeUTF8))
        pB__.sT..(?G...?A...translate("MainWindow", "Start", None, ?G...?A...UnicodeUTF8))
        checkBox.sT..(?G...?A...translate("MainWindow", "Show", None, ?G...?A...UnicodeUTF8))
        radioButton_2.sT..(?G...?A...translate("MainWindow", "Enable", None, ?G...?A...UnicodeUTF8))
        radioButton.sT..(?G...?A...translate("MainWindow", "Disable", None, ?G...?A...UnicodeUTF8))
        treeWidget.headerItem.sT..(0, ?G...?A...translate("MainWindow", "1", None, ?G...?A...UnicodeUTF8))
        __sortingEnabled _ treeWidget.isSortingEnabled
        treeWidget.setSortingEnabled(F..)
        treeWidget.topLevelItem(0).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).child(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(1).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(2).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(1).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(2).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(3).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(3).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.setSortingEnabled(__sortingEnabled)
        cB__.setItemText(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        cB__.setItemText(1, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        cB__.setItemText(2, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        cB__.setItemText(3, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        cB__.setItemText(4, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        menuFile.setTitle(?G...?A...translate("MainWindow", "File", None, ?G...?A...UnicodeUTF8))
        menuOpen.setTitle(?G...?A...translate("MainWindow", "Open", None, ?G...?A...UnicodeUTF8))
        menuHelop.setTitle(?G...?A...translate("MainWindow", "Help", None, ?G...?A...UnicodeUTF8))
        actionClose.sT..(?G...?A...translate("MainWindow", "Close", None, ?G...?A...UnicodeUTF8))
        actionExit.sT..(?G...?A...translate("MainWindow", "Exit", None, ?G...?A...UnicodeUTF8))
        actionAbout.sT..(?G...?A...translate("MainWindow", "About", None, ?G...?A...UnicodeUTF8))
        actionFile.sT..(?G...?A...translate("MainWindow", "File", None, ?G...?A...UnicodeUTF8))
        actionProject.sT..(?G...?A...translate("MainWindow", "Project", None, ?G...?A...UnicodeUTF8))

