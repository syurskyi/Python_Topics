# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:46:58 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_MainWindow(object):
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 605)
        self.centralWidget _ ?W...QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.hboxlayout _ ?W...QHBoxLayout(self.centralWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.Frame3 _ ?W...QFrame(self.centralWidget)
        self.Frame3.setFrameShape(?W...QFrame.StyledPanel)
        self.Frame3.setFrameShadow(?W...QFrame.Sunken)
        self.Frame3.setObjectName("Frame3")
        self.vboxlayout _ ?W...QVBoxLayout(self.Frame3)
        self.vboxlayout.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.WebBrowser _ QAxContainer.QAxWidget(self.Frame3)
        self.WebBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.WebBrowser.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.WebBrowser.setObjectName("WebBrowser")
        self.vboxlayout.addWidget(self.WebBrowser)
        self.hboxlayout.addWidget(self.Frame3)
        MainWindow.sCW..(self.centralWidget)
        self.tbNavigate _ ?W...QToolBar(MainWindow)
        self.tbNavigate.setOrientation(QtCore.Qt.Horizontal)
        self.tbNavigate.setObjectName("tbNavigate")
        MainWindow.addToolBar(4, self.tbNavigate)
        self.tbAddress _ ?W...QToolBar(MainWindow)
        self.tbAddress.setOrientation(QtCore.Qt.Horizontal)
        self.tbAddress.setObjectName("tbAddress")
        MainWindow.addToolBar(4, self.tbAddress)
        self.menubar _ ?W...QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        self.PopupMenu _ ?W...QMenu(self.menubar)
        self.PopupMenu.setObjectName("PopupMenu")
        self.FileNewGroup_2 _ ?W...QMenu(self.PopupMenu)
        self.FileNewGroup_2.setObjectName("FileNewGroup_2")
        self.unnamed _ ?W...QMenu(self.menubar)
        self.unnamed.setObjectName("unnamed")
        MainWindow.setMenuBar(self.menubar)
        self.actionGo _ ?W...?A..(MainWindow)
        icon _ ?G...QIcon()
        icon.addFile(":/icons/image0.xpm")
        self.actionGo.setIcon(icon)
        self.actionGo.setObjectName("actionGo")
        self.actionBack _ ?W...?A..(MainWindow)
        icon1 _ ?G...QIcon()
        icon1.addFile(":/icons/image1.xpm")
        self.actionBack.setIcon(icon1)
        self.actionBack.setObjectName("actionBack")
        self.actionForward _ ?W...?A..(MainWindow)
        icon2 _ ?G...QIcon()
        icon2.addFile(":/icons/image2.xpm")
        self.actionForward.setIcon(icon2)
        self.actionForward.setObjectName("actionForward")
        self.actionStop _ ?W...?A..(MainWindow)
        icon3 _ ?G...QIcon()
        icon3.addFile(":/icons/image3.xpm")
        self.actionStop.setIcon(icon3)
        self.actionStop.setObjectName("actionStop")
        self.actionRefresh _ ?W...?A..(MainWindow)
        icon4 _ ?G...QIcon()
        icon4.addFile(":/icons/image4.xpm")
        self.actionRefresh.setIcon(icon4)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionHome _ ?W...?A..(MainWindow)
        icon5 _ ?G...QIcon()
        icon5.addFile(":/icons/image5.xpm")
        self.actionHome.setIcon(icon5)
        self.actionHome.setObjectName("actionHome")
        self.actionFileClose _ ?W...?A..(MainWindow)
        self.actionFileClose.setObjectName("actionFileClose")
        self.actionSearch _ ?W...?A..(MainWindow)
        icon6 _ ?G...QIcon()
        icon6.addFile(":/icons/image6.xpm")
        self.actionSearch.setIcon(icon6)
        self.actionSearch.setObjectName("actionSearch")
        self.actionAbout _ ?W...?A..(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt _ ?W...?A..(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.FileNewGroup _ ?W...QActionGroup(MainWindow)
        self.FileNewGroup.setObjectName("FileNewGroup")
        self.actionNewWindow _ ?W...?A..(self.FileNewGroup)
        self.actionNewWindow.setObjectName("actionNewWindow")
        self.tbNavigate.aA..(self.actionBack)
        self.tbNavigate.aA..(self.actionForward)
        self.tbNavigate.aA..(self.actionStop)
        self.tbNavigate.aA..(self.actionRefresh)
        self.tbNavigate.aA..(self.actionHome)
        self.tbNavigate.addSeparator()
        self.tbNavigate.aA..(self.actionSearch)
        self.tbAddress.aA..(self.actionGo)
        self.FileNewGroup_2.aA..(self.actionNewWindow)
        self.PopupMenu.aA..(self.FileNewGroup_2.menuAction())
        self.PopupMenu.addSeparator()
        self.PopupMenu.aA..(self.actionFileClose)
        self.unnamed.aA..(self.actionAbout)
        self.unnamed.aA..(self.actionAboutQt)
        self.menubar.aA..(self.PopupMenu.menuAction())
        self.menubar.aA..(self.unnamed.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt WebBrowser"))
        self.tbNavigate.setWindowTitle(_translate("MainWindow", "Navigation"))
        self.tbAddress.setWindowTitle(_translate("MainWindow", "Address"))
        self.PopupMenu.setTitle(_translate("MainWindow", "&File"))
        self.FileNewGroup_2.setTitle(_translate("MainWindow", "New"))
        self.unnamed.setTitle(_translate("MainWindow", "&Help"))
        self.actionGo.setIconText(_translate("MainWindow", "Go"))
        self.actionBack.setIconText(_translate("MainWindow", "Back"))
        self.actionBack.sS..(_translate("MainWindow", "Backspace"))
        self.actionForward.setIconText(_translate("MainWindow", "Forward"))
        self.actionStop.setIconText(_translate("MainWindow", "Stop"))
        self.actionRefresh.setIconText(_translate("MainWindow", "Refresh"))
        self.actionHome.setIconText(_translate("MainWindow", "Home"))
        self.actionFileClose.sT..(_translate("MainWindow", "C&lose"))
        self.actionFileClose.setIconText(_translate("MainWindow", "Close"))
        self.actionSearch.setIconText(_translate("MainWindow", "Search"))
        self.actionAbout.setIconText(_translate("MainWindow", "About"))
        self.actionAboutQt.setIconText(_translate("MainWindow", "About Qt"))
        self.actionNewWindow.setIconText(_translate("MainWindow", "Window"))
        self.actionNewWindow.sS..(_translate("MainWindow", "Ctrl+N"))

____ ? ______ QAxContainer
