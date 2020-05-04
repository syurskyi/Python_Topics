# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week4\imageConverter\widgets\imageConverter.ui'
#
# Created: Tue Oct 21 17:49:06 2014
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

c_ Ui_imageConverter(object
    ___ setupUi , imageConverter
        imageConverter.setObjectName(_fromUtf8("imageConverter"))
        imageConverter.r..(339, 379)
        centralwidget _ ?G...?W..(imageConverter)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout _ ?G...QVBoxLayout(centralwidget)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        iconvert_lb _ ?G...QLabel(centralwidget)
        iconvert_lb.setObjectName(_fromUtf8("iconvert_lb"))
        horizontalLayout.addWidget(iconvert_lb)
        browseIconvert_btn _ ?G...?PB..(centralwidget)
        browseIconvert_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseIconvert_btn.setObjectName(_fromUtf8("browseIconvert_btn"))
        horizontalLayout.addWidget(browseIconvert_btn)
        verticalLayout.addLayout(horizontalLayout)
        files_ly _ ?G...QVBoxLayout
        files_ly.setObjectName(_fromUtf8("files_ly"))
        verticalLayout.addLayout(files_ly)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        out_le _ ?G...QLineEdit(centralwidget)
        out_le.setObjectName(_fromUtf8("out_le"))
        horizontalLayout_2.addWidget(out_le)
        browseOut_btn _ ?G...?PB..(centralwidget)
        browseOut_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseOut_btn.setObjectName(_fromUtf8("browseOut_btn"))
        horizontalLayout_2.addWidget(browseOut_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        start_btn _ ?G...?PB..(centralwidget)
        start_btn.setObjectName(_fromUtf8("start_btn"))
        verticalLayout.addWidget(start_btn)
        progressBar _ ?G...QProgressBar(centralwidget)
        pB__.setProperty("value", 0)
        pB__.setObjectName(_fromUtf8("progressBar"))
        verticalLayout.addWidget(pB__)
        verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(centralwidget)

        retranslateUi(imageConverter)
        ?C...QMetaObject.connectSlotsByName(imageConverter)

    ___ retranslateUi , imageConverter
        imageConverter.setWindowTitle(_translate("imageConverter", "MainWindow", N..))
        iconvert_lb.sT..(_translate("imageConverter", "Path", N..))
        browseIconvert_btn.sT..(_translate("imageConverter", "...", N..))
        browseOut_btn.sT..(_translate("imageConverter", "...", N..))
        start_btn.sT..(_translate("imageConverter", "Strat", N..))

