# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:46:58 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow o..
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(812, 605)
        centralWidget _ ?W...?W..(MainWindow)
        centralWidget.setObjectName("centralWidget")
        hboxlayout _ ?W...?HBL..(centralWidget)
        hboxlayout.sCM..(0, 0, 0, 0)
        hboxlayout.setSpacing(6)
        hboxlayout.setObjectName("hboxlayout")
        Frame3 _ ?W...QFrame(centralWidget)
        Frame3.setFrameShape(?W...QFrame.StyledPanel)
        Frame3.setFrameShadow(?W...QFrame.Sunken)
        Frame3.setObjectName("Frame3")
        vboxlayout _ ?W...?VBL..(Frame3)
        vboxlayout.sCM..(1, 1, 1, 1)
        vboxlayout.setSpacing(0)
        vboxlayout.setObjectName("vboxlayout")
        WebBrowser _ QAxContainer.QAxWidget(Frame3)
        WebBrowser.sFP..(?C...__.StrongFocus)
        WebBrowser.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        WebBrowser.setObjectName("WebBrowser")
        vboxlayout.aW..(WebBrowser)
        hboxlayout.aW..(Frame3)
        MainWindow.sCW..(centralWidget)
        tbNavigate _ ?W...QToolBar(MainWindow)
        tbNavigate.setOrientation(?C...__.H..)
        tbNavigate.setObjectName("tbNavigate")
        MainWindow.aTB..(4, tbNavigate)
        tbAddress _ ?W...QToolBar(MainWindow)
        tbAddress.setOrientation(?C...__.H..)
        tbAddress.setObjectName("tbAddress")
        MainWindow.aTB..(4, tbAddress)
        menubar _ ?W...QMenuBar(MainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 812, 26))
        menubar.setObjectName("menubar")
        PopupMenu _ ?W...?M..(menubar)
        PopupMenu.setObjectName("PopupMenu")
        FileNewGroup_2 _ ?W...?M..(PopupMenu)
        FileNewGroup_2.setObjectName("FileNewGroup_2")
        unnamed _ ?W...?M..(menubar)
        unnamed.setObjectName("unnamed")
        MainWindow.setMenuBar(menubar)
        actionGo _ ?W...?A..(MainWindow)
        icon _ ?G...?I..
        icon.addFile(":/icons/image0.xpm")
        actionGo.sI..(icon)
        actionGo.setObjectName("actionGo")
        actionBack _ ?W...?A..(MainWindow)
        icon1 _ ?G...?I..
        icon1.addFile(":/icons/image1.xpm")
        actionBack.sI..(icon1)
        actionBack.setObjectName("actionBack")
        actionForward _ ?W...?A..(MainWindow)
        icon2 _ ?G...?I..
        icon2.addFile(":/icons/image2.xpm")
        actionForward.sI..(icon2)
        actionForward.setObjectName("actionForward")
        actionStop _ ?W...?A..(MainWindow)
        icon3 _ ?G...?I..
        icon3.addFile(":/icons/image3.xpm")
        actionStop.sI..(icon3)
        actionStop.setObjectName("actionStop")
        actionRefresh _ ?W...?A..(MainWindow)
        icon4 _ ?G...?I..
        icon4.addFile(":/icons/image4.xpm")
        actionRefresh.sI..(icon4)
        actionRefresh.setObjectName("actionRefresh")
        actionHome _ ?W...?A..(MainWindow)
        icon5 _ ?G...?I..
        icon5.addFile(":/icons/image5.xpm")
        actionHome.sI..(icon5)
        actionHome.setObjectName("actionHome")
        actionFileClose _ ?W...?A..(MainWindow)
        actionFileClose.setObjectName("actionFileClose")
        actionSearch _ ?W...?A..(MainWindow)
        icon6 _ ?G...?I..
        icon6.addFile(":/icons/image6.xpm")
        actionSearch.sI..(icon6)
        actionSearch.setObjectName("actionSearch")
        actionAbout _ ?W...?A..(MainWindow)
        actionAbout.setObjectName("actionAbout")
        actionAboutQt _ ?W...?A..(MainWindow)
        actionAboutQt.setObjectName("actionAboutQt")
        FileNewGroup _ ?W...QActionGroup(MainWindow)
        FileNewGroup.setObjectName("FileNewGroup")
        actionNewWindow _ ?W...?A..(FileNewGroup)
        actionNewWindow.setObjectName("actionNewWindow")
        tbNavigate.aA..(actionBack)
        tbNavigate.aA..(actionForward)
        tbNavigate.aA..(actionStop)
        tbNavigate.aA..(actionRefresh)
        tbNavigate.aA..(actionHome)
        tbNavigate.aS..)
        tbNavigate.aA..(actionSearch)
        tbAddress.aA..(actionGo)
        FileNewGroup_2.aA..(actionNewWindow)
        PopupMenu.aA..(FileNewGroup_2.menuAction())
        PopupMenu.aS..)
        PopupMenu.aA..(actionFileClose)
        unnamed.aA..(actionAbout)
        unnamed.aA..(actionAboutQt)
        menubar.aA..(PopupMenu.menuAction())
        menubar.aA..(unnamed.menuAction())

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Qt WebBrowser"))
        tbNavigate.sWT..(_translate("MainWindow", "Navigation"))
        tbAddress.sWT..(_translate("MainWindow", "Address"))
        PopupMenu.setTitle(_translate("MainWindow", "&File"))
        FileNewGroup_2.setTitle(_translate("MainWindow", "New"))
        unnamed.setTitle(_translate("MainWindow", "&Help"))
        actionGo.setIconText(_translate("MainWindow", "Go"))
        actionBack.setIconText(_translate("MainWindow", "Back"))
        actionBack.sS..(_translate("MainWindow", "Backspace"))
        actionForward.setIconText(_translate("MainWindow", "Forward"))
        actionStop.setIconText(_translate("MainWindow", "Stop"))
        actionRefresh.setIconText(_translate("MainWindow", "Refresh"))
        actionHome.setIconText(_translate("MainWindow", "Home"))
        actionFileClose.sT..(_translate("MainWindow", "C&lose"))
        actionFileClose.setIconText(_translate("MainWindow", "Close"))
        actionSearch.setIconText(_translate("MainWindow", "Search"))
        actionAbout.setIconText(_translate("MainWindow", "About"))
        actionAboutQt.setIconText(_translate("MainWindow", "About Qt"))
        actionNewWindow.setIconText(_translate("MainWindow", "Window"))
        actionNewWindow.sS..(_translate("MainWindow", "Ctrl+N"))

____ ? ______ QAxContainer