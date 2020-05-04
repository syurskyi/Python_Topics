# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\templateEditor.ui'
#
# Created: Thu Oct 09 13:59:10 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., ?G..

___
    _fromUtf8 _ ?C...QString.fromUtf8
_____ AttributeError:
    ___ _fromUtf8(s
        r_ s

___
    _encoding _ ?G...?A...UnicodeUTF8
    ___ _translate(context, t.., disambig
        r_ ?G...?A...translate(context, t.., disambig, _encoding)
_____ AttributeError:
    ___ _translate(context, t.., disambig
        r_ ?G...?A...translate(context, t.., disambig)

c_ Ui_templateEditor(object
    ___ setupUi , templateEditor
        templateEditor.setObjectName(_fromUtf8("templateEditor"))
        templateEditor.r..(357, 461)
        verticalLayout _ ?G...QVBoxLayout(templateEditor)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        add_btn _ ?G...?PB..(templateEditor)
        add_btn.setMinimumSize(?C...QSize(30, 30))
        add_btn.setMaximumSize(?C...QSize(30, 30))
        font _ ?G...?F..
        font.setPointSize(16)
        font.setBold(T..)
        font.setWeight(75)
        add_btn.sF..(font)
        add_btn.setObjectName(_fromUtf8("add_btn"))
        horizontalLayout_2.addWidget(add_btn)
        remove_btn _ ?G...?PB..(templateEditor)
        remove_btn.setMinimumSize(?C...QSize(30, 30))
        remove_btn.setMaximumSize(?C...QSize(30, 30))
        font _ ?G...?F..
        font.setPointSize(16)
        font.setBold(T..)
        font.setWeight(75)
        remove_btn.sF..(font)
        remove_btn.setObjectName(_fromUtf8("remove_btn"))
        horizontalLayout_2.addWidget(remove_btn)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        tree _ ?G...QTreeWidget(templateEditor)
        tree.setObjectName(_fromUtf8("tree"))
        tree.headerItem.sT..(0, _fromUtf8("1"))
        tree.header.setVisible(F..)
        verticalLayout.addWidget(tree)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        save_btn _ ?G...?PB..(templateEditor)
        save_btn.setObjectName(_fromUtf8("save_btn"))
        horizontalLayout.addWidget(save_btn)
        close_btn _ ?G...?PB..(templateEditor)
        close_btn.setObjectName(_fromUtf8("close_btn"))
        horizontalLayout.addWidget(close_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(templateEditor)
        ?C...QMetaObject.connectSlotsByName(templateEditor)

    ___ retranslateUi , templateEditor
        templateEditor.setWindowTitle(_translate("templateEditor", "Form", N..))
        add_btn.sT..(_translate("templateEditor", "+", N..))
        remove_btn.sT..(_translate("templateEditor", "-", N..))
        save_btn.sT..(_translate("templateEditor", "Save", N..))
        close_btn.sT..(_translate("templateEditor", "Close", N..))

