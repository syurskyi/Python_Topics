# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\client.ui'
#
# Created: Fri Nov 21 11:09:54 2014
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

c_ Ui_client(object
    ___ setupUi , client
        client.setObjectName(_fromUtf8("client"))
        client.resize(366, 107)
        verticalLayout _ QtGui.QVBoxLayout(client)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        ip_le _ QtGui.QLineEdit(client)
        ip_le.setObjectName(_fromUtf8("ip_le"))
        verticalLayout.addWidget(ip_le)
        connect_btn _ QtGui.?PB..(client)
        connect_btn.setObjectName(_fromUtf8("connect_btn"))
        verticalLayout.addWidget(connect_btn)
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        progress_sle _ QtGui.QSlider(client)
        progress_sle.setOrientation(?C...Qt.Horizontal)
        progress_sle.setObjectName(_fromUtf8("progress_sle"))
        horizontalLayout.addWidget(progress_sle)
        label _ QtGui.QLabel(client)
        label.setMinimumSize(?C...QSize(50, 0))
        label.setObjectName(_fromUtf8("label"))
        horizontalLayout.addWidget(label)
        verticalLayout.addLayout(horizontalLayout)

        retranslateUi(client)
        ?C...QObject.c..(progress_sle, ?C...SIGNAL(_fromUtf8("valueChanged(int)")), label.setNum)
        ?C...QMetaObject.connectSlotsByName(client)

    ___ retranslateUi , client
        client.setWindowTitle(_translate("client", "Client", None))
        connect_btn.sT..(_translate("client", "Connect", None))
        label.sT..(_translate("client", "0", None))

