#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2015 Riverbank Computing Limited
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
###########################################################################


____ ?.?C.. ______ ?D.., QLocale, __
____ ?.?G.. ______ ?F.., QTextCharFormat
____ ?.?W.. ______ (?A.., QCalendarWidget, QCheckBox,
        ?CB, ?DE.., QGridLayout, ?GB.., ?HBL.., ?L..,
        QLayout, ?W..)


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        createPreviewGroupBox()
        createGeneralOptionsGroupBox()
        createDatesGroupBox()
        createTextFormatsGroupBox()

        layout _ QGridLayout()
        layout.aW..(previewGroupBox, 0, 0)
        layout.aW..(generalOptionsGroupBox, 0, 1)
        layout.aW..(datesGroupBox, 1, 0)
        layout.aW..(textFormatsGroupBox, 1, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        sL..(layout)

        previewLayout.setRowMinimumHeight(0,
                calendar.sH..().height())
        previewLayout.setColumnMinimumWidth(0,
                calendar.sH..().width())

        sWT..("Calendar Widget")

    ___ localeChanged  index):
        calendar.setLocale(localeCombo.itemData(index))

    ___ firstDayChanged  index):
        calendar.setFirstDayOfWeek(
                __.DayOfWeek(firstDayCombo.itemData(index)))

    ___ selectionModeChanged  index):
        calendar.setSelectionMode(
                QCalendarWidget.SelectionMode(
                        selectionModeCombo.itemData(index)))

    ___ horizontalHeaderChanged  index):
        calendar.setHorizontalHeaderFormat(
                QCalendarWidget.HorizontalHeaderFormat(
                        horizontalHeaderCombo.itemData(index)))

    ___ verticalHeaderChanged  index):
        calendar.setVerticalHeaderFormat(
                QCalendarWidget.VerticalHeaderFormat(
                        verticalHeaderCombo.itemData(index)))

    ___ selectedDateChanged
        currentDateEdit.setDate(calendar.selectedDate())

    ___ minimumDateChanged  date):
        calendar.setMinimumDate(date)
        maximumDateEdit.setDate(calendar.maximumDate())

    ___ maximumDateChanged  date):
        calendar.setMaximumDate(date)
        minimumDateEdit.setDate(calendar.minimumDate())

    ___ weekdayFormatChanged
        f.. _ QTextCharFormat()
        f...setForeground(
                __.GlobalColor(
                        weekdayColorCombo.itemData(
                                weekdayColorCombo.currentIndex())))

        calendar.setWeekdayTextFormat(__.Monday, f..)
        calendar.setWeekdayTextFormat(__.Tuesday, f..)
        calendar.setWeekdayTextFormat(__.Wednesday, f..)
        calendar.setWeekdayTextFormat(__.Thursday, f..)
        calendar.setWeekdayTextFormat(__.Friday, f..)

    ___ weekendFormatChanged
        f.. _ QTextCharFormat()
        f...setForeground(
                __.GlobalColor(
                        weekendColorCombo.itemData(
                                weekendColorCombo.currentIndex())))

        calendar.setWeekdayTextFormat(__.Saturday, f..)
        calendar.setWeekdayTextFormat(__.Sunday, f..)

    ___ reformatHeaders
        t__ _ headerTextFormatCombo.currentText()
        f.. _ QTextCharFormat()

        __ t__ __ "Bold":
            f...setFontWeight(?F...Bold)
        ____ t__ __ "Italic":
            f...setFontItalic( st.
        ____ t__ __ "Green":
            f...setForeground(__.green)

        calendar.setHeaderTextFormat(f..)

    ___ reformatCalendarPage
        __ firstFridayCheckBox.isChecked
            firstFriday _ ?D..(calendar.yearShown(),
                    calendar.monthShown(), 1)

            w__ firstFriday.dayOfWeek() !_ __.Friday:
                firstFriday _ firstFriday.addDays(1)

            firstFridayFormat _ QTextCharFormat()
            firstFridayFormat.setForeground(__.blue)

            calendar.setDateTextFormat(firstFriday, firstFridayFormat)

        # May 1st in Red takes precedence.
        __ mayFirstCheckBox.isChecked
            mayFirst _ ?D..(calendar.yearShown(), 5, 1)

            mayFirstFormat _ QTextCharFormat()
            mayFirstFormat.setForeground(__.red)

            calendar.setDateTextFormat(mayFirst, mayFirstFormat)

    ___ createPreviewGroupBox
        previewGroupBox _ ?GB..("Preview")

        calendar _ QCalendarWidget()
        calendar.setMinimumDate(?D..(1900, 1, 1))
        calendar.setMaximumDate(?D..(3000, 1, 1))
        calendar.setGridVisible( st.
        calendar.currentPageChanged.c..(reformatCalendarPage)

        previewLayout _ QGridLayout()
        previewLayout.aW..(calendar, 0, 0, __.AlignCenter)
        previewGroupBox.sL..(previewLayout)
 
    ___ createGeneralOptionsGroupBox
        generalOptionsGroupBox _ ?GB..("General Options")

        localeCombo _ ?CB()

        curLocaleIndex _ -1
        index _ 0

        this_language _ locale().nativeLanguageName()
        this_country _ locale().nativeCountryName()

        ___ locale __ QLocale.matchingLocales(QLocale.AnyLanguage, QLocale.AnyScript, QLocale.AnyCountry):
            language _ locale.nativeLanguageName()
            country _ locale.nativeCountryName()

            __ language __ this_language and country __ this_country:
                curLocaleIndex _ index

            localeCombo.aI..('%s/%s' % (language, country), locale)
            index +_ 1

        __ curLocaleIndex !_ -1:
            localeCombo.sCI..(curLocaleIndex)

        localeLabel _ ?L..("&Locale")
        localeLabel.setBuddy(localeCombo)

        firstDayCombo _ ?CB()
        firstDayCombo.aI..("Sunday", __.Sunday)
        firstDayCombo.aI..("Monday", __.Monday)
        firstDayCombo.aI..("Tuesday", __.Tuesday)
        firstDayCombo.aI..("Wednesday", __.Wednesday)
        firstDayCombo.aI..("Thursday", __.Thursday)
        firstDayCombo.aI..("Friday", __.Friday)
        firstDayCombo.aI..("Saturday", __.Saturday)

        firstDayLabel _ ?L..("Wee&k starts on:")
        firstDayLabel.setBuddy(firstDayCombo)

        selectionModeCombo _ ?CB()
        selectionModeCombo.aI..("Single selection",
                QCalendarWidget.SingleSelection)
        selectionModeCombo.aI..("None",
                QCalendarWidget.NoSelection)
        selectionModeLabel _ ?L..("&Selection mode:")
        selectionModeLabel.setBuddy(selectionModeCombo)

        gridCheckBox _ QCheckBox("&Grid")
        gridCheckBox.sC__(calendar.isGridVisible())

        navigationCheckBox _ QCheckBox("&Navigation bar")
        navigationCheckBox.sC__( st.

        horizontalHeaderCombo _ ?CB()
        horizontalHeaderCombo.aI..("Single letter day names",
                QCalendarWidget.SingleLetterDayNames)
        horizontalHeaderCombo.aI..("Short day names",
                QCalendarWidget.ShortDayNames)
        horizontalHeaderCombo.aI..("Long day names",
                QCalendarWidget.LongDayNames)
        horizontalHeaderCombo.aI..("None",
                QCalendarWidget.NoHorizontalHeader)
        horizontalHeaderCombo.sCI..(1)

        horizontalHeaderLabel _ ?L..("&Horizontal header:")
        horizontalHeaderLabel.setBuddy(horizontalHeaderCombo)

        verticalHeaderCombo _ ?CB()
        verticalHeaderCombo.aI..("ISO week numbers",
                QCalendarWidget.ISOWeekNumbers)
        verticalHeaderCombo.aI..("None",
                QCalendarWidget.NoVerticalHeader)

        verticalHeaderLabel _ ?L..("&Vertical header:")
        verticalHeaderLabel.setBuddy(verticalHeaderCombo)

        localeCombo.currentIndexChanged.c..(localeChanged)
        firstDayCombo.currentIndexChanged.c..(firstDayChanged)
        selectionModeCombo.currentIndexChanged.c..(
                selectionModeChanged)
        gridCheckBox.t__.c..(calendar.setGridVisible)
        navigationCheckBox.t__.c..(
                calendar.setNavigationBarVisible)
        horizontalHeaderCombo.currentIndexChanged.c..(
                horizontalHeaderChanged)
        verticalHeaderCombo.currentIndexChanged.c..(
                verticalHeaderChanged)

        checkBoxLayout _ ?HBL..
        checkBoxLayout.aW..(gridCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.aW..(navigationCheckBox)

        outerLayout _ QGridLayout()
        outerLayout.aW..(localeLabel, 0, 0)
        outerLayout.aW..(localeCombo, 0, 1)
        outerLayout.aW..(firstDayLabel, 1, 0)
        outerLayout.aW..(firstDayCombo, 1, 1)
        outerLayout.aW..(selectionModeLabel, 2, 0)
        outerLayout.aW..(selectionModeCombo, 2, 1)
        outerLayout.aL..(checkBoxLayout, 3, 0, 1, 2)
        outerLayout.aW..(horizontalHeaderLabel, 4, 0)
        outerLayout.aW..(horizontalHeaderCombo, 4, 1)
        outerLayout.aW..(verticalHeaderLabel, 5, 0)
        outerLayout.aW..(verticalHeaderCombo, 5, 1)
        generalOptionsGroupBox.sL..(outerLayout)

        firstDayChanged(firstDayCombo.cI..
        selectionModeChanged(selectionModeCombo.cI..
        horizontalHeaderChanged(horizontalHeaderCombo.cI..
        verticalHeaderChanged(verticalHeaderCombo.cI..
 
    ___ createDatesGroupBox
        datesGroupBox _ ?GB..(tr("Dates"))

        minimumDateEdit _ ?DE..()
        minimumDateEdit.setDisplayFormat('MMM d yyyy')
        minimumDateEdit.setDateRange(calendar.minimumDate(),
                                          calendar.maximumDate())
        minimumDateEdit.setDate(calendar.minimumDate())

        minimumDateLabel _ ?L..("&Minimum Date:")
        minimumDateLabel.setBuddy(minimumDateEdit)

        currentDateEdit _ ?DE..()
        currentDateEdit.setDisplayFormat('MMM d yyyy')
        currentDateEdit.setDate(calendar.selectedDate())
        currentDateEdit.setDateRange(calendar.minimumDate(),
                calendar.maximumDate())

        currentDateLabel _ ?L..("&Current Date:")
        currentDateLabel.setBuddy(currentDateEdit)

        maximumDateEdit _ ?DE..()
        maximumDateEdit.setDisplayFormat('MMM d yyyy')
        maximumDateEdit.setDateRange(calendar.minimumDate(),
                calendar.maximumDate())
        maximumDateEdit.setDate(calendar.maximumDate())

        maximumDateLabel _ ?L..("Ma&ximum Date:")
        maximumDateLabel.setBuddy(maximumDateEdit)

        currentDateEdit.dateChanged.c..(calendar.setSelectedDate)
        calendar.sC__.c..(selectedDateChanged)
        minimumDateEdit.dateChanged.c..(minimumDateChanged)
        maximumDateEdit.dateChanged.c..(maximumDateChanged)
 
        dateBoxLayout _ QGridLayout()
        dateBoxLayout.aW..(currentDateLabel, 1, 0)
        dateBoxLayout.aW..(currentDateEdit, 1, 1)
        dateBoxLayout.aW..(minimumDateLabel, 0, 0)
        dateBoxLayout.aW..(minimumDateEdit, 0, 1)
        dateBoxLayout.aW..(maximumDateLabel, 2, 0)
        dateBoxLayout.aW..(maximumDateEdit, 2, 1)
        dateBoxLayout.setRowStretch(3, 1)

        datesGroupBox.sL..(dateBoxLayout)

    ___ createTextFormatsGroupBox
        textFormatsGroupBox _ ?GB..("Text Formats")

        weekdayColorCombo _ createColorComboBox()
        weekdayColorCombo.sCI..(
                weekdayColorCombo.findText("Black"))

        weekdayColorLabel _ ?L..("&Weekday color:")
        weekdayColorLabel.setBuddy(weekdayColorCombo)

        weekendColorCombo _ createColorComboBox()
        weekendColorCombo.sCI..(
                weekendColorCombo.findText("Red"))

        weekendColorLabel _ ?L..("Week&end color:")
        weekendColorLabel.setBuddy(weekendColorCombo)

        headerTextFormatCombo _ ?CB()
        headerTextFormatCombo.aI..("Bold")
        headerTextFormatCombo.aI..("Italic")
        headerTextFormatCombo.aI..("Plain")

        headerTextFormatLabel _ ?L..("&Header text:")
        headerTextFormatLabel.setBuddy(headerTextFormatCombo)

        firstFridayCheckBox _ QCheckBox("&First Friday in blue")

        mayFirstCheckBox _ QCheckBox("May &1 in red")

        weekdayColorCombo.currentIndexChanged.c..(
                weekdayFormatChanged)
        weekendColorCombo.currentIndexChanged.c..(
                weekendFormatChanged)
        headerTextFormatCombo.currentIndexChanged.c..(
                reformatHeaders)
        firstFridayCheckBox.t__.c..(reformatCalendarPage)
        mayFirstCheckBox.t__.c..(reformatCalendarPage)

        checkBoxLayout _ ?HBL..
        checkBoxLayout.aW..(firstFridayCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.aW..(mayFirstCheckBox)

        outerLayout _ QGridLayout()
        outerLayout.aW..(weekdayColorLabel, 0, 0)
        outerLayout.aW..(weekdayColorCombo, 0, 1)
        outerLayout.aW..(weekendColorLabel, 1, 0)
        outerLayout.aW..(weekendColorCombo, 1, 1)
        outerLayout.aW..(headerTextFormatLabel, 2, 0)
        outerLayout.aW..(headerTextFormatCombo, 2, 1)
        outerLayout.aL..(checkBoxLayout, 3, 0, 1, 2)
        textFormatsGroupBox.sL..(outerLayout)

        weekdayFormatChanged()
        weekendFormatChanged()

        reformatHeaders()
        reformatCalendarPage()
 
    ___ createColorComboBox
        comboBox _ ?CB()
        comboBox.aI..("Red", __.red)
        comboBox.aI..("Blue", __.blue)
        comboBox.aI..("Black", __.black)
        comboBox.aI..("Magenta", __.magenta)

        r_ comboBox


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ Window()
    window.s..

    ___.e.. ?.e..
