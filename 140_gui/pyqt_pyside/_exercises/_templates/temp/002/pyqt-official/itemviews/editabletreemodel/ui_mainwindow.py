# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:51:23 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow o..
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(573, 468)
        centralwidget _ ?W...?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        vboxlayout _ ?W...?VBL..(centralwidget)
        vboxlayout.sCM..(0, 0, 0, 0)
        vboxlayout.setSpacing(0)
        vboxlayout.setObjectName("vboxlayout")
        view _ ?W...QTreeView(centralwidget)
        view.setAlternatingRowColors( st.
        view.setSelectionBehavior(?W...?AIV...SelectItems)
        view.setHorizontalScrollMode(?W...?AIV...ScrollPerPixel)
        view.setAnimated F..
        view.setAllColumnsShowFocus( st.
        view.setObjectName("view")
        vboxlayout.aW..(view)
        MainWindow.sCW..(centralwidget)
        menubar _ ?W...QMenuBar(MainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 573, 31))
        menubar.setObjectName("menubar")
        fileMenu _ ?W...?M..(menubar)
        fileMenu.setObjectName("fileMenu")
        actionsMenu _ ?W...?M..(menubar)
        actionsMenu.setObjectName("actionsMenu")
        MainWindow.setMenuBar(menubar)
        statusbar _ ?W...QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.sSB..(statusbar)
        exitAction _ ?W...?A..(MainWindow)
        exitAction.setObjectName("exitAction")
        insertRowAction _ ?W...?A..(MainWindow)
        insertRowAction.setObjectName("insertRowAction")
        removeRowAction _ ?W...?A..(MainWindow)
        removeRowAction.setObjectName("removeRowAction")
        insertColumnAction _ ?W...?A..(MainWindow)
        insertColumnAction.setObjectName("insertColumnAction")
        removeColumnAction _ ?W...?A..(MainWindow)
        removeColumnAction.setObjectName("removeColumnAction")
        insertChildAction _ ?W...?A..(MainWindow)
        insertChildAction.setObjectName("insertChildAction")
        fileMenu.aA..(exitAction)
        actionsMenu.aA..(insertRowAction)
        actionsMenu.aA..(insertColumnAction)
        actionsMenu.aS..)
        actionsMenu.aA..(removeRowAction)
        actionsMenu.aA..(removeColumnAction)
        actionsMenu.aS..)
        actionsMenu.aA..(insertChildAction)
        menubar.aA..(fileMenu.menuAction())
        menubar.aA..(actionsMenu.menuAction())

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Editable Tree Model"))
        fileMenu.setTitle(_translate("MainWindow", "&File"))
        actionsMenu.setTitle(_translate("MainWindow", "&Actions"))
        exitAction.sT..(_translate("MainWindow", "E&xit"))
        exitAction.sS..(_translate("MainWindow", "Ctrl+Q"))
        insertRowAction.sT..(_translate("MainWindow", "Insert Row"))
        insertRowAction.sS..(_translate("MainWindow", "Ctrl+I, R"))
        removeRowAction.sT..(_translate("MainWindow", "Remove Row"))
        removeRowAction.sS..(_translate("MainWindow", "Ctrl+R, R"))
        insertColumnAction.sT..(_translate("MainWindow", "Insert Column"))
        insertColumnAction.sS..(_translate("MainWindow", "Ctrl+I, C"))
        removeColumnAction.sT..(_translate("MainWindow", "Remove Column"))
        removeColumnAction.sS..(_translate("MainWindow", "Ctrl+R, C"))
        insertChildAction.sT..(_translate("MainWindow", "Insert Child"))
        insertChildAction.sS..(_translate("MainWindow", "Ctrl+N"))

