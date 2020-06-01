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
        ChatMainWindow.resize(800, 600)
        self.centralwidget _ ?W...QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hboxlayout _ ?W...QHBoxLayout(self.centralwidget)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout _ ?W...?VBL..
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.chatHistory _ ?W...QTextBrowser(self.centralwidget)
        self.chatHistory.setAcceptDrops F..
        self.chatHistory.setAcceptRichText(True)
        self.chatHistory.setObjectName("chatHistory")
        self.vboxlayout.aW..(self.chatHistory)
        self.hboxlayout1 _ ?W...QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label _ ?W...QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.hboxlayout1.aW..(self.label)
        self.messageLineEdit _ ?W...QLineEdit(self.centralwidget)
        self.messageLineEdit.setObjectName("messageLineEdit")
        self.hboxlayout1.aW..(self.messageLineEdit)
        self.sendButton _ ?W...?PB..(self.centralwidget)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setWhatsThis("")
        self.sendButton.setObjectName("sendButton")
        self.hboxlayout1.aW..(self.sendButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)
        ChatMainWindow.sCW..(self.centralwidget)
        self.menubar _ ?W...QMenuBar(ChatMainWindow)
        self.menubar.setGeometry(?C...QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuQuit _ ?W...QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        self.menuFile _ ?W...QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ChatMainWindow.setMenuBar(self.menubar)
        self.statusbar _ ?W...QStatusBar(ChatMainWindow)
        self.statusbar.setObjectName("statusbar")
        ChatMainWindow.setStatusBar(self.statusbar)
        self.actionQuit _ ?W...?A..(ChatMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAboutQt _ ?W...?A..(ChatMainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionChangeNickname _ ?W...?A..(ChatMainWindow)
        self.actionChangeNickname.setObjectName("actionChangeNickname")
        self.menuQuit.aA..(self.actionAboutQt)
        self.menuFile.aA..(self.actionChangeNickname)
        self.menuFile.addSeparator()
        self.menuFile.aA..(self.actionQuit)
        self.menubar.aA..(self.menuFile.menuAction())
        self.menubar.aA..(self.menuQuit.menuAction())
        self.label.setBuddy(self.messageLineEdit)

        self.retranslateUi(ChatMainWindow)
        self.messageLineEdit.rP__.c..(self.sendButton.animateClick)
        self.actionQuit.t__['bool'].c..(ChatMainWindow.close)
        ?C...QMetaObject.connectSlotsByName(ChatMainWindow)
        ChatMainWindow.setTabOrder(self.chatHistory, self.messageLineEdit)
        ChatMainWindow.setTabOrder(self.messageLineEdit, self.sendButton)

    ___ retranslateUi  ChatMainWindow):
        _translate _ ?C...QCoreApplication.translate
        ChatMainWindow.setWindowTitle(_translate("ChatMainWindow", "Qt D-Bus Chat"))
        self.chatHistory.setToolTip(_translate("ChatMainWindow", "Messages sent and received from other users"))
        self.label.sT..(_translate("ChatMainWindow", "Message:"))
        self.sendButton.setToolTip(_translate("ChatMainWindow", "Sends a message to other people"))
        self.sendButton.sT..(_translate("ChatMainWindow", "Send"))
        self.menuQuit.setTitle(_translate("ChatMainWindow", "Help"))
        self.menuFile.setTitle(_translate("ChatMainWindow", "File"))
        self.actionQuit.sT..(_translate("ChatMainWindow", "Quit"))
        self.actionQuit.sS..(_translate("ChatMainWindow", "Ctrl+Q"))
        self.actionAboutQt.sT..(_translate("ChatMainWindow", "About Qt..."))
        self.actionChangeNickname.sT..(_translate("ChatMainWindow", "Change nickname..."))
        self.actionChangeNickname.sS..(_translate("ChatMainWindow", "Ctrl+N"))

