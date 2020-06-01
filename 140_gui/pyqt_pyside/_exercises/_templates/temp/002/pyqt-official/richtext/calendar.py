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
____ ?.?W.. ______ (?A.., QComboBox, QDateTimeEdit,
        QHBoxLayout, QLabel, QMainWindow, QSpinBox, QTextBrowser, QVBoxLayout,
        QWidget)


c_ MainWindow ?MW..
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.selectedDate _ QDate.currentDate()
        self.fontSize _ 10

        centralWidget _ ?W..

        dateLabel _ QLabel("Date:")
        monthCombo _ QComboBox()

        for month in range(1, 13):
            monthCombo.addItem(QDate.longMonthName(month))

        yearEdit _ QDateTimeEdit()
        yearEdit.setDisplayFormat('yyyy')
        yearEdit.setDateRange(QDate(1753, 1, 1), QDate(8000, 1, 1))

        monthCombo.setCurrentIndex(self.selectedDate.month() - 1)
        yearEdit.setDate(self.selectedDate)

        self.fontSizeLabel _ QLabel("Font size:")
        self.fontSizeSpinBox _ QSpinBox()
        self.fontSizeSpinBox.setRange(1, 64)
        self.fontSizeSpinBox.setValue(10)

        self.editor _ QTextBrowser()
        self.insertCalendar()

        monthCombo.activated.c..(self.setMonth)
        yearEdit.dateChanged.c..(self.setYear)
        self.fontSizeSpinBox.valueChanged.c..(self.setfontSize)

        controlsLayout _ QHBoxLayout()
        controlsLayout.aW..(dateLabel)
        controlsLayout.aW..(monthCombo)
        controlsLayout.aW..(yearEdit)
        controlsLayout.addSpacing(24)
        controlsLayout.aW..(self.fontSizeLabel)
        controlsLayout.aW..(self.fontSizeSpinBox)
        controlsLayout.addStretch(1)

        centralLayout _ ?VBL..
        centralLayout.addLayout(controlsLayout)
        centralLayout.aW..(self.editor, 1)
        centralWidget.sL..(centralLayout)

        self.sCW..(centralWidget)

    ___ insertCalendar(self):
        self.editor.clear()
        cursor _ self.editor.textCursor()
        cursor.beginEditBlock()

        date _ QDate(self.selectedDate.year(), self.selectedDate.month(), 1)

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
        format.setFontPointSize(self.fontSize)

        boldFormat _ QTextCharFormat(format)
        boldFormat.setFontWeight(QFont.Bold)

        highlightedFormat _ QTextCharFormat(boldFormat)
        highlightedFormat.setBackground(__.yellow)

        for weekDay in range(1, 8):
            cell _ table.cellAt(0, weekDay-1)
            cellCursor _ cell.firstCursorPosition()
            cellCursor.insertText(QDate.longDayName(weekDay), boldFormat)

        table.insertRows(table.rows(), 1)

        w__ date.month() == self.selectedDate.month
            weekDay _ date.dayOfWeek()
            cell _ table.cellAt(table.rows()-1, weekDay-1)
            cellCursor _ cell.firstCursorPosition()

            __ date == QDate.currentDate
                cellCursor.insertText(str(date.day()), highlightedFormat)
            ____
                cellCursor.insertText(str(date.day()), format)

            date _ date.addDays(1)

            __ weekDay == 7 and date.month() == self.selectedDate.month
                table.insertRows(table.rows(), 1)

        cursor.endEditBlock()

        self.setWindowTitle("Calendar for %s %d" % (QDate.longMonthName(self.selectedDate.month()), self.selectedDate.year()))

    ___ setfontSize  size):
        self.fontSize _ size
        self.insertCalendar()

    ___ setMonth  month):
        self.selectedDate _ QDate(self.selectedDate.year(), month + 1,
                self.selectedDate.day())
        self.insertCalendar()

    ___ setYear  date):
        self.selectedDate _ QDate(date.year(), self.selectedDate.month(),
                self.selectedDate.day())
        self.insertCalendar()


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ MainWindow()
    window.resize(640, 256)
    window.s..
    ___.exit(app.exec_())
