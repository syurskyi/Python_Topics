# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\015_Custom_Widget\sineWindow.ui'
#
# Created: Fri Dec 01 21:35:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 444)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 30, 461, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lenght_label = QtGui.QLabel(self.widget)
        self.lenght_label.setObjectName("lenght_label")
        self.gridLayout.addWidget(self.lenght_label, 0, 0, 1, 1)
        self.length_horizontalSlider = QtGui.QSlider(self.widget)
        self.length_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.length_horizontalSlider.setObjectName("length_horizontalSlider")
        self.gridLayout.addWidget(self.length_horizontalSlider, 0, 1, 1, 1)
        self.length_value_label = QtGui.QLabel(self.widget)
        self.length_value_label.setObjectName("length_value_label")
        self.gridLayout.addWidget(self.length_value_label, 0, 2, 1, 1)
        self.height_label = QtGui.QLabel(self.widget)
        self.height_label.setObjectName("height_label")
        self.gridLayout.addWidget(self.height_label, 1, 0, 1, 1)
        self.height_horizontalSlider = QtGui.QSlider(self.widget)
        self.height_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.height_horizontalSlider.setObjectName("height_horizontalSlider")
        self.gridLayout.addWidget(self.height_horizontalSlider, 1, 1, 1, 1)
        self.height_value_label = QtGui.QLabel(self.widget)
        self.height_value_label.setObjectName("height_value_label")
        self.gridLayout.addWidget(self.height_value_label, 1, 2, 1, 1)
        self.width_label = QtGui.QLabel(self.widget)
        self.width_label.setObjectName("width_label")
        self.gridLayout.addWidget(self.width_label, 2, 0, 1, 1)
        self.width_horizontalSlider = QtGui.QSlider(self.widget)
        self.width_horizontalSlider.setMaximum(20)
        self.width_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.width_horizontalSlider.setObjectName("width_horizontalSlider")
        self.gridLayout.addWidget(self.width_horizontalSlider, 2, 1, 1, 1)
        self.width_value_label = QtGui.QLabel(self.widget)
        self.width_value_label.setObjectName("width_value_label")
        self.gridLayout.addWidget(self.width_value_label, 2, 2, 1, 1)
        self.grid_label = QtGui.QLabel(self.widget)
        self.grid_label.setObjectName("grid_label")
        self.gridLayout.addWidget(self.grid_label, 3, 0, 1, 1)
        self.grid_horizontalSlider = QtGui.QSlider(self.widget)
        self.grid_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.grid_horizontalSlider.setObjectName("grid_horizontalSlider")
        self.gridLayout.addWidget(self.grid_horizontalSlider, 3, 1, 1, 1)
        self.grid_value_label = QtGui.QLabel(self.widget)
        self.grid_value_label.setObjectName("grid_value_label")
        self.gridLayout.addWidget(self.grid_value_label, 3, 2, 1, 1)
        self.sine_verticalLayout = QtGui.QVBoxLayout()
        self.sine_verticalLayout.setObjectName("sine_verticalLayout")
        self.gridLayout.addLayout(self.sine_verticalLayout, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lenght_label.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.length_value_label.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.height_label.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.height_value_label.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.width_label.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.width_value_label.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_label.setText(QtGui.QApplication.translate("MainWindow", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_value_label.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))

