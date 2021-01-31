# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\compileUI\splitChannel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ _C.., _G..

___
    _fromUtf8 = _C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s):
        r_ s

___
    _encoding = QApplication.UnicodeUTF8
    ___ _translate(context, text, disambig):
        r_ QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig):
        r_ QApplication.translate(context, text, disambig)

c_ Ui_Form(object):
    ___ setupUi(, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(267, 228)
        verticalLayout_3 = QVBoxLayout(Form)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        AdditiveRebuild_grp = QGroupBox(Form)
        AdditiveRebuild_grp.setObjectName(_fromUtf8("AdditiveRebuild_grp"))
        verticalLayout = QVBoxLayout(AdditiveRebuild_grp)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        MentalRay_btn = QPushButton(AdditiveRebuild_grp)
        MentalRay_btn.setObjectName(_fromUtf8("MentalRay_btn"))
        horizontalLayout.addWidget(MentalRay_btn)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem1)
        PrMan_btn = QPushButton(AdditiveRebuild_grp)
        PrMan_btn.setObjectName(_fromUtf8("PrMan_btn"))
        horizontalLayout_2.addWidget(PrMan_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        horizontalLayout_3 = QHBoxLayout()
        horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_3.addItem(spacerItem2)
        VRAY_btn = QPushButton(AdditiveRebuild_grp)
        VRAY_btn.setObjectName(_fromUtf8("VRAY_btn"))
        horizontalLayout_3.addWidget(VRAY_btn)
        verticalLayout.addLayout(horizontalLayout_3)
        verticalLayout_3.addWidget(AdditiveRebuild_grp)
        RelightSetup_grp = QGroupBox(Form)
        RelightSetup_grp.setObjectName(_fromUtf8("RelightSetup_grp"))
        verticalLayout_2 = QVBoxLayout(RelightSetup_grp)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        horizontalLayout_4 = QHBoxLayout()
        horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        horizontalLayout_4.addItem(spacerItem3)
        relight_btn = QPushButton(RelightSetup_grp)
        relight_btn.setObjectName(_fromUtf8("relight_btn"))
        horizontalLayout_4.addWidget(relight_btn)
        verticalLayout_2.addLayout(horizontalLayout_4)
        verticalLayout_3.addWidget(RelightSetup_grp)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
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

