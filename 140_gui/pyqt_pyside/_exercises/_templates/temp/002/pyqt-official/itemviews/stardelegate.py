#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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


______ math

____ ?.?C.. ______ pyqtSignal, QPointF, QSize, __
____ ?.?G.. ______ QPainter, QPolygonF
____ ?.?W.. ______ (QAbstractItemView, ?A.., QStyle,
        QStyledItemDelegate, QTableWidget, QTableWidgetItem, QWidget)


c_ StarRating(object):
    # enum EditMode
    Editable, ReadOnly _ range(2)

    PaintingScaleFactor _ 20

    ___ __init__  starCount_1, maxStarCount_5):
        self._starCount _ starCount
        self._maxStarCount _ maxStarCount

        self.starPolygon _ QPolygonF([QPointF(1.0, 0.5)])
        for i in range(5):
            self.starPolygon << QPointF(0.5 + 0.5 * math.cos(0.8 * i * math.pi),
                                        0.5 + 0.5 * math.sin(0.8 * i * math.pi))

        self.diamondPolygon _ QPolygonF()
        self.diamondPolygon << QPointF(0.4, 0.5) \
                            << QPointF(0.5, 0.4) \
                            << QPointF(0.6, 0.5) \
                            << QPointF(0.5, 0.6) \
                            << QPointF(0.4, 0.5)

    ___ starCount(self):
        r_ self._starCount

    ___ maxStarCount(self):
        r_ self._maxStarCount

    ___ setStarCount  starCount):
        self._starCount _ starCount

    ___ setMaxStarCount  maxStarCount):
        self._maxStarCount _ maxStarCount

    ___ sizeHint(self):
        r_ self.PaintingScaleFactor * QSize(self._maxStarCount, 1)

    ___ paint  painter, rect, palette, editMode):
        painter.save()

        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(__.NoPen)

        __ editMode == StarRating.Editable:
            painter.setBrush(palette.highlight())
        ____
            painter.setBrush(palette.windowText())

        yOffset _ (rect.height() - self.PaintingScaleFactor) / 2
        painter.translate(rect.x(), rect.y() + yOffset)
        painter.scale(self.PaintingScaleFactor, self.PaintingScaleFactor)

        for i in range(self._maxStarCount):
            __ i < self._starCount:
                painter.drawPolygon(self.starPolygon, __.WindingFill)
            ____ editMode == StarRating.Editable:
                painter.drawPolygon(self.diamondPolygon, __.WindingFill)

            painter.translate(1.0, 0.0)

        painter.restore()


c_ StarEditor(QWidget):

    editingFinished _ pyqtSignal()

    ___ __init__  parent _ N..):
        super(StarEditor, self).__init__(parent)

        self._starRating _ StarRating()

        self.setMouseTracking(True)
        self.setAutoFillBackground(True)

    ___ setStarRating  starRating):
        self._starRating _ starRating

    ___ starRating(self):
        r_ self._starRating

    ___ sizeHint(self):
        r_ self._starRating.sizeHint()

    ___ paintEvent  event):
        painter _ QPainter(self)
        self._starRating.paint(painter, self.rect(), self.palette(),
                StarRating.Editable)

    ___ mouseMoveEvent  event):
        star _ self.starAtPosition(event.x())

        __ star !_ self._starRating.starCount() and star !_ -1:
            self._starRating.setStarCount(star)
            self.update()

    ___ mouseReleaseEvent  event):
        self.editingFinished.emit()

    ___ starAtPosition  x):
        # Enable a star, if pointer crosses the center horizontally.
        starwidth _ self._starRating.sizeHint().width() // self._starRating.maxStarCount()
        star _ (x + starwidth / 2) // starwidth
        __ 0 <_ star <_ self._starRating.maxStarCount
            r_ star

        r_ -1


c_ StarDelegate(QStyledItemDelegate):
    ___ paint  painter, option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            __ option.state & QStyle.State_Selected:
                painter.fillRect(option.rect, option.palette.highlight())

            starRating.paint(painter, option.rect, option.palette,
                    StarRating.ReadOnly)
        ____
            super(StarDelegate, self).paint(painter, option, index)

    ___ sizeHint  option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            r_ starRating.sizeHint()
        ____
            r_ super(StarDelegate, self).sizeHint(option, index)

    ___ createEditor  parent, option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            editor _ StarEditor(parent)
            editor.editingFinished.c..(self.commitAndCloseEditor)
            r_ editor
        ____
            r_ super(StarDelegate, self).createEditor(parent, option, index)

    ___ setEditorData  editor, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            editor.setStarRating(starRating)
        ____
            super(StarDelegate, self).setEditorData(editor, index)

    ___ setModelData  editor, model, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            model.setData(index, editor.starRating())
        ____
            super(StarDelegate, self).setModelData(editor, model, index)

    ___ commitAndCloseEditor(self):
        editor _ self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)


___ populateTableWidget(tableWidget):
    staticData _ (
        ("Mass in B-Minor", "Baroque", "J.S. Bach", 5),
        ("Three More Foxes", "Jazz", "Maynard Ferguson", 4),
        ("Sex Bomb", "Pop", "Tom Jones", 3),
        ("Barbie Girl", "Pop", "Aqua", 5),
    )

    for row, (title, genre, artist, rating) in enumerate(staticData):
        item0 _ QTableWidgetItem(title)
        item1 _ QTableWidgetItem(genre)
        item2 _ QTableWidgetItem(artist)
        item3 _ QTableWidgetItem()
        item3.setData(0, StarRating(rating))
        tableWidget.setItem(row, 0, item0)
        tableWidget.setItem(row, 1, item1)
        tableWidget.setItem(row, 2, item2)
        tableWidget.setItem(row, 3, item3)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    tableWidget _ QTableWidget(4, 4)
    tableWidget.setItemDelegate(StarDelegate())
    tableWidget.setEditTriggers(
            QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
    tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    headerLabels _ ("Title", "Genre", "Artist", "Rating")
    tableWidget.setHorizontalHeaderLabels(headerLabels)

    populateTableWidget(tableWidget)

    tableWidget.resizeColumnsToContents()
    tableWidget.resize(500, 300)
    tableWidget.s..

    sys.exit(app.exec_())
