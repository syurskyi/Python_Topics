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


____ ?.?C.. ______ ?D.., ?DT__, __, ?T..
____ ?.?W.. ______ (?A.., ?CB, ?DE.., ?DTE..,
        QDoubleSpinBox, ?GB.., ?HBL.., ?L.., SB.., ?TE..,
        ?VBL.., ?W..)


c_ Window(?W..):
    ___  -  
        s__(Window, self). - ()

        createSpinBoxes()
        createDateTimeEdits()
        createDoubleSpinBoxes()

        layout _ ?HBL..
        layout.aW..(spinBoxesGroup)
        layout.aW..(editsGroup)
        layout.aW..(doubleSpinBoxesGroup)
        sL..(layout)

        sWT..("Spin Boxes")

    ___ createSpinBoxes 
        spinBoxesGroup _ ?GB..("Spinboxes")

        integerLabel _ ?L..("Enter a value between %d and %d:" % (-20, 20))
        integerSpinBox _ SB..()
        integerSpinBox.setRange(-20, 20)
        integerSpinBox.setSingleStep(1)
        integerSpinBox.sV..(0)

        zoomLabel _ ?L..("Enter a zoom value between %d and %d:" % (0, 1000))
        zoomSpinBox _ SB..()
        zoomSpinBox.setRange(0, 1000)
        zoomSpinBox.setSingleStep(10)
        zoomSpinBox.setSuffix('%')
        zoomSpinBox.setSpecialValueText("Automatic")
        zoomSpinBox.sV..(100)

        priceLabel _ ?L..("Enter a price between %d and %d:" % (0, 999))
        priceSpinBox _ SB..()
        priceSpinBox.setRange(0, 999)
        priceSpinBox.setSingleStep(1)
        priceSpinBox.setPrefix('$')
        priceSpinBox.sV..(99)

        spinBoxLayout _ ?VBL..
        spinBoxLayout.aW..(integerLabel)
        spinBoxLayout.aW..(integerSpinBox)
        spinBoxLayout.aW..(zoomLabel)
        spinBoxLayout.aW..(zoomSpinBox)
        spinBoxLayout.aW..(priceLabel)
        spinBoxLayout.aW..(priceSpinBox)
        spinBoxesGroup.sL..(spinBoxLayout)

    ___ createDateTimeEdits 
        editsGroup _ ?GB..("Date and time spin boxes")

        dateLabel _ ?L..
        dateEdit _ ?DE..(?D...currentDate())
        dateEdit.setDateRange(?D..(2005, 1, 1), ?D..(2010, 12, 31))
        dateLabel.sT..("Appointment date (between %s and %s):" %
                    (dateEdit.minimumDate().toString(__.ISODate),
                    dateEdit.maximumDate().toString(__.ISODate)))

        timeLabel _ ?L..
        timeEdit _ ?TE..(?T...currentTime())
        timeEdit.setTimeRange(?T..(9, 0, 0, 0), ?T..(16, 30, 0, 0))
        timeLabel.sT..("Appointment time (between %s and %s):" %
                    (timeEdit.minimumTime().toString(__.ISODate),
                    timeEdit.maximumTime().toString(__.ISODate)))

        meetingLabel _ ?L..
        meetingEdit _ ?DTE..(?DT__.currentDateTime())

        formatLabel _ ?L..("Format string for the meeting date and time:")

        formatComboBox _ ?CB()
        formatComboBox.aI..('yyyy-MM-dd hh:mm:ss (zzz \'ms\')')
        formatComboBox.aI..('hh:mm:ss MM/dd/yyyy')
        formatComboBox.aI..('hh:mm:ss dd/MM/yyyy')
        formatComboBox.aI..('hh:mm:ss')
        formatComboBox.aI..('hh:mm ap')

        formatComboBox.activated[st.].c..(setFormatString)

        setFormatString(formatComboBox.currentText())

        editsLayout _ ?VBL..
        editsLayout.aW..(dateLabel)
        editsLayout.aW..(dateEdit)
        editsLayout.aW..(timeLabel)
        editsLayout.aW..(timeEdit)
        editsLayout.aW..(meetingLabel)
        editsLayout.aW..(meetingEdit)
        editsLayout.aW..(formatLabel)
        editsLayout.aW..(formatComboBox)
        editsGroup.sL..(editsLayout)

    ___ setFormatString  formatString):
        meetingEdit.setDisplayFormat(formatString)

        __ meetingEdit.displayedSections() & ?DTE...DateSections_Mask:
            meetingEdit.setDateRange(?D..(2004, 11, 1), ?D..(2005, 11, 30))
            meetingLabel.sT..("Meeting date (between %s and %s):" %
                    (meetingEdit.minimumDate().toString(__.ISODate),
                    meetingEdit.maximumDate().toString(__.ISODate)))
        ____
            meetingEdit.setTimeRange(?T..(0, 7, 20, 0), ?T..(21, 0, 0, 0))
            meetingLabel.sT..("Meeting time (between %s and %s):" %
                    (meetingEdit.minimumTime().toString(__.ISODate),
                    meetingEdit.maximumTime().toString(__.ISODate)))

    ___ createDoubleSpinBoxes 
        doubleSpinBoxesGroup _ ?GB..("Double precision spinboxes")

        precisionLabel _ ?L..("Number of decimal places to show:")
        precisionSpinBox _ SB..()
        precisionSpinBox.setRange(0, 100)
        precisionSpinBox.sV..(2)

        doubleLabel _ ?L..("Enter a value between %d and %d:" % (-20, 20))
        doubleSpinBox _ QDoubleSpinBox()
        doubleSpinBox.setRange(-20.0, 20.0)
        doubleSpinBox.setSingleStep(1.0)
        doubleSpinBox.sV..(0.0)

        scaleLabel _ ?L..("Enter a scale factor between %d and %d:" % (0, 1000))
        scaleSpinBox _ QDoubleSpinBox()
        scaleSpinBox.setRange(0.0, 1000.0)
        scaleSpinBox.setSingleStep(10.0)
        scaleSpinBox.setSuffix('%')
        scaleSpinBox.setSpecialValueText("No scaling")
        scaleSpinBox.sV..(100.0)

        priceLabel _ ?L..("Enter a price between %d and %d:" % (0, 1000))
        priceSpinBox _ QDoubleSpinBox()
        priceSpinBox.setRange(0.0, 1000.0)
        priceSpinBox.setSingleStep(1.0)
        priceSpinBox.setPrefix('$')
        priceSpinBox.sV..(99.99)

        precisionSpinBox.valueChanged.c..(changePrecision)

        spinBoxLayout _ ?VBL..
        spinBoxLayout.aW..(precisionLabel)
        spinBoxLayout.aW..(precisionSpinBox)
        spinBoxLayout.aW..(doubleLabel)
        spinBoxLayout.aW..(doubleSpinBox)
        spinBoxLayout.aW..(scaleLabel)
        spinBoxLayout.aW..(scaleSpinBox)
        spinBoxLayout.aW..(priceLabel)
        spinBoxLayout.aW..(priceSpinBox)
        doubleSpinBoxesGroup.sL..(spinBoxLayout)

    ___ changePrecision  decimals):
        doubleSpinBox.setDecimals(decimals)
        scaleSpinBox.setDecimals(decimals)
        priceSpinBox.setDecimals(decimals)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
