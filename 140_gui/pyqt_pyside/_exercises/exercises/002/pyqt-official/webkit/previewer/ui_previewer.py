# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewer.ui'
#
# Created: Tue May 14 22:35:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form o..
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.r..(911, 688)
        horizontalLayout_4 _ ?W...?HBL..(Form)
        horizontalLayout_4.setObjectName("horizontalLayout_4")
        splitter _ ?W...?S..(Form)
        splitter.setOrientation(?C...__.H..)
        splitter.setObjectName("splitter")
        editorBox _ ?W...?GB..(splitter)
        editorBox.setObjectName("editorBox")
        horizontalLayout_2 _ ?W...?HBL..(editorBox)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        verticalLayout_2 _ ?W...?VBL..
        verticalLayout_2.setObjectName("verticalLayout_2")
        plainTextEdit _ ?W...?PTE..(editorBox)
        plainTextEdit.setObjectName("plainTextEdit")
        verticalLayout_2.aW..(plainTextEdit)
        horizontalLayout _ ?W...?HBL..
        horizontalLayout.setObjectName("horizontalLayout")
        clearButton _ ?W...?PB..(editorBox)
        clearButton.setObjectName("clearButton")
        horizontalLayout.aW..(clearButton)
        previewButton _ ?W...?PB..(editorBox)
        previewButton.setObjectName("previewButton")
        horizontalLayout.aW..(previewButton)
        verticalLayout_2.aL..(horizontalLayout)
        horizontalLayout_2.aL..(verticalLayout_2)
        previewerBox _ ?W...?GB..(splitter)
        previewerBox.setObjectName("previewerBox")
        horizontalLayout_3 _ ?W...?HBL..(previewerBox)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        webView _ QtWebKitWidgets.QWebView(previewerBox)
        webView.setUrl(?C...?U..("about:blank"))
        webView.setObjectName("webView")
        horizontalLayout_3.aW..(webView)
        horizontalLayout_4.aW..(splitter)

        retranslateUi(Form)
        clearButton.c__.c..(plainTextEdit.clear)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C... ?CA...translate
        Form.sWT..(_translate("Form", "Form"))
        editorBox.setTitle(_translate("Form", "HTML Editor"))
        clearButton.sT..(_translate("Form", "Clear"))
        previewButton.sT..(_translate("Form", "Preview"))
        previewerBox.setTitle(_translate("Form", "HTML Preview"))

____ ? ______ QtWebKitWidgets
