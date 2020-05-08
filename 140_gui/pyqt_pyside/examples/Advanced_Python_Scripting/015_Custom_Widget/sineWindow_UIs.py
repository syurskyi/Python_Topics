# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\015_Custom_Widget\sineWindow.ui'
#
# Created: Fri Dec 01 21:35:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 30, 461, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lenght_label = QtWidgets.QLabel(self.widget)
        self.lenght_label.setObjectName("lenght_label")
        self.gridLayout.addWidget(self.lenght_label, 0, 0, 1, 1)
        self.length_horizontalSlider = QtWidgets.QSlider(self.widget)
        self.length_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.length_horizontalSlider.setObjectName("length_horizontalSlider")
        self.gridLayout.addWidget(self.length_horizontalSlider, 0, 1, 1, 1)
        self.length_value_label = QtWidgets.QLabel(self.widget)
        self.length_value_label.setObjectName("length_value_label")
        self.gridLayout.addWidget(self.length_value_label, 0, 2, 1, 1)
        self.height_label = QtWidgets.QLabel(self.widget)
        self.height_label.setObjectName("height_label")
        self.gridLayout.addWidget(self.height_label, 1, 0, 1, 1)
        self.height_horizontalSlider = QtWidgets.QSlider(self.widget)
        self.height_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.height_horizontalSlider.setObjectName("height_horizontalSlider")
        self.gridLayout.addWidget(self.height_horizontalSlider, 1, 1, 1, 1)
        self.height_value_label = QtWidgets.QLabel(self.widget)
        self.height_value_label.setObjectName("height_value_label")
        self.gridLayout.addWidget(self.height_value_label, 1, 2, 1, 1)
        self.width_label = QtWidgets.QLabel(self.widget)
        self.width_label.setObjectName("width_label")
        self.gridLayout.addWidget(self.width_label, 2, 0, 1, 1)
        self.width_horizontalSlider = QtWidgets.QSlider(self.widget)
        self.width_horizontalSlider.setMaximum(20)
        self.width_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.width_horizontalSlider.setObjectName("width_horizontalSlider")
        self.gridLayout.addWidget(self.width_horizontalSlider, 2, 1, 1, 1)
        self.width_value_label = QtWidgets.QLabel(self.widget)
        self.width_value_label.setObjectName("width_value_label")
        self.gridLayout.addWidget(self.width_value_label, 2, 2, 1, 1)
        self.grid_label = QtWidgets.QLabel(self.widget)
        self.grid_label.setObjectName("grid_label")
        self.gridLayout.addWidget(self.grid_label, 3, 0, 1, 1)
        self.grid_horizontalSlider = QtWidgets.QSlider(self.widget)
        self.grid_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.grid_horizontalSlider.setObjectName("grid_horizontalSlider")
        self.gridLayout.addWidget(self.grid_horizontalSlider, 3, 1, 1, 1)
        self.grid_value_label = QtWidgets.QLabel(self.widget)
        self.grid_value_label.setObjectName("grid_value_label")
        self.gridLayout.addWidget(self.grid_value_label, 3, 2, 1, 1)
        self.sine_verticalLayout = QtWidgets.QVBoxLayout()
        self.sine_verticalLayout.setObjectName("sine_verticalLayout")
        self.gridLayout.addLayout(self.sine_verticalLayout, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None))
        self.lenght_label.setText(QtWidgets.QApplication.translate("MainWindow", "Length", None))
        self.length_value_label.setText(QtWidgets.QApplication.translate("MainWindow", "0", None))
        self.height_label.setText(QtWidgets.QApplication.translate("MainWindow", "Height", None))
        self.height_value_label.setText(QtWidgets.QApplication.translate("MainWindow", "0", None))
        self.width_label.setText(QtWidgets.QApplication.translate("MainWindow", "Width", None))
        self.width_value_label.setText(QtWidgets.QApplication.translate("MainWindow", "1", None))
        self.grid_label.setText(QtWidgets.QApplication.translate("MainWindow", "Grid", None))
        self.grid_value_label.setText(QtWidgets.QApplication.translate("MainWindow", "3", None))

