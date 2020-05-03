# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\createProject.ui'
#
# Created: Thu Oct 09 13:31:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., ?G..

c_ Ui_createDialog(object
    ___ setupUi , createDialog
        createDialog.setObjectName("createDialog")
        createDialog.resize(240, 219)
        verticalLayout _ ?G...QVBoxLayout(createDialog)
        verticalLayout.setObjectName("verticalLayout")
        gridLayout _ ?G...QGridLayout
        gridLayout.setObjectName("gridLayout")
        label _ ?G...QLabel(createDialog)
        label.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label.setObjectName("label")
        gridLayout.addWidget(label, 0, 0, 1, 1)
        name_lb _ ?G...QLineEdit(createDialog)
        name_lb.setObjectName("name_lb")
        gridLayout.addWidget(name_lb, 0, 1, 1, 1)
        label_2 _ ?G...QLabel(createDialog)
        label_2.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTop|?C...Qt.AlignTrailing)
        label_2.setObjectName("label_2")
        gridLayout.addWidget(label_2, 1, 0, 1, 1)
        comment_te _ ?G...QPlainTextEdit(createDialog)
        comment_te.setObjectName("comment_te")
        gridLayout.addWidget(comment_te, 1, 1, 1, 1)
        verticalLayout.addLayout(gridLayout)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        create_btn _ ?G...?PB..(createDialog)
        create_btn.setObjectName("create_btn")
        horizontalLayout.addWidget(create_btn)
        cancel_btn _ ?G...?PB..(createDialog)
        cancel_btn.setObjectName("cancel_btn")
        horizontalLayout.addWidget(cancel_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(createDialog)
        ?C...QMetaObject.connectSlotsByName(createDialog)

    ___ retranslateUi , createDialog
        createDialog.setWindowTitle(?G...?A...translate("createDialog", "Dialog", None, ?G...?A...UnicodeUTF8))
        label.sT..(?G...?A...translate("createDialog", "Name", None, ?G...?A...UnicodeUTF8))
        label_2.sT..(?G...?A...translate("createDialog", "Comment", None, ?G...?A...UnicodeUTF8))
        create_btn.sT..(?G...?A...translate("createDialog", "Create", None, ?G...?A...UnicodeUTF8))
        cancel_btn.sT..(?G...?A...translate("createDialog", "Cancel", None, ?G...?A...UnicodeUTF8))

