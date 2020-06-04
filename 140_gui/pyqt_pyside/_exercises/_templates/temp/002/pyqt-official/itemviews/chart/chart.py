#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited.
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

____ ?.?C.. ______ (QByteArray, QFile, QItemSelection,
        QItemSelectionModel, QModelIndex, QPoint, QRect, ?S.., __,
        QTextStream)
____ ?.?G.. ______ (?B.., ?C.., QFontMetrics, QPainter, QPainterPath,
        ?P.., ?P.., QRegion, ?SIM..)
____ ?.?W.. ______ (?AIV.., ?A.., ?FD..,
        ?MW.., ?M.., QRubberBand, ?S.., ?S.., QTableView)

______ chart_rc


c_ PieView(?AIV..):
    ___  -   parent_None):
        s__(PieView, self). - (parent)

        horizontalScrollBar().setRange(0, 0)
        verticalScrollBar().setRange(0, 0)

        margin _ 8
        totalSize _ 300
        pieSize _ totalSize - 2*margin
        validItems _ 0
        totalValue _ 0.0
        origin _ QPoint()
        rubberBand _ N..

    ___ dataChanged  topLeft, bottomRight, roles):
        s__(PieView, self).dataChanged(topLeft, bottomRight, roles)

        validItems _ 0
        totalValue _ 0.0

        ___ row __ ra..(model().rowCount(rootIndex())):

            index _ model().index(row, 1, rootIndex())
            value _ model().data(index)

            __ value __ no. N.. and value > 0.0:
                totalValue +_ value
                validItems +_ 1

        viewport().update()

    ___ edit  index, trigger, event):
        __ index.column() __ 0:
            r_ s__(PieView, self).edit(index, trigger, event)
        ____
            r_ F..

    ___ indexAt  point):
        __ validItems __ 0:
            r_ QModelIndex()

        # Transform the view coordinates into contents widget coordinates.
        wx _ point.x() + horizontalScrollBar().v..
        wy _ point.y() + verticalScrollBar().v..

        __ wx < totalSize:
            cx _ wx - totalSize/2
            cy _ totalSize/2 - wy; # positive cy for items above the center

            # Determine the distance from the center point of the pie chart.
            d _ (cx**2 + cy**2)**0.5

            __ d __ 0 or d > pieSize/2:
                r_ QModelIndex()

            # Determine the angle of the point.
            angle _ (180 / m__.pi) * m__.acos(cx/d)
            __ cy < 0:
                angle _ 360 - angle

            # Find the relevant slice of the pie.
            startAngle _ 0.0

            ___ row __ ra..(model().rowCount(rootIndex())):

                index _ model().index(row, 1, rootIndex())
                value _ model().data(index)

                __ value > 0.0:
                    sliceAngle _ 360*value/totalValue

                    __ angle >_ startAngle and angle < (startAngle + sliceAngle):
                        r_ model().index(row, 1, rootIndex())

                    startAngle +_ sliceAngle

        ____
            itemHeight _ QFontMetrics(viewOptions().font).height()
            listItem _ in.((wy - margin) / itemHeight)
            validRow _ 0

            ___ row __ ra..(model().rowCount(rootIndex())):

                index _ model().index(row, 1, rootIndex())
                __ model().data(index) > 0.0:

                    __ listItem __ validRow:
                        r_ model().index(row, 0, rootIndex())

                    # Update the list index that corresponds to the next valid
                    # row.
                    validRow +_ 1

        r_ QModelIndex()

    ___ isIndexHidden  index):
        r_ F..

    ___ itemRect  index):
        __ no. index.isValid
            r_ QRect()

        # Check whether the index's row is in the list of rows represented
        # by slices.

        __ index.column() !_ 1:
            valueIndex _ model().index(index.row(), 1, rootIndex())
        ____
            valueIndex _ index

        value _ model().data(valueIndex)
        __ value __ no. N.. and value > 0.0:

            listItem _ 0
            ___ row __ ra..(index.row()-1, -1, -1):
                __ model().data(model().index(row, 1, rootIndex())) > 0.0:
                    listItem +_ 1

            __ index.column() __ 0:
            
                itemHeight _ QFontMetrics(viewOptions().font).height()
                r_ QRect(totalSize,
                             in.(margin + listItem*itemHeight),
                             totalSize - margin, in.(itemHeight))
            ____ index.column() __ 1:
                r_ viewport().rect()

        r_ QRect()

    ___ itemRegion  index):
        __ no. index.isValid
            r_ QRegion()

        __ index.column() !_ 1:
            r_ QRegion(itemRect(index))

        __ model().data(index) <_ 0.0:
            r_ QRegion()

        startAngle _ 0.0
        ___ row __ ra..(model().rowCount(rootIndex())):

            sliceIndex _ model().index(row, 1, rootIndex())
            value _ model().data(sliceIndex)

            __ value > 0.0:
                angle _ 360*value/totalValue

                __ sliceIndex __ index:
                    slicePath _ QPainterPath()
                    slicePath.moveTo(totalSize/2, totalSize/2)
                    slicePath.arcTo(margin, margin,
                            margin+pieSize, margin+pieSize,
                            startAngle, angle)
                    slicePath.closeSubpath()

                    r_ QRegion(slicePath.toFillPolygon().toPolygon())

                startAngle +_ angle

        r_ QRegion()

    ___ horizontalOffset
        r_ horizontalScrollBar().v..

    ___ mousePressEvent  event):
        s__(PieView, self).mousePressEvent(event)

        origin _ event.pos()
        __ no. rubberBand:
            rubberBand _ QRubberBand(QRubberBand.Rectangle, self)
        rubberBand.setGeometry(QRect(origin, ?S..()))
        rubberBand.s..

    ___ mouseMoveEvent  event):
        __ rubberBand:
            rubberBand.setGeometry(QRect(origin, event.pos()).normalized())

        s__(PieView, self).mouseMoveEvent(event)

    ___ mouseReleaseEvent  event):
        s__(PieView, self).mouseReleaseEvent(event)

        __ rubberBand:
            rubberBand.hide()

        viewport().update()

    ___ moveCursor  cursorAction, modifiers):
        current _ currentIndex()

        __ cursorAction __ (?AIV...MoveLeft, ?AIV...MoveUp):

            __ current.row() > 0:
                current _ model().index(current.row() - 1,
                        current.column(), rootIndex())
            ____
                current _ model().index(0, current.column(),
                        rootIndex())

        ____ cursorAction __ (?AIV...MoveRight, ?AIV...MoveDown):

            __ current.row() < rows(current) - 1:
                current _ model().index(current.row() + 1,
                        current.column(), rootIndex())
            ____
                current _ model().index(rows(current) - 1,
                        current.column(), rootIndex())

        viewport().update()
        r_ current

    ___ paintEvent  event):
        selections _ selectionModel()
        option _ viewOptions()
        state _ option.state

        background _ option.palette.base()
        foreground _ ?P..(option.palette.color(?P...WindowText))
        textPen _ ?P..(option.palette.color(?P...Text))
        highlightedPen _ ?P..(option.palette.color(?P...HighlightedText))

        painter _ QPainter(viewport())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(event.rect(), background)
        painter.sP..(foreground)

        # Viewport rectangles
        pieRect _ QRect(margin, margin, pieSize,
                pieSize)
        keyPoint _ QPoint(totalSize - horizontalScrollBar().v..,
                margin - verticalScrollBar().value())

        __ validItems > 0:
            painter.save()
            painter.translate(pieRect.x() - horizontalScrollBar().v..,
                    pieRect.y() - verticalScrollBar().value())
            painter.drawEllipse(0, 0, pieSize, pieSize)
            startAngle _ 0.0

            ___ row __ ra..(model().rowCount(rootIndex())):

                index _ model().index(row, 1, rootIndex())
                value _ model().data(index)

                __ value > 0.0:
                    angle _ 360*value/totalValue

                    colorIndex _ model().index(row, 0, rootIndex())
                    color _ model().data(colorIndex, __.DecorationRole)

                    __ currentIndex() __ index:
                        painter.sB..(?B..(color, __.Dense4Pattern))
                    ____ selections.isSelected(index):
                        painter.sB..(?B..(color, __.Dense3Pattern))
                    ____
                        painter.sB..(?B..(color))

                    painter.drawPie(0, 0, pieSize, pieSize,
                            in.(startAngle*16), in.(angle*16))

                    startAngle +_ angle

            painter.restore()

            keyNumber _ 0

            ___ row __ ra..(model().rowCount(rootIndex())):
                index _ model().index(row, 1, rootIndex())
                value _ model().data(index)

                __ value > 0.0:
                    labelIndex _ model().index(row, 0, rootIndex())

                    option _ viewOptions()
                    option.rect _ visualRect(labelIndex)
                    __ selections.isSelected(labelIndex):
                        option.state |_ ?S...State_Selected
                    __ currentIndex() __ labelIndex:
                        option.state |_ ?S...State_HasFocus
                    itemDelegate().paint(painter, option, labelIndex)

                    keyNumber +_ 1

    ___ resizeEvent  event):
        updateGeometries()

    ___ rows  index):
        r_ model().rowCount(model().parent(index))

    ___ rowsInserted  parent, start, end):
        ___ row __ ra..(start, end + 1):
            index _ model().index(row, 1, rootIndex())
            value _ model().data(index)

            __ value __ no. N.. and value > 0.0:
                totalValue +_ value
                validItems +_ 1

        s__(PieView, self).rowsInserted(parent, start, end)

    ___ rowsAboutToBeRemoved  parent, start, end):
        ___ row __ ra..(start, end + 1):
            index _ model().index(row, 1, rootIndex())
            value _ model().data(index)

            __ value __ no. N.. and value > 0.0:
                totalValue -_ value
                validItems -_ 1

        s__(PieView, self).rowsAboutToBeRemoved(parent, start, end)

    ___ scrollContentsBy  dx, dy):
        viewport().scroll(dx, dy)

    ___ scrollTo  index, ScrollHint):
        area _ viewport().rect()
        rect _ visualRect(index)

        __ rect.left() < area.left
            horizontalScrollBar().sV..(
                horizontalScrollBar().v.. + rect.left() - area.left())
        ____ rect.right() > area.right
            horizontalScrollBar().sV..(
                horizontalScrollBar().v.. + min(
                    rect.right() - area.right(), rect.left() - area.left()))

        __ rect.top() < area.top
            verticalScrollBar().sV..(
                verticalScrollBar().v.. + rect.top() - area.top())
        ____ rect.bottom() > area.bottom
            verticalScrollBar().sV..(
                verticalScrollBar().v.. + min(
                    rect.bottom() - area.bottom(), rect.top() - area.top()))

    ___ setSelection  rect, command):
        # Use content widget coordinates because we will use the itemRegion()
        # function to check for intersections.

        contentsRect _ rect.translated(horizontalScrollBar().v..,
                verticalScrollBar().value()).normalized()

        rows _ model().rowCount(rootIndex())
        columns _ model().columnCount(rootIndex())
        indexes _   # list

        ___ row __ ra..(rows):
            ___ column __ ra..(columns):
                index _ model().index(row, column, rootIndex())
                region _ itemRegion(index)
                __ region.intersects(QRegion(contentsRect)):
                    indexes.ap..(index)

        __ le.(indexes) > 0:
            firstRow _ indexes[0].row()
            lastRow _ indexes[0].row()
            firstColumn _ indexes[0].column()
            lastColumn _ indexes[0].column()

            ___ i __ ra..(1, le.(indexes)):
                firstRow _ min(firstRow, indexes[i].row())
                lastRow _ max(lastRow, indexes[i].row())
                firstColumn _ min(firstColumn, indexes[i].column())
                lastColumn _ max(lastColumn, indexes[i].column())

            selection _ QItemSelection(
                model().index(firstRow, firstColumn, rootIndex()),
                model().index(lastRow, lastColumn, rootIndex()))
            selectionModel().select(selection, command)
        ____
            noIndex _ QModelIndex()
            selection _ QItemSelection(noIndex, noIndex)
            selectionModel().select(selection, command)

        update()

    ___ updateGeometries
        horizontalScrollBar().setPageStep(viewport().width())
        horizontalScrollBar().setRange(0, max(0, 2*totalSize - viewport().width()))
        verticalScrollBar().setPageStep(viewport().height())
        verticalScrollBar().setRange(0, max(0, totalSize - viewport().height()))

    ___ verticalOffset
        r_ verticalScrollBar().v..

    ___ visualRect  index):
        rect _ itemRect(index)
        __ rect.isValid
            r_ QRect(rect.left() - horizontalScrollBar().v..,
                         rect.top() - verticalScrollBar().v..,
                         rect.width(), rect.height())
        ____
            r_ rect

    ___ visualRegionForSelection  selection):
        region _ QRegion()

        ___ span __ selection:
            ___ row __ ra..(span.top(), span.bottom() + 1):
                ___ col __ ra..(span.left(), span.right() + 1):
                    index _ model().index(row, col, rootIndex())
                    region +_ visualRect(index)

        r_ region


