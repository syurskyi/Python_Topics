# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\settingsDialog.ui'
#
# Created: Thu Oct 09 13:34:28 2014
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

c_ Ui_settingsDialog(object
    ___ setupUi , settingsDialog
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.r..(458, 153)
        verticalLayout _ ?G...QVBoxLayout(settingsDialog)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        table _ ?G...QTableWidget(settingsDialog)
        table.setObjectName(_fromUtf8("table"))
        table.setColumnCount(0)
        table.setRowCount(0)
        verticalLayout.addWidget(table)
        buttonBox _ ?G...QDialogButtonBox(settingsDialog)
        buttonBox.setOrientation(?C...__.Horizontal)
        buttonBox.setStandardButtons(?G...QDialogButtonBox.Cancel|?G...QDialogButtonBox.Ok)
        buttonBox.setObjectName(_fromUtf8("buttonBox"))
        verticalLayout.addWidget(buttonBox)

        retranslateUi(settingsDialog)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL(_fromUtf8("accepted()")), settingsDialog.a..)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        ?C...QMetaObject.connectSlotsByName(settingsDialog)

    ___ retranslateUi , settingsDialog
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog", N..))

