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


____ ?.QtCore ______ Qt
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, QGroupBox,
        QHBoxLayout, ?PB.., QRadioButton, QTextEdit, QVBoxLayout,
        QWidget)


class PreviewWindow(QWidget):
    ___ __init__(self, parent_None):
        super(PreviewWindow, self).__init__(parent)

        self.textEdit _ QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeButton _ ?PB..("&Close")
        closeButton.c__.c..(self.close)

        layout _ QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

    ___ setWindowFlags(self, flags):
        super(PreviewWindow, self).setWindowFlags(flags)

        flag_type _ (flags & Qt.WindowType_Mask)

        if flag_type == Qt.Window:
            text _ "Qt.Window"
        elif flag_type == Qt.Dialog:
            text _ "Qt.Dialog"
        elif flag_type == Qt.Sheet:
            text _ "Qt.Sheet"
        elif flag_type == Qt.Drawer:
            text _ "Qt.Drawer"
        elif flag_type == Qt.Popup:
            text _ "Qt.Popup"
        elif flag_type == Qt.Tool:
            text _ "Qt.Tool"
        elif flag_type == Qt.ToolTip:
            text _ "Qt.ToolTip"
        elif flag_type == Qt.SplashScreen:
            text _ "Qt.SplashScreen"
        else:
            text _ ""

        if flags & Qt.MSWindowsFixedSizeDialogHint:
            text +_ "\n| Qt.MSWindowsFixedSizeDialogHint"
        if flags & Qt.X11BypassWindowManagerHint:
            text +_ "\n| Qt.X11BypassWindowManagerHint"
        if flags & Qt.FramelessWindowHint:
            text +_ "\n| Qt.FramelessWindowHint"
        if flags & Qt.WindowTitleHint:
            text +_ "\n| Qt.WindowTitleHint"
        if flags & Qt.WindowSystemMenuHint:
            text +_ "\n| Qt.WindowSystemMenuHint"
        if flags & Qt.WindowMinimizeButtonHint:
            text +_ "\n| Qt.WindowMinimizeButtonHint"
        if flags & Qt.WindowMaximizeButtonHint:
            text +_ "\n| Qt.WindowMaximizeButtonHint"
        if flags & Qt.WindowCloseButtonHint:
            text +_ "\n| Qt.WindowCloseButtonHint"
        if flags & Qt.WindowContextHelpButtonHint:
            text +_ "\n| Qt.WindowContextHelpButtonHint"
        if flags & Qt.WindowShadeButtonHint:
            text +_ "\n| Qt.WindowShadeButtonHint"
        if flags & Qt.WindowStaysOnTopHint:
            text +_ "\n| Qt.WindowStaysOnTopHint"
        if flags & Qt.WindowStaysOnBottomHint:
            text +_ "\n| Qt.WindowStaysOnBottomHint"
        if flags & Qt.CustomizeWindowHint:
            text +_ "\n| Qt.CustomizeWindowHint"

        self.textEdit.setPlainText(text)


