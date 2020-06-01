# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stylesheeteditor.ui'
#
# Created: Fri Jul 26 06:50:07 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ QtCore, ?G.., ?W..

c_ Ui_StyleSheetEditor(object):
    ___ setupUi  StyleSheetEditor):
        StyleSheetEditor.setObjectName("StyleSheetEditor")
        StyleSheetEditor.resize(445, 289)
        self.gridlayout _ ?W...QGridLayout(StyleSheetEditor)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem _ ?W...QSpacerItem(32, 20, ?W...QSizePolicy.MinimumExpanding, ?W...QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 6, 1, 1)
        spacerItem1 _ ?W...QSpacerItem(32, 20, ?W...QSizePolicy.MinimumExpanding, ?W...QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.styleSheetCombo _ ?W...QComboBox(StyleSheetEditor)
        self.styleSheetCombo.setObjectName("styleSheetCombo")
        self.styleSheetCombo.addItem("")
        self.styleSheetCombo.addItem("")
        self.styleSheetCombo.addItem("")
        self.gridlayout.addWidget(self.styleSheetCombo, 0, 5, 1, 1)
        spacerItem2 _ ?W...QSpacerItem(10, 16, ?W...QSizePolicy.Fixed, ?W...QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.styleCombo _ ?W...QComboBox(StyleSheetEditor)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Preferred, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.styleCombo.sizePolicy().hasHeightForWidth())
        self.styleCombo.setSizePolicy(sizePolicy)
        self.styleCombo.setObjectName("styleCombo")
        self.gridlayout.addWidget(self.styleCombo, 0, 2, 1, 1)
        self.label_7 _ ?W...QLabel(StyleSheetEditor)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Fixed, ?W...QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.hboxlayout _ ?W...QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem3 _ ?W...QSpacerItem(321, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.saveButton _ ?W...?PB..(StyleSheetEditor)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName("saveButton")
        self.hboxlayout.addWidget(self.saveButton)
        self.applyButton _ ?W...?PB..(StyleSheetEditor)
        self.applyButton.setEnabled F..
        self.applyButton.setObjectName("applyButton")
        self.hboxlayout.addWidget(self.applyButton)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 7)
        self.styleTextEdit _ ?W...QTextEdit(StyleSheetEditor)
        self.styleTextEdit.setObjectName("styleTextEdit")
        self.gridlayout.addWidget(self.styleTextEdit, 1, 0, 1, 7)
        self.label_8 _ ?W...QLabel(StyleSheetEditor)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Fixed, ?W...QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8, 0, 4, 1, 1)

        self.retranslateUi(StyleSheetEditor)
        QtCore.QMetaObject.connectSlotsByName(StyleSheetEditor)

    ___ retranslateUi  StyleSheetEditor):
        _translate _ QtCore.QCoreApplication.translate
        StyleSheetEditor.setWindowTitle(_translate("StyleSheetEditor", "Style Editor"))
        self.styleSheetCombo.setItemText(0, _translate("StyleSheetEditor", "Default"))
        self.styleSheetCombo.setItemText(1, _translate("StyleSheetEditor", "Coffee"))
        self.styleSheetCombo.setItemText(2, _translate("StyleSheetEditor", "Pagefold"))
        self.label_7.sT..(_translate("StyleSheetEditor", "Style:"))
        self.saveButton.sT..(_translate("StyleSheetEditor", "&Save"))
        self.applyButton.sT..(_translate("StyleSheetEditor", "&Apply"))
        self.label_8.sT..(_translate("StyleSheetEditor", "Style Sheet:"))

