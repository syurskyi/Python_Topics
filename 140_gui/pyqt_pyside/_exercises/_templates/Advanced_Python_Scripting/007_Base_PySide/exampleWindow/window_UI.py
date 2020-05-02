# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\exampleWindow\window.ui'
#
# Created: Sun Nov 05 15:05:59 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., QtGui

try:
    _fromUtf8 _ ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding _ QtGui.?A...UnicodeUTF8
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig)

c_ Ui_example(object
    ___ setupUi , example
        example.setObjectName(_fromUtf8("example"))
        example.resize(241, 204)
        verticalLayout_2 _ QtGui.QVBoxLayout(example)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        additem_btn _ QtGui.?PB..(example)
        additem_btn.setObjectName(_fromUtf8("additem_btn"))
        verticalLayout_2.addWidget(additem_btn)
        name_le _ QtGui.QLineEdit(example)
        name_le.setObjectName(_fromUtf8("name_le"))
        verticalLayout_2.addWidget(name_le)
        items_ly _ QtGui.QVBoxLayout()
        items_ly.setObjectName(_fromUtf8("items_ly"))
        verticalLayout_2.addLayout(items_ly)
        spacerItem _ QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        verticalLayout_2.addItem(spacerItem)

        retranslateUi(example)
        ?C...QMetaObject.connectSlotsByName(example)

    ___ retranslateUi , example
        example.setWindowTitle(_translate("example", "Item List", None))
        additem_btn.sT..(_translate("example", "Add", None))

