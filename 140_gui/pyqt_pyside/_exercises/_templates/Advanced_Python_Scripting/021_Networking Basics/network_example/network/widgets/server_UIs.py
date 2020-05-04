# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\server.ui'
#
# Created: Fri Nov 21 11:35:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_Server(object
    ___ setupUi , Server
        Server.setObjectName("Server")
        Server.r..(396, 407)
        verticalLayout _ ?G...QVBoxLayout(Server)
        verticalLayout.setObjectName("verticalLayout")
        progress_pbr _ ?G...QProgressBar(Server)
        progress_pbr.setProperty("value", 0)
        progress_pbr.setObjectName("progress_pbr")
        verticalLayout.addWidget(progress_pbr)
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        info_lb _ ?G...QLabel(Server)
        info_lb.setObjectName("info_lb")
        horizontalLayout.addWidget(info_lb)
        ip_le _ ?G...QLineEdit(Server)
        ip_le.setReadOnly(T..)
        ip_le.setObjectName("ip_le")
        horizontalLayout.addWidget(ip_le)
        verticalLayout.addLayout(horizontalLayout)
        out_tb _ ?G...QTextBrowser(Server)
        out_tb.setObjectName("out_tb")
        verticalLayout.addWidget(out_tb)

        retranslateUi(Server)
        ?C...QMetaObject.connectSlotsByName(Server)

    ___ retranslateUi , Server
        Server.setWindowTitle(?G...?A...translate("Server", "Server", N.., ?G...?A...UnicodeUTF8))
        info_lb.sT..(?G...?A...translate("Server", "IP:", N.., ?G...?A...UnicodeUTF8))

