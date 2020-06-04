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


______ m__

____ ?.?C.. ______ pS.., QPointF, ?S.., __
____ ?.?G.. ______ QPainter, QPolygonF
____ ?.?W.. ______ (?AIV.., ?A.., ?S..,
        ?SID.., ?TW.., ?TWI.., ?W..)


c_ StarRating o..
    # enum EditMode
    Editable, ReadOnly _ ra..(2)

    PaintingScaleFactor _ 20

    ___  -   starCount_1, maxStarCount_5):
        _starCount _ starCount
        _maxStarCount _ maxStarCount

        starPolygon _ QPolygonF([QPointF(1.0, 0.5)])
        ___ i __ ra..(5):
            starPolygon << QPointF(0.5 + 0.5 * m__.cos(0.8 * i * m__.pi),
                                        0.5 + 0.5 * m__.sin(0.8 * i * m__.pi))

        diamondPolygon _ QPolygonF()
        diamondPolygon << QPointF(0.4, 0.5) \
                            << QPointF(0.5, 0.4) \
                            << QPointF(0.6, 0.5) \
                            << QPointF(0.5, 0.6) \
                            << QPointF(0.4, 0.5)

    ___ starCount
        r_ _starCount

    ___ maxStarCount
        r_ _maxStarCount

    ___ setStarCount  starCount):
        _starCount _ starCount

    ___ setMaxStarCount  maxStarCount):
        _maxStarCount _ maxStarCount

    ___ sH..
        r_ PaintingScaleFactor * ?S..(_maxStarCount, 1)

    ___ paint  painter, rect, palette, editMode):
        painter.save()

        painter.setRenderHint(QPainter.Antialiasing,  st.
        painter.sP..(__.NoPen)

        __ editMode __ StarRating.Editable:
            painter.sB..(palette.highlight())
        ____
            painter.sB..(palette.windowText())

        yOffset _ (rect.height() - PaintingScaleFactor) / 2
        painter.translate(rect.x(), rect.y() + yOffset)
        painter.scale(PaintingScaleFactor, PaintingScaleFactor)

        ___ i __ ra..(_maxStarCount):
            __ i < _starCount:
                painter.drawPolygon(starPolygon, __.WindingFill)
            ____ editMode __ StarRating.Editable:
                painter.drawPolygon(diamondPolygon, __.WindingFill)

            painter.translate(1.0, 0.0)

        painter.restore()


c_ StarEditor(?W..):

    eF__ _ pS..()

    ___  -   parent _ N..):
        s__(StarEditor, self). - (parent)

        _starRating _ StarRating()

        setMouseTracking( st.
        setAutoFillBackground( st.

    ___ setStarRating  starRating):
        _starRating _ starRating

    ___ starRating
        r_ _starRating

    ___ sH..
        r_ _starRating.sH..()

    ___ paintEvent  event):
        painter _ QPainter
        _starRating.paint(painter, rect(), p..,
                StarRating.Editable)

    ___ mouseMoveEvent  event):
        star _ starAtPosition(event.x())

        __ star !_ _starRating.starCount() and star !_ -1:
            _starRating.setStarCount(star)
            update()

    ___ mouseReleaseEvent  event):
        eF__.e..()

    ___ starAtPosition  x):
        # Enable a star, if pointer crosses the center horizontally.
        starwidth _ _starRating.sH..().width() // _starRating.maxStarCount()
        star _ (x + starwidth / 2) // starwidth
        __ 0 <_ star <_ _starRating.maxStarCount
            r_ star

        r_ -1


c_ StarDelegate(?SID..):
    ___ paint  painter, option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            __ option.state & ?S...State_Selected:
                painter.fillRect(option.rect, option.palette.highlight())

            starRating.paint(painter, option.rect, option.palette,
                    StarRating.ReadOnly)
        ____
            s__(StarDelegate, self).paint(painter, option, index)

    ___ sH..  option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            r_ starRating.sH..()
        ____
            r_ s__(StarDelegate, self).sH..(option, index)

    ___ createEditor  parent, option, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            editor _ StarEditor(parent)
            editor.eF__.c..(commitAndCloseEditor)
            r_ editor
        ____
            r_ s__(StarDelegate, self).createEditor(parent, option, index)

    ___ setEditorData  editor, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            editor.setStarRating(starRating)
        ____
            s__(StarDelegate, self).setEditorData(editor, index)

    ___ setModelData  editor, model, index):
        starRating _ index.data()
        __ isinstance(starRating, StarRating):
            model.setData(index, editor.starRating())
        ____
            s__(StarDelegate, self).setModelData(editor, model, index)

    ___ commitAndCloseEditor
        editor _ sender()
        commitData.e..(editor)
        closeEditor.e..(editor)


___ populateTableWidget(tableWidget):
    staticData _ (
        ("Mass in B-Minor", "Baroque", "J.S. Bach", 5),
        ("Three More Foxes", "Jazz", "Maynard Ferguson", 4),
        ("Sex Bomb", "Pop", "Tom Jones", 3),
        ("Barbie Girl", "Pop", "Aqua", 5),
    )

    ___ row, (title, genre, artist, rating) __ en..(staticData):
        item0 _ ?TWI..(title)
        item1 _ ?TWI..(genre)
        item2 _ ?TWI..(artist)
        item3 _ ?TWI..()
        item3.setData(0, StarRating(rating))
        tableWidget.setItem(row, 0, item0)
        tableWidget.setItem(row, 1, item1)
        tableWidget.setItem(row, 2, item2)
        tableWidget.setItem(row, 3, item3)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    tableWidget _ ?TW..(4, 4)
    tableWidget.sID..(StarDelegate())
    tableWidget.setEditTriggers(
            ?AIV...DoubleClicked | ?AIV...SelectedClicked)
    tableWidget.setSelectionBehavior(?AIV...SelectRows)

    headerLabels _ ("Title", "Genre", "Artist", "Rating")
    tableWidget.sHHL..(headerLabels)

    populateTableWidget(tableWidget)

    tableWidget.rCTC..
    tableWidget.r..(500, 300)
    tableWidget.s..

    ___.e.. ?.e..
