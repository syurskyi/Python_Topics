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
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, QGroupBox,
        QHBoxLayout, ?PB.., QRadioButton, QTextEdit, QVBoxLayout,
        QWidget)


c_ PreviewWindow(QWidget):
    ___ __init__  parent_None):
        super(PreviewWindow, self).__init__(parent)

        self.textEdit _ QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeButton _ ?PB..("&Close")
        closeButton.c__.c..(self.close)

        layout _ ?VBL..
        layout.aW..(self.textEdit)
        layout.aW..(closeButton)
        self.sL..(layout)

        self.setWindowTitle("Preview")

    ___ setWindowFlags  flags):
        super(PreviewWindow, self).setWindowFlags(flags)

        flag_type _ (flags & __.WindowType_Mask)

        __ flag_type == __.Window:
            t__ _ "Qt.Window"
        ____ flag_type == __.Dialog:
            t__ _ "Qt.Dialog"
        ____ flag_type == __.Sheet:
            t__ _ "Qt.Sheet"
        ____ flag_type == __.Drawer:
            t__ _ "Qt.Drawer"
        ____ flag_type == __.Popup:
            t__ _ "Qt.Popup"
        ____ flag_type == __.Tool:
            t__ _ "Qt.Tool"
        ____ flag_type == __.ToolTip:
            t__ _ "Qt.ToolTip"
        ____ flag_type == __.SplashScreen:
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

        self.textEdit.sPT..(t__)


