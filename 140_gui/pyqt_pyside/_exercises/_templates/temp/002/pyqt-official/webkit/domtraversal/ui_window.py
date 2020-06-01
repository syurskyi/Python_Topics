# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Jul 26 06:50:59 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Window(object):
    ___ setupUi  Window):
        Window.setObjectName("Window")
        Window.resize(800, 600)
        self.centralwidget _ ?W...QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 _ ?W...QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.webView _ QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setUrl(?C...QUrl("http://qt.nokia.com/"))
        self.webView.setObjectName("webView")
        self.verticalLayout_2.aW..(self.webView)
        Window.sCW..(self.centralwidget)
        self.menubar _ ?W...QMenuBar(Window)
        self.menubar.setGeometry(?C...QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar _ ?W...QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)
        self.dockWidget _ ?W...QDockWidget(Window)
        self.dockWidget.setAllowedAreas(?C...__.LeftDockWidgetArea|?C...__.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents _ ?W...?W..
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout _ ?W...QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget _ ?W...QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().sT..(0, "1")
        self.treeWidget.header().setVisible F..
        self.verticalLayout.aW..(self.treeWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Window.addDockWidget(?C...__.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(Window)
        ?C...QMetaObject.connectSlotsByName(Window)

    ___ retranslateUi  Window):
        _translate _ ?C...QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Web Element DOM Traversal"))
        self.dockWidget.setWindowTitle(_translate("Window", "Document Structure"))

____ ? ______ QtWebKitWidgets
