# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\compileUI\splitChannel.ui'
#
# Created: Mon Jan 16 20:10:30 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide _____ QtCore, QtGui

class Ui_Form(object):
    ___ setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(267, 228)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AdditiveRebuild_grp = QGroupBox(Form)
        self.AdditiveRebuild_grp.setObjectName("AdditiveRebuild_grp")
        self.verticalLayout = QVBoxLayout(self.AdditiveRebuild_grp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.MentalRay_btn = QPushButton(self.AdditiveRebuild_grp)
        self.MentalRay_btn.setObjectName("MentalRay_btn")
        self.horizontalLayout.addWidget(self.MentalRay_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.PrMan_btn = QPushButton(self.AdditiveRebuild_grp)
        self.PrMan_btn.setObjectName("PrMan_btn")
        self.horizontalLayout_2.addWidget(self.PrMan_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.VRAY_btn = QPushButton(self.AdditiveRebuild_grp)
        self.VRAY_btn.setObjectName("VRAY_btn")
        self.horizontalLayout_3.addWidget(self.VRAY_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.AdditiveRebuild_grp)
        self.RelightSetup_grp = QGroupBox(Form)
        self.RelightSetup_grp.setObjectName("RelightSetup_grp")
        self.verticalLayout_2 = QVBoxLayout(self.RelightSetup_grp)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.relight_btn = QPushButton(self.RelightSetup_grp)
        self.relight_btn.setObjectName("relight_btn")
        self.horizontalLayout_4.addWidget(self.relight_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.RelightSetup_grp)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Split Channel", N.., QApplication.UnicodeUTF8))
        self.AdditiveRebuild_grp.setTitle(QApplication.translate("Form", "Additive Rebuild", N.., QApplication.UnicodeUTF8))
        self.MentalRay_btn.setText(QApplication.translate("Form", "Mental Ray", N.., QApplication.UnicodeUTF8))
        self.PrMan_btn.setText(QApplication.translate("Form", "PrMan", N.., QApplication.UnicodeUTF8))
        self.VRAY_btn.setText(QApplication.translate("Form", "VRAY", N.., QApplication.UnicodeUTF8))
        self.RelightSetup_grp.setTitle(QApplication.translate("Form", "Relight Setup", N.., QApplication.UnicodeUTF8))
        self.relight_btn.setText(QApplication.translate("Form", "Relight", N.., QApplication.UnicodeUTF8))

