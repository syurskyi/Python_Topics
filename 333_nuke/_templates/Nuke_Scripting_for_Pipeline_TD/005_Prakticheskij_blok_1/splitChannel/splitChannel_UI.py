# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\compileUI\splitChannel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ _C.., _G..

___
    _fromUtf8 _ _C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s):
        r_ s

___
    _encoding _ QApplication.UnicodeUTF8
    ___ _translate(context, text, disambig):
        r_ QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig):
        r_ QApplication.translate(context, text, disambig)

c_ Ui_Form(object):
    ___ setupUi(, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(267, 228)
        verticalLayout_3 _ QVBoxLayout(Form)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        AdditiveRebuild_grp _ QGroupBox(Form)
        AdditiveRebuild_grp.setObjectName(_fromUtf8("AdditiveRebuild_grp"))
        verticalLayout _ QVBoxLayout(AdditiveRebuild_grp)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout _ QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem _ QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        MentalRay_btn _ QPushButton(AdditiveRebuild_grp)
        MentalRay_btn.setObjectName(_fromUtf8("MentalRay_btn"))
        horizontalLayout.aW..(MentalRay_btn)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout_2 _ QHBoxLayout()
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 _ QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem1)
        PrMan_btn _ QPushButton(AdditiveRebuild_grp)
        PrMan_btn.setObjectName(_fromUtf8("PrMan_btn"))
        horizontalLayout_2.aW..(PrMan_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        horizontalLayout_3 _ QHBoxLayout()
        horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 _ QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_3.addItem(spacerItem2)
        VRAY_btn _ QPushButton(AdditiveRebuild_grp)
        VRAY_btn.setObjectName(_fromUtf8("VRAY_btn"))
        horizontalLayout_3.aW..(VRAY_btn)
        verticalLayout.addLayout(horizontalLayout_3)
        verticalLayout_3.aW..(AdditiveRebuild_grp)
        RelightSetup_grp _ QGroupBox(Form)
        RelightSetup_grp.setObjectName(_fromUtf8("RelightSetup_grp"))
        verticalLayout_2 _ QVBoxLayout(RelightSetup_grp)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        horizontalLayout_4 _ QHBoxLayout()
        horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 _ QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_4.addItem(spacerItem3)
        relight_btn _ QPushButton(RelightSetup_grp)
        relight_btn.setObjectName(_fromUtf8("relight_btn"))
        horizontalLayout_4.aW..(relight_btn)
        verticalLayout_2.addLayout(horizontalLayout_4)
        verticalLayout_3.aW..(RelightSetup_grp)
        spacerItem4 _ QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        verticalLayout_3.addItem(spacerItem4)

        retranslateUi(Form)
        _C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi(, Form):
        Form.setWindowTitle(_translate("Form", "Split Channel", N..))
        AdditiveRebuild_grp.setTitle(_translate("Form", "Additive Rebuild", N..))
        MentalRay_btn.setText(_translate("Form", "Mental Ray", N..))
        PrMan_btn.setText(_translate("Form", "PrMan", N..))
        VRAY_btn.setText(_translate("Form", "VRAY", N..))
        RelightSetup_grp.setTitle(_translate("Form", "Relight Setup", N..))
        relight_btn.setText(_translate("Form", "Relight", N..))

