# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatsetnickname.ui'
#
# Created: Fri Jul 26 06:48:20 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, QtGui, ?W..

class Ui_NicknameDialog(object):
    ___ setupUi(self, NicknameDialog):
        NicknameDialog.setObjectName("NicknameDialog")
        NicknameDialog.resize(396, 105)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NicknameDialog.sizePolicy().hasHeightForWidth())
        NicknameDialog.setSizePolicy(sizePolicy)
        self.vboxlayout _ ?W...QVBoxLayout(NicknameDialog)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 _ ?W...QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label _ ?W...QLabel(NicknameDialog)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(1), ?W...QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.nickname _ ?W...QLineEdit(NicknameDialog)
        self.nickname.setObjectName("nickname")
        self.vboxlayout1.addWidget(self.nickname)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout _ ?W...QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem _ ?W...QSpacerItem(131, 31, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton _ ?W...?PB..(NicknameDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton _ ?W...?PB..(NicknameDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem1 _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(NicknameDialog)
        self.okButton.c__.c..(NicknameDialog.accept)
        self.cancelButton.c__.c..(NicknameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NicknameDialog)

    ___ retranslateUi(self, NicknameDialog):
        _translate _ QtCore.QCoreApplication.translate
        NicknameDialog.setWindowTitle(_translate("NicknameDialog", "Set nickname"))
        self.label.sT..(_translate("NicknameDialog", "New nickname:"))
        self.okButton.sT..(_translate("NicknameDialog", "OK"))
        self.cancelButton.sT..(_translate("NicknameDialog", "Cancel"))

