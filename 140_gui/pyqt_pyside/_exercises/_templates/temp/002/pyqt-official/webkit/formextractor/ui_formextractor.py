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
        self.horizontalLayout _ ?W...QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webFormGroupBox _ ?W...QGroupBox(Form)
        self.webFormGroupBox.setObjectName("webFormGroupBox")
        self.verticalLayout_2 _ ?W...QVBoxLayout(self.webFormGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout _ ?W...?VBL..
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView _ QtWebKitWidgets.QWebView(self.webFormGroupBox)
        self.webView.setMinimumSize(?C...QSize(200, 150))
        self.webView.setMaximumSize(?C...QSize(400, 16777215))
        self.webView.setUrl(?C...QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.aW..(self.webView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.aW..(self.webFormGroupBox)
        spacerItem _ ?W...QSpacerItem(28, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dataGroupBox _ ?W...QGroupBox(Form)
        self.dataGroupBox.setObjectName("dataGroupBox")
        self.verticalLayout_3 _ ?W...QVBoxLayout(self.dataGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout _ ?W...QFormLayout()
        self.formLayout.setFieldGrowthPolicy(?W...QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel _ ?W...QLabel(self.dataGroupBox)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, ?W...QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameEdit _ ?W...QLineEdit(self.dataGroupBox)
        self.firstNameEdit.setReadOnly(True)
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.formLayout.setWidget(0, ?W...QFormLayout.FieldRole, self.firstNameEdit)
        self.lastNameLabel _ ?W...QLabel(self.dataGroupBox)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, ?W...QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameEdit _ ?W...QLineEdit(self.dataGroupBox)
        self.lastNameEdit.setReadOnly(True)
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.formLayout.setWidget(1, ?W...QFormLayout.FieldRole, self.lastNameEdit)
        self.genderLabel _ ?W...QLabel(self.dataGroupBox)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(2, ?W...QFormLayout.LabelRole, self.genderLabel)
        self.genderEdit _ ?W...QLineEdit(self.dataGroupBox)
        self.genderEdit.setReadOnly(True)
        self.genderEdit.setObjectName("genderEdit")
        self.formLayout.setWidget(2, ?W...QFormLayout.FieldRole, self.genderEdit)
        self.updatesLabel _ ?W...QLabel(self.dataGroupBox)
        self.updatesLabel.setObjectName("updatesLabel")
        self.formLayout.setWidget(3, ?W...QFormLayout.LabelRole, self.updatesLabel)
        self.updatesEdit _ ?W...QLineEdit(self.dataGroupBox)
        self.updatesEdit.setReadOnly(True)
        self.updatesEdit.setObjectName("updatesEdit")
        self.formLayout.setWidget(3, ?W...QFormLayout.FieldRole, self.updatesEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem1 _ ?W...QSpacerItem(20, 24, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.aW..(self.dataGroupBox)

        self.retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C...QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.webFormGroupBox.setTitle(_translate("Form", "Web Form"))
        self.dataGroupBox.setTitle(_translate("Form", "Extracted Data"))
        self.firstNameLabel.sT..(_translate("Form", "First Name"))
        self.lastNameLabel.sT..(_translate("Form", "Last Name"))
        self.genderLabel.sT..(_translate("Form", "Gender"))
        self.updatesLabel.sT..(_translate("Form", "Receive Updates"))

____ ? ______ QtWebKitWidgets