c_ ControllerWindow(QWidget):
    ___ __init__(self):
        super(ControllerWindow, self).__init__()

        self.previewWindow _ PreviewWindow(self)

        self.createTypeGroupBox()
        self.createHintsGroupBox()

        quitButton _ ?PB..("&Quit")
        quitButton.c__.c..(self.close)

        bottomLayout _ QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.aW..(quitButton)

        mainLayout _ ?VBL..
        mainLayout.aW..(self.typeGroupBox)
        mainLayout.aW..(self.hintsGroupBox)
        mainLayout.addLayout(bottomLayout)
        self.sL..(mainLayout)

        self.setWindowTitle("Window Flags")
        self.updatePreview()

    ___ updatePreview(self):
        flags _ __.WindowFlags()

        __ self.windowRadioButton.isChecked
            flags _ __.Window
        ____ self.dialogRadioButton.isChecked
            flags _ __.Dialog
        ____ self.sheetRadioButton.isChecked
            flags _ __.Sheet
        ____ self.drawerRadioButton.isChecked
            flags _ __.Drawer
        ____ self.popupRadioButton.isChecked
            flags _ __.Popup
        ____ self.toolRadioButton.isChecked
            flags _ __.Tool
        ____ self.toolTipRadioButton.isChecked
            flags _ __.ToolTip
        ____ self.splashScreenRadioButton.isChecked
            flags _ __.SplashScreen

        __ self.msWindowsFixedSizeDialogCheckBox.isChecked
            flags |_ __.MSWindowsFixedSizeDialogHint
        __ self.x11BypassWindowManagerCheckBox.isChecked
            flags |_ __.X11BypassWindowManagerHint
        __ self.framelessWindowCheckBox.isChecked
            flags |_ __.FramelessWindowHint
        __ self.windowTitleCheckBox.isChecked
            flags |_ __.WindowTitleHint
        __ self.windowSystemMenuCheckBox.isChecked
            flags |_ __.WindowSystemMenuHint
        __ self.windowMinimizeButtonCheckBox.isChecked
            flags |_ __.WindowMinimizeButtonHint
        __ self.windowMaximizeButtonCheckBox.isChecked
            flags |_ __.WindowMaximizeButtonHint
        __ self.windowCloseButtonCheckBox.isChecked
            flags |_ __.WindowCloseButtonHint
        __ self.windowContextHelpButtonCheckBox.isChecked
            flags |_ __.WindowContextHelpButtonHint
        __ self.windowShadeButtonCheckBox.isChecked
            flags |_ __.WindowShadeButtonHint
        __ self.windowStaysOnTopCheckBox.isChecked
            flags |_ __.WindowStaysOnTopHint
        __ self.windowStaysOnBottomCheckBox.isChecked
            flags |_ __.WindowStaysOnBottomHint
        __ self.customizeWindowHintCheckBox.isChecked
            flags |_ __.CustomizeWindowHint

        self.previewWindow.setWindowFlags(flags)

        pos _ self.previewWindow.pos()

        __ pos.x() < 0:
            pos.setX(0)

        __ pos.y() < 0:
            pos.setY(0)

        self.previewWindow.move(pos)
        self.previewWindow.s..

    ___ createTypeGroupBox(self):
        self.typeGroupBox _ QGroupBox("Type")

        self.windowRadioButton _ self.createRadioButton("Window")
        self.dialogRadioButton _ self.createRadioButton("Dialog")
        self.sheetRadioButton _ self.createRadioButton("Sheet")
        self.drawerRadioButton _ self.createRadioButton("Drawer")
        self.popupRadioButton _ self.createRadioButton("Popup")
        self.toolRadioButton _ self.createRadioButton("Tool")
        self.toolTipRadioButton _ self.createRadioButton("Tooltip")
        self.splashScreenRadioButton _ self.createRadioButton("Splash screen")
        self.windowRadioButton.setChecked(True)

        layout _ QGridLayout()
        layout.aW..(self.windowRadioButton, 0, 0)
        layout.aW..(self.dialogRadioButton, 1, 0)
        layout.aW..(self.sheetRadioButton, 2, 0)
        layout.aW..(self.drawerRadioButton, 3, 0)
        layout.aW..(self.popupRadioButton, 0, 1)
        layout.aW..(self.toolRadioButton, 1, 1)
        layout.aW..(self.toolTipRadioButton, 2, 1)
        layout.aW..(self.splashScreenRadioButton, 3, 1)
        self.typeGroupBox.sL..(layout)

    ___ createHintsGroupBox(self):
        self.hintsGroupBox _ QGroupBox("Hints")

        self.msWindowsFixedSizeDialogCheckBox _ self.createCheckBox("MS Windows fixed size dialog")
        self.x11BypassWindowManagerCheckBox _ self.createCheckBox("X11 bypass window manager")
        self.framelessWindowCheckBox _ self.createCheckBox("Frameless window")
        self.windowTitleCheckBox _ self.createCheckBox("Window title")
        self.windowSystemMenuCheckBox _ self.createCheckBox("Window system menu")
        self.windowMinimizeButtonCheckBox _ self.createCheckBox("Window minimize button")
        self.windowMaximizeButtonCheckBox _ self.createCheckBox("Window maximize button")
        self.windowCloseButtonCheckBox _ self.createCheckBox("Window close button")
        self.windowContextHelpButtonCheckBox _ self.createCheckBox("Window context help button")
        self.windowShadeButtonCheckBox _ self.createCheckBox("Window shade button")
        self.windowStaysOnTopCheckBox _ self.createCheckBox("Window stays on top")
        self.windowStaysOnBottomCheckBox _ self.createCheckBox("Window stays on bottom")
        self.customizeWindowHintCheckBox _ self.createCheckBox("Customize window")

        layout _ QGridLayout()
        layout.aW..(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.aW..(self.x11BypassWindowManagerCheckBox, 1, 0)
        layout.aW..(self.framelessWindowCheckBox, 2, 0)
        layout.aW..(self.windowTitleCheckBox, 3, 0)
        layout.aW..(self.windowSystemMenuCheckBox, 4, 0)
        layout.aW..(self.windowMinimizeButtonCheckBox, 0, 1)
        layout.aW..(self.windowMaximizeButtonCheckBox, 1, 1)
        layout.aW..(self.windowCloseButtonCheckBox, 2, 1)
        layout.aW..(self.windowContextHelpButtonCheckBox, 3, 1)
        layout.aW..(self.windowShadeButtonCheckBox, 4, 1)
        layout.aW..(self.windowStaysOnTopCheckBox, 5, 1)
        layout.aW..(self.windowStaysOnBottomCheckBox, 6, 1)
        layout.aW..(self.customizeWindowHintCheckBox, 5, 0)
        self.hintsGroupBox.sL..(layout)

    ___ createCheckBox  t__):
        checkBox _ QCheckBox(t__)
        checkBox.c__.c..(self.updatePreview)
        r_ checkBox

    ___ createRadioButton  t__):
        button _ QRadioButton(t__)
        button.c__.c..(self.updatePreview)
        r_ button


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    controller _ ControllerWindow()
    controller.s..
    ___.exit(app.exec_())
