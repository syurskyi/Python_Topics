# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatmainwindow.ui'
#
# Created: Fri Jul 26 06:48:06 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_ChatMainWindow(object):
    ___ setupUi  ChatMainWindow):
        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.r..(800, 600)
        centralwidget _ ?W...?W..(ChatMainWindow)
        centralwidget.setObjectName("centralwidget")
        hboxlayout _ ?W...QHBoxLayout(centralwidget)
        hboxlayout.setContentsMargins(9, 9, 9, 9)
        hboxlayout.setSpacing(6)
        hboxlayout.setObjectName("hboxlayout")
        vboxlayout _ ?W...?VBL..
        vboxlayout.setContentsMargins(0, 0, 0, 0)
        vboxlayout.setSpacing(6)
        vboxlayout.setObjectName("vboxlayout")
        chatHistory _ ?W...QTextBrowser(centralwidget)
        chatHistory.setAcceptDrops F..
        chatHistory.setAcceptRichText(True)
        chatHistory.setObjectName("chatHistory")
        vboxlayout.aW..(chatHistory)
        hboxlayout1 _ ?W...QHBoxLayout()
        hboxlayout1.setContentsMargins(0, 0, 0, 0)
        hboxlayout1.setSpacing(6)
        hboxlayout1.setObjectName("hboxlayout1")
        label _ ?W...QLabel(centralwidget)
        label.setObjectName("label")
        hboxlayout1.aW..(label)
        messageLineEdit _ ?W...QLineEdit(centralwidget)
        messageLineEdit.setObjectName("messageLineEdit")
        hboxlayout1.aW..(messageLineEdit)
        sendButton _ ?W...?PB..(centralwidget)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sendButton.sizePolicy().hasHeightForWidth())
        sendButton.sSP..(sizePolicy)
        sendButton.setWhatsThis("")
        sendButton.setObjectName("sendButton")
        hboxlayout1.aW..(sendButton)
        vboxlayout.aL..(hboxlayout1)
        hboxlayout.aL..(vboxlayout)
        ChatMainWindow.sCW..(centralwidget)
        menubar _ ?W...QMenuBar(ChatMainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 800, 31))
        menubar.setObjectName("menubar")
        menuQuit _ ?W...QMenu(menubar)
        menuQuit.setObjectName("menuQuit")
        menuFile _ ?W...QMenu(menubar)
        menuFile.setObjectName("menuFile")
        ChatMainWindow.setMenuBar(menubar)
        statusbar _ ?W...QStatusBar(ChatMainWindow)
        statusbar.setObjectName("statusbar")
        ChatMainWindow.setStatusBar(statusbar)
        actionQuit _ ?W...?A..(ChatMainWindow)
        actionQuit.setObjectName("actionQuit")
        actionAboutQt _ ?W...?A..(ChatMainWindow)
        actionAboutQt.setObjectName("actionAboutQt")
        actionChangeNickname _ ?W...?A..(ChatMainWindow)
        actionChangeNickname.setObjectName("actionChangeNickname")
        menuQuit.aA..(actionAboutQt)
        menuFile.aA..(actionChangeNickname)
        menuFile.addSeparator()
        menuFile.aA..(actionQuit)
        menubar.aA..(menuFile.menuAction())
        menubar.aA..(menuQuit.menuAction())
        label.setBuddy(messageLineEdit)

        retranslateUi(ChatMainWindow)
        messageLineEdit.rP__.c..(sendButton.animateClick)
        actionQuit.t__['bool'].c..(ChatMainWindow.close)
        ?C...QMetaObject.connectSlotsByName(ChatMainWindow)
        ChatMainWindow.setTabOrder(chatHistory, messageLineEdit)
        ChatMainWindow.setTabOrder(messageLineEdit, sendButton)

    ___ retranslateUi  ChatMainWindow):
        _translate _ ?C...QCoreApplication.translate
        ChatMainWindow.sWT..(_translate("ChatMainWindow", "Qt D-Bus Chat"))
        chatHistory.sTT..(_translate("ChatMainWindow", "Messages sent and received from other users"))
        label.sT..(_translate("ChatMainWindow", "Message:"))
        sendButton.sTT..(_translate("ChatMainWindow", "Sends a message to other people"))
        sendButton.sT..(_translate("ChatMainWindow", "Send"))
        menuQuit.setTitle(_translate("ChatMainWindow", "Help"))
        menuFile.setTitle(_translate("ChatMainWindow", "File"))
        actionQuit.sT..(_translate("ChatMainWindow", "Quit"))
        actionQuit.sS..(_translate("ChatMainWindow", "Ctrl+Q"))
        actionAboutQt.sT..(_translate("ChatMainWindow", "About Qt..."))
        actionChangeNickname.sT..(_translate("ChatMainWindow", "Change nickname..."))
        actionChangeNickname.sS..(_translate("ChatMainWindow", "Ctrl+N"))

