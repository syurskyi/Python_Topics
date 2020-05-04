# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:54 2014
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

c_ Ui_client(object
    ___ setupUi , client
        client.setObjectName(_fromUtf8("client"))
        client.r..(366, 107)
        verticalLayout _ ?G...QVBoxLayout(client)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        ip_le _ ?G...QLineEdit(client)
        ip_le.setObjectName(_fromUtf8("ip_le"))
        verticalLayout.addWidget(ip_le)
        connect_btn _ ?G...?PB..(client)
        connect_btn.setObjectName(_fromUtf8("connect_btn"))
        verticalLayout.addWidget(connect_btn)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        progress_sle _ ?G...QSlider(client)
        progress_sle.setOrientation(?C...__.Horizontal)
        progress_sle.setObjectName(_fromUtf8("progress_sle"))
        horizontalLayout.addWidget(progress_sle)
        label _ ?G...QLabel(client)
        label.setMinimumSize(?C...QSize(50, 0))
        label.setObjectName(_fromUtf8("label"))
        horizontalLayout.addWidget(label)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(client)
        ?C...QObject.c..(progress_sle, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), label.setNum)
        ?C...QMetaObject.connectSlotsByName(client)

    ___ retranslateUi , client
        client.setWindowTitle(_translate("client", "Client", N..))
        connect_btn.sT..(_translate("client", "Connect", N..))
        label.sT..(_translate("client", "0", N..))

