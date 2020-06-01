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

____ ?.QtCore ______ pyqtSignal, QSize, Qt
____ ?.QtGui ______ (QClipboard, QFont, QFontDatabase, QFontMetrics,
        QPainter)
____ ?.?W.. ______ (QApplication, QCheckBox, QComboBox, QFontComboBox,
        QHBoxLayout, QLabel, QLineEdit, QMainWindow, ?PB.., QScrollArea,
        QToolTip, QVBoxLayout, QWidget)


class CharacterWidget(QWidget):

    characterSelected _ pyqtSignal(str)

    ___ __init__(self, parent_None):
        super(CharacterWidget, self).__init__(parent)

        self.displayFont _ QFont()
        self.squareSize _ 24
        self.columns _ 16
        self.lastKey _ -1
        self.setMouseTracking(True)

    ___ updateFont(self, fontFamily):
        self.displayFont.setFamily(fontFamily)
        self.squareSize _ max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update()

    ___ updateSize(self, fontSize):
        fontSize, _ _ fontSize.toInt()
        self.displayFont.setPointSize(fontSize)
        self.squareSize _ max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update() 

    ___ updateStyle(self, fontStyle):
        fontDatabase _ QFontDatabase()
        oldStrategy _ self.displayFont.styleStrategy()
        self.displayFont _ fontDatabase.font(self.displayFont.family(),
                fontStyle, self.displayFont.pointSize())
        self.displayFont.setStyleStrategy(oldStrategy)
        self.squareSize _ max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update()

    ___ updateFontMerging(self, enable):
        if enable:
            self.displayFont.setStyleStrategy(QFont.PreferDefault)
        else:
            self.displayFont.setStyleStrategy(QFont.NoFontMerging)
        self.adjustSize()
        self.update()

    ___ sizeHint(self):
        return QSize(self.columns * self.squareSize,
                (65536 / self.columns) * self.squareSize)

    ___ mouseMoveEvent(self, event):
        widgetPosition _ self.mapFromGlobal(event.globalPos())
        key _ (widgetPosition.y() // self.squareSize) * self.columns + widgetPosition.x() // self.squareSize

        text _ '<p>Character: <span style="font-size: 24pt; font-family: %s">%s</span><p>Value: 0x%x' % (self.displayFont.family(), self._chr(key), key)
        QToolTip.showText(event.globalPos(), text, self)

    ___ mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastKey _ (event.y() // self.squareSize) * self.columns + event.x() // self.squareSize
            key_ch _ self._chr(self.lastKey)

            if unicodedata.category(key_ch) !_ 'Cn':
                self.characterSelected.emit(key_ch)
            self.update()
        else:
            super(CharacterWidget, self).mousePressEvent(event)

    ___ paintEvent(self, event):
        painter _ QPainter(self)
        painter.fillRect(event.rect(), Qt.white)
        painter.setFont(self.displayFont)

        redrawRect _ event.rect()
        beginRow _ redrawRect.top() // self.squareSize
        endRow _ redrawRect.bottom() // self.squareSize
        beginColumn _ redrawRect.left() // self.squareSize
        endColumn _ redrawRect.right() // self.squareSize

        painter.setPen(Qt.gray)
        for row in range(beginRow, endRow + 1):
            for column in range(beginColumn, endColumn + 1):
                painter.drawRect(column * self.squareSize,
                        row * self.squareSize, self.squareSize,
                        self.squareSize)

        fontMetrics _ QFontMetrics(self.displayFont)
        painter.setPen(Qt.black)
        for row in range(beginRow, endRow + 1):
            for column in range(beginColumn, endColumn + 1):
                key _ row * self.columns + column
                painter.setClipRect(column * self.squareSize,
                        row * self.squareSize, self.squareSize,
                        self.squareSize)

                if key == self.lastKey:
                    painter.fillRect(column * self.squareSize + 1,
                            row * self.squareSize + 1, self.squareSize,
                            self.squareSize, Qt.red)

                key_ch _ self._chr(key)
                painter.drawText(column * self.squareSize + (self.squareSize / 2) - fontMetrics.width(key_ch) / 2,
                        row * self.squareSize + 4 + fontMetrics.ascent(),
                        key_ch)

    @staticmethod
    ___ _chr(codepoint):
        try:
            # Python v2.
            return unichr(codepoint)
        except NameError:
            # Python v3.
            return chr(codepoint)


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        centralWidget _ QWidget()

        fontLabel _ QLabel("Font:")
        self.fontCombo _ QFontComboBox()
        sizeLabel _ QLabel("Size:")
        self.sizeCombo _ QComboBox()
        styleLabel _ QLabel("Style:")
        self.styleCombo _ QComboBox()
        fontMergingLabel _ QLabel("Automatic Font Merging:")
        self.fontMerging _ QCheckBox()
        self.fontMerging.setChecked(True)

        self.scrollArea _ QScrollArea()
        self.characterWidget _ CharacterWidget()
        self.scrollArea.setWidget(self.characterWidget)

        self.findStyles(self.fontCombo.currentFont())
        self.findSizes(self.fontCombo.currentFont())

        self.lineEdit _ QLineEdit()
        clipboardButton _ ?PB..("&To clipboard")

        self.clipboard _ QApplication.clipboard()

        self.fontCombo.currentFontChanged.c..(self.findStyles)
        self.fontCombo.activated[str].c..(self.characterWidget.updateFont)
        self.styleCombo.activated[str].c..(self.characterWidget.updateStyle)
        self.sizeCombo.currentIndexChanged[str].c..(self.characterWidget.updateSize)
        self.characterWidget.characterSelected.c..(self.insertCharacter)
        clipboardButton.c__.c..(self.updateClipboard)

        controlsLayout _ QHBoxLayout()
        controlsLayout.addWidget(fontLabel)
        controlsLayout.addWidget(self.fontCombo, 1)
        controlsLayout.addWidget(sizeLabel)
        controlsLayout.addWidget(self.sizeCombo, 1)
        controlsLayout.addWidget(styleLabel)
        controlsLayout.addWidget(self.styleCombo, 1)
        controlsLayout.addWidget(fontMergingLabel)
        controlsLayout.addWidget(self.fontMerging, 1)
        controlsLayout.addStretch(1)

        lineLayout _ QHBoxLayout()
        lineLayout.addWidget(self.lineEdit, 1)
        lineLayout.addSpacing(12)
        lineLayout.addWidget(clipboardButton)

        centralLayout _ QVBoxLayout()
        centralLayout.addLayout(controlsLayout)
        centralLayout.addWidget(self.scrollArea, 1)
        centralLayout.addSpacing(4)
        centralLayout.addLayout(lineLayout)
        centralWidget.setLayout(centralLayout)

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Character Map")

    ___ findStyles(self, font):
        fontDatabase _ QFontDatabase()
        currentItem _ self.styleCombo.currentText()
        self.styleCombo.clear()

        for style in fontDatabase.styles(font.family()):
            self.styleCombo.addItem(style)

        styleIndex _ self.styleCombo.findText(currentItem)
        if styleIndex == -1:
            self.styleCombo.setCurrentIndex(0)
        else:
            self.styleCombo.setCurrentIndex(styleIndex)

    ___ findSizes(self, font):
        fontDatabase _ QFontDatabase()
        currentSize _ self.sizeCombo.currentText()
        self.sizeCombo.blockSignals(True)
        self.sizeCombo.clear()

        if fontDatabase.isSmoothlyScalable(font.family(), fontDatabase.styleString(font)):
            for size in QFontDatabase.standardSizes
                self.sizeCombo.addItem(str(size))
                self.sizeCombo.setEditable(True)
        else:
            for size in fontDatabase.smoothSizes(font.family(), fontDatabase.styleString(font)):
                self.sizeCombo.addItem(str(size))
                self.sizeCombo.setEditable(False)

        self.sizeCombo.blockSignals(False)

        sizeIndex _ self.sizeCombo.findText(currentSize)
        if sizeIndex == -1:
            self.sizeCombo.setCurrentIndex(max(0, self.sizeCombo.count() / 3))
        else:
            self.sizeCombo.setCurrentIndex(sizeIndex)

    ___ insertCharacter(self, character):
        self.lineEdit.insert(character)

    ___ updateClipboard(self):
        self.clipboard.sT..(self.lineEdit.text(), QClipboard.Clipboard)
        self.clipboard.sT..(self.lineEdit.text(), QClipboard.Selection)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
