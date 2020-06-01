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


____ ?.?C.. ______ QDate, __
____ ?.?G.. ______ (?C.., QFont, QTextCharFormat, QTextLength,
        QTextTableFormat)
____ ?.?W.. ______ (?A.., ?CB, ?DTE..,
        QHBoxLayout, QLabel, QMainWindow, SB.., QTextBrowser, QVBoxLayout,
        ?W..)


c_ MainWindow ?MW..
    ___  - 
        super(MainWindow, self). - ()

        selectedDate _ QDate.currentDate()
        fontSize _ 10

        centralWidget _ ?W..

        dateLabel _ QLabel("Date:")
        monthCombo _ ?CB()

        ___ month __ range(1, 13):
            monthCombo.aI..(QDate.longMonthName(month))

        yearEdit _ ?DTE..()
        yearEdit.setDisplayFormat('yyyy')
        yearEdit.setDateRange(QDate(1753, 1, 1), QDate(8000, 1, 1))

        monthCombo.setCurrentIndex(selectedDate.month() - 1)
        yearEdit.setDate(selectedDate)

        fontSizeLabel _ QLabel("Font size:")
        fontSizeSpinBox _ SB..()
        fontSizeSpinBox.setRange(1, 64)
        fontSizeSpinBox.setValue(10)

        editor _ QTextBrowser()
        insertCalendar()

        monthCombo.activated.c..(setMonth)
        yearEdit.dateChanged.c..(setYear)
        fontSizeSpinBox.valueChanged.c..(setfontSize)

        controlsLayout _ QHBoxLayout()
        controlsLayout.aW..(dateLabel)
        controlsLayout.aW..(monthCombo)
        controlsLayout.aW..(yearEdit)
        controlsLayout.addSpacing(24)
        controlsLayout.aW..(fontSizeLabel)
        controlsLayout.aW..(fontSizeSpinBox)
        controlsLayout.addStretch(1)

        centralLayout _ ?VBL..
        centralLayout.aL..(controlsLayout)
        centralLayout.aW..(editor, 1)
        centralWidget.sL..(centralLayout)

        sCW..(centralWidget)

    ___ insertCalendar
        editor.c..
        cursor _ editor.textCursor()
        cursor.beginEditBlock()

        date _ QDate(selectedDate.year(), selectedDate.month(), 1)

        tableFormat _ QTextTableFormat()
        tableFormat.setAlignment(__.AlignHCenter)
        tableFormat.setBackground(?C..('#e0e0e0'))
        tableFormat.setCellPadding(2)
        tableFormat.setCellSpacing(4)
        constraints _ [QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14)]

        tableFormat.setColumnWidthConstraints(constraints)

        table _ cursor.insertTable(1, 7, tableFormat)

        frame _ cursor.currentFrame()
        frameFormat _ frame.frameFormat()
        frameFormat.setBorder(1)
        frame.setFrameFormat(frameFormat)

        format _ cursor.charFormat()
        format.setFontPointSize(fontSize)

        boldFormat _ QTextCharFormat(format)
        boldFormat.setFontWeight(QFont.Bold)

        highlightedFormat _ QTextCharFormat(boldFormat)
        highlightedFormat.setBackground(__.yellow)

        ___ weekDay __ range(1, 8):
            cell _ table.cellAt(0, weekDay-1)
            cellCursor _ cell.firstCursorPosition()
            cellCursor.insertText(QDate.longDayName(weekDay), boldFormat)

        table.insertRows(table.rows(), 1)

        w__ date.month() __ selectedDate.month
            weekDay _ date.dayOfWeek()
            cell _ table.cellAt(table.rows()-1, weekDay-1)
            cellCursor _ cell.firstCursorPosition()

            __ date __ QDate.currentDate
                cellCursor.insertText(str(date.day()), highlightedFormat)
            ____
                cellCursor.insertText(str(date.day()), format)

            date _ date.addDays(1)

            __ weekDay __ 7 and date.month() __ selectedDate.month
                table.insertRows(table.rows(), 1)

        cursor.endEditBlock()

        sWT..("Calendar for %s %d" % (QDate.longMonthName(selectedDate.month()), selectedDate.year()))

    ___ setfontSize  size):
        fontSize _ size
        insertCalendar()

    ___ setMonth  month):
        selectedDate _ QDate(selectedDate.year(), month + 1,
                selectedDate.day())
        insertCalendar()

    ___ setYear  date):
        selectedDate _ QDate(date.year(), selectedDate.month(),
                selectedDate.day())
        insertCalendar()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.r..(640, 256)
    window.s..
    ___.e..(app.exec_())
