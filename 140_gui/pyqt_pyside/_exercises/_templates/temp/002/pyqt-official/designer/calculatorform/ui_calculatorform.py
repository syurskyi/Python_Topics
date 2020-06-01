# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorform.ui'
#
# Created: Fri Jul 26 06:41:48 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_CalculatorForm(object):
    ___ setupUi  CalculatorForm):
        CalculatorForm.setObjectName("CalculatorForm")
        CalculatorForm.resize(400, 300)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Policy(5), ?W...QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorForm.sizePolicy().hasHeightForWidth())
        CalculatorForm.setSizePolicy(sizePolicy)
        self.gridlayout _ ?W...QGridLayout(CalculatorForm)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 6, 1, 1)
        self.label_3_2 _ ?W...QLabel(CalculatorForm)
        self.label_3_2.setGeometry(QtCore.QRect(169, 9, 20, 52))
        self.label_3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3_2.setObjectName("label_3_2")
        self.gridlayout.addWidget(self.label_3_2, 0, 4, 1, 1)
        self.vboxlayout _ ?W...QVBoxLayout()
        self.vboxlayout.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_2_2_2 _ ?W...QLabel(CalculatorForm)
        self.label_2_2_2.setGeometry(QtCore.QRect(1, 1, 36, 17))
        self.label_2_2_2.setObjectName("label_2_2_2")
        self.vboxlayout.addWidget(self.label_2_2_2)
        self.outputWidget _ ?W...QLabel(CalculatorForm)
        self.outputWidget.setGeometry(QtCore.QRect(1, 24, 36, 27))
        self.outputWidget.setFrameShape(?W...QFrame.Box)
        self.outputWidget.setFrameShadow(?W...QFrame.Sunken)
        self.outputWidget.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignBottom|QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignHorizontal_Mask|QtCore.Qt.AlignJustify|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignVertical_Mask)
        self.outputWidget.setObjectName("outputWidget")
        self.vboxlayout.addWidget(self.outputWidget)
        self.gridlayout.addLayout(self.vboxlayout, 0, 5, 1, 1)
        spacerItem1 _ ?W...QSpacerItem(20, 40, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.vboxlayout1 _ ?W...QVBoxLayout()
        self.vboxlayout1.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.label_2 _ ?W...QLabel(CalculatorForm)
        self.label_2.setGeometry(QtCore.QRect(1, 1, 46, 19))
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)
        self.inputSpinBox2 _ ?W...QSpinBox(CalculatorForm)
        self.inputSpinBox2.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox2.setObjectName("inputSpinBox2")
        self.vboxlayout1.addWidget(self.inputSpinBox2)
        self.gridlayout.addLayout(self.vboxlayout1, 0, 3, 1, 1)
        self.label_3 _ ?W...QLabel(CalculatorForm)
        self.label_3.setGeometry(QtCore.QRect(63, 9, 20, 52))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.vboxlayout2 _ ?W...QVBoxLayout()
        self.vboxlayout2.setContentsMargins(1, 1, 1, 1)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label _ ?W...QLabel(CalculatorForm)
        self.label.setGeometry(QtCore.QRect(1, 1, 46, 19))
        self.label.setObjectName("label")
        self.vboxlayout2.addWidget(self.label)
        self.inputSpinBox1 _ ?W...QSpinBox(CalculatorForm)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox1.setObjectName("inputSpinBox1")
        self.vboxlayout2.addWidget(self.inputSpinBox1)
        self.gridlayout.addLayout(self.vboxlayout2, 0, 0, 1, 1)

        self.retranslateUi(CalculatorForm)
        QtCore.QMetaObject.connectSlotsByName(CalculatorForm)

    ___ retranslateUi  CalculatorForm):
        _translate _ QtCore.QCoreApplication.translate
        CalculatorForm.setWindowTitle(_translate("CalculatorForm", "Calculator Form"))
        self.label_3_2.sT..(_translate("CalculatorForm", "="))
        self.label_2_2_2.sT..(_translate("CalculatorForm", "Output"))
        self.outputWidget.sT..(_translate("CalculatorForm", "0"))
        self.label_2.sT..(_translate("CalculatorForm", "Input 2"))
        self.label_3.sT..(_translate("CalculatorForm", "+"))
        self.label.sT..(_translate("CalculatorForm", "Input 1"))

