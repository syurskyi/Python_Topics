# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stylesheeteditor.ui'
#
# Created: Fri Jul 26 06:50:07 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_StyleSheetEditor o..
    ___ setupUi  StyleSheetEditor):
        StyleSheetEditor.setObjectName("StyleSheetEditor")
        StyleSheetEditor.r..(445, 289)
        gridlayout _ ?W...QGridLayout(StyleSheetEditor)
        gridlayout.sCM..(9, 9, 9, 9)
        gridlayout.setSpacing(6)
        gridlayout.setObjectName("gridlayout")
        spacerItem _ ?W...?SI..(32, 20, ?W...?SP...ME.., ?W...?SP...Minimum)
        gridlayout.aI..(spacerItem, 0, 6, 1, 1)
        spacerItem1 _ ?W...?SI..(32, 20, ?W...?SP...ME.., ?W...?SP...Minimum)
        gridlayout.aI..(spacerItem1, 0, 0, 1, 1)
        styleSheetCombo _ ?W...?CB(StyleSheetEditor)
        styleSheetCombo.setObjectName("styleSheetCombo")
        styleSheetCombo.aI..("")
        styleSheetCombo.aI..("")
        styleSheetCombo.aI..("")
        gridlayout.aW..(styleSheetCombo, 0, 5, 1, 1)
        spacerItem2 _ ?W...?SI..(10, 16, ?W...?SP...Fixed, ?W...?SP...Minimum)
        gridlayout.aI..(spacerItem2, 0, 3, 1, 1)
        styleCombo _ ?W...?CB(StyleSheetEditor)
        sizePolicy _ ?W...?SP..(?W...?SP...Preferred, ?W...?SP...Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(styleCombo.sizePolicy().hasHeightForWidth())
        styleCombo.sSP..(sizePolicy)
        styleCombo.setObjectName("styleCombo")
        gridlayout.aW..(styleCombo, 0, 2, 1, 1)
        label_7 _ ?W...?L..(StyleSheetEditor)
        sizePolicy _ ?W...?SP..(?W...?SP...Fixed, ?W...?SP...Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_7.sizePolicy().hasHeightForWidth())
        label_7.sSP..(sizePolicy)
        label_7.setObjectName("label_7")
        gridlayout.aW..(label_7, 0, 1, 1, 1)
        hboxlayout _ ?W...?HBL..
        hboxlayout.setSpacing(6)
        hboxlayout.sCM..(0, 0, 0, 0)
        hboxlayout.setObjectName("hboxlayout")
        spacerItem3 _ ?W...?SI..(321, 20, ?W...?SP...E.., ?W...?SP...Minimum)
        hboxlayout.aI..(spacerItem3)
        saveButton _ ?W...?PB..(StyleSheetEditor)
        saveButton.sE..( st.
        saveButton.setObjectName("saveButton")
        hboxlayout.aW..(saveButton)
        applyButton _ ?W...?PB..(StyleSheetEditor)
        applyButton.sE.. F..
        applyButton.setObjectName("applyButton")
        hboxlayout.aW..(applyButton)
        gridlayout.aL..(hboxlayout, 2, 0, 1, 7)
        styleTextEdit _ ?W...?TE..(StyleSheetEditor)
        styleTextEdit.setObjectName("styleTextEdit")
        gridlayout.aW..(styleTextEdit, 1, 0, 1, 7)
        label_8 _ ?W...?L..(StyleSheetEditor)
        sizePolicy _ ?W...?SP..(?W...?SP...Fixed, ?W...?SP...Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_8.sizePolicy().hasHeightForWidth())
        label_8.sSP..(sizePolicy)
        label_8.setObjectName("label_8")
        gridlayout.aW..(label_8, 0, 4, 1, 1)

        retranslateUi(StyleSheetEditor)
        ?C...QMetaObject.connectSlotsByName(StyleSheetEditor)

    ___ retranslateUi  StyleSheetEditor):
        _translate _ ?C... ?CA...translate
        StyleSheetEditor.sWT..(_translate("StyleSheetEditor", "Style Editor"))
        styleSheetCombo.setItemText(0, _translate("StyleSheetEditor", "Default"))
        styleSheetCombo.setItemText(1, _translate("StyleSheetEditor", "Coffee"))
        styleSheetCombo.setItemText(2, _translate("StyleSheetEditor", "Pagefold"))
        label_7.sT..(_translate("StyleSheetEditor", "Style:"))
        saveButton.sT..(_translate("StyleSheetEditor", "&Save"))
        applyButton.sT..(_translate("StyleSheetEditor", "&Apply"))
        label_8.sT..(_translate("StyleSheetEditor", "Style Sheet:"))

