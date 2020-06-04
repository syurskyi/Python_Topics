# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue May 14 22:42:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Window o..
    ___ setupUi  Window):
        Window.setObjectName("Window")
        Window.r..(640, 480)
        verticalLayout _ ?W...?VBL..(Window)
        verticalLayout.setObjectName("verticalLayout")
        webView _ QtWebKitWidgets.QWebView(Window)
        webView.setUrl(?C...?U..("http://webkit.org/"))
        webView.setObjectName("webView")
        verticalLayout.aW..(webView)
        horizontalLayout _ ?W...?HBL..
        horizontalLayout.setObjectName("horizontalLayout")
        formLayout _ ?W...?FL..
        formLayout.setFieldGrowthPolicy(?W...?FL...ExpandingFieldsGrow)
        formLayout.setObjectName("formLayout")
        elementLabel _ ?W...?L..(Window)
        elementLabel.setObjectName("elementLabel")
        formLayout.setWidget(0, ?W...?FL...LabelRole, elementLabel)
        elementLineEdit _ ?W...QLineEdit(Window)
        elementLineEdit.setObjectName("elementLineEdit")
        formLayout.setWidget(0, ?W...?FL...FieldRole, elementLineEdit)
        horizontalLayout.aL..(formLayout)
        highlightButton _ ?W...?PB..(Window)
        highlightButton.setObjectName("highlightButton")
        horizontalLayout.aW..(highlightButton)
        verticalLayout.aL..(horizontalLayout)
        elementLabel.setBuddy(elementLineEdit)

        retranslateUi(Window)
        ?C...QMetaObject.connectSlotsByName(Window)

    ___ retranslateUi  Window):
        _translate _ ?C... ?CA...translate
        Window.sWT..(_translate("Window", "Web Element Selector"))
        elementLabel.sT..(_translate("Window", "&Element:"))
        elementLineEdit.sT..(_translate("Window", "li a"))
        highlightButton.sT..(_translate("Window", "&Highlight"))

____ ? ______ QtWebKitWidgets
