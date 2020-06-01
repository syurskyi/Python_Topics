# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatsetnickname.ui'
#
# Created: Fri Jul 26 06:48:20 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_NicknameDialog(object):
    ___ setupUi  NicknameDialog):
        NicknameDialog.setObjectName("NicknameDialog")
        NicknameDialog.resize(396, 105)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NicknameDialog.sizePolicy().hasHeightForWidth())
        NicknameDialog.sSP..(sizePolicy)
        vboxlayout _ ?W...QVBoxLayout(NicknameDialog)
        vboxlayout.setContentsMargins(9, 9, 9, 9)
        vboxlayout.setSpacing(6)
        vboxlayout.setObjectName("vboxlayout")
        vboxlayout1 _ ?W...?VBL..
        vboxlayout1.setContentsMargins(0, 0, 0, 0)
        vboxlayout1.setSpacing(6)
        vboxlayout1.setObjectName("vboxlayout1")
        label _ ?W...QLabel(NicknameDialog)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.sSP..(sizePolicy)
        label.setObjectName("label")
        vboxlayout1.aW..(label)
        nickname _ ?W...QLineEdit(NicknameDialog)
        nickname.setObjectName("nickname")
        vboxlayout1.aW..(nickname)
        vboxlayout.aL..(vboxlayout1)
        hboxlayout _ ?W...QHBoxLayout()
        hboxlayout.setContentsMargins(0, 0, 0, 0)
        hboxlayout.setSpacing(6)
        hboxlayout.setObjectName("hboxlayout")
        spacerItem _ ?W...QSpacerItem(131, 31, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        hboxlayout.addItem(spacerItem)
        okButton _ ?W...?PB..(NicknameDialog)
        okButton.setObjectName("okButton")
        hboxlayout.aW..(okButton)
        cancelButton _ ?W...?PB..(NicknameDialog)
        cancelButton.setObjectName("cancelButton")
        hboxlayout.aW..(cancelButton)
        spacerItem1 _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        hboxlayout.addItem(spacerItem1)
        vboxlayout.aL..(hboxlayout)

        retranslateUi(NicknameDialog)
        okButton.c__.c..(NicknameDialog.accept)
        cancelButton.c__.c..(NicknameDialog.reject)
        ?C...QMetaObject.connectSlotsByName(NicknameDialog)

    ___ retranslateUi  NicknameDialog):
        _translate _ ?C...QCoreApplication.translate
        NicknameDialog.setWindowTitle(_translate("NicknameDialog", "Set nickname"))
        label.sT..(_translate("NicknameDialog", "New nickname:"))
        okButton.sT..(_translate("NicknameDialog", "OK"))
        cancelButton.sT..(_translate("NicknameDialog", "Cancel"))

