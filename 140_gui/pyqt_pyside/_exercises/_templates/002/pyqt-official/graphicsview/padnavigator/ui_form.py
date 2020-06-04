# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sun May  5 07:55:08 2013
#      by: PyQt5 UI code generator 5.0-snapshot-74eb89bd4fb2
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form o..
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.r..(378, 385)
        verticalLayout_2 _ ?W...?VBL..(Form)
        verticalLayout_2.setObjectName("verticalLayout_2")
        groupBox _ ?W...?GB..(Form)
        groupBox.setFlat( st.
        groupBox.setCheckable( st.
        groupBox.setObjectName("groupBox")
        gridLayout _ ?W...QGridLayout(groupBox)
        gridLayout.setObjectName("gridLayout")
        label _ ?W...?L..(groupBox)
        label.setObjectName("label")
        gridLayout.aW..(label, 0, 0, 1, 1)
        hostName _ ?W...QLineEdit(groupBox)
        hostName.setObjectName("hostName")
        gridLayout.aW..(hostName, 0, 1, 1, 1)
        label_2 _ ?W...?L..(groupBox)
        label_2.setObjectName("label_2")
        gridLayout.aW..(label_2, 1, 0, 1, 1)
        label_3 _ ?W...?L..(groupBox)
        label_3.setObjectName("label_3")
        gridLayout.aW..(label_3, 2, 0, 1, 1)
        horizontalLayout _ ?W...?HBL..
        horizontalLayout.setObjectName("horizontalLayout")
        horizontalSlider _ ?W...?S..(groupBox)
        horizontalSlider.setProperty("value", 42)
        horizontalSlider.setOrientation(?C...__.H..)
        horizontalSlider.setObjectName("horizontalSlider")
        horizontalLayout.aW..(horizontalSlider)
        spinBox _ ?W...SB..(groupBox)
        spinBox.setProperty("value", 42)
        spinBox.setObjectName("spinBox")
        horizontalLayout.aW..(spinBox)
        gridLayout.aL..(horizontalLayout, 2, 1, 1, 1)
        dateTimeEdit _ ?W...?DTE..(groupBox)
        dateTimeEdit.setObjectName("dateTimeEdit")
        gridLayout.aW..(dateTimeEdit, 1, 1, 1, 1)
        verticalLayout_2.aW..(groupBox)
        groupBox_2 _ ?W...?GB..(Form)
        groupBox_2.setFlat( st.
        groupBox_2.setCheckable( st.
        groupBox_2.setObjectName("groupBox_2")
        horizontalLayout_2 _ ?W...?HBL..(groupBox_2)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        treeWidget _ ?W...QTreeWidget(groupBox_2)
        tW__.setObjectName("treeWidget")
        item_0 _ ?W...?TWI..(tW__)
        item_1 _ ?W...?TWI..(item_0)
        item_2 _ ?W...?TWI..(item_1)
        item_2 _ ?W...?TWI..(item_1)
        item_2 _ ?W...?TWI..(item_1)
        item_0 _ ?W...?TWI..(tW__)
        item_1 _ ?W...?TWI..(item_0)
        item_2 _ ?W...?TWI..(item_1)
        item_0 _ ?W...?TWI..(tW__)
        item_1 _ ?W...?TWI..(item_0)
        item_2 _ ?W...?TWI..(item_1)
        horizontalLayout_2.aW..(tW__)
        verticalLayout_2.aW..(groupBox_2)

        retranslateUi(Form)
        horizontalSlider.valueChanged['int'].c..(spinBox.sV..)
        spinBox.valueChanged['int'].c..(horizontalSlider.sV..)
        ?C...QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(groupBox, hostName)
        Form.setTabOrder(hostName, dateTimeEdit)
        Form.setTabOrder(dateTimeEdit, horizontalSlider)
        Form.setTabOrder(horizontalSlider, spinBox)
        Form.setTabOrder(spinBox, groupBox_2)
        Form.setTabOrder(groupBox_2, tW__)

    ___ retranslateUi  Form):
        _translate _ ?C... ?CA...translate
        Form.sWT..(_translate("Form", "BackSide"))
        groupBox.setTitle(_translate("Form", "Settings"))
        label.sT..(_translate("Form", "Title:"))
        hostName.sT..(_translate("Form", "Pad Navigator Example"))
        label_2.sT..(_translate("Form", "Modified:"))
        label_3.sT..(_translate("Form", "Extent"))
        groupBox_2.setTitle(_translate("Form", "Other input"))
        tW__.headerItem().sT..(0, _translate("Form", "Widgets On Graphics View"))
        __sortingEnabled _ tW__.isSortingEnabled()
        tW__.setSortingEnabled F..
        tW__.topLevelItem(0).sT..(0, _translate("Form", "QGraphicsProxyWidget"))
        tW__.topLevelItem(0).child(0).sT..(0, _translate("Form", "QGraphicsWidget"))
        tW__.topLevelItem(0).child(0).child(0).sT..(0, _translate("Form", "QObject"))
        tW__.topLevelItem(0).child(0).child(1).sT..(0, _translate("Form", "QGraphicsItem"))
        tW__.topLevelItem(0).child(0).child(2).sT..(0, _translate("Form", "QGraphicsLayoutItem"))
        tW__.topLevelItem(1).sT..(0, _translate("Form", "QGraphicsGridLayout"))
        tW__.topLevelItem(1).child(0).sT..(0, _translate("Form", "QGraphicsLayout"))
        tW__.topLevelItem(1).child(0).child(0).sT..(0, _translate("Form", "QGraphicsLayoutItem"))
        tW__.topLevelItem(2).sT..(0, _translate("Form", "QGraphicsLinearLayout"))
        tW__.topLevelItem(2).child(0).sT..(0, _translate("Form", "QGraphicsLayout"))
        tW__.topLevelItem(2).child(0).child(0).sT..(0, _translate("Form", "QGraphicsLayoutItem"))
        tW__.sSE..__sortingEnabled)

