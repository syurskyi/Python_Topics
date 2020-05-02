# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\window.ui'
#
# Created: Sun Nov 05 12:51:12 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_Form(object
    ___ setupUi , Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        horizontalLayout = QtGui.QHBoxLayout(Form)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QtGui.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        pushButton = QtGui.?PB..(Form)
        pushButton.setObjectName("pushButton")
        verticalLayout.addWidget(pushButton)
        pushButton_2 = QtGui.?PB..(Form)
        pushButton_2.setObjectName("pushButton_2")
        verticalLayout.addWidget(pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        horizontalLayout.addLayout(verticalLayout)

        retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi , Form
        Form.setWindowTitle(QtGui.?A...translate("Form", "Form", None, QtGui.?A...UnicodeUTF8))
        pushButton.sT..(QtGui.?A...translate("Form", "PushButton", None, QtGui.?A...UnicodeUTF8))
        pushButton_2.sT..(QtGui.?A...translate("Form", "PushButton", None, QtGui.?A...UnicodeUTF8))

