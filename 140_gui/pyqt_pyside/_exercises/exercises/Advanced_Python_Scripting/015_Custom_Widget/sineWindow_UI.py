# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\015_Custom_Widget\sineWindow.ui'
#
# Created: Fri Dec 01 21:35:02 2017
#      by: PyQt4 UI code generator 4.10.1
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

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.r..(624, 444)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        widget _ ?G...?W..(centralwidget)
        widget.setGeometry(?C...?R..(100, 30, 461, 361))
        widget.setObjectName(_fromUtf8("widget"))
        gridLayout _ ?G...QGridLayout(widget)
        gridLayout.setMargin(0)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))
        lenght_label _ ?G...QLabel(widget)
        lenght_label.setObjectName(_fromUtf8("lenght_label"))
        gridLayout.addWidget(lenght_label, 0, 0, 1, 1)
        length_horizontalSlider _ ?G...QSlider(widget)
        length_horizontalSlider.setOrientation(?C...__.Horizontal)
        length_horizontalSlider.setObjectName(_fromUtf8("length_horizontalSlider"))
        gridLayout.addWidget(length_horizontalSlider, 0, 1, 1, 1)
        length_value_label _ ?G...QLabel(widget)
        length_value_label.setObjectName(_fromUtf8("length_value_label"))
        gridLayout.addWidget(length_value_label, 0, 2, 1, 1)
        height_label _ ?G...QLabel(widget)
        height_label.setObjectName(_fromUtf8("height_label"))
        gridLayout.addWidget(height_label, 1, 0, 1, 1)
        height_horizontalSlider _ ?G...QSlider(widget)
        height_horizontalSlider.setOrientation(?C...__.Horizontal)
        height_horizontalSlider.setObjectName(_fromUtf8("height_horizontalSlider"))
        gridLayout.addWidget(height_horizontalSlider, 1, 1, 1, 1)
        height_value_label _ ?G...QLabel(widget)
        height_value_label.setObjectName(_fromUtf8("height_value_label"))
        gridLayout.addWidget(height_value_label, 1, 2, 1, 1)
        width_label _ ?G...QLabel(widget)
        width_label.setObjectName(_fromUtf8("width_label"))
        gridLayout.addWidget(width_label, 2, 0, 1, 1)
        width_horizontalSlider _ ?G...QSlider(widget)
        width_horizontalSlider.setMaximum(20)
        width_horizontalSlider.setOrientation(?C...__.Horizontal)
        width_horizontalSlider.setObjectName(_fromUtf8("width_horizontalSlider"))
        gridLayout.addWidget(width_horizontalSlider, 2, 1, 1, 1)
        width_value_label _ ?G...QLabel(widget)
        width_value_label.setObjectName(_fromUtf8("width_value_label"))
        gridLayout.addWidget(width_value_label, 2, 2, 1, 1)
        grid_label _ ?G...QLabel(widget)
        grid_label.setObjectName(_fromUtf8("grid_label"))
        gridLayout.addWidget(grid_label, 3, 0, 1, 1)
        grid_horizontalSlider _ ?G...QSlider(widget)
        grid_horizontalSlider.setOrientation(?C...__.Horizontal)
        grid_horizontalSlider.setObjectName(_fromUtf8("grid_horizontalSlider"))
        gridLayout.addWidget(grid_horizontalSlider, 3, 1, 1, 1)
        grid_value_label _ ?G...QLabel(widget)
        grid_value_label.setObjectName(_fromUtf8("grid_value_label"))
        gridLayout.addWidget(grid_value_label, 3, 2, 1, 1)
        sine_verticalLayout _ ?G...QVBoxLayout
        sine_verticalLayout.setObjectName(_fromUtf8("sine_verticalLayout"))
        gridLayout.addLayout(sine_verticalLayout, 4, 1, 1, 1)
        MainWindow.setCentralWidget(centralwidget)

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", N..))
        lenght_label.sT..(_translate("MainWindow", "Length", N..))
        length_value_label.sT..(_translate("MainWindow", "0", N..))
        height_label.sT..(_translate("MainWindow", "Height", N..))
        height_value_label.sT..(_translate("MainWindow", "0", N..))
        width_label.sT..(_translate("MainWindow", "Width", N..))
        width_value_label.sT..(_translate("MainWindow", "1", N..))
        grid_label.sT..(_translate("MainWindow", "Grid", N..))
        grid_value_label.sT..(_translate("MainWindow", "3", N..))

