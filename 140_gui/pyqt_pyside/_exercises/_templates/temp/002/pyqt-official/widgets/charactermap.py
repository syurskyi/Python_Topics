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

____ ?.?C.. ______ pyqtSignal, QSize, __
____ ?.?G.. ______ (QClipboard, QFont, QFontDatabase, QFontMetrics,
        QPainter)
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QFontComboBox,
        QHBoxLayout, QLabel, QLineEdit, QMainWindow, ?PB.., QScrollArea,
        QToolTip, QVBoxLayout, QWidget)


c_ CharacterWidget(QWidget):

    characterSelected _ pyqtSignal(str)

    ___  -   parent_None):
        super(CharacterWidget, self). - (parent)

        displayFont _ QFont()
        squareSize _ 24
        columns _ 16
        lastKey _ -1
        setMouseTracking(True)

    ___ updateFont  fontFamily):
        displayFont.setFamily(fontFamily)
        squareSize _ max(24, QFontMetrics(displayFont).xHeight() * 3)
        adjustSize()
        update()

    ___ updateSize  fontSize):
        fontSize, _ _ fontSize.toInt()
        displayFont.setPointSize(fontSize)
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
            displayFont.setStyleStrategy(QFont.PreferDefault)
        ____
            displayFont.setStyleStrategy(QFont.NoFontMerging)
        adjustSize()
        update()

    ___ sizeHint 
        r_ QSize(columns * squareSize,
                (65536 / columns) * squareSize)

    ___ mouseMoveEvent  event):
        widgetPosition _ mapFromGlobal(event.globalPos())
        key _ (widgetPosition.y() // squareSize) * columns + widgetPosition.x() // squareSize

        t__ _ '<p>Character: <span style="font-size: 24pt; font-family: %s">%s</span><p>Value: 0x%x' % (displayFont.family(), _chr(key), key)
        QToolTip.showText(event.globalPos(), t__, self)

    ___ mousePressEvent  event):
        __ event.button() == __.LeftButton:
            lastKey _ (event.y() // squareSize) * columns + event.x() // squareSize
            key_ch _ _chr(lastKey)

            __ unicodedata.category(key_ch) !_ 'Cn':
                characterSelected.emit(key_ch)
            update()
        ____
            super(CharacterWidget, self).mousePressEvent(event)

    ___ paintEvent  event):
        painter _ QPainter
        painter.fillRect(event.rect(), __.white)
        painter.setFont(displayFont)

        redrawRect _ event.rect()
        beginRow _ redrawRect.top() // squareSize
        endRow _ redrawRect.bottom() // squareSize
        beginColumn _ redrawRect.left() // squareSize
        endColumn _ redrawRect.right() // squareSize

        painter.setPen(__.gray)
        ___ row __ range(beginRow, endRow + 1):
            ___ column __ range(beginColumn, endColumn + 1):
                painter.drawRect(column * squareSize,
                        row * squareSize, squareSize,
                        squareSize)

        fontMetrics _ QFontMetrics(displayFont)
        painter.setPen(__.black)
        ___ row __ range(beginRow, endRow + 1):
            ___ column __ range(beginColumn, endColumn + 1):
                key _ row * columns + column
                painter.setClipRect(column * squareSize,
                        row * squareSize, squareSize,
                        squareSize)

                __ key == lastKey:
                    painter.fillRect(column * squareSize + 1,
                            row * squareSize + 1, squareSize,
                            squareSize, __.red)

                key_ch _ _chr(key)
                painter.drawText(column * squareSize + (squareSize / 2) - fontMetrics.width(key_ch) / 2,
                        row * squareSize + 4 + fontMetrics.ascent(),
                        key_ch)

    @staticmethod
    ___ _chr(codepoint):
        try:
            # Python v2.
            r_ unichr(codepoint)
        except NameError:
            # Python v3.
            r_ chr(codepoint)


c_ MainWindow ?MW..
    ___  -
        super(MainWindow, self). - ()

        centralWidget _ ?W..

        fontLabel _ QLabel("Font:")
        fontCombo _ QFontComboBox()
        sizeLabel _ QLabel("Size:")
        sizeCombo _ QComboBox()
        styleLabel _ QLabel("Style:")
        styleCombo _ QComboBox()
        fontMergingLabel _ QLabel("Automatic Font Merging:")
        fontMerging _ QCheckBox()
        fontMerging.setChecked(True)

        scrollArea _ QScrollArea()
        characterWidget _ CharacterWidget()
        scrollArea.setWidget(characterWidget)

        findStyles(fontCombo.currentFont())
        findSizes(fontCombo.currentFont())

        lineEdit _ ?LE..
        clipboardButton _ ?PB..("&To clipboard")

        clipboard _ ?A...clipboard()

        fontCombo.currentFontChanged.c..(findStyles)
        fontCombo.activated[str].c..(characterWidget.updateFont)
        styleCombo.activated[str].c..(characterWidget.updateStyle)
        sizeCombo.currentIndexChanged[str].c..(characterWidget.updateSize)
        characterWidget.characterSelected.c..(insertCharacter)
        clipboardButton.c__.c..(updateClipboard)

        controlsLayout _ QHBoxLayout()
        controlsLayout.aW..(fontLabel)
        controlsLayout.aW..(fontCombo, 1)
        controlsLayout.aW..(sizeLabel)
        controlsLayout.aW..(sizeCombo, 1)
        controlsLayout.aW..(styleLabel)
        controlsLayout.aW..(styleCombo, 1)
        controlsLayout.aW..(fontMergingLabel)
        controlsLayout.aW..(fontMerging, 1)
        controlsLayout.addStretch(1)

        lineLayout _ QHBoxLayout()
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
        setWindowTitle("Character Map")

    ___ findStyles  font):
        fontDatabase _ QFontDatabase()
        currentItem _ styleCombo.currentText()
        styleCombo.clear()

        ___ style __ fontDatabase.styles(font.family()):
            styleCombo.addItem(style)

        styleIndex _ styleCombo.findText(currentItem)
        __ styleIndex == -1:
            styleCombo.setCurrentIndex(0)
        ____
            styleCombo.setCurrentIndex(styleIndex)

    ___ findSizes  font):
        fontDatabase _ QFontDatabase()
        currentSize _ sizeCombo.currentText()
        sizeCombo.blockSignals(True)
        sizeCombo.clear()

        __ fontDatabase.isSmoothlyScalable(font.family(), fontDatabase.styleString(font)):
            ___ size __ QFontDatabase.standardSizes
                sizeCombo.addItem(str(size))
                sizeCombo.setEditable(True)
        ____
            ___ size __ fontDatabase.smoothSizes(font.family(), fontDatabase.styleString(font)):
                sizeCombo.addItem(str(size))
                sizeCombo.setEditable F..

        sizeCombo.blockSignals F..

        sizeIndex _ sizeCombo.findText(currentSize)
        __ sizeIndex == -1:
            sizeCombo.setCurrentIndex(max(0, sizeCombo.count() / 3))
        ____
            sizeCombo.setCurrentIndex(sizeIndex)

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
    ___.exit(app.exec_())
