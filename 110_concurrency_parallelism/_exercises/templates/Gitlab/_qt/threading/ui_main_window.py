# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made __ this file will be lost!

from PyQt4 ______ QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s):
        r_ s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    ___ _translate(context, text, disambig):
        r_ QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig):
        r_ QtGui.QApplication.translate(context, text, disambig)

class Ui_Countdown(object):
    ___ setupUi(self, Countdown):
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

    ___ retranslateUi(self, Countdown):
        Countdown.setWindowTitle(_translate("Countdown", "Countdown Window", N..))
        self.countdownButton.setText(_translate("Countdown", "Start", N..))

