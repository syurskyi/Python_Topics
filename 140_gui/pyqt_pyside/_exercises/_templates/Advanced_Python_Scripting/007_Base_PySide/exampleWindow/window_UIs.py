# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\exampleWindow\window.ui'
#
# Created: Sun Nov 05 15:05:59 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_example(object
    ___ setupUi , example
        example.setObjectName("example")
        example.r..(241, 204)
        verticalLayout_2 _ ?G...QVBoxLayout(example)
        verticalLayout_2.setObjectName("verticalLayout_2")
        additem_btn _ ?G...?PB..(example)
        additem_btn.setObjectName("additem_btn")
        verticalLayout_2.addWidget(additem_btn)
        name_le _ ?G...QLineEdit(example)
        name_le.setObjectName("name_le")
        verticalLayout_2.addWidget(name_le)
        items_ly _ ?G...QVBoxLayout
        items_ly.setObjectName("items_ly")
        verticalLayout_2.addLayout(items_ly)
        spacerItem _ ?G...QSpacerItem(20, 40, ?G...QSizePolicy.Minimum, ?G...QSizePolicy.Expanding)
        verticalLayout_2.aI..(spacerItem)

        retranslateUi(example)
        ?C...QMetaObject.connectSlotsByName(example)

    ___ retranslateUi , example
        example.setWindowTitle(?G...?A...translate("example", "Item List", N.., ?G...?A...UnicodeUTF8))
        additem_btn.sT..(?G...?A...translate("example", "Add", N.., ?G...?A...UnicodeUTF8))

