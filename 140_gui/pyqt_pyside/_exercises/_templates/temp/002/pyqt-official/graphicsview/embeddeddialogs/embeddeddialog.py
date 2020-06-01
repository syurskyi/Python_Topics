# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddeddialog.ui'
#
# Created: Wed May 15 16:13:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-8d430da208a7
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_embeddedDialog(object):
    ___ setupUi  embeddedDialog):
        embeddedDialog.setObjectName("embeddedDialog")
        embeddedDialog.resize(407, 134)
        self.formLayout _ ?W...QFormLayout(embeddedDialog)
        self.formLayout.setObjectName("formLayout")
        self.label _ ?W...QLabel(embeddedDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, ?W...QFormLayout.LabelRole, self.label)
        self.layoutDirection _ ?W...QComboBox(embeddedDialog)
        self.layoutDirection.setObjectName("layoutDirection")
        self.layoutDirection.addItem("")
        self.layoutDirection.addItem("")
        self.formLayout.setWidget(0, ?W...QFormLayout.FieldRole, self.layoutDirection)
        self.label_2 _ ?W...QLabel(embeddedDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, ?W...QFormLayout.LabelRole, self.label_2)
        self.fontComboBox _ ?W...QFontComboBox(embeddedDialog)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(1, ?W...QFormLayout.FieldRole, self.fontComboBox)
        self.label_3 _ ?W...QLabel(embeddedDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, ?W...QFormLayout.LabelRole, self.label_3)
        self.style _ ?W...QComboBox(embeddedDialog)
        self.style.setObjectName("style")
        self.formLayout.setWidget(2, ?W...QFormLayout.FieldRole, self.style)
        self.label_4 _ ?W...QLabel(embeddedDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, ?W...QFormLayout.LabelRole, self.label_4)
        self.spacing _ ?W...QSlider(embeddedDialog)
        self.spacing.setOrientation(?C...__.Horizontal)
        self.spacing.setObjectName("spacing")
        self.formLayout.setWidget(3, ?W...QFormLayout.FieldRole, self.spacing)
        self.label.setBuddy(self.layoutDirection)
        self.label_2.setBuddy(self.fontComboBox)
        self.label_3.setBuddy(self.style)
        self.label_4.setBuddy(self.spacing)

        self.retranslateUi(embeddedDialog)
        ?C...QMetaObject.connectSlotsByName(embeddedDialog)

    ___ retranslateUi  embeddedDialog):
        _translate _ ?C...QCoreApplication.translate
        embeddedDialog.setWindowTitle(_translate("embeddedDialog", "Embedded Dialog"))
        self.label.sT..(_translate("embeddedDialog", "Layout Direction:"))
        self.layoutDirection.setItemText(0, _translate("embeddedDialog", "Left to Right"))
        self.layoutDirection.setItemText(1, _translate("embeddedDialog", "Right to Left"))
        self.label_2.sT..(_translate("embeddedDialog", "Select Font:"))
        self.label_3.sT..(_translate("embeddedDialog", "Style:"))
        self.label_4.sT..(_translate("embeddedDialog", "Layout spacing:"))

