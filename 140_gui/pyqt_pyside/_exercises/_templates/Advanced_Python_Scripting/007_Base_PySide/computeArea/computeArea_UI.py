# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\computeArea\computeArea.ui'
#
# Created: Sun Nov 05 16:17:46 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_computeArea(object):
    def setupUi(self, computeArea):
        computeArea.setObjectName(_fromUtf8("computeArea"))
        computeArea.resize(741, 777)
        self.centralwidget = QtGui.QWidget(computeArea)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.shape_cbb = QtGui.QComboBox(self.groupBox)
        self.shape_cbb.setObjectName(_fromUtf8("shape_cbb"))
        self.shape_cbb.addItem(_fromUtf8(""))
        self.shape_cbb.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.shape_cbb)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.square_gb = QtGui.QGroupBox(self.centralwidget)
        self.square_gb.setObjectName(_fromUtf8("square_gb"))
        self.layoutWidget = QtGui.QWidget(self.square_gb)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 401, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.square_height_spx = QtGui.QSpinBox(self.layoutWidget)
        self.square_height_spx.setMinimum(1)
        self.square_height_spx.setMaximum(9999999)
        self.square_height_spx.setObjectName(_fromUtf8("square_height_spx"))
        self.horizontalLayout.addWidget(self.square_height_spx)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.square_width_spx = QtGui.QSpinBox(self.layoutWidget)
        self.square_width_spx.setMinimum(1)
        self.square_width_spx.setMaximum(9999999)
        self.square_width_spx.setObjectName(_fromUtf8("square_width_spx"))
        self.horizontalLayout_2.addWidget(self.square_width_spx)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.square_gb)
        self.circle_gb = QtGui.QGroupBox(self.centralwidget)
        self.circle_gb.setObjectName(_fromUtf8("circle_gb"))
        self.layoutWidget_4 = QtGui.QWidget(self.circle_gb)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 30, 401, 31))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(70, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.circle_radius_spx = QtGui.QSpinBox(self.layoutWidget_4)
        self.circle_radius_spx.setMinimum(1)
        self.circle_radius_spx.setMaximum(9999999)
        self.circle_radius_spx.setObjectName(_fromUtf8("circle_radius_spx"))
        self.horizontalLayout_7.addWidget(self.circle_radius_spx)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.circle_gb)
        self.compute_btn = QtGui.QPushButton(self.centralwidget)
        self.compute_btn.setObjectName(_fromUtf8("compute_btn"))
        self.verticalLayout_3.addWidget(self.compute_btn)
        self.result_lbl = QtGui.QLabel(self.centralwidget)
        self.result_lbl.setObjectName(_fromUtf8("result_lbl"))
        self.verticalLayout_3.addWidget(self.result_lbl)
        computeArea.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(computeArea)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        computeArea.setStatusBar(self.statusbar)

        self.retranslateUi(computeArea)
        QtCore.QMetaObject.connectSlotsByName(computeArea)

    def retranslateUi(self, computeArea):
        computeArea.setWindowTitle(_translate("computeArea", "ComputeArea", None))
        self.groupBox.setTitle(_translate("computeArea", "Select Shape", None))
        self.shape_cbb.setItemText(0, _translate("computeArea", "Square", None))
        self.shape_cbb.setItemText(1, _translate("computeArea", "Radius", None))
        self.square_gb.setTitle(_translate("computeArea", "Square", None))
        self.label.setText(_translate("computeArea", "Height", None))
        self.label_2.setText(_translate("computeArea", "Width", None))
        self.circle_gb.setTitle(_translate("computeArea", "Circle", None))
        self.label_7.setText(_translate("computeArea", "Radius", None))
        self.compute_btn.setText(_translate("computeArea", "COMPUTE", None))
        self.result_lbl.setText(_translate("computeArea", "Result", None))

