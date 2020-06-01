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


____ ?.?C.. ______ QDate, QLocale, __
____ ?.?G.. ______ QFont, QTextCharFormat
____ ?.?W.. ______ (?A.., QCalendarWidget, QCheckBox,
        QComboBox, QDateEdit, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
        QLayout, QWidget)


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.createPreviewGroupBox()
        self.createGeneralOptionsGroupBox()
        self.createDatesGroupBox()
        self.createTextFormatsGroupBox()

        layout _ QGridLayout()
        layout.aW..(self.previewGroupBox, 0, 0)
        layout.aW..(self.generalOptionsGroupBox, 0, 1)
        layout.aW..(self.datesGroupBox, 1, 0)
        layout.aW..(self.textFormatsGroupBox, 1, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.sL..(layout)

        self.previewLayout.setRowMinimumHeight(0,
                self.calendar.sizeHint().height())
        self.previewLayout.setColumnMinimumWidth(0,
                self.calendar.sizeHint().width())

        self.setWindowTitle("Calendar Widget")

    ___ localeChanged  index):
        self.calendar.setLocale(self.localeCombo.itemData(index))

    ___ firstDayChanged  index):
        self.calendar.setFirstDayOfWeek(
                __.DayOfWeek(self.firstDayCombo.itemData(index)))

    ___ selectionModeChanged  index):
        self.calendar.setSelectionMode(
                QCalendarWidget.SelectionMode(
                        self.selectionModeCombo.itemData(index)))

    ___ horizontalHeaderChanged  index):
        self.calendar.setHorizontalHeaderFormat(
                QCalendarWidget.HorizontalHeaderFormat(
                        self.horizontalHeaderCombo.itemData(index)))

    ___ verticalHeaderChanged  index):
        self.calendar.setVerticalHeaderFormat(
                QCalendarWidget.VerticalHeaderFormat(
                        self.verticalHeaderCombo.itemData(index)))

    ___ selectedDateChanged(self):
        self.currentDateEdit.setDate(self.calendar.selectedDate())

    ___ minimumDateChanged  date):
        self.calendar.setMinimumDate(date)
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

    ___ maximumDateChanged  date):
        self.calendar.setMaximumDate(date)
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

    ___ weekdayFormatChanged(self):
        format _ QTextCharFormat()
        format.setForeground(
                __.GlobalColor(
                        self.weekdayColorCombo.itemData(
                                self.weekdayColorCombo.currentIndex())))

        self.calendar.setWeekdayTextFormat(__.Monday, format)
        self.calendar.setWeekdayTextFormat(__.Tuesday, format)
        self.calendar.setWeekdayTextFormat(__.Wednesday, format)
        self.calendar.setWeekdayTextFormat(__.Thursday, format)
        self.calendar.setWeekdayTextFormat(__.Friday, format)

    ___ weekendFormatChanged(self):
        format _ QTextCharFormat()
        format.setForeground(
                __.GlobalColor(
                        self.weekendColorCombo.itemData(
                                self.weekendColorCombo.currentIndex())))

        self.calendar.setWeekdayTextFormat(__.Saturday, format)
        self.calendar.setWeekdayTextFormat(__.Sunday, format)

    ___ reformatHeaders(self):
        t__ _ self.headerTextFormatCombo.currentText()
        format _ QTextCharFormat()

        __ t__ == "Bold":
            format.setFontWeight(QFont.Bold)
        ____ t__ == "Italic":
            format.setFontItalic(True)
        ____ t__ == "Green":
            format.setForeground(__.green)

        self.calendar.setHeaderTextFormat(format)

    ___ reformatCalendarPage(self):
        __ self.firstFridayCheckBox.isChecked
            firstFriday _ QDate(self.calendar.yearShown(),
                    self.calendar.monthShown(), 1)

            w__ firstFriday.dayOfWeek() !_ __.Friday:
                firstFriday _ firstFriday.addDays(1)

            firstFridayFormat _ QTextCharFormat()
            firstFridayFormat.setForeground(__.blue)

            self.calendar.setDateTextFormat(firstFriday, firstFridayFormat)

        # May 1st in Red takes precedence.
        __ self.mayFirstCheckBox.isChecked
            mayFirst _ QDate(self.calendar.yearShown(), 5, 1)

            mayFirstFormat _ QTextCharFormat()
            mayFirstFormat.setForeground(__.red)

            self.calendar.setDateTextFormat(mayFirst, mayFirstFormat)

    ___ createPreviewGroupBox(self):
        self.previewGroupBox _ QGroupBox("Preview")

        self.calendar _ QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.currentPageChanged.c..(self.reformatCalendarPage)

        self.previewLayout _ QGridLayout()
        self.previewLayout.aW..(self.calendar, 0, 0, __.AlignCenter)
        self.previewGroupBox.sL..(self.previewLayout)
 
    ___ createGeneralOptionsGroupBox(self):
        self.generalOptionsGroupBox _ QGroupBox("General Options")

        self.localeCombo _ QComboBox()

        curLocaleIndex _ -1
        index _ 0

        this_language _ self.locale().nativeLanguageName()
        this_country _ self.locale().nativeCountryName()

        for locale in QLocale.matchingLocales(QLocale.AnyLanguage, QLocale.AnyScript, QLocale.AnyCountry):
            language _ locale.nativeLanguageName()
            country _ locale.nativeCountryName()

            __ language == this_language and country == this_country:
                curLocaleIndex _ index

            self.localeCombo.addItem('%s/%s' % (language, country), locale)
            index +_ 1

        __ curLocaleIndex !_ -1:
            self.localeCombo.setCurrentIndex(curLocaleIndex)

        self.localeLabel _ QLabel("&Locale")
        self.localeLabel.setBuddy(self.localeCombo)

        self.firstDayCombo _ QComboBox()
        self.firstDayCombo.addItem("Sunday", __.Sunday)
        self.firstDayCombo.addItem("Monday", __.Monday)
        self.firstDayCombo.addItem("Tuesday", __.Tuesday)
        self.firstDayCombo.addItem("Wednesday", __.Wednesday)
        self.firstDayCombo.addItem("Thursday", __.Thursday)
        self.firstDayCombo.addItem("Friday", __.Friday)
        self.firstDayCombo.addItem("Saturday", __.Saturday)

        self.firstDayLabel _ QLabel("Wee&k starts on:")
        self.firstDayLabel.setBuddy(self.firstDayCombo)

        self.selectionModeCombo _ QComboBox()
        self.selectionModeCombo.addItem("Single selection",
                QCalendarWidget.SingleSelection)
        self.selectionModeCombo.addItem("None",
                QCalendarWidget.NoSelection)
        self.selectionModeLabel _ QLabel("&Selection mode:")
        self.selectionModeLabel.setBuddy(self.selectionModeCombo)

        self.gridCheckBox _ QCheckBox("&Grid")
        self.gridCheckBox.setChecked(self.calendar.isGridVisible())

        self.navigationCheckBox _ QCheckBox("&Navigation bar")
        self.navigationCheckBox.setChecked(True)

        self.horizontalHeaderCombo _ QComboBox()
        self.horizontalHeaderCombo.addItem("Single letter day names",
                QCalendarWidget.SingleLetterDayNames)
        self.horizontalHeaderCombo.addItem("Short day names",
                QCalendarWidget.ShortDayNames)
        self.horizontalHeaderCombo.addItem("Long day names",
                QCalendarWidget.LongDayNames)
        self.horizontalHeaderCombo.addItem("None",
                QCalendarWidget.NoHorizontalHeader)
        self.horizontalHeaderCombo.setCurrentIndex(1)

        self.horizontalHeaderLabel _ QLabel("&Horizontal header:")
        self.horizontalHeaderLabel.setBuddy(self.horizontalHeaderCombo)

        self.verticalHeaderCombo _ QComboBox()
        self.verticalHeaderCombo.addItem("ISO week numbers",
                QCalendarWidget.ISOWeekNumbers)
        self.verticalHeaderCombo.addItem("None",
                QCalendarWidget.NoVerticalHeader)

        self.verticalHeaderLabel _ QLabel("&Vertical header:")
        self.verticalHeaderLabel.setBuddy(self.verticalHeaderCombo)

        self.localeCombo.currentIndexChanged.c..(self.localeChanged)
        self.firstDayCombo.currentIndexChanged.c..(self.firstDayChanged)
        self.selectionModeCombo.currentIndexChanged.c..(
                self.selectionModeChanged)
        self.gridCheckBox.toggled.c..(self.calendar.setGridVisible)
        self.navigationCheckBox.toggled.c..(
                self.calendar.setNavigationBarVisible)
        self.horizontalHeaderCombo.currentIndexChanged.c..(
                self.horizontalHeaderChanged)
        self.verticalHeaderCombo.currentIndexChanged.c..(
                self.verticalHeaderChanged)

        checkBoxLayout _ QHBoxLayout()
        checkBoxLayout.aW..(self.gridCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.aW..(self.navigationCheckBox)

        outerLayout _ QGridLayout()
        outerLayout.aW..(self.localeLabel, 0, 0)
        outerLayout.aW..(self.localeCombo, 0, 1)
        outerLayout.aW..(self.firstDayLabel, 1, 0)
        outerLayout.aW..(self.firstDayCombo, 1, 1)
        outerLayout.aW..(self.selectionModeLabel, 2, 0)
        outerLayout.aW..(self.selectionModeCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        outerLayout.aW..(self.horizontalHeaderLabel, 4, 0)
        outerLayout.aW..(self.horizontalHeaderCombo, 4, 1)
        outerLayout.aW..(self.verticalHeaderLabel, 5, 0)
        outerLayout.aW..(self.verticalHeaderCombo, 5, 1)
        self.generalOptionsGroupBox.sL..(outerLayout)

        self.firstDayChanged(self.firstDayCombo.currentIndex())
        self.selectionModeChanged(self.selectionModeCombo.currentIndex())
        self.horizontalHeaderChanged(self.horizontalHeaderCombo.currentIndex())
        self.verticalHeaderChanged(self.verticalHeaderCombo.currentIndex())
 
    ___ createDatesGroupBox(self):
        self.datesGroupBox _ QGroupBox(self.tr("Dates"))

        self.minimumDateEdit _ QDateEdit()
        self.minimumDateEdit.setDisplayFormat('MMM d yyyy')
        self.minimumDateEdit.setDateRange(self.calendar.minimumDate(),
                                          self.calendar.maximumDate())
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

        self.minimumDateLabel _ QLabel("&Minimum Date:")
        self.minimumDateLabel.setBuddy(self.minimumDateEdit)

        self.currentDateEdit _ QDateEdit()
        self.currentDateEdit.setDisplayFormat('MMM d yyyy')
        self.currentDateEdit.setDate(self.calendar.selectedDate())
        self.currentDateEdit.setDateRange(self.calendar.minimumDate(),
                self.calendar.maximumDate())

        self.currentDateLabel _ QLabel("&Current Date:")
        self.currentDateLabel.setBuddy(self.currentDateEdit)

        self.maximumDateEdit _ QDateEdit()
        self.maximumDateEdit.setDisplayFormat('MMM d yyyy')
        self.maximumDateEdit.setDateRange(self.calendar.minimumDate(),
                self.calendar.maximumDate())
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

        self.maximumDateLabel _ QLabel("Ma&ximum Date:")
        self.maximumDateLabel.setBuddy(self.maximumDateEdit)

        self.currentDateEdit.dateChanged.c..(self.calendar.setSelectedDate)
        self.calendar.selectionChanged.c..(self.selectedDateChanged)
        self.minimumDateEdit.dateChanged.c..(self.minimumDateChanged)
        self.maximumDateEdit.dateChanged.c..(self.maximumDateChanged)
 
        dateBoxLayout _ QGridLayout()
        dateBoxLayout.aW..(self.currentDateLabel, 1, 0)
        dateBoxLayout.aW..(self.currentDateEdit, 1, 1)
        dateBoxLayout.aW..(self.minimumDateLabel, 0, 0)
        dateBoxLayout.aW..(self.minimumDateEdit, 0, 1)
        dateBoxLayout.aW..(self.maximumDateLabel, 2, 0)
        dateBoxLayout.aW..(self.maximumDateEdit, 2, 1)
        dateBoxLayout.setRowStretch(3, 1)

        self.datesGroupBox.sL..(dateBoxLayout)

    ___ createTextFormatsGroupBox(self):
        self.textFormatsGroupBox _ QGroupBox("Text Formats")

        self.weekdayColorCombo _ self.createColorComboBox()
        self.weekdayColorCombo.setCurrentIndex(
                self.weekdayColorCombo.findText("Black"))

        self.weekdayColorLabel _ QLabel("&Weekday color:")
        self.weekdayColorLabel.setBuddy(self.weekdayColorCombo)

        self.weekendColorCombo _ self.createColorComboBox()
        self.weekendColorCombo.setCurrentIndex(
                self.weekendColorCombo.findText("Red"))

        self.weekendColorLabel _ QLabel("Week&end color:")
        self.weekendColorLabel.setBuddy(self.weekendColorCombo)

        self.headerTextFormatCombo _ QComboBox()
        self.headerTextFormatCombo.addItem("Bold")
        self.headerTextFormatCombo.addItem("Italic")
        self.headerTextFormatCombo.addItem("Plain")

        self.headerTextFormatLabel _ QLabel("&Header text:")
        self.headerTextFormatLabel.setBuddy(self.headerTextFormatCombo)

        self.firstFridayCheckBox _ QCheckBox("&First Friday in blue")

        self.mayFirstCheckBox _ QCheckBox("May &1 in red")

        self.weekdayColorCombo.currentIndexChanged.c..(
                self.weekdayFormatChanged)
        self.weekendColorCombo.currentIndexChanged.c..(
                self.weekendFormatChanged)
        self.headerTextFormatCombo.currentIndexChanged.c..(
                self.reformatHeaders)
        self.firstFridayCheckBox.toggled.c..(self.reformatCalendarPage)
        self.mayFirstCheckBox.toggled.c..(self.reformatCalendarPage)

        checkBoxLayout _ QHBoxLayout()
        checkBoxLayout.aW..(self.firstFridayCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.aW..(self.mayFirstCheckBox)

        outerLayout _ QGridLayout()
        outerLayout.aW..(self.weekdayColorLabel, 0, 0)
        outerLayout.aW..(self.weekdayColorCombo, 0, 1)
        outerLayout.aW..(self.weekendColorLabel, 1, 0)
        outerLayout.aW..(self.weekendColorCombo, 1, 1)
        outerLayout.aW..(self.headerTextFormatLabel, 2, 0)
        outerLayout.aW..(self.headerTextFormatCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        self.textFormatsGroupBox.sL..(outerLayout)

        self.weekdayFormatChanged()
        self.weekendFormatChanged()

        self.reformatHeaders()
        self.reformatCalendarPage()
 
    ___ createColorComboBox(self):
        comboBox _ QComboBox()
        comboBox.addItem("Red", __.red)
        comboBox.addItem("Blue", __.blue)
        comboBox.addItem("Black", __.black)
        comboBox.addItem("Magenta", __.magenta)

        r_ comboBox


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    window _ Window()
    window.s..

    sys.exit(app.exec_())
