# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week8\netMessage\widgets\server.ui'
#
# Created: Fri Nov 21 11:35:48 2014
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

c_ Ui_Server(object
    ___ setupUi , Server
        Server.setObjectName(_fromUtf8("Server"))
        Server.resize(396, 407)
        verticalLayout _ QtGui.QVBoxLayout(Server)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        progress_pbr _ QtGui.QProgressBar(Server)
        progress_pbr.setProperty("value", 0)
        progress_pbr.setObjectName(_fromUtf8("progress_pbr"))
        verticalLayout.addWidget(progress_pbr)
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        info_lb _ QtGui.QLabel(Server)
        info_lb.setObjectName(_fromUtf8("info_lb"))
        horizontalLayout.addWidget(info_lb)
        ip_le _ QtGui.QLineEdit(Server)
        ip_le.setReadOnly(T..)
        ip_le.setObjectName(_fromUtf8("ip_le"))
        horizontalLayout.addWidget(ip_le)
        verticalLayout.addLayout(horizontalLayout)
        out_tb _ QtGui.QTextBrowser(Server)
        out_tb.setObjectName(_fromUtf8("out_tb"))
        verticalLayout.addWidget(out_tb)

        retranslateUi(Server)
        ?C...QMetaObject.connectSlotsByName(Server)

    ___ retranslateUi , Server
        Server.setWindowTitle(_translate("Server", "Server", None))
        info_lb.sT..(_translate("Server", "IP:", None))

