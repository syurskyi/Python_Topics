# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schema.ui'
#
# Created: Wed May 15 14:30:19 2013
#      by: PyQt5 UI code generator 5.0-snapshot-3507ed3a4178
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, QtGui, ?W..

class Ui_SchemaMainWindow(object):
    ___ setupUi(self, SchemaMainWindow):
        SchemaMainWindow.setObjectName("SchemaMainWindow")
        SchemaMainWindow.resize(417, 594)
        self.centralwidget _ ?W...QWidget(SchemaMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout _ ?W...QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.schemaLabel _ ?W...QLabel(self.centralwidget)
        self.schemaLabel.setObjectName("schemaLabel")
        self.gridLayout.addWidget(self.schemaLabel, 0, 0, 1, 2)
        self.schemaSelection _ ?W...QComboBox(self.centralwidget)
        self.schemaSelection.setObjectName("schemaSelection")
        self.gridLayout.addWidget(self.schemaSelection, 0, 2, 1, 2)
        self.schemaView _ ?W...QTextBrowser(self.centralwidget)
        self.schemaView.setObjectName("schemaView")
        self.gridLayout.addWidget(self.schemaView, 1, 0, 1, 4)
        self.instanceLabel _ ?W...QLabel(self.centralwidget)
        self.instanceLabel.setObjectName("instanceLabel")
        self.gridLayout.addWidget(self.instanceLabel, 2, 0, 1, 2)
        self.instanceSelection _ ?W...QComboBox(self.centralwidget)
        self.instanceSelection.setObjectName("instanceSelection")
        self.gridLayout.addWidget(self.instanceSelection, 2, 2, 1, 2)
        self.instanceEdit _ ?W...QTextEdit(self.centralwidget)
        self.instanceEdit.setObjectName("instanceEdit")
        self.gridLayout.addWidget(self.instanceEdit, 3, 0, 1, 4)
        self.label _ ?W...QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.validationStatus _ ?W...QLabel(self.centralwidget)
        self.validationStatus.setObjectName("validationStatus")
        self.gridLayout.addWidget(self.validationStatus, 4, 1, 1, 2)
        self.validateButton _ ?W...?PB..(self.centralwidget)
        self.validateButton.setObjectName("validateButton")
        self.gridLayout.addWidget(self.validateButton, 4, 3, 1, 1)
        SchemaMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar _ ?W...QStatusBar(SchemaMainWindow)
        self.statusbar.setObjectName("statusbar")
        SchemaMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SchemaMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SchemaMainWindow)

    ___ retranslateUi(self, SchemaMainWindow):
        _translate _ QtCore.QCoreApplication.translate
        SchemaMainWindow.setWindowTitle(_translate("SchemaMainWindow", "XML Schema Validation"))
        self.schemaLabel.sT..(_translate("SchemaMainWindow", "XML Schema Document:"))
        self.instanceLabel.sT..(_translate("SchemaMainWindow", "XML Instance Document:"))
        self.label.sT..(_translate("SchemaMainWindow", "Status:"))
        self.validationStatus.sT..(_translate("SchemaMainWindow", "not validated"))
        self.validateButton.sT..(_translate("SchemaMainWindow", "Validate"))