class ControllerWindow(QWidget):
    ___ __init__(self):
        super(ControllerWindow, self).__init__()

        self.previewWindow _ PreviewWindow(self)

        self.createTypeGroupBox()
        self.createHintsGroupBox()

        quitButton _ ?PB..("&Quit")
        quitButton.c__.c..(self.close)

        bottomLayout _ QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(quitButton)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.typeGroupBox)
        mainLayout.addWidget(self.hintsGroupBox)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Window Flags")
        self.updatePreview()

    ___ updatePreview(self):
        flags _ Qt.WindowFlags()

        if self.windowRadioButton.isChecked
            flags _ Qt.Window
        elif self.dialogRadioButton.isChecked
            flags _ Qt.Dialog
        elif self.sheetRadioButton.isChecked
            flags _ Qt.Sheet
        elif self.drawerRadioButton.isChecked
            flags _ Qt.Drawer
        elif self.popupRadioButton.isChecked
            flags _ Qt.Popup
        elif self.toolRadioButton.isChecked
            flags _ Qt.Tool
        elif self.toolTipRadioButton.isChecked
            flags _ Qt.ToolTip
        elif self.splashScreenRadioButton.isChecked
            flags _ Qt.SplashScreen

        if self.msWindowsFixedSizeDialogCheckBox.isChecked
            flags |_ Qt.MSWindowsFixedSizeDialogHint
        if self.x11BypassWindowManagerCheckBox.isChecked
            flags |_ Qt.X11BypassWindowManagerHint
        if self.framelessWindowCheckBox.isChecked
            flags |_ Qt.FramelessWindowHint
        if self.windowTitleCheckBox.isChecked
            flags |_ Qt.WindowTitleHint
        if self.windowSystemMenuCheckBox.isChecked
            flags |_ Qt.WindowSystemMenuHint
        if self.windowMinimizeButtonCheckBox.isChecked
            flags |_ Qt.WindowMinimizeButtonHint
        if self.windowMaximizeButtonCheckBox.isChecked
            flags |_ Qt.WindowMaximizeButtonHint
        if self.windowCloseButtonCheckBox.isChecked
            flags |_ Qt.WindowCloseButtonHint
        if self.windowContextHelpButtonCheckBox.isChecked
            flags |_ Qt.WindowContextHelpButtonHint
        if self.windowShadeButtonCheckBox.isChecked
            flags |_ Qt.WindowShadeButtonHint
        if self.windowStaysOnTopCheckBox.isChecked
            flags |_ Qt.WindowStaysOnTopHint
        if self.windowStaysOnBottomCheckBox.isChecked
            flags |_ Qt.WindowStaysOnBottomHint
        if self.customizeWindowHintCheckBox.isChecked
            flags |_ Qt.CustomizeWindowHint

        self.previewWindow.setWindowFlags(flags)

        pos _ self.previewWindow.pos()

        if pos.x() < 0:
            pos.setX(0)

        if pos.y() < 0:
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
        layout.addWidget(self.windowRadioButton, 0, 0)
        layout.addWidget(self.dialogRadioButton, 1, 0)
        layout.addWidget(self.sheetRadioButton, 2, 0)
        layout.addWidget(self.drawerRadioButton, 3, 0)
        layout.addWidget(self.popupRadioButton, 0, 1)
        layout.addWidget(self.toolRadioButton, 1, 1)
        layout.addWidget(self.toolTipRadioButton, 2, 1)
        layout.addWidget(self.splashScreenRadioButton, 3, 1)
        self.typeGroupBox.setLayout(layout)

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
        layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.addWidget(self.x11BypassWindowManagerCheckBox, 1, 0)
        layout.addWidget(self.framelessWindowCheckBox, 2, 0)
        layout.addWidget(self.windowTitleCheckBox, 3, 0)
        layout.addWidget(self.windowSystemMenuCheckBox, 4, 0)
        layout.addWidget(self.windowMinimizeButtonCheckBox, 0, 1)
        layout.addWidget(self.windowMaximizeButtonCheckBox, 1, 1)
        layout.addWidget(self.windowCloseButtonCheckBox, 2, 1)
        layout.addWidget(self.windowContextHelpButtonCheckBox, 3, 1)
        layout.addWidget(self.windowShadeButtonCheckBox, 4, 1)
        layout.addWidget(self.windowStaysOnTopCheckBox, 5, 1)
        layout.addWidget(self.windowStaysOnBottomCheckBox, 6, 1)
        layout.addWidget(self.customizeWindowHintCheckBox, 5, 0)
        self.hintsGroupBox.setLayout(layout)

    ___ createCheckBox(self, text):
        checkBox _ QCheckBox(text)
        checkBox.c__.c..(self.updatePreview)
        return checkBox

    ___ createRadioButton(self, text):
        button _ QRadioButton(text)
        button.c__.c..(self.updatePreview)
        return button


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    controller _ ControllerWindow()
    controller.s..
    sys.exit(app.exec_())
