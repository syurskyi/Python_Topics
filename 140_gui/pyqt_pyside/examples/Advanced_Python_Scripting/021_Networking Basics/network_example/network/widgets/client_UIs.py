# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(366, 107)
        self.verticalLayout = QtWidgets.QVBoxLayout(client)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ip_le = QtWidgets.QLineEdit(client)
        self.ip_le.setObjectName("ip_le")
        self.verticalLayout.addWidget(self.ip_le)
        self.connect_btn = QtWidgets.QPushButton(client)
        self.connect_btn.setObjectName("connect_btn")
        self.verticalLayout.addWidget(self.connect_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progress_sle = QtWidgets.QSlider(client)
        self.progress_sle.setOrientation(QtCore.Qt.Horizontal)
        self.progress_sle.setObjectName("progress_sle")
        self.horizontalLayout.addWidget(self.progress_sle)
        self.label = QtWidgets.QLabel(client)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(client)
        QtCore.QObject.connect(self.progress_sle, QtCore.SIGNAL("valueChanged(int)"), self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        client.setWindowTitle(QtWidgets.QApplication.translate("client", "Client", None))
        self.connect_btn.setText(QtWidgets.QApplication.translate("client", "Connect", None))
        self.label.setText(QtWidgets.QApplication.translate("client", "0", None))

