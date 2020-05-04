# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week4\imageConverter\widgets\imageConverter.ui'
#
# Created: Tue Oct 21 17:49:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ ? _____ ?C.., ?G..

c_ Ui_imageConverter(object
    ___ setupUi , imageConverter
        imageConverter.setObjectName("imageConverter")
        imageConverter.r..(339, 379)
        centralwidget _ ?G...?W..(imageConverter)
        centralwidget.setObjectName("centralwidget")
        verticalLayout _ ?G...QVBoxLayout(centralwidget)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName("horizontalLayout")
        iconvert_lb _ ?G...QLabel(centralwidget)
        iconvert_lb.setObjectName("iconvert_lb")
        horizontalLayout.addWidget(iconvert_lb)
        browseIconvert_btn _ ?G...?PB..(centralwidget)
        browseIconvert_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseIconvert_btn.setObjectName("browseIconvert_btn")
        horizontalLayout.addWidget(browseIconvert_btn)
        verticalLayout.addLayout(horizontalLayout)
        files_ly _ ?G...QVBoxLayout
        files_ly.setObjectName("files_ly")
        verticalLayout.addLayout(files_ly)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        out_le _ ?G...QLineEdit(centralwidget)
        out_le.setObjectName("out_le")
        horizontalLayout_2.addWidget(out_le)
        browseOut_btn _ ?G...?PB..(centralwidget)
        browseOut_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseOut_btn.setObjectName("browseOut_btn")
        horizontalLayout_2.addWidget(browseOut_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        start_btn _ ?G...?PB..(centralwidget)
        start_btn.setObjectName("start_btn")
        verticalLayout.addWidget(start_btn)
        progressBar _ ?G...QProgressBar(centralwidget)
        progressBar.setProperty("value", 0)
        pB__.setObjectName("progressBar")
        verticalLayout.addWidget(pB__)
        verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(centralwidget)

        retranslateUi(imageConverter)
        ?C...QMetaObject.connectSlotsByName(imageConverter)

    ___ retranslateUi , imageConverter
        imageConverter.setWindowTitle(?G...?A...translate("imageConverter", "MainWindow", N.., ?G...?A...UnicodeUTF8))
        iconvert_lb.sT..(?G...?A...translate("imageConverter", "Path", N.., ?G...?A...UnicodeUTF8))
        browseIconvert_btn.sT..(?G...?A...translate("imageConverter", "...", N.., ?G...?A...UnicodeUTF8))
        browseOut_btn.sT..(?G...?A...translate("imageConverter", "...", N.., ?G...?A...UnicodeUTF8))
        start_btn.sT..(?G...?A...translate("imageConverter", "Strat", N.., ?G...?A...UnicodeUTF8))

