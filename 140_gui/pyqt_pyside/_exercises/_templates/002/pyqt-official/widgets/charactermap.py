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


______ unicodedata

____ ?.?C.. ______ pS.., ?S.., __
____ ?.?G.. ______ (QClipboard, ?F.., QFontDatabase, QFontMetrics,
        QPainter)
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, QFontComboBox,
        ?HBL.., ?L.., QLineEdit, ?MW.., ?PB.., QScrollArea,
        QToolTip, ?VBL.., ?W..)


c_ CharacterWidget(?W..):

    characterSelected _ pS.. st.

    ___  -   parent_None):
        s__(CharacterWidget, self). - (parent)

        displayFont _ ?F..()
        squareSize _ 24
        columns _ 16
        lastKey _ -1
        setMouseTracking( st.

    ___ updateFont  fontFamily):
        displayFont.sF..(fontFamily)
        squareSize _ max(24, QFontMetrics(displayFont).xHeight() * 3)
        adjustSize()
        update()

    ___ updateSize  fontSize):
        fontSize, _ _ fontSize.toInt()
        displayFont.sPS..(fontSize)
        squareSize _ max(24, QFontMetrics(displayFont).xHeight() * 3)
        adjustSize()
        update()

    ___ updateStyle  fontStyle):
        fontDatabase _ QFontDatabase()
        oldStrategy _ displayFont.styleStrategy()
        displayFont _ fontDatabase.font(displayFont.family(),
                fontStyle, displayFont.pointSize())
        displayFont.setStyleStrategy(oldStrategy)
        squareSize _ max(24, QFontMetrics(displayFont).xHeight() * 3)
        adjustSize()
        update()

    ___ updateFontMerging  enable):
        __ enable:
            displayFont.setStyleStrategy(?F...PreferDefault)
        ____
            displayFont.setStyleStrategy(?F...NoFontMerging)
        adjustSize()
        update()

    ___ sH..
        r_ ?S..(columns * squareSize,
                (65536 / columns) * squareSize)

    ___ mouseMoveEvent  event):
        widgetPosition _ mapFromGlobal(event.globalPos())
        key _ (widgetPosition.y() // squareSize) * columns + widgetPosition.x() // squareSize

        t__ _ '<p>Character: <span style="font-size: 24pt; font-family: %s">%s</span><p>Value: 0x%x' % (displayFont.family(), _chr(key), key)
        QToolTip.showText(event.globalPos(), t__, self)

    ___ mousePressEvent  event):
        __ event.button() __ __.LeftButton:
            lastKey _ (event.y() // squareSize) * columns + event.x() // squareSize
            key_ch _ _chr(lastKey)

            __ unicodedata.category(key_ch) !_ 'Cn':
                characterSelected.e..(key_ch)
            update()
        ____
            s__(CharacterWidget, self).mousePressEvent(event)

    ___ paintEvent  event):
        painter _ QPainter
        painter.fillRect(event.rect(), __.white)
        painter.sF..(displayFont)

        redrawRect _ event.rect()
        beginRow _ redrawRect.top() // squareSize
        endRow _ redrawRect.bottom() // squareSize
        beginColumn _ redrawRect.left() // squareSize
        endColumn _ redrawRect.right() // squareSize

        painter.sP..(__.gray)
        ___ row __ ra..(beginRow, endRow + 1):
            ___ column __ ra..(beginColumn, endColumn + 1):
                painter.drawRect(column * squareSize,
                        row * squareSize, squareSize,
                        squareSize)

        fontMetrics _ QFontMetrics(displayFont)
        painter.sP..(__.black)
        ___ row __ ra..(beginRow, endRow + 1):
            ___ column __ ra..(beginColumn, endColumn + 1):
                key _ row * columns + column
                painter.setClipRect(column * squareSize,
                        row * squareSize, squareSize,
                        squareSize)

                __ key __ lastKey:
                    painter.fillRect(column * squareSize + 1,
                            row * squareSize + 1, squareSize,
                            squareSize, __.red)

                key_ch _ _chr(key)
                painter.drawText(column * squareSize + (squareSize / 2) - fontMetrics.width(key_ch) / 2,
                        row * squareSize + 4 + fontMetrics.ascent(),
                        key_ch)

    @staticmethod
    ___ _chr(codepoint):
        ___
            # Python v2.
            r_ unichr(codepoint)
        _____ NameError:
            # Python v3.
            r_ chr(codepoint)


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        centralWidget _ ?W..

        fontLabel _ ?L..("Font:")
        fontCombo _ QFontComboBox()
        sizeLabel _ ?L..("Size:")
        sizeCombo _ ?CB()
        styleLabel _ ?L..("Style:")
        styleCombo _ ?CB()
        fontMergingLabel _ ?L..("Automatic Font Merging:")
        fontMerging _ QCheckBox()
        fontMerging.sC__( st.

        scrollArea _ QScrollArea()
        characterWidget _ CharacterWidget()
        scrollArea.setWidget(characterWidget)

        findStyles(fontCombo.currentFont())
        findSizes(fontCombo.currentFont())

        lineEdit _ ?LE..
        clipboardButton _ ?PB..("&To clipboard")

        clipboard _ ?A...clipboard()

        fontCombo.currentFontChanged.c..(findStyles)
        fontCombo.activated[st.].c..(characterWidget.updateFont)
        styleCombo.activated[st.].c..(characterWidget.updateStyle)
        sizeCombo.currentIndexChanged[st.].c..(characterWidget.updateSize)
        characterWidget.characterSelected.c..(insertCharacter)
        clipboardButton.c__.c..(updateClipboard)

        controlsLayout _ ?HBL..
        controlsLayout.aW..(fontLabel)
        controlsLayout.aW..(fontCombo, 1)
        controlsLayout.aW..(sizeLabel)
        controlsLayout.aW..(sizeCombo, 1)
        controlsLayout.aW..(styleLabel)
        controlsLayout.aW..(styleCombo, 1)
        controlsLayout.aW..(fontMergingLabel)
        controlsLayout.aW..(fontMerging, 1)
        controlsLayout.addStretch(1)

        lineLayout _ ?HBL..
        lineLayout.aW..(lineEdit, 1)
        lineLayout.addSpacing(12)
        lineLayout.aW..(clipboardButton)

        centralLayout _ ?VBL..
        centralLayout.aL..(controlsLayout)
        centralLayout.aW..(scrollArea, 1)
        centralLayout.addSpacing(4)
        centralLayout.aL..(lineLayout)
        centralWidget.sL..(centralLayout)

        sCW..(centralWidget)
        sWT..("Character Map")

    ___ findStyles  font):
        fontDatabase _ QFontDatabase()
        currentItem _ styleCombo.currentText()
        styleCombo.c..

        ___ style __ fontDatabase.styles(font.family()):
            styleCombo.aI..(style)

        styleIndex _ styleCombo.findText(currentItem)
        __ styleIndex __ -1:
            styleCombo.sCI..(0)
        ____
            styleCombo.sCI..(styleIndex)

    ___ findSizes  font):
        fontDatabase _ QFontDatabase()
        currentSize _ sizeCombo.currentText()
        sizeCombo.blockSignals( st.
        sizeCombo.c..

        __ fontDatabase.isSmoothlyScalable(font.family(), fontDatabase.styleString(font)):
            ___ size __ QFontDatabase.standardSizes
                sizeCombo.aI..(st.(size))
                sizeCombo.sE..( st.
        ____
            ___ size __ fontDatabase.smoothSizes(font.family(), fontDatabase.styleString(font)):
                sizeCombo.aI..(st.(size))
                sizeCombo.sE.. F..

        sizeCombo.blockSignals F..

        sizeIndex _ sizeCombo.findText(currentSize)
        __ sizeIndex __ -1:
            sizeCombo.sCI..(max(0, sizeCombo.count() / 3))
        ____
            sizeCombo.sCI..(sizeIndex)

    ___ insertCharacter  character):
        lineEdit.insert(character)

    ___ updateClipboard 
        clipboard.sT..(lineEdit.t__(), QClipboard.Clipboard)
        clipboard.sT..(lineEdit.t__(), QClipboard.Selection)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
