# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\server.ui'
#
# Created: Fri Nov 21 11:35:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_Server(object
    ___ setupUi , Server
        Server.setObjectName("Server")
        Server.resize(396, 407)
        verticalLayout = QtGui.QVBoxLayout(Server)
        verticalLayout.setObjectName("verticalLayout")
        progress_pbr = QtGui.QProgressBar(Server)
        progress_pbr.setProperty("value", 0)
        progress_pbr.setObjectName("progress_pbr")
        verticalLayout.addWidget(progress_pbr)
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        info_lb = QtGui.QLabel(Server)
        info_lb.setObjectName("info_lb")
        horizontalLayout.addWidget(info_lb)
        ip_le = QtGui.QLineEdit(Server)
        ip_le.setReadOnly(T..)
        ip_le.setObjectName("ip_le")
        horizontalLayout.addWidget(ip_le)
        verticalLayout.addLayout(horizontalLayout)
        out_tb = QtGui.QTextBrowser(Server)
        out_tb.setObjectName("out_tb")
        verticalLayout.addWidget(out_tb)

        retranslateUi(Server)
        ?C...QMetaObject.connectSlotsByName(Server)

    ___ retranslateUi , Server
        Server.setWindowTitle(QtGui.?A...translate("Server", "Server", None, QtGui.?A...UnicodeUTF8))
        info_lb.sT..(QtGui.?A...translate("Server", "IP:", None, QtGui.?A...UnicodeUTF8))

