# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_client(object
    ___ setupUi , client
        client.setObjectName("client")
        client.r..(366, 107)
        verticalLayout _ ?G...QVBoxLayout(client)
        verticalLayout.setObjectName("verticalLayout")
        ip_le _ ?G...QLineEdit(client)
        ip_le.setObjectName("ip_le")
        verticalLayout.addWidget(ip_le)
        connect_btn _ ?G...?PB..(client)
        connect_btn.setObjectName("connect_btn")
        verticalLayout.addWidget(connect_btn)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        progress_sle _ ?G...QSlider(client)
        progress_sle.setOrientation(?C...__.Horizontal)
        progress_sle.setObjectName("progress_sle")
        horizontalLayout.addWidget(progress_sle)
        label _ ?G...QLabel(client)
        label.setMinimumSize(?C...QSize(50, 0))
        label.setObjectName("label")
        horizontalLayout.addWidget(label)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(client)
        ?C...QObject.c..(progress_sle, ?C...SIGNAL("valueChanged(int)"), label.setNum)
        ?C...QMetaObject.connectSlotsByName(client)

    ___ retranslateUi , client
        client.setWindowTitle(?G...?A...translate("client", "Client", N.., ?G...?A...UnicodeUTF8))
        connect_btn.sT..(?G...?A...translate("client", "Connect", N.., ?G...?A...UnicodeUTF8))
        label.sT..(?G...?A...translate("client", "0", N.., ?G...?A...UnicodeUTF8))

