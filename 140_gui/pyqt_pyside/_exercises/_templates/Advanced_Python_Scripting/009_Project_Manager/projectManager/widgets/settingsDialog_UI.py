# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\settingsDialog.ui'
#
# Created: Thu Oct 09 13:34:28 2014
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

c_ Ui_settingsDialog(object
    ___ setupUi , settingsDialog
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(458, 153)
        verticalLayout _ QtGui.QVBoxLayout(settingsDialog)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        table _ QtGui.QTableWidget(settingsDialog)
        table.setObjectName(_fromUtf8("table"))
        table.setColumnCount(0)
        table.setRowCount(0)
        verticalLayout.addWidget(table)
        buttonBox _ QtGui.QDialogButtonBox(settingsDialog)
        buttonBox.setOrientation(?C...Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.setObjectName(_fromUtf8("buttonBox"))
        verticalLayout.addWidget(buttonBox)

        retranslateUi(settingsDialog)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL(_fromUtf8("accepted()")), settingsDialog.accept)
        ?C...QObject.c..(buttonBox, ?C...SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        ?C...QMetaObject.connectSlotsByName(settingsDialog)

    ___ retranslateUi , settingsDialog
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog", None))

