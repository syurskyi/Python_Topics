# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewer.ui'
#
# Created: Tue May 14 22:35:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form(object):
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.resize(911, 688)
        self.horizontalLayout_4 _ ?W...QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter _ ?W...QSplitter(Form)
        self.splitter.setOrientation(?C...__.Horizontal)
        self.splitter.setObjectName("splitter")
        self.editorBox _ ?W...QGroupBox(self.splitter)
        self.editorBox.setObjectName("editorBox")
        self.horizontalLayout_2 _ ?W...QHBoxLayout(self.editorBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 _ ?W...?VBL..
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit _ ?W...QPlainTextEdit(self.editorBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.aW..(self.plainTextEdit)
        self.horizontalLayout _ ?W...QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton _ ?W...?PB..(self.editorBox)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.aW..(self.clearButton)
        self.previewButton _ ?W...?PB..(self.editorBox)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout.aW..(self.previewButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.previewerBox _ ?W...QGroupBox(self.splitter)
        self.previewerBox.setObjectName("previewerBox")
        self.horizontalLayout_3 _ ?W...QHBoxLayout(self.previewerBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.webView _ QtWebKitWidgets.QWebView(self.previewerBox)
        self.webView.setUrl(?C...QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.horizontalLayout_3.aW..(self.webView)
        self.horizontalLayout_4.aW..(self.splitter)

        self.retranslateUi(Form)
        self.clearButton.c__.c..(self.plainTextEdit.clear)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C...QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.editorBox.setTitle(_translate("Form", "HTML Editor"))
        self.clearButton.sT..(_translate("Form", "Clear"))
        self.previewButton.sT..(_translate("Form", "Preview"))
        self.previewerBox.setTitle(_translate("Form", "HTML Preview"))

____ ? ______ QtWebKitWidgets
