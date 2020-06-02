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


____ ?.?C.. ______ ?D.., __, QTimer
____ ?.?G.. ______ ?P..
____ ?.?W.. ______ (?A.., QCheckBox, ?FD.., QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, ?PB.., QSizePolicy, SB..,
        QVBoxLayout, ?W..)


c_ Screenshot(?W..):
    ___  -
        super(Screenshot, self). - ()

        screenshotLabel _ QLabel()
        screenshotLabel.sSP..(QSizePolicy.E..,
                QSizePolicy.E..)
        screenshotLabel.setAlignment(__.AlignCenter)
        screenshotLabel.sMS..(240, 160)

        createOptionsGroupBox()
        createButtonsLayout()

        mainLayout _ ?VBL..
        mainLayout.aW..(screenshotLabel)
        mainLayout.aW..(optionsGroupBox)
        mainLayout.aL..(buttonsLayout)
        sL..(mainLayout)

        shootScreen()
        delaySpinBox.setValue(5)

        sWT..("Screenshot")
        r..(300, 200)

    ___ resizeEvent  event):
        scaledSize _ originalPixmap.size()
        scaledSize.scale(screenshotLabel.size(), __.KeepAspectRatio)
        __ no. screenshotLabel.pixmap() or scaledSize !_ screenshotLabel.pixmap().size
            updateScreenshotLabel()

    ___ newScreenshot
        __ hideThisWindowCheckBox.isChecked
            hide()
        newScreenshotButton.sD..( st.

        QTimer.singleShot(delaySpinBox.value() * 1000,
                shootScreen)

    ___ saveScreenshot
        format _ 'png'
        initialPath _ ?D...currentPath() + "/untitled." + format

        fileName, _ _ ?FD...getSaveFileName  "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        __ fileName:
            originalPixmap.save(fileName, format)

    ___ shootScreen
        __ delaySpinBox.value() !_ 0:
            ?A...instance().beep()

        screen _ ?A...primaryScreen()
        __ screen __ no. N..:
            originalPixmap _ screen.grabWindow(0)
        ____
            originalPixmap _ ?P..()

        updateScreenshotLabel()

        newScreenshotButton.sD.. F..
        __ hideThisWindowCheckBox.isChecked
            s..

    ___ updateCheckBox
        __ delaySpinBox.value() __ 0:
            hideThisWindowCheckBox.sD..( st.
        ____
            hideThisWindowCheckBox.sD.. F..

    ___ createOptionsGroupBox
        optionsGroupBox _ QGroupBox("Options")

        delaySpinBox _ SB..()
        delaySpinBox.setSuffix(" s")
        delaySpinBox.sM..(60)
        delaySpinBox.valueChanged.c..(updateCheckBox)

        delaySpinBoxLabel _ QLabel("Screenshot Delay:")

        hideThisWindowCheckBox _ QCheckBox("Hide This Window")

        optionsGroupBoxLayout _ QGridLayout()
        optionsGroupBoxLayout.aW..(delaySpinBoxLabel, 0, 0)
        optionsGroupBoxLayout.aW..(delaySpinBox, 0, 1)
        optionsGroupBoxLayout.aW..(hideThisWindowCheckBox, 1, 0, 1, 2)
        optionsGroupBox.sL..(optionsGroupBoxLayout)

    ___ createButtonsLayout
        newScreenshotButton _ createButton("New Screenshot",
                newScreenshot)

        saveScreenshotButton _ createButton("Save Screenshot",
                saveScreenshot)

        quitScreenshotButton _ createButton("Quit", close)

        buttonsLayout _ QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.aW..(newScreenshotButton)
        buttonsLayout.aW..(saveScreenshotButton)
        buttonsLayout.aW..(quitScreenshotButton)

    ___ createButton  t__, member):
        button _ ?PB..(t__)
        button.c__.c..(member)
        r_ button

    ___ updateScreenshotLabel
        screenshotLabel.setPixmap(originalPixmap.scaled(
                screenshotLabel.size(), __.KeepAspectRatio,
                __.SmoothTransformation))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    screenshot _ Screenshot()
    screenshot.s..
    ___.e.. ?.exec_())
