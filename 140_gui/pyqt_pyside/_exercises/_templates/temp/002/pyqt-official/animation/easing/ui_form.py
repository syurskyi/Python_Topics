# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Thu May  2 16:46:55 2013
#      by: PyQt5 UI code generator snapshot-5.0-e46cc7cf20da
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Form(object):
    ___ setupUi  Form):
        Form.setObjectName("Form")
        Form.r..(545, 471)
        gridLayout _ ?W...QGridLayout(Form)
        gridLayout.setObjectName("gridLayout")
        easingCurvePicker _ ?W...QListWidget(Form)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.E.., ?W...QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(easingCurvePicker.sizePolicy().hasHeightForWidth())
        easingCurvePicker.sSP..(sizePolicy)
        easingCurvePicker.sMS..(?C...?S..(16777215, 120))
        easingCurvePicker.setVerticalScrollBarPolicy(?C...__.ScrollBarAlwaysOff)
        easingCurvePicker.setMovement(?W...QListView.Static)
        easingCurvePicker.setProperty("isWrapping", F..)
        easingCurvePicker.setViewMode(?W...QListView.IconMode)
        easingCurvePicker.setSelectionRectVisible F..
        easingCurvePicker.setObjectName("easingCurvePicker")
        gridLayout.aW..(easingCurvePicker, 0, 0, 1, 2)
        verticalLayout _ ?W...?VBL..
        verticalLayout.setObjectName("verticalLayout")
        groupBox_2 _ ?W...QGroupBox(Form)
        groupBox_2.sMS..(?C...?S..(16777215, 16777215))
        groupBox_2.setObjectName("groupBox_2")
        gridLayout_2 _ ?W...QGridLayout(groupBox_2)
        gridLayout_2.setObjectName("gridLayout_2")
        lineRadio _ ?W...QRadioButton(groupBox_2)
        lineRadio.sMS..(?C...?S..(16777215, 40))
        lineRadio.setLayoutDirection(?C...__.LeftToRight)
        lineRadio.sC__( st.
        lineRadio.setObjectName("lineRadio")
        buttonGroup _ ?W...QButtonGroup(Form)
        buttonGroup.setObjectName("buttonGroup")
        buttonGroup.addButton(lineRadio)
        gridLayout_2.aW..(lineRadio, 0, 0, 1, 1)
        circleRadio _ ?W...QRadioButton(groupBox_2)
        circleRadio.sMS..(?C...?S..(16777215, 40))
        circleRadio.setObjectName("circleRadio")
        buttonGroup.addButton(circleRadio)
        gridLayout_2.aW..(circleRadio, 1, 0, 1, 1)
        verticalLayout.aW..(groupBox_2)
        groupBox _ ?W...QGroupBox(Form)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Fixed, ?W...QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(groupBox.sizePolicy().hasHeightForWidth())
        groupBox.sSP..(sizePolicy)
        groupBox.setObjectName("groupBox")
        formLayout _ ?W...?FL..(groupBox)
        formLayout.setFieldGrowthPolicy(?W...?FL...AllNonFixedFieldsGrow)
        formLayout.setObjectName("formLayout")
        label _ ?W...QLabel(groupBox)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Preferred, ?W...QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.sSP..(sizePolicy)
        label.sMS..(?C...?S..(0, 30))
        label.setObjectName("label")
        formLayout.setWidget(0, ?W...?FL...LabelRole, label)
        periodSpinBox _ ?W...QDoubleSpinBox(groupBox)
        periodSpinBox.sE.. F..
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Minimum, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(periodSpinBox.sizePolicy().hasHeightForWidth())
        periodSpinBox.sSP..(sizePolicy)
        periodSpinBox.sMS..(?C...?S..(0, 30))
        periodSpinBox.setMinimum(-1.0)
        periodSpinBox.setSingleStep(0.1)
        periodSpinBox.setProperty("value", -1.0)
        periodSpinBox.setObjectName("periodSpinBox")
        formLayout.setWidget(0, ?W...?FL...FieldRole, periodSpinBox)
        amplitudeSpinBox _ ?W...QDoubleSpinBox(groupBox)
        amplitudeSpinBox.sE.. F..
        amplitudeSpinBox.sMS..(?C...?S..(0, 30))
        amplitudeSpinBox.setMinimum(-1.0)
        amplitudeSpinBox.setSingleStep(0.1)
        amplitudeSpinBox.setProperty("value", -1.0)
        amplitudeSpinBox.setObjectName("amplitudeSpinBox")
        formLayout.setWidget(2, ?W...?FL...FieldRole, amplitudeSpinBox)
        label_3 _ ?W...QLabel(groupBox)
        label_3.sMS..(?C...?S..(0, 30))
        label_3.setObjectName("label_3")
        formLayout.setWidget(4, ?W...?FL...LabelRole, label_3)
        overshootSpinBox _ ?W...QDoubleSpinBox(groupBox)
        overshootSpinBox.sE.. F..
        overshootSpinBox.sMS..(?C...?S..(0, 30))
        overshootSpinBox.setMinimum(-1.0)
        overshootSpinBox.setSingleStep(0.1)
        overshootSpinBox.setProperty("value", -1.0)
        overshootSpinBox.setObjectName("overshootSpinBox")
        formLayout.setWidget(4, ?W...?FL...FieldRole, overshootSpinBox)
        label_2 _ ?W...QLabel(groupBox)
        label_2.sMS..(?C...?S..(0, 30))
        label_2.setObjectName("label_2")
        formLayout.setWidget(2, ?W...?FL...LabelRole, label_2)
        verticalLayout.aW..(groupBox)
        spacerItem _ ?W...QSpacerItem(20, 40, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.E..)
        verticalLayout.aI..(spacerItem)
        gridLayout.aL..(verticalLayout, 1, 0, 1, 1)
        graphicsView _ ?W...QGraphicsView(Form)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.E.., ?W...QSizePolicy.E..)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(graphicsView.sizePolicy().hasHeightForWidth())
        graphicsView.sSP..(sizePolicy)
        graphicsView.setObjectName("graphicsView")
        gridLayout.aW..(graphicsView, 1, 1, 1, 1)

        retranslateUi(Form)
        ?C...QMetaObject.connectSlotsByName(Form)

    ___ retranslateUi  Form):
        _translate _ ?C... ?CA...translate
        Form.sWT..(_translate("Form", "Easing curves"))
        groupBox_2.setTitle(_translate("Form", "Path type"))
        lineRadio.sT..(_translate("Form", "Line"))
        circleRadio.sT..(_translate("Form", "Circle"))
        groupBox.setTitle(_translate("Form", "Properties"))
        label.sT..(_translate("Form", "Period"))
        label_3.sT..(_translate("Form", "Overshoot"))
        label_2.sT..(_translate("Form", "Amplitude"))

