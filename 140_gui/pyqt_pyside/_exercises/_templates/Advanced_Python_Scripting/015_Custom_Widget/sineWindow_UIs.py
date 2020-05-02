# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\015_Custom_Widget\sineWindow.ui'
#
# Created: Fri Dec 01 21:35:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., QtGui

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 444)
        centralwidget _ QtGui.?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        widget _ QtGui.?W..(centralwidget)
        widget.setGeometry(?C...QRect(100, 30, 461, 361))
        widget.setObjectName("widget")
        gridLayout _ QtGui.QGridLayout(widget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout")
        lenght_label _ QtGui.QLabel(widget)
        lenght_label.setObjectName("lenght_label")
        gridLayout.addWidget(lenght_label, 0, 0, 1, 1)
        length_horizontalSlider _ QtGui.QSlider(widget)
        length_horizontalSlider.setOrientation(?C...Qt.Horizontal)
        length_horizontalSlider.setObjectName("length_horizontalSlider")
        gridLayout.addWidget(length_horizontalSlider, 0, 1, 1, 1)
        length_value_label _ QtGui.QLabel(widget)
        length_value_label.setObjectName("length_value_label")
        gridLayout.addWidget(length_value_label, 0, 2, 1, 1)
        height_label _ QtGui.QLabel(widget)
        height_label.setObjectName("height_label")
        gridLayout.addWidget(height_label, 1, 0, 1, 1)
        height_horizontalSlider _ QtGui.QSlider(widget)
        height_horizontalSlider.setOrientation(?C...Qt.Horizontal)
        height_horizontalSlider.setObjectName("height_horizontalSlider")
        gridLayout.addWidget(height_horizontalSlider, 1, 1, 1, 1)
        height_value_label _ QtGui.QLabel(widget)
        height_value_label.setObjectName("height_value_label")
        gridLayout.addWidget(height_value_label, 1, 2, 1, 1)
        width_label _ QtGui.QLabel(widget)
        width_label.setObjectName("width_label")
        gridLayout.addWidget(width_label, 2, 0, 1, 1)
        width_horizontalSlider _ QtGui.QSlider(widget)
        width_horizontalSlider.setMaximum(20)
        width_horizontalSlider.setOrientation(?C...Qt.Horizontal)
        width_horizontalSlider.setObjectName("width_horizontalSlider")
        gridLayout.addWidget(width_horizontalSlider, 2, 1, 1, 1)
        width_value_label _ QtGui.QLabel(widget)
        width_value_label.setObjectName("width_value_label")
        gridLayout.addWidget(width_value_label, 2, 2, 1, 1)
        grid_label _ QtGui.QLabel(widget)
        grid_label.setObjectName("grid_label")
        gridLayout.addWidget(grid_label, 3, 0, 1, 1)
        grid_horizontalSlider _ QtGui.QSlider(widget)
        grid_horizontalSlider.setOrientation(?C...Qt.Horizontal)
        grid_horizontalSlider.setObjectName("grid_horizontalSlider")
        gridLayout.addWidget(grid_horizontalSlider, 3, 1, 1, 1)
        grid_value_label _ QtGui.QLabel(widget)
        grid_value_label.setObjectName("grid_value_label")
        gridLayout.addWidget(grid_value_label, 3, 2, 1, 1)
        sine_verticalLayout _ QtGui.QVBoxLayout()
        sine_verticalLayout.setObjectName("sine_verticalLayout")
        gridLayout.addLayout(sine_verticalLayout, 4, 1, 1, 1)
        MainWindow.setCentralWidget(centralwidget)

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(QtGui.?A...translate("MainWindow", "MainWindow", None, QtGui.?A...UnicodeUTF8))
        lenght_label.sT..(QtGui.?A...translate("MainWindow", "Length", None, QtGui.?A...UnicodeUTF8))
        length_value_label.sT..(QtGui.?A...translate("MainWindow", "0", None, QtGui.?A...UnicodeUTF8))
        height_label.sT..(QtGui.?A...translate("MainWindow", "Height", None, QtGui.?A...UnicodeUTF8))
        height_value_label.sT..(QtGui.?A...translate("MainWindow", "0", None, QtGui.?A...UnicodeUTF8))
        width_label.sT..(QtGui.?A...translate("MainWindow", "Width", None, QtGui.?A...UnicodeUTF8))
        width_value_label.sT..(QtGui.?A...translate("MainWindow", "1", None, QtGui.?A...UnicodeUTF8))
        grid_label.sT..(QtGui.?A...translate("MainWindow", "Grid", None, QtGui.?A...UnicodeUTF8))
        grid_value_label.sT..(QtGui.?A...translate("MainWindow", "3", None, QtGui.?A...UnicodeUTF8))

