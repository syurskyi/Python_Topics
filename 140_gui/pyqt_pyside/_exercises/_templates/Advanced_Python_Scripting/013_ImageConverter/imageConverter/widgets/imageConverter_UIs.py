# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\013_ImageConverter\imageConverter\widgets\imageConverter.ui'
#
# Created: Wed Nov 29 22:31:01 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_imageConverter(object
    ___ setupUi , imageConverter
        imageConverter.setObjectName("imageConverter")
        imageConverter.resize(456, 399)
        centralwidget _ QtGui.?W..(imageConverter)
        centralwidget.setObjectName("centralwidget")
        verticalLayout _ QtGui.QVBoxLayout(centralwidget)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout _ QtGui.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        iconver_lb _ QtGui.QLabel(centralwidget)
        iconver_lb.setObjectName("iconver_lb")
        horizontalLayout.addWidget(iconver_lb)
        browseIconvert_btn _ QtGui.?PB..(centralwidget)
        browseIconvert_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseIconvert_btn.setObjectName("browseIconvert_btn")
        horizontalLayout.addWidget(browseIconvert_btn)
        verticalLayout.addLayout(horizontalLayout)
        files_ly _ QtGui.QVBoxLayout()
        files_ly.setObjectName("files_ly")
        verticalLayout.addLayout(files_ly)
        horizontalLayout_2 _ QtGui.QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        out_le _ QtGui.QLineEdit(centralwidget)
        out_le.setObjectName("out_le")
        horizontalLayout_2.addWidget(out_le)
        browseOut_btn _ QtGui.?PB..(centralwidget)
        browseOut_btn.setMaximumSize(?C...QSize(30, 16777215))
        browseOut_btn.setObjectName("browseOut_btn")
        horizontalLayout_2.addWidget(browseOut_btn)
        verticalLayout.addLayout(horizontalLayout_2)
        start_btn _ QtGui.?PB..(centralwidget)
        start_btn.setObjectName("start_btn")
        verticalLayout.addWidget(start_btn)
        progressBar _ QtGui.QProgressBar(centralwidget)
        progressBar.setProperty("value", 0)
        progressBar.setObjectName("progressBar")
        verticalLayout.addWidget(progressBar)
        verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(centralwidget)

        retranslateUi(imageConverter)
        ?C...QMetaObject.connectSlotsByName(imageConverter)

    ___ retranslateUi , imageConverter
        imageConverter.setWindowTitle(QtGui.?A...translate("imageConverter", "MainWindow", None, QtGui.?A...UnicodeUTF8))
        iconver_lb.sT..(QtGui.?A...translate("imageConverter", "Path", None, QtGui.?A...UnicodeUTF8))
        browseIconvert_btn.sT..(QtGui.?A...translate("imageConverter", "...", None, QtGui.?A...UnicodeUTF8))
        browseOut_btn.sT..(QtGui.?A...translate("imageConverter", "...", None, QtGui.?A...UnicodeUTF8))
        start_btn.sT..(QtGui.?A...translate("imageConverter", "Start", None, QtGui.?A...UnicodeUTF8))

