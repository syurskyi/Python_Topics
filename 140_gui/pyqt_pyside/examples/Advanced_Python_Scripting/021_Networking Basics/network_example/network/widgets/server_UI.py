# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\server.ui'
#
# Created: Fri Nov 21 11:35:48 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName(_fromUtf8("Server"))
        Server.resize(396, 407)
        self.verticalLayout = QtGui.QVBoxLayout(Server)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progress_pbr = QtGui.QProgressBar(Server)
        self.progress_pbr.setProperty("value", 0)
        self.progress_pbr.setObjectName(_fromUtf8("progress_pbr"))
        self.verticalLayout.addWidget(self.progress_pbr)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.info_lb = QtGui.QLabel(Server)
        self.info_lb.setObjectName(_fromUtf8("info_lb"))
        self.horizontalLayout.addWidget(self.info_lb)
        self.ip_le = QtGui.QLineEdit(Server)
        self.ip_le.setReadOnly(True)
        self.ip_le.setObjectName(_fromUtf8("ip_le"))
        self.horizontalLayout.addWidget(self.ip_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.out_tb = QtGui.QTextBrowser(Server)
        self.out_tb.setObjectName(_fromUtf8("out_tb"))
        self.verticalLayout.addWidget(self.out_tb)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        Server.setWindowTitle(_translate("Server", "Server", None))
        self.info_lb.setText(_translate("Server", "IP:", None))

