# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formextractor.ui'
#
# Created: Tue May 14 17:59:08 2013
#      by: PyQt5 UI code generator 5.0-snapshot-b0831183bf83
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form(object):
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.resize(680, 218)
        horizontalLayout _ ?W...QHBoxLayout(Form)
        horizontalLayout.setObjectName("horizontalLayout")
        webFormGroupBox _ ?W...QGroupBox(Form)
        webFormGroupBox.setObjectName("webFormGroupBox")
        verticalLayout_2 _ ?W...QVBoxLayout(webFormGroupBox)
        verticalLayout_2.setObjectName("verticalLayout_2")
        verticalLayout _ ?W...?VBL..
        verticalLayout.setObjectName("verticalLayout")
        webView _ QtWebKitWidgets.QWebView(webFormGroupBox)
        webView.setMinimumSize(?C...QSize(200, 150))
        webView.setMaximumSize(?C...QSize(400, 16777215))
        webView.setUrl(?C...QUrl("about:blank"))
        webView.setObjectName("webView")
        verticalLayout.aW..(webView)
        verticalLayout_2.aL..(verticalLayout)
        horizontalLayout.aW..(webFormGroupBox)
        spacerItem _ ?W...QSpacerItem(28, 20, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        dataGroupBox _ ?W...QGroupBox(Form)
        dataGroupBox.setObjectName("dataGroupBox")
        verticalLayout_3 _ ?W...QVBoxLayout(dataGroupBox)
        verticalLayout_3.setObjectName("verticalLayout_3")
        formLayout _ ?W...QFormLayout()
        formLayout.setFieldGrowthPolicy(?W...QFormLayout.FieldsStayAtSizeHint)
        formLayout.setObjectName("formLayout")
        firstNameLabel _ ?W...QLabel(dataGroupBox)
        firstNameLabel.setObjectName("firstNameLabel")
        formLayout.setWidget(0, ?W...QFormLayout.LabelRole, firstNameLabel)
        firstNameEdit _ ?W...QLineEdit(dataGroupBox)
        firstNameEdit.setReadOnly(True)
        firstNameEdit.setObjectName("firstNameEdit")
        formLayout.setWidget(0, ?W...QFormLayout.FieldRole, firstNameEdit)
        lastNameLabel _ ?W...QLabel(dataGroupBox)
        lastNameLabel.setObjectName("lastNameLabel")
        formLayout.setWidget(1, ?W...QFormLayout.LabelRole, lastNameLabel)
        lastNameEdit _ ?W...QLineEdit(dataGroupBox)
        lastNameEdit.setReadOnly(True)
        lastNameEdit.setObjectName("lastNameEdit")
        formLayout.setWidget(1, ?W...QFormLayout.FieldRole, lastNameEdit)
        genderLabel _ ?W...QLabel(dataGroupBox)
        genderLabel.setObjectName("genderLabel")
        formLayout.setWidget(2, ?W...QFormLayout.LabelRole, genderLabel)
        genderEdit _ ?W...QLineEdit(dataGroupBox)
        genderEdit.setReadOnly(True)
        genderEdit.setObjectName("genderEdit")
        formLayout.setWidget(2, ?W...QFormLayout.FieldRole, genderEdit)
        updatesLabel _ ?W...QLabel(dataGroupBox)
        updatesLabel.setObjectName("updatesLabel")
        formLayout.setWidget(3, ?W...QFormLayout.LabelRole, updatesLabel)
        updatesEdit _ ?W...QLineEdit(dataGroupBox)
        updatesEdit.setReadOnly(True)
        updatesEdit.setObjectName("updatesEdit")
        formLayout.setWidget(3, ?W...QFormLayout.FieldRole, updatesEdit)
        verticalLayout_3.aL..(formLayout)
        spacerItem1 _ ?W...QSpacerItem(20, 24, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.E..)
        verticalLayout_3.addItem(spacerItem1)
        horizontalLayout.aW..(dataGroupBox)

        retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C...QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        webFormGroupBox.setTitle(_translate("Form", "Web Form"))
        dataGroupBox.setTitle(_translate("Form", "Extracted Data"))
        firstNameLabel.sT..(_translate("Form", "First Name"))
        lastNameLabel.sT..(_translate("Form", "Last Name"))
        genderLabel.sT..(_translate("Form", "Gender"))
        updatesLabel.sT..(_translate("Form", "Receive Updates"))

____ ? ______ QtWebKitWidgets
