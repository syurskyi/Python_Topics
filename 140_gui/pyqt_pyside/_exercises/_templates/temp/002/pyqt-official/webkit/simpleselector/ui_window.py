# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue May 14 22:42:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_Window(object):
    ___ setupUi  Window):
        Window.setObjectName("Window")
        Window.resize(640, 480)
        self.verticalLayout _ ?W...QVBoxLayout(Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView _ QtWebKitWidgets.QWebView(Window)
        self.webView.setUrl(QtCore.QUrl("http://webkit.org/"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout _ ?W...QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout _ ?W...QFormLayout()
        self.formLayout.setFieldGrowthPolicy(?W...QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.elementLabel _ ?W...QLabel(Window)
        self.elementLabel.setObjectName("elementLabel")
        self.formLayout.setWidget(0, ?W...QFormLayout.LabelRole, self.elementLabel)
        self.elementLineEdit _ ?W...QLineEdit(Window)
        self.elementLineEdit.setObjectName("elementLineEdit")
        self.formLayout.setWidget(0, ?W...QFormLayout.FieldRole, self.elementLineEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.highlightButton _ ?W...?PB..(Window)
        self.highlightButton.setObjectName("highlightButton")
        self.horizontalLayout.addWidget(self.highlightButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.elementLabel.setBuddy(self.elementLineEdit)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    ___ retranslateUi  Window):
        _translate _ QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Web Element Selector"))
        self.elementLabel.sT..(_translate("Window", "&Element:"))
        self.elementLineEdit.sT..(_translate("Window", "li a"))
        self.highlightButton.sT..(_translate("Window", "&Highlight"))

____ ? ______ QtWebKitWidgets
