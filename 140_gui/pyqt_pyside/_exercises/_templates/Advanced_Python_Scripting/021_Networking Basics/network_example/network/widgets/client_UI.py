# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:54 2014
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

class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName(_fromUtf8("client"))
        client.resize(366, 107)
        self.verticalLayout = QtGui.QVBoxLayout(client)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ip_le = QtGui.QLineEdit(client)
        self.ip_le.setObjectName(_fromUtf8("ip_le"))
        self.verticalLayout.addWidget(self.ip_le)
        self.connect_btn = QtGui.QPushButton(client)
        self.connect_btn.setObjectName(_fromUtf8("connect_btn"))
        self.verticalLayout.addWidget(self.connect_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progress_sle = QtGui.QSlider(client)
        self.progress_sle.setOrientation(QtCore.Qt.Horizontal)
        self.progress_sle.setObjectName(_fromUtf8("progress_sle"))
        self.horizontalLayout.addWidget(self.progress_sle)
        self.label = QtGui.QLabel(client)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(client)
        QtCore.QObject.connect(self.progress_sle, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        client.setWindowTitle(_translate("client", "Client", None))
        self.connect_btn.setText(_translate("client", "Connect", None))
        self.label.setText(_translate("client", "0", None))

