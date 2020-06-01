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


____ ?.QtCore ______ QDir, Qt, QTimer
____ ?.QtGui ______ QPixmap
____ ?.?W.. ______ (QApplication, QCheckBox, QFileDialog, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, ?PB.., QSizePolicy, QSpinBox,
        QVBoxLayout, QWidget)


class Screenshot(QWidget):
    ___ __init__(self):
        super(Screenshot, self).__init__()

        self.screenshotLabel _ QLabel()
        self.screenshotLabel.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        self.screenshotLabel.setAlignment(Qt.AlignCenter)
        self.screenshotLabel.setMinimumSize(240, 160)

        self.createOptionsGroupBox()
        self.createButtonsLayout()

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.screenshotLabel)
        mainLayout.addWidget(self.optionsGroupBox)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)

        self.shootScreen()
        self.delaySpinBox.setValue(5)

        self.setWindowTitle("Screenshot")
        self.resize(300, 200)

    ___ resizeEvent(self, event):
        scaledSize _ self.originalPixmap.size()
        scaledSize.scale(self.screenshotLabel.size(), Qt.KeepAspectRatio)
        if not self.screenshotLabel.pixmap() or scaledSize !_ self.screenshotLabel.pixmap().size
            self.updateScreenshotLabel()

    ___ newScreenshot(self):
        if self.hideThisWindowCheckBox.isChecked
            self.hide()
        self.newScreenshotButton.setDisabled(True)

        QTimer.singleShot(self.delaySpinBox.value() * 1000,
                self.shootScreen)

    ___ saveScreenshot(self):
        format _ 'png'
        initialPath _ QDir.currentPath() + "/untitled." + format

        fileName, _ _ QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if fileName:
            self.originalPixmap.save(fileName, format)

    ___ shootScreen(self):
        if self.delaySpinBox.value() !_ 0:
            QApplication.instance().beep()

        screen _ QApplication.primaryScreen()
        if screen is not None:
            self.originalPixmap _ screen.grabWindow(0)
        else:
            self.originalPixmap _ QPixmap()

        self.updateScreenshotLabel()

        self.newScreenshotButton.setDisabled(False)
        if self.hideThisWindowCheckBox.isChecked
            self.s..

    ___ updateCheckBox(self):
        if self.delaySpinBox.value() == 0:
            self.hideThisWindowCheckBox.setDisabled(True)
        else:
            self.hideThisWindowCheckBox.setDisabled(False)

    ___ createOptionsGroupBox(self):
        self.optionsGroupBox _ QGroupBox("Options")

        self.delaySpinBox _ QSpinBox()
        self.delaySpinBox.setSuffix(" s")
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.valueChanged.c..(self.updateCheckBox)

        self.delaySpinBoxLabel _ QLabel("Screenshot Delay:")

        self.hideThisWindowCheckBox _ QCheckBox("Hide This Window")

        optionsGroupBoxLayout _ QGridLayout()
        optionsGroupBoxLayout.addWidget(self.delaySpinBoxLabel, 0, 0)
        optionsGroupBoxLayout.addWidget(self.delaySpinBox, 0, 1)
        optionsGroupBoxLayout.addWidget(self.hideThisWindowCheckBox, 1, 0, 1, 2)
        self.optionsGroupBox.setLayout(optionsGroupBoxLayout)

    ___ createButtonsLayout(self):
        self.newScreenshotButton _ self.createButton("New Screenshot",
                self.newScreenshot)

        self.saveScreenshotButton _ self.createButton("Save Screenshot",
                self.saveScreenshot)

        self.quitScreenshotButton _ self.createButton("Quit", self.close)

        self.buttonsLayout _ QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.newScreenshotButton)
        self.buttonsLayout.addWidget(self.saveScreenshotButton)
        self.buttonsLayout.addWidget(self.quitScreenshotButton)

    ___ createButton(self, text, member):
        button _ ?PB..(text)
        button.c__.c..(member)
        return button

    ___ updateScreenshotLabel(self):
        self.screenshotLabel.setPixmap(self.originalPixmap.scaled(
                self.screenshotLabel.size(), Qt.KeepAspectRatio,
                Qt.SmoothTransformation))


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    screenshot _ Screenshot()
    screenshot.s..
    sys.exit(app.exec_())
