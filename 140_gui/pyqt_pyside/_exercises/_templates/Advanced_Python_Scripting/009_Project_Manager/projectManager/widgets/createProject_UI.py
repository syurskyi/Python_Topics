# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\createProject.ui'
#
# Created: Thu Oct 09 13:31:13 2014
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

c_ Ui_createDialog(object
    ___ setupUi , createDialog
        createDialog.setObjectName(_fromUtf8("createDialog"))
        createDialog.r..(240, 219)
        verticalLayout _ ?G...QVBoxLayout(createDialog)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        gridLayout _ ?G...QGridLayout
        gridLayout.setObjectName(_fromUtf8("gridLayout"))
        label _ ?G...QLabel(createDialog)
        label.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        label.setObjectName(_fromUtf8("label"))
        gridLayout.addWidget(label, 0, 0, 1, 1)
        name_lb _ ?G...QLineEdit(createDialog)
        name_lb.setObjectName(_fromUtf8("name_lb"))
        gridLayout.addWidget(name_lb, 0, 1, 1, 1)
        label_2 _ ?G...QLabel(createDialog)
        label_2.setAlignment(?C...__.AlignRight|?C...__.AlignTop|?C...__.AlignTrailing)
        label_2.setObjectName(_fromUtf8("label_2"))
        gridLayout.addWidget(label_2, 1, 0, 1, 1)
        comment_te _ ?G...QPlainTextEdit(createDialog)
        comment_te.setObjectName(_fromUtf8("comment_te"))
        gridLayout.addWidget(comment_te, 1, 1, 1, 1)
        verticalLayout.addLayout(gridLayout)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        create_btn _ ?G...?PB..(createDialog)
        create_btn.setObjectName(_fromUtf8("create_btn"))
        horizontalLayout.addWidget(create_btn)
        cancel_btn _ ?G...?PB..(createDialog)
        cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        horizontalLayout.addWidget(cancel_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(createDialog)
        ?C...QMetaObject.connectSlotsByName(createDialog)

    ___ retranslateUi , createDialog
        createDialog.setWindowTitle(_translate("createDialog", "Dialog", N..))
        label.sT..(_translate("createDialog", "Name", N..))
        label_2.sT..(_translate("createDialog", "Comment", N..))
        create_btn.sT..(_translate("createDialog", "Create", N..))
        cancel_btn.sT..(_translate("createDialog", "Cancel", N..))

