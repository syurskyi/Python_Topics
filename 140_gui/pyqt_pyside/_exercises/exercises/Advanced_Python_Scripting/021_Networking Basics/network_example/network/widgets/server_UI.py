# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\server.ui'
#
# Created: Fri Nov 21 11:35:48 2014
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

c_ Ui_Server(object
    ___ setupUi , Server
        Server.setObjectName(_fromUtf8("Server"))
        Server.r..(396, 407)
        verticalLayout _ ?G...QVBoxLayout(Server)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        progress_pbr _ ?G...QProgressBar(Server)
        progress_pbr.setProperty("value", 0)
        progress_pbr.setObjectName(_fromUtf8("progress_pbr"))
        verticalLayout.addWidget(progress_pbr)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        info_lb _ ?G...QLabel(Server)
        info_lb.setObjectName(_fromUtf8("info_lb"))
        horizontalLayout.addWidget(info_lb)
        ip_le _ ?G...QLineEdit(Server)
        ip_le.setReadOnly(T..)
        ip_le.setObjectName(_fromUtf8("ip_le"))
        horizontalLayout.addWidget(ip_le)
        verticalLayout.addLayout(horizontalLayout)
        out_tb _ ?G...QTextBrowser(Server)
        out_tb.setObjectName(_fromUtf8("out_tb"))
        verticalLayout.addWidget(out_tb)

        retranslateUi(Server)
        ?C...QMetaObject.connectSlotsByName(Server)

    ___ retranslateUi , Server
        Server.setWindowTitle(_translate("Server", "Server", N..))
        info_lb.sT..(_translate("Server", "IP:", N..))

