# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\compileUI\splitChannel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 _____ QtCore, QtGui

___
    _fromUtf8 = QtCore.QString.fromUtf8
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

class Ui_Form(object):
    ___ setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(267, 228)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.AdditiveRebuild_grp = QGroupBox(Form)
        self.AdditiveRebuild_grp.setObjectName(_fromUtf8("AdditiveRebuild_grp"))
        self.verticalLayout = QVBoxLayout(self.AdditiveRebuild_grp)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.MentalRay_btn = QPushButton(self.AdditiveRebuild_grp)
        self.MentalRay_btn.setObjectName(_fromUtf8("MentalRay_btn"))
        self.horizontalLayout.addWidget(self.MentalRay_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.PrMan_btn = QPushButton(self.AdditiveRebuild_grp)
        self.PrMan_btn.setObjectName(_fromUtf8("PrMan_btn"))
        self.horizontalLayout_2.addWidget(self.PrMan_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.VRAY_btn = QPushButton(self.AdditiveRebuild_grp)
        self.VRAY_btn.setObjectName(_fromUtf8("VRAY_btn"))
        self.horizontalLayout_3.addWidget(self.VRAY_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.AdditiveRebuild_grp)
        self.RelightSetup_grp = QGroupBox(Form)
        self.RelightSetup_grp.setObjectName(_fromUtf8("RelightSetup_grp"))
        self.verticalLayout_2 = QVBoxLayout(self.RelightSetup_grp)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.relight_btn = QPushButton(self.RelightSetup_grp)
        self.relight_btn.setObjectName(_fromUtf8("relight_btn"))
        self.horizontalLayout_4.addWidget(self.relight_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.RelightSetup_grp)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Split Channel", N..))
        self.AdditiveRebuild_grp.setTitle(_translate("Form", "Additive Rebuild", N..))
        self.MentalRay_btn.setText(_translate("Form", "Mental Ray", N..))
        self.PrMan_btn.setText(_translate("Form", "PrMan", N..))
        self.VRAY_btn.setText(_translate("Form", "VRAY", N..))
        self.RelightSetup_grp.setTitle(_translate("Form", "Relight Setup", N..))
        self.relight_btn.setText(_translate("Form", "Relight", N..))

