# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sun May 12 11:56:49 2013
#      by: PyQt5 UI code generator 5.0-snapshot-b0831183bf83
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, QtGui, ?W..

class Ui_Dialog(object):
    ___ setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 322)
        self.gridlayout _ ?W...QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.loadFromFileButton _ ?W...?PB..(Dialog)
        self.loadFromFileButton.setObjectName("loadFromFileButton")
        self.gridlayout.addWidget(self.loadFromFileButton, 0, 0, 1, 1)
        self.label _ ?W...QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.loadFromSharedMemoryButton _ ?W...?PB..(Dialog)
        self.loadFromSharedMemoryButton.setObjectName("loadFromSharedMemoryButton")
        self.gridlayout.addWidget(self.loadFromSharedMemoryButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    ___ retranslateUi(self, Dialog):
        _translate _ QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loadFromFileButton.sT..(_translate("Dialog", "Load Image From File..."))
        self.label.sT..(_translate("Dialog", "Launch two of these dialogs.  In the first, press the top button and load an image from a file.  In the second, press the bottom button and display the loaded image from shared memory."))
        self.loadFromSharedMemoryButton.sT..(_translate("Dialog", "Display Image From Shared Memory"))

