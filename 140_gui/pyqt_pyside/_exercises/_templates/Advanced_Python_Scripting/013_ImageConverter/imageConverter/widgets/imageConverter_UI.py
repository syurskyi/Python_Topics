# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\013_ImageConverter\imageConverter\widgets\imageConverter.ui'
#
# Created: Wed Nov 29 22:30:59 2017
#      by: PyQt4 UI code generator 4.10.1
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
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig)

c_ Ui_imageConverter(object
    ___ setupUi , imageConverter
        imageConverter.setObjectName(_fromUtf8("imageConverter"))
        imageConverter.resize(456, 399)
        centralwidget _ QtGui.?W..(imageConverter)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout _ QtGui.QVBoxLayout(centralwidget)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        iconver_lb _ QtGui.QLabel(centralwidget)
        iconver_lb.setObjectName(_fromUtf8("iconver_lb"))
        horizontalLayout.addWidget(iconver_lb)
        browseIconvert_btn _ QtGui.?PB..(centralwidget)
        browseIconvert_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseIconvert_btn.setObjectName(_fromUtf8("browseIconvert_btn"))
        horizontalLayout.addWidget(browseIconvert_btn)
        verticalLayout.addLayout(horizontalLayout)
        files_ly _ QtGui.QVBoxLayout()
        files_ly.setObjectName(_fromUtf8("files_ly"))
        verticalLayout.addLayout(files_ly)
        horizontalLayout_2 _ QtGui.QHBoxLayout()
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        out_le _ QtGui.QLineEdit(centralwidget)
        out_le.setObjectName(_fromUtf8("out_le"))
        horizontalLayout_2.addWidget(out_le)
        browseOut_btn _ QtGui.?PB..(centralwidget)
        browseOut_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseOut_btn.setObjectName(_fromUtf8("browseOut_btn"))
        horizontalLayout_2.addWidget(browseOut_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        start_btn _ QtGui.?PB..(centralwidget)
        start_btn.setObjectName(_fromUtf8("start_btn"))
        verticalLayout.addWidget(start_btn)
        progressBar _ QtGui.QProgressBar(centralwidget)
        progressBar.setProperty("value", 0)
        progressBar.setObjectName(_fromUtf8("progressBar"))
        verticalLayout.addWidget(progressBar)
        verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(centralwidget)

        retranslateUi(imageConverter)
        ?C...QMetaObject.connectSlotsByName(imageConverter)

    ___ retranslateUi , imageConverter
        imageConverter.setWindowTitle(_translate("imageConverter", "MainWindow", None))
        iconver_lb.sT..(_translate("imageConverter", "Path", None))
        browseIconvert_btn.sT..(_translate("imageConverter", "...", None))
        browseOut_btn.sT..(_translate("imageConverter", "...", None))
        start_btn.sT..(_translate("imageConverter", "Start", None))

