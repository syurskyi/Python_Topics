# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\settingsDialog.ui'
#
# Created: Thu Oct 09 13:34:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_settingsDialog(object
    ___ setupUi , settingsDialog
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.r..(458, 153)
        verticalLayout _ ?G...QVBoxLayout(settingsDialog)
        verticalLayout.setObjectName("verticalLayout")
        table _ ?G...QTableWidget(settingsDialog)
        table.setObjectName("table")
        table.setColumnCount(0)
        table.setRowCount(0)
        verticalLayout.addWidget(table)
        buttonBox _ ?G...QDialogButtonBox(settingsDialog)
        buttonBox.setOrientation(?C...__.Horizontal)
        buttonBox.setStandardButtons(?G...QDialogButtonBox.Cancel|?G...QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        verticalLayout.addWidget(buttonBox)

        retranslateUi(settingsDialog)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL("accepted()"), settingsDialog.a..)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL("rejected()"), settingsDialog.reject)
        ?C...QMetaObject.connectSlotsByName(settingsDialog)

    ___ retranslateUi , settingsDialog
        settingsDialog.setWindowTitle(?G...?A...translate("settingsDialog", "Dialog", N.., ?G...?A...UnicodeUTF8))

