# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Jul 26 06:50:59 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Window o..
    ___ setupUi  Window):
        Window.setObjectName("Window")
        Window.r..(800, 600)
        centralwidget _ ?W...?W..(Window)
        centralwidget.setObjectName("centralwidget")
        verticalLayout_2 _ ?W...?VBL..(centralwidget)
        verticalLayout_2.sCM..(-1, 4, -1, 4)
        verticalLayout_2.setObjectName("verticalLayout_2")
        webView _ QtWebKitWidgets.QWebView(centralwidget)
        webView.setUrl(?C...?U..("http://qt.nokia.com/"))
        webView.setObjectName("webView")
        verticalLayout_2.aW..(webView)
        Window.sCW..(centralwidget)
        menubar _ ?W...QMenuBar(Window)
        menubar.setGeometry(?C...QRect(0, 0, 800, 27))
        menubar.setObjectName("menubar")
        Window.setMenuBar(menubar)
        statusbar _ ?W...QStatusBar(Window)
        statusbar.setObjectName("statusbar")
        Window.sSB..(statusbar)
        dockWidget _ ?W...QDockWidget(Window)
        dockWidget.setAllowedAreas(?C...__.LeftDockWidgetArea|?C...__.RightDockWidgetArea)
        dockWidget.setObjectName("dockWidget")
        dockWidgetContents _ ?W...?W..
        dockWidgetContents.setObjectName("dockWidgetContents")
        verticalLayout _ ?W...?VBL..(dockWidgetContents)
        verticalLayout.sCM..(4, 4, 4, 4)
        verticalLayout.setObjectName("verticalLayout")
        treeWidget _ ?W...QTreeWidget(dockWidgetContents)
        tW__.setObjectName("treeWidget")
        tW__.headerItem().sT..(0, "1")
        tW__.header().setVisible F..
        verticalLayout.aW..(tW__)
        dockWidget.setWidget(dockWidgetContents)
        Window.addDockWidget(?C...__.DockWidgetArea(1), dockWidget)

        retranslateUi(Window)
        ?C...QMetaObject.connectSlotsByName(Window)

    ___ retranslateUi  Window):
        _translate _ ?C... ?CA...translate
        Window.sWT..(_translate("Window", "Web Element DOM Traversal"))
        dockWidget.sWT..(_translate("Window", "Document Structure"))

____ ? ______ QtWebKitWidgets
