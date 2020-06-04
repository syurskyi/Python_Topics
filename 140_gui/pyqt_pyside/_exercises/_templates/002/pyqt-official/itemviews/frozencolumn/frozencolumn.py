#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2017 Hans-Peter Jansen <hpj@urpla.net>
## Copyright (C) 2016 The Qt Company Ltd.
##
## This file is part of the examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https:#www.qt.io/terms-conditions. For further
## information use the contact form at https:#www.qt.io/contact-us.
##
## BSD License Usage
## Alternatively, you may use self file under the terms of the BSD license
## as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, self list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, self list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from self software without specific prior written permission.
##
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
##
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ QFile, QFileInfo, __
____ ?.?G.. ______ ?SI.., ?SIM..
____ ?.?W.. ______ ?A.., ?HV.., QTableView


c_ FreezeTableWidget(QTableView):
    ___  -   model):
        s__(FreezeTableWidget, self). - ()
        sM..(model)
        frozenTableView _ QTableView
        init()
        hH.. .sectionResized.c..(updateSectionWidth)
        vH.. .sectionResized.c..(updateSectionHeight)
        frozenTableView.verticalScrollBar().valueChanged.c..(
            verticalScrollBar().sV..)
        verticalScrollBar().valueChanged.c..(
            frozenTableView.verticalScrollBar().sV..)

    ___ init
        frozenTableView.sM..(model())
        frozenTableView.sFP..(__.NF..)
        frozenTableView.vH.. .hide()
        frozenTableView.hH.. .sSRM..(
                ?HV...Fixed)
        viewport().stackUnder(frozenTableView)

        frozenTableView.sSS..('''
            QTableView { border: none;
                         background-color: #8EDE21;
                         selection-background-color: #999;
            }''') # for demo purposes

        frozenTableView.setSelectionModel(selectionModel())
        ___ col __ ra..(1, model().columnCount()):
            frozenTableView.setColumnHidden(col,  st.
        frozenTableView.setColumnWidth(0, columnWidth(0))
        frozenTableView.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        frozenTableView.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        frozenTableView.s..
        updateFrozenTableGeometry()
        setHorizontalScrollMode(ScrollPerPixel)
        setVerticalScrollMode(ScrollPerPixel)
        frozenTableView.setVerticalScrollMode(ScrollPerPixel)

    ___ updateSectionWidth  logicalIndex, oldSize, newSize):
        __ logicalIndex __ 0:
            frozenTableView.setColumnWidth(0, newSize)
            updateFrozenTableGeometry()

    ___ updateSectionHeight  logicalIndex, oldSize, newSize):
        frozenTableView.setRowHeight(logicalIndex, newSize)

    ___ resizeEvent  event):
        s__(FreezeTableWidget, self).resizeEvent(event)
        updateFrozenTableGeometry()

    ___ moveCursor  cursorAction, modifiers):
        current _ s__(FreezeTableWidget, self).moveCursor(cursorAction, modifiers)
        __ (cursorAction __ MoveLeft and
                current.column() > 0 and
                visualRect(current).topLeft().x() <
                    frozenTableView.columnWidth(0)):
            newValue _ (horizontalScrollBar().v.. +
                        visualRect(current).topLeft().x() -
                        frozenTableView.columnWidth(0))
            horizontalScrollBar().sV..(newValue)
        r_ current

    ___ scrollTo  index, hint):
        __ index.column() > 0:
            s__(FreezeTableWidget, self).scrollTo(index, hint)

    ___ updateFrozenTableGeometry
        frozenTableView.setGeometry(
                vH.. .width() + frameWidth(),
                frameWidth(), columnWidth(0),
                viewport().height() + hH.. .height())


___ main(args):
    ___ split_and_strip(s, splitter):
        r_ [s.s.. ___ s __ line.sp..(splitter)]

    app _ ?A..(args)
    model _ ?SIM..()
    file _ QFile(QFileInfo(__file__).absolutePath() + '/grades.txt')
    __ file.o..(QFile.ReadOnly):
        line _ file.readLine(200).d..('utf-8')
        header _ split_and_strip(line, ',')
        model.sHHL..(header)
        row _ 0
        w__ file.canReadLine
            line _ file.readLine(200).d..('utf-8')
            __ no. line.s_w_('#') and ',' __ line:
                fields _ split_and_strip(line, ',')
                ___ col, field __ en..(fields):
                    newItem _ ?SI..(field)
                    model.setItem(row, col, newItem)
                row +_ 1
    file.c..
    tableView _ FreezeTableWidget(model)
    tableView.sWT..("Frozen Column Example")
    tableView.r..(560, 680)
    tableView.s..
    r_ app.e..


__ ______ __ ______
    ______ ___
    main(___.a..
