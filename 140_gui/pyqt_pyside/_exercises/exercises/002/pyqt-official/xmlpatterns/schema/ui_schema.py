# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schema.ui'
#
# Created: Wed May 15 14:30:19 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_SchemaMainWindow o..
    ___ setupUi  SchemaMainWindow):
        SchemaMainWindow.setObjectName("SchemaMainWindow")
        SchemaMainWindow.r..(417, 594)
        centralwidget _ ?W...?W..(SchemaMainWindow)
        centralwidget.setObjectName("centralwidget")
        gridLayout _ ?W...QGridLayout(centralwidget)
        gridLayout.setObjectName("gridLayout")
        schemaLabel _ ?W...?L..(centralwidget)
        schemaLabel.setObjectName("schemaLabel")
        gridLayout.aW..(schemaLabel, 0, 0, 1, 2)
        schemaSelection _ ?W...?CB(centralwidget)
        schemaSelection.setObjectName("schemaSelection")
        gridLayout.aW..(schemaSelection, 0, 2, 1, 2)
        schemaView _ ?W...QTextBrowser(centralwidget)
        schemaView.setObjectName("schemaView")
        gridLayout.aW..(schemaView, 1, 0, 1, 4)
        instanceLabel _ ?W...?L..(centralwidget)
        instanceLabel.setObjectName("instanceLabel")
        gridLayout.aW..(instanceLabel, 2, 0, 1, 2)
        instanceSelection _ ?W...?CB(centralwidget)
        instanceSelection.setObjectName("instanceSelection")
        gridLayout.aW..(instanceSelection, 2, 2, 1, 2)
        instanceEdit _ ?W...?TE..(centralwidget)
        instanceEdit.setObjectName("instanceEdit")
        gridLayout.aW..(instanceEdit, 3, 0, 1, 4)
        label _ ?W...?L..(centralwidget)
        label.setObjectName("label")
        gridLayout.aW..(label, 4, 0, 1, 1)
        validationStatus _ ?W...?L..(centralwidget)
        validationStatus.setObjectName("validationStatus")
        gridLayout.aW..(validationStatus, 4, 1, 1, 2)
        validateButton _ ?W...?PB..(centralwidget)
        validateButton.setObjectName("validateButton")
        gridLayout.aW..(validateButton, 4, 3, 1, 1)
        SchemaMainWindow.sCW..(centralwidget)
        statusbar _ ?W...QStatusBar(SchemaMainWindow)
        statusbar.setObjectName("statusbar")
        SchemaMainWindow.sSB..(statusbar)

        retranslateUi(SchemaMainWindow)
        ?C...QMetaObject.connectSlotsByName(SchemaMainWindow)

    ___ retranslateUi  SchemaMainWindow):
        _translate _ ?C... ?CA...translate
        SchemaMainWindow.sWT..(_translate("SchemaMainWindow", "XML Schema Validation"))
        schemaLabel.sT..(_translate("SchemaMainWindow", "XML Schema Document:"))
        instanceLabel.sT..(_translate("SchemaMainWindow", "XML Instance Document:"))
        label.sT..(_translate("SchemaMainWindow", "Status:"))
        validationStatus.sT..(_translate("SchemaMainWindow", "not validated"))
        validateButton.sT..(_translate("SchemaMainWindow", "Validate"))

