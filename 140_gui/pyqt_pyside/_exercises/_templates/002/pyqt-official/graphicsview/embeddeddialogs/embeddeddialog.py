# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddeddialog.ui'
#
# Created: Wed May 15 16:13:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-8d430da208a7
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_embeddedDialog o..
    ___ setupUi  embeddedDialog):
        embeddedDialog.setObjectName("embeddedDialog")
        embeddedDialog.r..(407, 134)
        formLayout _ ?W...?FL..(embeddedDialog)
        formLayout.setObjectName("formLayout")
        label _ ?W...?L..(embeddedDialog)
        label.setObjectName("label")
        formLayout.setWidget(0, ?W...?FL...LabelRole, label)
        layoutDirection _ ?W...?CB(embeddedDialog)
        layoutDirection.setObjectName("layoutDirection")
        layoutDirection.aI..("")
        layoutDirection.aI..("")
        formLayout.setWidget(0, ?W...?FL...FieldRole, layoutDirection)
        label_2 _ ?W...?L..(embeddedDialog)
        label_2.setObjectName("label_2")
        formLayout.setWidget(1, ?W...?FL...LabelRole, label_2)
        fontComboBox _ ?W...QFontComboBox(embeddedDialog)
        fontComboBox.setObjectName("fontComboBox")
        formLayout.setWidget(1, ?W...?FL...FieldRole, fontComboBox)
        label_3 _ ?W...?L..(embeddedDialog)
        label_3.setObjectName("label_3")
        formLayout.setWidget(2, ?W...?FL...LabelRole, label_3)
        style _ ?W...?CB(embeddedDialog)
        style.setObjectName("style")
        formLayout.setWidget(2, ?W...?FL...FieldRole, style)
        label_4 _ ?W...?L..(embeddedDialog)
        label_4.setObjectName("label_4")
        formLayout.setWidget(3, ?W...?FL...LabelRole, label_4)
        spacing _ ?W...?S..(embeddedDialog)
        spacing.setOrientation(?C...__.H..)
        spacing.setObjectName("spacing")
        formLayout.setWidget(3, ?W...?FL...FieldRole, spacing)
        label.setBuddy(layoutDirection)
        label_2.setBuddy(fontComboBox)
        label_3.setBuddy(style)
        label_4.setBuddy(spacing)

        retranslateUi(embeddedDialog)
        ?C...QMetaObject.connectSlotsByName(embeddedDialog)

    ___ retranslateUi  embeddedDialog):
        _translate _ ?C... ?CA...translate
        embeddedDialog.sWT..(_translate("embeddedDialog", "Embedded Dialog"))
        label.sT..(_translate("embeddedDialog", "Layout Direction:"))
        layoutDirection.setItemText(0, _translate("embeddedDialog", "Left to Right"))
        layoutDirection.setItemText(1, _translate("embeddedDialog", "Right to Left"))
        label_2.sT..(_translate("embeddedDialog", "Select Font:"))
        label_3.sT..(_translate("embeddedDialog", "Style:"))
        label_4.sT..(_translate("embeddedDialog", "Layout spacing:"))

