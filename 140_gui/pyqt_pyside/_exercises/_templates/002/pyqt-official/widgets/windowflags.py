#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ __
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, ?GB..,
        ?HBL.., ?PB.., QRadioButton, ?TE.., ?VBL..,
        ?W..)


c_ PreviewWindow(?W..):
    ___  -   parent_None):
        s__(PreviewWindow, self). - (parent)

        textEdit _ ?TE..()
        textEdit.sRO..( st.
        textEdit.setLineWrapMode(?TE...NoWrap)

        closeButton _ ?PB..("&Close")
        closeButton.c__.c..(close)

        layout _ ?VBL..
        layout.aW..(textEdit)
        layout.aW..(closeButton)
        sL..(layout)

        sWT..("Preview")

    ___ setWindowFlags  flags):
        s__(PreviewWindow, self).setWindowFlags(flags)

        flag_type _ (flags & __.WindowType_Mask)

        __ flag_type __ __.Window:
            t__ _ "Qt.Window"
        ____ flag_type __ __.Dialog:
            t__ _ "Qt.Dialog"
        ____ flag_type __ __.Sheet:
            t__ _ "Qt.Sheet"
        ____ flag_type __ __.Drawer:
            t__ _ "Qt.Drawer"
        ____ flag_type __ __.Popup:
            t__ _ "Qt.Popup"
        ____ flag_type __ __.Tool:
            t__ _ "Qt.Tool"
        ____ flag_type __ __.ToolTip:
            t__ _ "Qt.ToolTip"
        ____ flag_type __ __.SplashScreen:
            t__ _ "Qt.SplashScreen"
        ____
            t__ _ ""

        __ flags & __.MSWindowsFixedSizeDialogHint:
            t__ +_ "\n| Qt.MSWindowsFixedSizeDialogHint"
        __ flags & __.X11BypassWindowManagerHint:
            t__ +_ "\n| Qt.X11BypassWindowManagerHint"
        __ flags & __.FramelessWindowHint:
            t__ +_ "\n| Qt.FramelessWindowHint"
        __ flags & __.WindowTitleHint:
            t__ +_ "\n| Qt.WindowTitleHint"
        __ flags & __.WindowSystemMenuHint:
            t__ +_ "\n| Qt.WindowSystemMenuHint"
        __ flags & __.WindowMinimizeButtonHint:
            t__ +_ "\n| Qt.WindowMinimizeButtonHint"
        __ flags & __.WindowMaximizeButtonHint:
            t__ +_ "\n| Qt.WindowMaximizeButtonHint"
        __ flags & __.WindowCloseButtonHint:
            t__ +_ "\n| Qt.WindowCloseButtonHint"
        __ flags & __.WindowContextHelpButtonHint:
            t__ +_ "\n| Qt.WindowContextHelpButtonHint"
        __ flags & __.WindowShadeButtonHint:
            t__ +_ "\n| Qt.WindowShadeButtonHint"
        __ flags & __.WindowStaysOnTopHint:
            t__ +_ "\n| Qt.WindowStaysOnTopHint"
        __ flags & __.WindowStaysOnBottomHint:
            t__ +_ "\n| Qt.WindowStaysOnBottomHint"
        __ flags & __.CustomizeWindowHint:
            t__ +_ "\n| Qt.CustomizeWindowHint"

        textEdit.sPT..(t__)


