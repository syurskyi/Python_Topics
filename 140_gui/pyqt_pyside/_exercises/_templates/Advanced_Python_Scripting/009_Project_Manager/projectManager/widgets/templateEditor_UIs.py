# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\templateEditor.ui'
#
# Created: Thu Oct 09 13:59:10 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_templateEditor(object
    ___ setupUi , templateEditor
        templateEditor.setObjectName("templateEditor")
        templateEditor.resize(357, 461)
        verticalLayout _ QtGui.QVBoxLayout(templateEditor)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout_2 _ QtGui.QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        add_btn _ QtGui.?PB..(templateEditor)
        add_btn.setMinimumSize(?C...QSize(30, 30))
        add_btn.setMaximumSize(?C...QSize(30, 30))
        font _ QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(T..)
        add_btn.setFont(font)
        add_btn.setObjectName("add_btn")
        horizontalLayout_2.addWidget(add_btn)
        remove_btn _ QtGui.?PB..(templateEditor)
        remove_btn.setMinimumSize(?C...QSize(30, 30))
        remove_btn.setMaximumSize(?C...QSize(30, 30))
        font _ QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(T..)
        remove_btn.setFont(font)
        remove_btn.setObjectName("remove_btn")
        horizontalLayout_2.addWidget(remove_btn)
        spacerItem _ QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        tree _ QtGui.QTreeWidget(templateEditor)
        tree.setObjectName("tree")
        tree.headerItem().sT..(0, "1")
        tree.header().setVisible(False)
        verticalLayout.addWidget(tree)
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        save_btn _ QtGui.?PB..(templateEditor)
        save_btn.setObjectName("save_btn")
        horizontalLayout.addWidget(save_btn)
        close_btn _ QtGui.?PB..(templateEditor)
        close_btn.setObjectName("close_btn")
        horizontalLayout.addWidget(close_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(templateEditor)
        ?C...QMetaObject.connectSlotsByName(templateEditor)

    ___ retranslateUi , templateEditor
        templateEditor.setWindowTitle(QtGui.?A...translate("templateEditor", "Form", None, QtGui.?A...UnicodeUTF8))
        add_btn.sT..(QtGui.?A...translate("templateEditor", "+", None, QtGui.?A...UnicodeUTF8))
        remove_btn.sT..(QtGui.?A...translate("templateEditor", "-", None, QtGui.?A...UnicodeUTF8))
        save_btn.sT..(QtGui.?A...translate("templateEditor", "Save", None, QtGui.?A...UnicodeUTF8))
        close_btn.sT..(QtGui.?A...translate("templateEditor", "Close", None, QtGui.?A...UnicodeUTF8))

