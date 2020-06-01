# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagesettings.ui'
#
# Created: Fri Jun 28 11:48:28 2013
#      by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_ImageSettingsUi(object):
    ___ setupUi  ImageSettingsUi):
        ImageSettingsUi.setObjectName("ImageSettingsUi")
        ImageSettingsUi.resize(332, 270)
        self.gridLayout _ ?W...QGridLayout(ImageSettingsUi)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 _ ?W...QGroupBox(ImageSettingsUi)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 _ ?W...QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 _ ?W...QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.aW..(self.label_8, 0, 0, 1, 2)
        self.imageResolutionBox _ ?W...QComboBox(self.groupBox_2)
        self.imageResolutionBox.setObjectName("imageResolutionBox")
        self.gridLayout_2.aW..(self.imageResolutionBox, 1, 0, 1, 2)
        self.label_6 _ ?W...QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.aW..(self.label_6, 2, 0, 1, 2)
        self.imageCodecBox _ ?W...QComboBox(self.groupBox_2)
        self.imageCodecBox.setObjectName("imageCodecBox")
        self.gridLayout_2.aW..(self.imageCodecBox, 3, 0, 1, 2)
        self.label_7 _ ?W...QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.aW..(self.label_7, 4, 0, 1, 1)
        self.imageQualitySlider _ ?W...QSlider(self.groupBox_2)
        self.imageQualitySlider.setMaximum(4)
        self.imageQualitySlider.setOrientation(?C...__.Horizontal)
        self.imageQualitySlider.setObjectName("imageQualitySlider")
        self.gridLayout_2.aW..(self.imageQualitySlider, 4, 1, 1, 1)
        self.gridLayout.aW..(self.groupBox_2, 0, 0, 1, 1)
        spacerItem _ ?W...QSpacerItem(20, 14, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox _ ?W...QDialogButtonBox(ImageSettingsUi)
        self.buttonBox.setOrientation(?C...__.Horizontal)
        self.buttonBox.setStandardButtons(?W...QDialogButtonBox.Cancel|?W...QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.aW..(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(ImageSettingsUi)
        self.buttonBox.accepted.c..(ImageSettingsUi.accept)
        self.buttonBox.rejected.c..(ImageSettingsUi.reject)
        ?C...QMetaObject.connectSlotsByName(ImageSettingsUi)

    ___ retranslateUi  ImageSettingsUi):
        _translate _ ?C...QCoreApplication.translate
        ImageSettingsUi.setWindowTitle(_translate("ImageSettingsUi", "Dialog"))
        self.groupBox_2.setTitle(_translate("ImageSettingsUi", "Image"))
        self.label_8.sT..(_translate("ImageSettingsUi", "Resolution:"))
        self.label_6.sT..(_translate("ImageSettingsUi", "Image Format:"))
        self.label_7.sT..(_translate("ImageSettingsUi", "Quality:"))

