# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_client(object
    ___ setupUi , client
        client.setObjectName("client")
        client.resize(366, 107)
        verticalLayout _ QtGui.QVBoxLayout(client)
        verticalLayout.setObjectName("verticalLayout")
        ip_le _ QtGui.QLineEdit(client)
        ip_le.setObjectName("ip_le")
        verticalLayout.addWidget(ip_le)
        connect_btn _ QtGui.?PB..(client)
        connect_btn.setObjectName("connect_btn")
        verticalLayout.addWidget(connect_btn)
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        progress_sle _ QtGui.QSlider(client)
        progress_sle.setOrientation(?C...Qt.Horizontal)
        progress_sle.setObjectName("progress_sle")
        horizontalLayout.addWidget(progress_sle)
        label _ QtGui.QLabel(client)
        label.setMinimumSize(?C...QSize(50, 0))
        label.setObjectName("label")
        horizontalLayout.addWidget(label)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(client)
        ?C...QObject.c..(progress_sle, ?C...SIGNAL("valueChanged(int)"), label.setNum)
        ?C...QMetaObject.connectSlotsByName(client)

    ___ retranslateUi , client
        client.setWindowTitle(QtGui.?A...translate("client", "Client", None, QtGui.?A...UnicodeUTF8))
        connect_btn.sT..(QtGui.?A...translate("client", "Connect", None, QtGui.?A...UnicodeUTF8))
        label.sT..(QtGui.?A...translate("client", "0", None, QtGui.?A...UnicodeUTF8))

