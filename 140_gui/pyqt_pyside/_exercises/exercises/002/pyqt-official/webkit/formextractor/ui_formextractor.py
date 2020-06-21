# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formextractor.ui'
#
# Created: Tue May 14 17:59:08 2013
#      by: PyQt5 UI code generator 5.0-snapshot-b0831183bf83
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form o..
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.r..(680, 218)
        horizontalLayout _ ?W...?HBL..(Form)
        horizontalLayout.setObjectName("horizontalLayout")
        webFormGroupBox _ ?W...?GB..(Form)
        webFormGroupBox.setObjectName("webFormGroupBox")
        verticalLayout_2 _ ?W...?VBL..(webFormGroupBox)
        verticalLayout_2.setObjectName("verticalLayout_2")
        verticalLayout _ ?W...?VBL..
        verticalLayout.setObjectName("verticalLayout")
        webView _ QtWebKitWidgets.QWebView(webFormGroupBox)
        webView.sMS..(?C...?S..(200, 150))
        webView.sMS..(?C...?S..(400, 16777215))
        webView.setUrl(?C...?U..("about:blank"))
        webView.setObjectName("webView")
        verticalLayout.aW..(webView)
        verticalLayout_2.aL..(verticalLayout)
        horizontalLayout.aW..(webFormGroupBox)
        spacerItem _ ?W...?SI..(28, 20, ?W...?SP...E.., ?W...?SP...Minimum)
        horizontalLayout.aI..(spacerItem)
        dataGroupBox _ ?W...?GB..(Form)
        dataGroupBox.setObjectName("dataGroupBox")
        verticalLayout_3 _ ?W...?VBL..(dataGroupBox)
        verticalLayout_3.setObjectName("verticalLayout_3")
        formLayout _ ?W...?FL..
        formLayout.setFieldGrowthPolicy(?W...?FL...FieldsStayAtSizeHint)
        formLayout.setObjectName("formLayout")
        firstNameLabel _ ?W...?L..(dataGroupBox)
        firstNameLabel.setObjectName("firstNameLabel")
        formLayout.setWidget(0, ?W...?FL...LabelRole, firstNameLabel)
        firstNameEdit _ ?W...QLineEdit(dataGroupBox)
        firstNameEdit.sRO..( st.
        firstNameEdit.setObjectName("firstNameEdit")
        formLayout.setWidget(0, ?W...?FL...FieldRole, firstNameEdit)
        lastNameLabel _ ?W...?L..(dataGroupBox)
        lastNameLabel.setObjectName("lastNameLabel")
        formLayout.setWidget(1, ?W...?FL...LabelRole, lastNameLabel)
        lastNameEdit _ ?W...QLineEdit(dataGroupBox)
        lastNameEdit.sRO..( st.
        lastNameEdit.setObjectName("lastNameEdit")
        formLayout.setWidget(1, ?W...?FL...FieldRole, lastNameEdit)
        genderLabel _ ?W...?L..(dataGroupBox)
        genderLabel.setObjectName("genderLabel")
        formLayout.setWidget(2, ?W...?FL...LabelRole, genderLabel)
        genderEdit _ ?W...QLineEdit(dataGroupBox)
        genderEdit.sRO..( st.
        genderEdit.setObjectName("genderEdit")
        formLayout.setWidget(2, ?W...?FL...FieldRole, genderEdit)
        updatesLabel _ ?W...?L..(dataGroupBox)
        updatesLabel.setObjectName("updatesLabel")
        formLayout.setWidget(3, ?W...?FL...LabelRole, updatesLabel)
        updatesEdit _ ?W...QLineEdit(dataGroupBox)
        updatesEdit.sRO..( st.
        updatesEdit.setObjectName("updatesEdit")
        formLayout.setWidget(3, ?W...?FL...FieldRole, updatesEdit)
        verticalLayout_3.aL..(formLayout)
        spacerItem1 _ ?W...?SI..(20, 24, ?W...?SP...Minimum, ?W...?SP...E..)
        verticalLayout_3.aI..(spacerItem1)
        horizontalLayout.aW..(dataGroupBox)

        retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C... ?CA...translate
        Form.sWT..(_translate("Form", "Form"))
        webFormGroupBox.setTitle(_translate("Form", "Web Form"))
        dataGroupBox.setTitle(_translate("Form", "Extracted Data"))
        firstNameLabel.sT..(_translate("Form", "First Name"))
        lastNameLabel.sT..(_translate("Form", "Last Name"))
        genderLabel.sT..(_translate("Form", "Gender"))
        updatesLabel.sT..(_translate("Form", "Receive Updates"))

____ ? ______ QtWebKitWidgets
