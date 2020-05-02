# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\computeArea\computeArea.ui'
#
# Created: Sun Nov 05 16:17:46 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., QtGui

try:
    _fromUtf8 = ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding = QtGui.?A...UnicodeUTF8
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig, _encoding)
except AttributeError:
    ___ _translate(context, text, disambig
        return QtGui.?A...translate(context, text, disambig)

c_ Ui_computeArea(object
    ___ setupUi , computeArea
        computeArea.setObjectName(_fromUtf8("computeArea"))
        computeArea.resize(741, 777)
        centralwidget = QtGui.?W..(computeArea)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout_3 = QtGui.QVBoxLayout(centralwidget)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        groupBox = QtGui.QGroupBox(centralwidget)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        verticalLayout = QtGui.QVBoxLayout(groupBox)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        shape_cbb = QtGui.QComboBox(groupBox)
        shape_cbb.setObjectName(_fromUtf8("shape_cbb"))
        shape_cbb.addItem(_fromUtf8(""))
        shape_cbb.addItem(_fromUtf8(""))
        verticalLayout.addWidget(shape_cbb)
        verticalLayout_3.addWidget(groupBox)
        square_gb = QtGui.QGroupBox(centralwidget)
        square_gb.setObjectName(_fromUtf8("square_gb"))
        layoutWidget = QtGui.?W..(square_gb)
        layoutWidget.setGeometry(?C...QRect(30, 30, 401, 101))
        layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        verticalLayout_2 = QtGui.QVBoxLayout(layoutWidget)
        verticalLayout_2.setMargin(0)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        label = QtGui.QLabel(layoutWidget)
        label.setMinimumSize(?C...QSize(70, 0))
        label.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label.setObjectName(_fromUtf8("label"))
        horizontalLayout.addWidget(label)
        square_height_spx = QtGui.QSpinBox(layoutWidget)
        square_height_spx.setMinimum(1)
        square_height_spx.setMaximum(9999999)
        square_height_spx.setObjectName(_fromUtf8("square_height_spx"))
        horizontalLayout.addWidget(square_height_spx)
        horizontalLayout.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout)
        horizontalLayout_2 = QtGui.QHBoxLayout()
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        label_2 = QtGui.QLabel(layoutWidget)
        label_2.setMinimumSize(?C...QSize(70, 0))
        label_2.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_2.setObjectName(_fromUtf8("label_2"))
        horizontalLayout_2.addWidget(label_2)
        square_width_spx = QtGui.QSpinBox(layoutWidget)
        square_width_spx.setMinimum(1)
        square_width_spx.setMaximum(9999999)
        square_width_spx.setObjectName(_fromUtf8("square_width_spx"))
        horizontalLayout_2.addWidget(square_width_spx)
        horizontalLayout_2.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout_2)
        verticalLayout_3.addWidget(square_gb)
        circle_gb = QtGui.QGroupBox(centralwidget)
        circle_gb.setObjectName(_fromUtf8("circle_gb"))
        layoutWidget_4 = QtGui.?W..(circle_gb)
        layoutWidget_4.setGeometry(?C...QRect(30, 30, 401, 31))
        layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        horizontalLayout_7 = QtGui.QHBoxLayout(layoutWidget_4)
        horizontalLayout_7.setMargin(0)
        horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        label_7 = QtGui.QLabel(layoutWidget_4)
        label_7.setMinimumSize(?C...QSize(70, 0))
        label_7.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_7.setObjectName(_fromUtf8("label_7"))
        horizontalLayout_7.addWidget(label_7)
        circle_radius_spx = QtGui.QSpinBox(layoutWidget_4)
        circle_radius_spx.setMinimum(1)
        circle_radius_spx.setMaximum(9999999)
        circle_radius_spx.setObjectName(_fromUtf8("circle_radius_spx"))
        horizontalLayout_7.addWidget(circle_radius_spx)
        horizontalLayout_7.setStretch(1, 1)
        verticalLayout_3.addWidget(circle_gb)
        compute_btn = QtGui.?PB..(centralwidget)
        compute_btn.setObjectName(_fromUtf8("compute_btn"))
        verticalLayout_3.addWidget(compute_btn)
        result_lbl = QtGui.QLabel(centralwidget)
        result_lbl.setObjectName(_fromUtf8("result_lbl"))
        verticalLayout_3.addWidget(result_lbl)
        computeArea.setCentralWidget(centralwidget)
        statusbar = QtGui.QStatusBar(computeArea)
        statusbar.setObjectName(_fromUtf8("statusbar"))
        computeArea.setStatusBar(statusbar)

        retranslateUi(computeArea)
        ?C...QMetaObject.connectSlotsByName(computeArea)

    ___ retranslateUi , computeArea
        computeArea.setWindowTitle(_translate("computeArea", "ComputeArea", None))
        groupBox.setTitle(_translate("computeArea", "Select Shape", None))
        shape_cbb.setItemText(0, _translate("computeArea", "Square", None))
        shape_cbb.setItemText(1, _translate("computeArea", "Radius", None))
        square_gb.setTitle(_translate("computeArea", "Square", None))
        label.sT..(_translate("computeArea", "Height", None))
        label_2.sT..(_translate("computeArea", "Width", None))
        circle_gb.setTitle(_translate("computeArea", "Circle", None))
        label_7.sT..(_translate("computeArea", "Radius", None))
        compute_btn.sT..(_translate("computeArea", "COMPUTE", None))
        result_lbl.sT..(_translate("computeArea", "Result", None))