c_ MainWindow ?MW..
    ___  - 
        s__(MainWindow, self). - ()

        fileMenu _ ?M..("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")
        saveAction _ fileMenu.aA..("&Save As...")
        saveAction.sS..("Ctrl+S")
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        setupModel()
        setupViews()

        openAction.t__.c..(openFile)
        saveAction.t__.c..(saveFile)
        quitAction.t__.c..(?A...i.. .quit)

        mB.. .aM..(fileMenu)
        sB..

        openFile(':/Charts/qtdata.cht')

        sWT..("Chart")
        r..(870, 550)

    ___ setupModel
        model _ ?SIM..(8, 2, self)
        model.setHeaderData(0, __.H.., "Label")
        model.setHeaderData(1, __.H.., "Quantity")

    ___ setupViews
        splitter _ ?S..()
        table _ ?TV..
        pieChart _ PieView()
        splitter.aW..(table)
        splitter.aW..(pieChart)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        table.sM..(model)
        pieChart.sM..(model)

        selectionModel _ QItemSelectionModel(model)
        table.setSelectionModel(selectionModel)
        pieChart.setSelectionModel(selectionModel)

        table.hH.. .setStretchLastSection( st.

        sCW..(splitter)

    ___ openFile  path_None):
        __ no. pa__:
            pa__, _ _ ?FD...gOFN..  "Choose a data file",
                    '', '*.cht')

        __ pa__:
            f _ QFile(pa__)

            __ f.o..(QFile.ReadOnly | QFile.Text):
                stream _ QTextStream(f)

                model.removeRows(0, model.rowCount(QModelIndex()),
                        QModelIndex())

                row _ 0
                line _ stream.readLine()
                w__ line:
                    model.insertRows(row, 1, QModelIndex())

                    pieces _ line.sp..(',')
                    model.setData(model.index(row, 0, QModelIndex()),
                                pieces[0])
                    model.setData(model.index(row, 1, QModelIndex()),
                                fl..(pieces[1]))
                    model.setData(model.index(row, 0, QModelIndex()),
                                ?C..(pieces[2]), __.DecorationRole)

                    row +_ 1
                    line _ stream.readLine()

                f.c..
                sB.. .sM..("Loaded %s" % pa__, 2000)

    ___ saveFile
        fileName, _ _ ?FD...getSaveFileName  "Save file as", '',
                '*.cht')

        __ fileName:
            f _ QFile(fileName)

            __ f.o..(QFile.WriteOnly | QFile.Text):
                ___ row __ ra..(model.rowCount(QModelIndex())):
                    pieces _   # list

                    pieces.ap..(
                            model.data(
                                    model.index(row, 0, QModelIndex()),
                                    __.DR..))
                    pieces.ap..(
                            '%g' % model.data(
                                    model.index(row, 1, QModelIndex()),
                                    __.DR..))
                    pieces.ap..(
                            model.data(
                                    model.index(row, 0, QModelIndex()),
                                    __.DecorationRole).name())

                    f.w..(b','.join([p.e..('utf-8') ___ p __ pieces]))
                    f.w..(b'\n')

            f.c..
            sB.. .sM..("Saved %s" % fileName, 2000)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
