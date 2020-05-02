# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\window.ui'
#
# Created: Sun Nov 05 12:51:12 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., ?G..

try:
    _fromUtf8 _ ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding _ ?G...?A...UnicodeUTF8
    ___ _translate(context, t.., disambig
        return ?G...?A...translate(context, t.., disambig, _encoding)
except AttributeError:
    ___ _translate(context, t.., disambig
        return ?G...?A...translate(context, t.., disambig)

c_ Ui_Form(object
    ___ setupUi , Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        horizontalLayout _ ?G...QHBoxLayout(Form)
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        verticalLayout _ ?G...QVBoxLayout()
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        pushButton _ ?G...?PB..(Form)
        pushButton.setObjectName(_fromUtf8("pushButton"))
        verticalLayout.addWidget(pushButton)
        pushButton_2 _ ?G...?PB..(Form)
        pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        verticalLayout.addWidget(pushButton_2)
        spacerItem _ ?G...QSpacerItem(20, 40, ?G...QSizePolicy.Minimum, ?G...QSizePolicy.Expanding)
        verticalLayout.aI..(spacerItem)
        horizontalLayout.addLayout(verticalLayout)

        retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi , Form
        Form.setWindowTitle(_translate("Form", "Form", None))
        pushButton.sT..(_translate("Form", "PushButton", None))
        pushButton_2.sT..(_translate("Form", "PushButton", None))

