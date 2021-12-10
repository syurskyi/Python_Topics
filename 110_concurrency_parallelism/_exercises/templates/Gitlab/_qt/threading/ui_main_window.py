# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Countdown(object):
    def setupUi(self, Countdown):
        Countdown.setObjectName(_fromUtf8("Countdown"))
        Countdown.resize(301, 162)
        self.centralwidget = QtGui.QWidget(Countdown)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.countdownButton = QtGui.QPushButton(self.centralwidget)
        self.countdownButton.setGeometry(QtCore.QRect(100, 70, 90, 27))
        self.countdownButton.setObjectName(_fromUtf8("countdownButton"))
        Countdown.setCentralWidget(self.centralwidget)

        self.retranslateUi(Countdown)
        QtCore.QMetaObject.connectSlotsByName(Countdown)

    def retranslateUi(self, Countdown):
        Countdown.setWindowTitle(_translate("Countdown", "Countdown Window", None))
        self.countdownButton.setText(_translate("Countdown", "Start", None))

