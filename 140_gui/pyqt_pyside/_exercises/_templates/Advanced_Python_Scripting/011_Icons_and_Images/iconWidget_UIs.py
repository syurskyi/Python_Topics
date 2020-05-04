# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week3\icon_widget\iconWidget.ui'
#
# Created: Wed Oct 15 18:38:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(237, 369)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        horizontalLayout_2 _ ?G...QHBoxLayout(centralwidget)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        verticalLayout _ ?G...QVBoxLayout
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        fill_btn _ ?G...?PB..(centralwidget)
        fill_btn.setObjectName("fill_btn")
        horizontalLayout.addWidget(fill_btn)
        clear_btn _ ?G...?PB..(centralwidget)
        clear_btn.setMinimumSize(?C...QSize(40, 0))
        clear_btn.setObjectName("clear_btn")
        horizontalLayout.addWidget(clear_btn)
        image_lb _ ?G...QLabel(centralwidget)
        image_lb.setObjectName("image_lb")
        horizontalLayout.addWidget(image_lb)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout)
        combo_cbb _ ?G...QComboBox(centralwidget)
        combo_cbb.setObjectName("combo_cbb")
        verticalLayout.addWidget(combo_cbb)
        list_lwd _ ?G...?LW..(centralwidget)
        list_lwd.setObjectName("list_lwd")
        verticalLayout.addWidget(list_lwd)
        horizontalLayout_2.addLayout(verticalLayout)
        label _ ?G...QLabel(centralwidget)
        label.sT..("")
        label.setObjectName("label")
        horizontalLayout_2.addWidget(label)
        MainWindow.setCentralWidget(centralwidget)
        statusbar _ ?G...QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(statusbar)
        toolBar _ ?G...QToolBar(MainWindow)
        toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(?C...__.TopToolBarArea, toolBar)
        menuBar _ ?G...QMenuBar(MainWindow)
        menuBar.setGeometry(?C...?R..(0, 0, 237, 21))
        menuBar.setObjectName("menuBar")
        menuFile _ ?G...QMenu(menuBar)
        menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(menuBar)
        fill_act _ ?G...?A__(MainWindow)
        fill_act.setObjectName("fill_act")
        clear_act _ ?G...?A__(MainWindow)
        clear_act.setObjectName("clear_act")
        open_act _ ?G...?A__(MainWindow)
        open_act.setObjectName("open_act")
        save_act _ ?G...?A__(MainWindow)
        save_act.setObjectName("save_act")
        exit_act _ ?G...?A__(MainWindow)
        exit_act.setObjectName("exit_act")
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
        MainWindow.setWindowTitle(?G...?A...translate("MainWindow", "MainWindow", N.., ?G...?A...UnicodeUTF8))
        fill_btn.sT..(?G...?A...translate("MainWindow", "Fill", N.., ?G...?A...UnicodeUTF8))
        clear_btn.sT..(?G...?A...translate("MainWindow", "Clear", N.., ?G...?A...UnicodeUTF8))
        image_lb.sT..(?G...?A...translate("MainWindow", "TextLabel", N.., ?G...?A...UnicodeUTF8))
        toolBar.setWindowTitle(?G...?A...translate("MainWindow", "toolBar", N.., ?G...?A...UnicodeUTF8))
        menuFile.setTitle(?G...?A...translate("MainWindow", "File", N.., ?G...?A...UnicodeUTF8))
        fill_act.sT..(?G...?A...translate("MainWindow", "Fill", N.., ?G...?A...UnicodeUTF8))
        clear_act.sT..(?G...?A...translate("MainWindow", "Clear", N.., ?G...?A...UnicodeUTF8))
        open_act.sT..(?G...?A...translate("MainWindow", "Open", N.., ?G...?A...UnicodeUTF8))
        save_act.sT..(?G...?A...translate("MainWindow", "Save", N.., ?G...?A...UnicodeUTF8))
        exit_act.sT..(?G...?A...translate("MainWindow", "Exit", N.., ?G...?A...UnicodeUTF8))

