# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week3\icon_widget\iconWidget.ui'
#
# Created: Wed Oct 15 18:38:42 2014
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
        MainWindow.r..(237, 369)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        horizontalLayout_2 _ ?G...QHBoxLayout(centralwidget)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        verticalLayout _ ?G...QVBoxLayout
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        fill_btn _ ?G...?PB..(centralwidget)
        fill_btn.setObjectName(_fromUtf8("fill_btn"))
        horizontalLayout.addWidget(fill_btn)
        clear_btn _ ?G...?PB..(centralwidget)
        clear_btn.setMinimumSize(?C...QSize(40, 0))
        clear_btn.setObjectName(_fromUtf8("clear_btn"))
        horizontalLayout.addWidget(clear_btn)
        image_lb _ ?G...QLabel(centralwidget)
        image_lb.setObjectName(_fromUtf8("image_lb"))
        horizontalLayout.addWidget(image_lb)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout)
        combo_cbb _ ?G...QComboBox(centralwidget)
        combo_cbb.setObjectName(_fromUtf8("combo_cbb"))
        verticalLayout.addWidget(combo_cbb)
        list_lwd _ ?G...?LW..(centralwidget)
        list_lwd.setObjectName(_fromUtf8("list_lwd"))
        verticalLayout.addWidget(list_lwd)
        horizontalLayout_2.addLayout(verticalLayout)
        label _ ?G...QLabel(centralwidget)
        label.sT..(_fromUtf8(""))
        label.setObjectName(_fromUtf8("label"))
        horizontalLayout_2.addWidget(label)
        MainWindow.setCentralWidget(centralwidget)
        statusbar _ ?G...QStatusBar(MainWindow)
        statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(statusbar)
        toolBar _ ?G...QToolBar(MainWindow)
        toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(?C...__.TopToolBarArea, toolBar)
        menuBar _ ?G...QMenuBar(MainWindow)
        menuBar.setGeometry(?C...?R..(0, 0, 237, 21))
        menuBar.setObjectName(_fromUtf8("menuBar"))
        menuFile _ ?G...QMenu(menuBar)
        menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(menuBar)
        fill_act _ ?G...?A__(MainWindow)
        fill_act.setObjectName(_fromUtf8("fill_act"))
        clear_act _ ?G...?A__(MainWindow)
        clear_act.setObjectName(_fromUtf8("clear_act"))
        open_act _ ?G...?A__(MainWindow)
        open_act.setObjectName(_fromUtf8("open_act"))
        save_act _ ?G...?A__(MainWindow)
        save_act.setObjectName(_fromUtf8("save_act"))
        exit_act _ ?G...?A__(MainWindow)
        exit_act.setObjectName(_fromUtf8("exit_act"))
        toolBar.addAction(fill_act)
        toolBar.addAction(clear_act)
        menuFile.addAction(open_act)
        menuFile.addAction(save_act)
        menuFile.addSeparator
        menuFile.addAction(exit_act)
        menuBar.addAction(menuFile.menuAction())

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", N..))
        fill_btn.sT..(_translate("MainWindow", "Fill", N..))
        clear_btn.sT..(_translate("MainWindow", "Clear", N..))
        image_lb.sT..(_translate("MainWindow", "TextLabel", N..))
        toolBar.setWindowTitle(_translate("MainWindow", "toolBar", N..))
        menuFile.setTitle(_translate("MainWindow", "File", N..))
        fill_act.sT..(_translate("MainWindow", "Fill", N..))
        clear_act.sT..(_translate("MainWindow", "Clear", N..))
        open_act.sT..(_translate("MainWindow", "Open", N..))
        save_act.sT..(_translate("MainWindow", "Save", N..))
        exit_act.sT..(_translate("MainWindow", "Exit", N..))

