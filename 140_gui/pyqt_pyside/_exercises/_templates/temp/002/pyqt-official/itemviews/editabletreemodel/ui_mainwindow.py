# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:51:23 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_MainWindow(object):
    ___ setupUi  MainWindow):
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
        self.view.setAnimated F..
        self.view.setAllColumnsShowFocus(True)
        self.view.setObjectName("view")
        self.vboxlayout.addWidget(self.view)
        MainWindow.sCW..(self.centralwidget)
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
        self.exitAction _ ?W...?A..(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.insertRowAction _ ?W...?A..(MainWindow)
        self.insertRowAction.setObjectName("insertRowAction")
        self.removeRowAction _ ?W...?A..(MainWindow)
        self.removeRowAction.setObjectName("removeRowAction")
        self.insertColumnAction _ ?W...?A..(MainWindow)
        self.insertColumnAction.setObjectName("insertColumnAction")
        self.removeColumnAction _ ?W...?A..(MainWindow)
        self.removeColumnAction.setObjectName("removeColumnAction")
        self.insertChildAction _ ?W...?A..(MainWindow)
        self.insertChildAction.setObjectName("insertChildAction")
        self.fileMenu.aA..(self.exitAction)
        self.actionsMenu.aA..(self.insertRowAction)
        self.actionsMenu.aA..(self.insertColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.aA..(self.removeRowAction)
        self.actionsMenu.aA..(self.removeColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.aA..(self.insertChildAction)
        self.menubar.aA..(self.fileMenu.menuAction())
        self.menubar.aA..(self.actionsMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editable Tree Model"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.actionsMenu.setTitle(_translate("MainWindow", "&Actions"))
        self.exitAction.sT..(_translate("MainWindow", "E&xit"))
        self.exitAction.sS..(_translate("MainWindow", "Ctrl+Q"))
        self.insertRowAction.sT..(_translate("MainWindow", "Insert Row"))
        self.insertRowAction.sS..(_translate("MainWindow", "Ctrl+I, R"))
        self.removeRowAction.sT..(_translate("MainWindow", "Remove Row"))
        self.removeRowAction.sS..(_translate("MainWindow", "Ctrl+R, R"))
        self.insertColumnAction.sT..(_translate("MainWindow", "Insert Column"))
        self.insertColumnAction.sS..(_translate("MainWindow", "Ctrl+I, C"))
        self.removeColumnAction.sT..(_translate("MainWindow", "Remove Column"))
        self.removeColumnAction.sS..(_translate("MainWindow", "Ctrl+R, C"))
        self.insertChildAction.sT..(_translate("MainWindow", "Insert Child"))
        self.insertChildAction.sS..(_translate("MainWindow", "Ctrl+N"))

