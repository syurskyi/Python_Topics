# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\templateEditor.ui'
#
# Created: Thu Oct 09 13:59:10 2014
#      by: PyQt4 UI code generator 4.11.2
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
    ___ _translate(context, t.., disambig
        return QtGui.?A...translate(context, t.., disambig, _encoding)
except AttributeError:
    ___ _translate(context, t.., disambig
        return QtGui.?A...translate(context, t.., disambig)

c_ Ui_templateEditor(object
    ___ setupUi , templateEditor
        templateEditor.setObjectName(_fromUtf8("templateEditor"))
        templateEditor.resize(357, 461)
        verticalLayout _ QtGui.QVBoxLayout(templateEditor)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout_2 _ QtGui.QHBoxLayout()
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        add_btn _ QtGui.?PB..(templateEditor)
        add_btn.setMinimumSize(?C...QSize(30, 30))
        add_btn.setMaximumSize(?C...QSize(30, 30))
        font _ QtGui.QFont()
        font.setPointSize(16)
        font.setBold(T..)
        font.setWeight(75)
        add_btn.setFont(font)
        add_btn.setObjectName(_fromUtf8("add_btn"))
        horizontalLayout_2.addWidget(add_btn)
        remove_btn _ QtGui.?PB..(templateEditor)
        remove_btn.setMinimumSize(?C...QSize(30, 30))
        remove_btn.setMaximumSize(?C...QSize(30, 30))
        font _ QtGui.QFont()
        font.setPointSize(16)
        font.setBold(T..)
        font.setWeight(75)
        remove_btn.setFont(font)
        remove_btn.setObjectName(_fromUtf8("remove_btn"))
        horizontalLayout_2.addWidget(remove_btn)
        spacerItem _ QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        tree _ QtGui.QTreeWidget(templateEditor)
        tree.setObjectName(_fromUtf8("tree"))
        tree.headerItem().sT..(0, _fromUtf8("1"))
        tree.header().setVisible(False)
        verticalLayout.addWidget(tree)
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        save_btn _ QtGui.?PB..(templateEditor)
        save_btn.setObjectName(_fromUtf8("save_btn"))
        horizontalLayout.addWidget(save_btn)
        close_btn _ QtGui.?PB..(templateEditor)
        close_btn.setObjectName(_fromUtf8("close_btn"))
        horizontalLayout.addWidget(close_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(templateEditor)
        ?C...QMetaObject.connectSlotsByName(templateEditor)

    ___ retranslateUi , templateEditor
        templateEditor.setWindowTitle(_translate("templateEditor", "Form", None))
        add_btn.sT..(_translate("templateEditor", "+", None))
        remove_btn.sT..(_translate("templateEditor", "-", None))
        save_btn.sT..(_translate("templateEditor", "Save", None))
        close_btn.sT..(_translate("templateEditor", "Close", None))