c_ ControllerWindow(?W..):
    ___  -
        s__(ControllerWindow, self). - ()

        previewWindow _ PreviewWindow

        createTypeGroupBox()
        createHintsGroupBox()

        quitButton _ ?PB..("&Quit")
        quitButton.c__.c..(close)

        bottomLayout _ ?HBL..
        bottomLayout.addStretch()
        bottomLayout.aW..(quitButton)

        mainLayout _ ?VBL..
        mainLayout.aW..(typeGroupBox)
        mainLayout.aW..(hintsGroupBox)
        mainLayout.aL..(bottomLayout)
        sL..(mainLayout)

        sWT..("Window Flags")
        updatePreview()

    ___ updatePreview
        flags _ __.WindowFlags()

        __ windowRadioButton.isChecked
            flags _ __.Window
        ____ dialogRadioButton.isChecked
            flags _ __.Dialog
        ____ sheetRadioButton.isChecked
            flags _ __.Sheet
        ____ drawerRadioButton.isChecked
            flags _ __.Drawer
        ____ popupRadioButton.isChecked
            flags _ __.Popup
        ____ toolRadioButton.isChecked
            flags _ __.Tool
        ____ toolTipRadioButton.isChecked
            flags _ __.ToolTip
        ____ splashScreenRadioButton.isChecked
            flags _ __.SplashScreen

        __ msWindowsFixedSizeDialogCheckBox.isChecked
            flags |_ __.MSWindowsFixedSizeDialogHint
        __ x11BypassWindowManagerCheckBox.isChecked
            flags |_ __.X11BypassWindowManagerHint
        __ framelessWindowCheckBox.isChecked
            flags |_ __.FramelessWindowHint
        __ windowTitleCheckBox.isChecked
            flags |_ __.WindowTitleHint
        __ windowSystemMenuCheckBox.isChecked
            flags |_ __.WindowSystemMenuHint
        __ windowMinimizeButtonCheckBox.isChecked
            flags |_ __.WindowMinimizeButtonHint
        __ windowMaximizeButtonCheckBox.isChecked
            flags |_ __.WindowMaximizeButtonHint
        __ windowCloseButtonCheckBox.isChecked
            flags |_ __.WindowCloseButtonHint
        __ windowContextHelpButtonCheckBox.isChecked
            flags |_ __.WindowContextHelpButtonHint
        __ windowShadeButtonCheckBox.isChecked
            flags |_ __.WindowShadeButtonHint
        __ windowStaysOnTopCheckBox.isChecked
            flags |_ __.WindowStaysOnTopHint
        __ windowStaysOnBottomCheckBox.isChecked
            flags |_ __.WindowStaysOnBottomHint
        __ customizeWindowHintCheckBox.isChecked
            flags |_ __.CustomizeWindowHint

        previewWindow.setWindowFlags(flags)

        pos _ previewWindow.pos()

        __ pos.x() < 0:
            pos.setX(0)

        __ pos.y() < 0:
            pos.setY(0)

        previewWindow.move(pos)
        previewWindow.s..

    ___ createTypeGroupBox
        typeGroupBox _ ?GB..("Type")

        windowRadioButton _ createRadioButton("Window")
        dialogRadioButton _ createRadioButton("Dialog")
        sheetRadioButton _ createRadioButton("Sheet")
        drawerRadioButton _ createRadioButton("Drawer")
        popupRadioButton _ createRadioButton("Popup")
        toolRadioButton _ createRadioButton("Tool")
        toolTipRadioButton _ createRadioButton("Tooltip")
        splashScreenRadioButton _ createRadioButton("Splash screen")
        windowRadioButton.sC__( st.

        layout _ QGridLayout()
        layout.aW..(windowRadioButton, 0, 0)
        layout.aW..(dialogRadioButton, 1, 0)
        layout.aW..(sheetRadioButton, 2, 0)
        layout.aW..(drawerRadioButton, 3, 0)
        layout.aW..(popupRadioButton, 0, 1)
        layout.aW..(toolRadioButton, 1, 1)
        layout.aW..(toolTipRadioButton, 2, 1)
        layout.aW..(splashScreenRadioButton, 3, 1)
        typeGroupBox.sL..(layout)

    ___ createHintsGroupBox
        hintsGroupBox _ ?GB..("Hints")

        msWindowsFixedSizeDialogCheckBox _ createCheckBox("MS Windows fixed size dialog")
        x11BypassWindowManagerCheckBox _ createCheckBox("X11 bypass window manager")
        framelessWindowCheckBox _ createCheckBox("Frameless window")
        windowTitleCheckBox _ createCheckBox("Window title")
        windowSystemMenuCheckBox _ createCheckBox("Window system menu")
        windowMinimizeButtonCheckBox _ createCheckBox("Window minimize button")
        windowMaximizeButtonCheckBox _ createCheckBox("Window maximize button")
        windowCloseButtonCheckBox _ createCheckBox("Window close button")
        windowContextHelpButtonCheckBox _ createCheckBox("Window context help button")
        windowShadeButtonCheckBox _ createCheckBox("Window shade button")
        windowStaysOnTopCheckBox _ createCheckBox("Window stays on top")
        windowStaysOnBottomCheckBox _ createCheckBox("Window stays on bottom")
        customizeWindowHintCheckBox _ createCheckBox("Customize window")

        layout _ QGridLayout()
        layout.aW..(msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.aW..(x11BypassWindowManagerCheckBox, 1, 0)
        layout.aW..(framelessWindowCheckBox, 2, 0)
        layout.aW..(windowTitleCheckBox, 3, 0)
        layout.aW..(windowSystemMenuCheckBox, 4, 0)
        layout.aW..(windowMinimizeButtonCheckBox, 0, 1)
        layout.aW..(windowMaximizeButtonCheckBox, 1, 1)
        layout.aW..(windowCloseButtonCheckBox, 2, 1)
        layout.aW..(windowContextHelpButtonCheckBox, 3, 1)
        layout.aW..(windowShadeButtonCheckBox, 4, 1)
        layout.aW..(windowStaysOnTopCheckBox, 5, 1)
        layout.aW..(windowStaysOnBottomCheckBox, 6, 1)
        layout.aW..(customizeWindowHintCheckBox, 5, 0)
        hintsGroupBox.sL..(layout)

    ___ createCheckBox  t__):
        checkBox _ QCheckBox(t__)
        checkBox.c__.c..(updatePreview)
        r_ checkBox

    ___ createRadioButton  t__):
        button _ QRadioButton(t__)
        button.c__.c..(updatePreview)
        r_ button


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    controller _ ControllerWindow()
    controller.s..
    ___.e.. ?.e..
