# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week3\icon_widget\iconWidget.ui'
#
# Created: Wed Oct 15 18:38:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(237, 369)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fill_btn = QtGui.QPushButton(self.centralwidget)
        self.fill_btn.setObjectName("fill_btn")
        self.horizontalLayout.addWidget(self.fill_btn)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.image_lb = QtGui.QLabel(self.centralwidget)
        self.image_lb.setObjectName("image_lb")
        self.horizontalLayout.addWidget(self.image_lb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.combo_cbb = QtGui.QComboBox(self.centralwidget)
        self.combo_cbb.setObjectName("combo_cbb")
        self.verticalLayout.addWidget(self.combo_cbb)
        self.list_lwd = QtGui.QListWidget(self.centralwidget)
        self.list_lwd.setObjectName("list_lwd")
        self.verticalLayout.addWidget(self.list_lwd)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 237, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.fill_act = QtGui.QAction(MainWindow)
        self.fill_act.setObjectName("fill_act")
        self.clear_act = QtGui.QAction(MainWindow)
        self.clear_act.setObjectName("clear_act")
        self.open_act = QtGui.QAction(MainWindow)
        self.open_act.setObjectName("open_act")
        self.save_act = QtGui.QAction(MainWindow)
        self.save_act.setObjectName("save_act")
        self.exit_act = QtGui.QAction(MainWindow)
        self.exit_act.setObjectName("exit_act")
        self.toolBar.addAction(self.fill_act)
        self.toolBar.addAction(self.clear_act)
        self.menuFile.addAction(self.open_act)
        self.menuFile.addAction(self.save_act)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_act)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.fill_btn.setText(QtGui.QApplication.translate("MainWindow", "Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.image_lb.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.fill_act.setText(QtGui.QApplication.translate("MainWindow", "Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_act.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.open_act.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.save_act.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_act.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

