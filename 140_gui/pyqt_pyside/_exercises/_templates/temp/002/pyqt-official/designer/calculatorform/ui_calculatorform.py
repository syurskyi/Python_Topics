# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorform.ui'
#
# Created: Fri Jul 26 06:41:48 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_CalculatorForm(object):
    ___ setupUi  CalculatorForm):
        CalculatorForm.setObjectName("CalculatorForm")
        CalculatorForm.r..(400, 300)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(5), ?W...QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorForm.sizePolicy().hasHeightForWidth())
        CalculatorForm.sSP..(sizePolicy)
        gridlayout _ ?W...QGridLayout(CalculatorForm)
        gridlayout.setContentsMargins(9, 9, 9, 9)
        gridlayout.setSpacing(6)
        gridlayout.setObjectName("gridlayout")
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        gridlayout.aI..(spacerItem, 0, 6, 1, 1)
        label_3_2 _ ?W...QLabel(CalculatorForm)
        label_3_2.setGeometry(?C...QRect(169, 9, 20, 52))
        label_3_2.setAlignment(?C...__.AlignCenter)
        label_3_2.setObjectName("label_3_2")
        gridlayout.aW..(label_3_2, 0, 4, 1, 1)
        vboxlayout _ ?W...?VBL..
        vboxlayout.setContentsMargins(1, 1, 1, 1)
        vboxlayout.setSpacing(6)
        vboxlayout.setObjectName("vboxlayout")
        label_2_2_2 _ ?W...QLabel(CalculatorForm)
        label_2_2_2.setGeometry(?C...QRect(1, 1, 36, 17))
        label_2_2_2.setObjectName("label_2_2_2")
        vboxlayout.aW..(label_2_2_2)
        outputWidget _ ?W...QLabel(CalculatorForm)
        outputWidget.setGeometry(?C...QRect(1, 24, 36, 27))
        outputWidget.setFrameShape(?W...QFrame.Box)
        outputWidget.setFrameShadow(?W...QFrame.Sunken)
        outputWidget.setAlignment(?C...__.AlignAbsolute|?C...__.AlignBottom|?C...__.AlignCenter|?C...__.AlignHCenter|?C...__.AlignHorizontal_Mask|?C...__.AlignJustify|?C...__.AlignLeading|?C...__.AlignLeft|?C...__.AlignRight|?C...__.AlignTop|?C...__.AlignTrailing|?C...__.AlignVCenter|?C...__.AlignVertical_Mask)
        outputWidget.setObjectName("outputWidget")
        vboxlayout.aW..(outputWidget)
        gridlayout.aL..(vboxlayout, 0, 5, 1, 1)
        spacerItem1 _ ?W...QSpacerItem(20, 40, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.E..)
        gridlayout.aI..(spacerItem1, 1, 2, 1, 1)
        vboxlayout1 _ ?W...?VBL..
        vboxlayout1.setContentsMargins(1, 1, 1, 1)
        vboxlayout1.setSpacing(6)
        vboxlayout1.setObjectName("vboxlayout1")
        label_2 _ ?W...QLabel(CalculatorForm)
        label_2.setGeometry(?C...QRect(1, 1, 46, 19))
        label_2.setObjectName("label_2")
        vboxlayout1.aW..(label_2)
        inputSpinBox2 _ ?W...SB..(CalculatorForm)
        inputSpinBox2.setGeometry(?C...QRect(1, 26, 46, 25))
        inputSpinBox2.setObjectName("inputSpinBox2")
        vboxlayout1.aW..(inputSpinBox2)
        gridlayout.aL..(vboxlayout1, 0, 3, 1, 1)
        label_3 _ ?W...QLabel(CalculatorForm)
        label_3.setGeometry(?C...QRect(63, 9, 20, 52))
        label_3.setAlignment(?C...__.AlignCenter)
        label_3.setObjectName("label_3")
        gridlayout.aW..(label_3, 0, 1, 1, 1)
        vboxlayout2 _ ?W...?VBL..
        vboxlayout2.setContentsMargins(1, 1, 1, 1)
        vboxlayout2.setSpacing(6)
        vboxlayout2.setObjectName("vboxlayout2")
        label _ ?W...QLabel(CalculatorForm)
        label.setGeometry(?C...QRect(1, 1, 46, 19))
        label.setObjectName("label")
        vboxlayout2.aW..(label)
        inputSpinBox1 _ ?W...SB..(CalculatorForm)
        inputSpinBox1.setGeometry(?C...QRect(1, 26, 46, 25))
        inputSpinBox1.setObjectName("inputSpinBox1")
        vboxlayout2.aW..(inputSpinBox1)
        gridlayout.aL..(vboxlayout2, 0, 0, 1, 1)

        retranslateUi(CalculatorForm)
        ?C...QMetaObject.connectSlotsByName(CalculatorForm)

    ___ retranslateUi  CalculatorForm):
        _translate _ ?C...QCoreApplication.translate
        CalculatorForm.sWT..(_translate("CalculatorForm", "Calculator Form"))
        label_3_2.sT..(_translate("CalculatorForm", "="))
        label_2_2_2.sT..(_translate("CalculatorForm", "Output"))
        outputWidget.sT..(_translate("CalculatorForm", "0"))
        label_2.sT..(_translate("CalculatorForm", "Input 2"))
        label_3.sT..(_translate("CalculatorForm", "+"))
        label.sT..(_translate("CalculatorForm", "Input 1"))

