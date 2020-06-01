# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:51:23 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, QtGui, ?W..

class Ui_MainWindow(object):
    ___ setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 468)
        self.centralwidget _ ?W...QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout _ ?W...QVBoxLayout(self.centralwidget)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.view _ ?W...QTreeView(self.centralwidget)
        self.view.setAlternatingRowColors(True)
        self.view.setSelectionBehavior(?W...QAbstractItemView.SelectItems)
        self.view.setHorizontalScrollMode(?W...QAbstractItemView.ScrollPerPixel)
        self.view.setAnimated(False)
        self.view.setAllColumnsShowFocus(True)
        self.view.setObjectName("view")
        self.vboxlayout.addWidget(self.view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar _ ?W...QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 31))
        self.menubar.setObjectName("menubar")
        self.fileMenu _ ?W...QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.actionsMenu _ ?W...QMenu(self.menubar)
        self.actionsMenu.setObjectName("actionsMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar _ ?W...QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction _ ?W...QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.insertRowAction _ ?W...QAction(MainWindow)
        self.insertRowAction.setObjectName("insertRowAction")
        self.removeRowAction _ ?W...QAction(MainWindow)
        self.removeRowAction.setObjectName("removeRowAction")
        self.insertColumnAction _ ?W...QAction(MainWindow)
        self.insertColumnAction.setObjectName("insertColumnAction")
        self.removeColumnAction _ ?W...QAction(MainWindow)
        self.removeColumnAction.setObjectName("removeColumnAction")
        self.insertChildAction _ ?W...QAction(MainWindow)
        self.insertChildAction.setObjectName("insertChildAction")
        self.fileMenu.addAction(self.exitAction)
        self.actionsMenu.addAction(self.insertRowAction)
        self.actionsMenu.addAction(self.insertColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.removeRowAction)
        self.actionsMenu.addAction(self.removeColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.insertChildAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.actionsMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi(self, MainWindow):
        _translate _ QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editable Tree Model"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.actionsMenu.setTitle(_translate("MainWindow", "&Actions"))
        self.exitAction.sT..(_translate("MainWindow", "E&xit"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.insertRowAction.sT..(_translate("MainWindow", "Insert Row"))
        self.insertRowAction.setShortcut(_translate("MainWindow", "Ctrl+I, R"))
        self.removeRowAction.sT..(_translate("MainWindow", "Remove Row"))
        self.removeRowAction.setShortcut(_translate("MainWindow", "Ctrl+R, R"))
        self.insertColumnAction.sT..(_translate("MainWindow", "Insert Column"))
        self.insertColumnAction.setShortcut(_translate("MainWindow", "Ctrl+I, C"))
        self.removeColumnAction.sT..(_translate("MainWindow", "Remove Column"))
        self.removeColumnAction.setShortcut(_translate("MainWindow", "Ctrl+R, C"))
        self.insertChildAction.sT..(_translate("MainWindow", "Insert Child"))
        self.insertChildAction.setShortcut(_translate("MainWindow", "Ctrl+N"))

