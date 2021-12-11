# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made __ this file will be lost!

____ PyQt4 ______ QtCore, QtGui

___
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s):
        r_ s

___
    _encoding = QtGui.QApplication.UnicodeUTF8
    ___ _translate(context, text, disambig):
        r_ QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig):
        r_ QtGui.QApplication.translate(context, text, disambig)

c_ Ui_Countdown(object):
    ___ setupUi Countdown):
        Countdown.setObjectName(_fromUtf8("Countdown"))
        Countdown.resize(301, 162)
        centralwidget = QtGui.QWidget(Countdown)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        countdownButton = QtGui.QPushButton(centralwidget)
        countdownButton.setGeometry(QtCore.QRect(100, 70, 90, 27))
        countdownButton.setObjectName(_fromUtf8("countdownButton"))
        Countdown.setCentralWidget(centralwidget)

        retranslateUi(Countdown)
        QtCore.QMetaObject.connectSlotsByName(Countdown)

    ___ retranslateUi Countdown):
        Countdown.setWindowTitle(_translate("Countdown", "Countdown Window", N..))
        countdownButton.setText(_translate("Countdown", "Start", N..))

