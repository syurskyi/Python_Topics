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


____ ?.?C.. ______ QDir, __, QTimer
____ ?.?G.. ______ QPixmap
____ ?.?W.. ______ (?A.., QCheckBox, ?FD.., QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, ?PB.., QSizePolicy, QSpinBox,
        QVBoxLayout, QWidget)


c_ Screenshot(QWidget):
    ___ __init__(self):
        super(Screenshot, self).__init__()

        self.screenshotLabel _ QLabel()
        self.screenshotLabel.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        self.screenshotLabel.setAlignment(__.AlignCenter)
        self.screenshotLabel.setMinimumSize(240, 160)

        self.createOptionsGroupBox()
        self.createButtonsLayout()

        mainLayout _ ?VBL..
        mainLayout.aW..(self.screenshotLabel)
        mainLayout.aW..(self.optionsGroupBox)
        mainLayout.addLayout(self.buttonsLayout)
        self.sL..(mainLayout)

        self.shootScreen()
        self.delaySpinBox.setValue(5)

        self.setWindowTitle("Screenshot")
        self.resize(300, 200)

    ___ resizeEvent  event):
        scaledSize _ self.originalPixmap.size()
        scaledSize.scale(self.screenshotLabel.size(), __.KeepAspectRatio)
        __ no. self.screenshotLabel.pixmap() or scaledSize !_ self.screenshotLabel.pixmap().size
            self.updateScreenshotLabel()

    ___ newScreenshot(self):
        __ self.hideThisWindowCheckBox.isChecked
            self.hide()
        self.newScreenshotButton.setDisabled(True)

        QTimer.singleShot(self.delaySpinBox.value() * 1000,
                self.shootScreen)

    ___ saveScreenshot(self):
        format _ 'png'
        initialPath _ QDir.currentPath() + "/untitled." + format

        fileName, _ _ ?FD...getSaveFileName  "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        __ fileName:
            self.originalPixmap.save(fileName, format)

    ___ shootScreen(self):
        __ self.delaySpinBox.value() !_ 0:
            ?A...instance().beep()

        screen _ ?A...primaryScreen()
        __ screen __ no. N..:
            self.originalPixmap _ screen.grabWindow(0)
        ____
            self.originalPixmap _ QPixmap()

        self.updateScreenshotLabel()

        self.newScreenshotButton.setDisabled F..
        __ self.hideThisWindowCheckBox.isChecked
            self.s..

    ___ updateCheckBox(self):
        __ self.delaySpinBox.value() == 0:
            self.hideThisWindowCheckBox.setDisabled(True)
        ____
            self.hideThisWindowCheckBox.setDisabled F..

    ___ createOptionsGroupBox(self):
        self.optionsGroupBox _ QGroupBox("Options")

        self.delaySpinBox _ QSpinBox()
        self.delaySpinBox.setSuffix(" s")
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.valueChanged.c..(self.updateCheckBox)

        self.delaySpinBoxLabel _ QLabel("Screenshot Delay:")

        self.hideThisWindowCheckBox _ QCheckBox("Hide This Window")

        optionsGroupBoxLayout _ QGridLayout()
        optionsGroupBoxLayout.aW..(self.delaySpinBoxLabel, 0, 0)
        optionsGroupBoxLayout.aW..(self.delaySpinBox, 0, 1)
        optionsGroupBoxLayout.aW..(self.hideThisWindowCheckBox, 1, 0, 1, 2)
        self.optionsGroupBox.sL..(optionsGroupBoxLayout)

    ___ createButtonsLayout(self):
        self.newScreenshotButton _ self.createButton("New Screenshot",
                self.newScreenshot)

        self.saveScreenshotButton _ self.createButton("Save Screenshot",
                self.saveScreenshot)

        self.quitScreenshotButton _ self.createButton("Quit", self.close)

        self.buttonsLayout _ QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.aW..(self.newScreenshotButton)
        self.buttonsLayout.aW..(self.saveScreenshotButton)
        self.buttonsLayout.aW..(self.quitScreenshotButton)

    ___ createButton  t__, member):
        button _ ?PB..(t__)
        button.c__.c..(member)
        r_ button

    ___ updateScreenshotLabel(self):
        self.screenshotLabel.setPixmap(self.originalPixmap.scaled(
                self.screenshotLabel.size(), __.KeepAspectRatio,
                __.SmoothTransformation))


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    screenshot _ Screenshot()
    screenshot.s..
    sys.exit(app.exec_())
