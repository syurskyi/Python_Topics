# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\templateEditor.ui'
#
# Created: Thu Oct 09 13:59:10 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_templateEditor(object
    ___ setupUi , templateEditor
        templateEditor.setObjectName("templateEditor")
        templateEditor.r..(357, 461)
        verticalLayout _ ?G...QVBoxLayout(templateEditor)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        add_btn _ ?G...?PB..(templateEditor)
        add_btn.setMinimumSize(?C...QSize(30, 30))
        add_btn.setMaximumSize(?C...QSize(30, 30))
        font _ ?G...?F..
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(T..)
        add_btn.sF..(font)
        add_btn.setObjectName("add_btn")
        horizontalLayout_2.addWidget(add_btn)
        remove_btn _ ?G...?PB..(templateEditor)
        remove_btn.setMinimumSize(?C...QSize(30, 30))
        remove_btn.setMaximumSize(?C...QSize(30, 30))
        font _ ?G...?F..
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(T..)
        remove_btn.sF..(font)
        remove_btn.setObjectName("remove_btn")
        horizontalLayout_2.addWidget(remove_btn)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        tree _ ?G...QTreeWidget(templateEditor)
        tree.setObjectName("tree")
        tree.headerItem.sT..(0, "1")
        tree.header.setVisible(F..)
        verticalLayout.addWidget(tree)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        save_btn _ ?G...?PB..(templateEditor)
        save_btn.setObjectName("save_btn")
        horizontalLayout.addWidget(save_btn)
        close_btn _ ?G...?PB..(templateEditor)
        close_btn.setObjectName("close_btn")
        horizontalLayout.addWidget(close_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(templateEditor)
        ?C...QMetaObject.connectSlotsByName(templateEditor)

    ___ retranslateUi , templateEditor
        templateEditor.setWindowTitle(?G...?A...translate("templateEditor", "Form", N.., ?G...?A...UnicodeUTF8))
        add_btn.sT..(?G...?A...translate("templateEditor", "+", N.., ?G...?A...UnicodeUTF8))
        remove_btn.sT..(?G...?A...translate("templateEditor", "-", N.., ?G...?A...UnicodeUTF8))
        save_btn.sT..(?G...?A...translate("templateEditor", "Save", N.., ?G...?A...UnicodeUTF8))
        close_btn.sT..(?G...?A...translate("templateEditor", "Close", N.., ?G...?A...UnicodeUTF8))

