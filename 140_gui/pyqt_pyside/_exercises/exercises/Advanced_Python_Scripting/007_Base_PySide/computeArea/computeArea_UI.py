# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\computeArea\computeArea.ui'
#
# Created: Sun Nov 05 16:17:46 2017
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

c_ Ui_computeArea(object
    ___ setupUi , computeArea
        computeArea.setObjectName(_fromUtf8("computeArea"))
        computeArea.r..(741, 777)
        centralwidget _ ?G...?W..(computeArea)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout_3 _ ?G...QVBoxLayout(centralwidget)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        groupBox _ ?G...QGroupBox(centralwidget)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        verticalLayout _ ?G...QVBoxLayout(groupBox)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        shape_cbb _ ?G...QComboBox(groupBox)
        shape_cbb.setObjectName(_fromUtf8("shape_cbb"))
        shape_cbb.aI..(_fromUtf8(""))
        shape_cbb.aI..(_fromUtf8(""))
        verticalLayout.addWidget(shape_cbb)
        verticalLayout_3.addWidget(groupBox)
        square_gb _ ?G...QGroupBox(centralwidget)
        square_gb.setObjectName(_fromUtf8("square_gb"))
        layoutWidget _ ?G...?W..(square_gb)
        layoutWidget.setGeometry(?C...?R..(30, 30, 401, 101))
        layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        verticalLayout_2 _ ?G...QVBoxLayout(layoutWidget)
        verticalLayout_2.setMargin(0)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        horizontalLayout _ ?G...QHBoxLayout
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        label _ ?G...QLabel(layoutWidget)
        label.setMinimumSize(?C...QSize(70, 0))
        label.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label.setObjectName(_fromUtf8("label"))
        horizontalLayout.addWidget(label)
        square_height_spx _ ?G...QSpinBox(layoutWidget)
        square_height_spx.setMinimum(1)
        square_height_spx.setMaximum(9999999)
        square_height_spx.setObjectName(_fromUtf8("square_height_spx"))
        horizontalLayout.addWidget(square_height_spx)
        horizontalLayout.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout)
        horizontalLayout_2 _ ?G...QHBoxLayout
        horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        label_2 _ ?G...QLabel(layoutWidget)
        label_2.setMinimumSize(?C...QSize(70, 0))
        label_2.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_2.setObjectName(_fromUtf8("label_2"))
        horizontalLayout_2.addWidget(label_2)
        square_width_spx _ ?G...QSpinBox(layoutWidget)
        square_width_spx.setMinimum(1)
        square_width_spx.setMaximum(9999999)
        square_width_spx.setObjectName(_fromUtf8("square_width_spx"))
        horizontalLayout_2.addWidget(square_width_spx)
        horizontalLayout_2.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout_2)
        verticalLayout_3.addWidget(square_gb)
        circle_gb _ ?G...QGroupBox(centralwidget)
        circle_gb.setObjectName(_fromUtf8("circle_gb"))
        layoutWidget_4 _ ?G...?W..(circle_gb)
        layoutWidget_4.setGeometry(?C...?R..(30, 30, 401, 31))
        layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        horizontalLayout_7 _ ?G...QHBoxLayout(layoutWidget_4)
        horizontalLayout_7.setMargin(0)
        horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        label_7 _ ?G...QLabel(layoutWidget_4)
        label_7.setMinimumSize(?C...QSize(70, 0))
        label_7.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_7.setObjectName(_fromUtf8("label_7"))
        horizontalLayout_7.addWidget(label_7)
        circle_radius_spx _ ?G...QSpinBox(layoutWidget_4)
        circle_radius_spx.setMinimum(1)
        circle_radius_spx.setMaximum(9999999)
        circle_radius_spx.setObjectName(_fromUtf8("circle_radius_spx"))
        horizontalLayout_7.addWidget(circle_radius_spx)
        horizontalLayout_7.setStretch(1, 1)
        verticalLayout_3.addWidget(circle_gb)
        compute_btn _ ?G...?PB..(centralwidget)
        compute_btn.setObjectName(_fromUtf8("compute_btn"))
        verticalLayout_3.addWidget(compute_btn)
        result_lbl _ ?G...QLabel(centralwidget)
        result_lbl.setObjectName(_fromUtf8("result_lbl"))
        verticalLayout_3.addWidget(result_lbl)
        computeArea.setCentralWidget(centralwidget)
        statusbar _ ?G...QStatusBar(computeArea)
        statusbar.setObjectName(_fromUtf8("statusbar"))
        computeArea.setStatusBar(statusbar)

        retranslateUi(computeArea)
        ?C...QMetaObject.connectSlotsByName(computeArea)

    ___ retranslateUi , computeArea
        computeArea.setWindowTitle(_translate("computeArea", "ComputeArea", N..))
        groupBox.setTitle(_translate("computeArea", "Select Shape", N..))
        shape_cbb.setItemText(0, _translate("computeArea", "Square", N..))
        shape_cbb.setItemText(1, _translate("computeArea", "Radius", N..))
        square_gb.setTitle(_translate("computeArea", "Square", N..))
        label.sT..(_translate("computeArea", "Height", N..))
        label_2.sT..(_translate("computeArea", "Width", N..))
        circle_gb.setTitle(_translate("computeArea", "Circle", N..))
        label_7.sT..(_translate("computeArea", "Radius", N..))
        compute_btn.sT..(_translate("computeArea", "COMPUTE", N..))
        result_lbl.sT..(_translate("computeArea", "Result", N..))

