# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sun May 12 11:56:49 2013
#      by: PyQt5 UI code generator 5.0-snapshot-b0831183bf83
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_Dialog o..
    ___ setupUi  Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.r..(451, 322)
        gridlayout _ ?W...QGridLayout(Dialog)
        gridlayout.setObjectName("gridlayout")
        loadFromFileButton _ ?W...?PB..(Dialog)
        loadFromFileButton.setObjectName("loadFromFileButton")
        gridlayout.aW..(loadFromFileButton, 0, 0, 1, 1)
        label _ ?W...?L..(Dialog)
        label.setAlignment(?C...__.AlignCenter)
        label.setWordWrap( st.
        label.setObjectName("label")
        gridlayout.aW..(label, 1, 0, 1, 1)
        loadFromSharedMemoryButton _ ?W...?PB..(Dialog)
        loadFromSharedMemoryButton.setObjectName("loadFromSharedMemoryButton")
        gridlayout.aW..(loadFromSharedMemoryButton, 2, 0, 1, 1)

        retranslateUi(Dialog)
        ?C...QMetaObject.connectSlotsByName(Dialog)

    ___ retranslateUi  Dialog):
        _translate _ ?C... ?CA...translate
        Dialog.sWT..(_translate("Dialog", "Dialog"))
        loadFromFileButton.sT..(_translate("Dialog", "Load Image From File..."))
        label.sT..(_translate("Dialog", "Launch two of these dialogs.  In the first, press the top button and load an image from a file.  In the second, press the bottom button and display the loaded image from shared memory."))
        loadFromSharedMemoryButton.sT..(_translate("Dialog", "Display Image From Shared Memory"))

