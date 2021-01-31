# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\compileUI\splitChannel.ui'
#
# Created: Mon Jan 16 20:10:30 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ _C.., _G..

c_ Ui_Form(object):
    ___ setupUi(, Form):
        Form.setObjectName("Form")
        Form.resize(267, 228)
        verticalLayout_3 = QVBoxLayout(Form)
        verticalLayout_3.setObjectName("verticalLayout_3")
        AdditiveRebuild_grp = QGroupBox(Form)
        AdditiveRebuild_grp.setObjectName("AdditiveRebuild_grp")
        verticalLayout = QVBoxLayout(AdditiveRebuild_grp)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        MentalRay_btn = QPushButton(AdditiveRebuild_grp)
        MentalRay_btn.setObjectName("MentalRay_btn")
        horizontalLayout.aW..(MentalRay_btn)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem1)
        PrMan_btn = QPushButton(AdditiveRebuild_grp)
        PrMan_btn.setObjectName("PrMan_btn")
        horizontalLayout_2.aW..(PrMan_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        horizontalLayout_3 = QHBoxLayout()
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_3.addItem(spacerItem2)
        VRAY_btn = QPushButton(AdditiveRebuild_grp)
        VRAY_btn.setObjectName("VRAY_btn")
        horizontalLayout_3.aW..(VRAY_btn)
        verticalLayout.addLayout(horizontalLayout_3)
        verticalLayout_3.aW..(AdditiveRebuild_grp)
        RelightSetup_grp = QGroupBox(Form)
        RelightSetup_grp.setObjectName("RelightSetup_grp")
        verticalLayout_2 = QVBoxLayout(RelightSetup_grp)
        verticalLayout_2.setObjectName("verticalLayout_2")
        horizontalLayout_4 = QHBoxLayout()
        horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_4.addItem(spacerItem3)
        relight_btn = QPushButton(RelightSetup_grp)
        relight_btn.setObjectName("relight_btn")
        horizontalLayout_4.aW..(relight_btn)
        verticalLayout_2.addLayout(horizontalLayout_4)
        verticalLayout_3.aW..(RelightSetup_grp)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        verticalLayout_3.addItem(spacerItem4)

        retranslateUi(Form)
        _C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi(, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Split Channel", N.., QApplication.UnicodeUTF8))
        AdditiveRebuild_grp.setTitle(QApplication.translate("Form", "Additive Rebuild", N.., QApplication.UnicodeUTF8))
        MentalRay_btn.setText(QApplication.translate("Form", "Mental Ray", N.., QApplication.UnicodeUTF8))
        PrMan_btn.setText(QApplication.translate("Form", "PrMan", N.., QApplication.UnicodeUTF8))
        VRAY_btn.setText(QApplication.translate("Form", "VRAY", N.., QApplication.UnicodeUTF8))
        RelightSetup_grp.setTitle(QApplication.translate("Form", "Relight Setup", N.., QApplication.UnicodeUTF8))
        relight_btn.setText(QApplication.translate("Form", "Relight", N.., QApplication.UnicodeUTF8))

