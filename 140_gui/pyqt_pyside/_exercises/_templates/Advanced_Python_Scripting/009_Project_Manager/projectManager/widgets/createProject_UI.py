# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\createProject.ui'
#
# Created: Thu Oct 09 13:31:13 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., QtGui

try:
    _fromUtf8 = ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding = QtGui.?A...UnicodeUTF8
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig)

c_ Ui_createDialog(object
    ___ setupUi , createDialog
        createDialog.setObjectName(_fromUtf8("createDialog"))
        createDialog.resize(240, 219)
        verticalLayout = QtGui.QVBoxLayout(createDialog)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        gridLayout = QtGui.QGridLayout()
        gridLayout.setObjectName(_fromUtf8("gridLayout"))
        label = QtGui.QLabel(createDialog)
        label.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label.setObjectName(_fromUtf8("label"))
        gridLayout.addWidget(label, 0, 0, 1, 1)
        name_lb = QtGui.QLineEdit(createDialog)
        name_lb.setObjectName(_fromUtf8("name_lb"))
        gridLayout.addWidget(name_lb, 0, 1, 1, 1)
        label_2 = QtGui.QLabel(createDialog)
        label_2.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTop|?C...Qt.AlignTrailing)
        label_2.setObjectName(_fromUtf8("label_2"))
        gridLayout.addWidget(label_2, 1, 0, 1, 1)
        comment_te = QtGui.QPlainTextEdit(createDialog)
        comment_te.setObjectName(_fromUtf8("comment_te"))
        gridLayout.addWidget(comment_te, 1, 1, 1, 1)
        verticalLayout.addLayout(gridLayout)
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        create_btn = QtGui.?PB..(createDialog)
        create_btn.setObjectName(_fromUtf8("create_btn"))
        horizontalLayout.addWidget(create_btn)
        cancel_btn = QtGui.?PB..(createDialog)
        cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        horizontalLayout.addWidget(cancel_btn)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(createDialog)
        ?C...QMetaObject.connectSlotsByName(createDialog)

    ___ retranslateUi , createDialog
        createDialog.setWindowTitle(_translate("createDialog", "Dialog", None))
        label.sT..(_translate("createDialog", "Name", None))
        label_2.sT..(_translate("createDialog", "Comment", None))
        create_btn.sT..(_translate("createDialog", "Create", None))
        cancel_btn.sT..(_translate("createDialog", "Cancel", None))

