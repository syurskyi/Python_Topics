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


____ ?.QtCore ______ QDate, QDateTime, Qt, QTime
____ ?.?W.. ______ (?A.., QComboBox, QDateEdit, QDateTimeEdit,
        QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel, QSpinBox, QTimeEdit,
        QVBoxLayout, QWidget)


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.createSpinBoxes()
        self.createDateTimeEdits()
        self.createDoubleSpinBoxes()

        layout _ QHBoxLayout()
        layout.addWidget(self.spinBoxesGroup)
        layout.addWidget(self.editsGroup)
        layout.addWidget(self.doubleSpinBoxesGroup)
        self.setLayout(layout)

        self.setWindowTitle("Spin Boxes")

    ___ createSpinBoxes(self):
        self.spinBoxesGroup _ QGroupBox("Spinboxes")

        integerLabel _ QLabel("Enter a value between %d and %d:" % (-20, 20))
        integerSpinBox _ QSpinBox()
        integerSpinBox.setRange(-20, 20)
        integerSpinBox.setSingleStep(1)
        integerSpinBox.setValue(0)

        zoomLabel _ QLabel("Enter a zoom value between %d and %d:" % (0, 1000))
        zoomSpinBox _ QSpinBox()
        zoomSpinBox.setRange(0, 1000)
        zoomSpinBox.setSingleStep(10)
        zoomSpinBox.setSuffix('%')
        zoomSpinBox.setSpecialValueText("Automatic")
        zoomSpinBox.setValue(100)

        priceLabel _ QLabel("Enter a price between %d and %d:" % (0, 999))
        priceSpinBox _ QSpinBox()
        priceSpinBox.setRange(0, 999)
        priceSpinBox.setSingleStep(1)
        priceSpinBox.setPrefix('$')
        priceSpinBox.setValue(99)

        spinBoxLayout _ QVBoxLayout()
        spinBoxLayout.addWidget(integerLabel)
        spinBoxLayout.addWidget(integerSpinBox)
        spinBoxLayout.addWidget(zoomLabel)
        spinBoxLayout.addWidget(zoomSpinBox)
        spinBoxLayout.addWidget(priceLabel)
        spinBoxLayout.addWidget(priceSpinBox)
        self.spinBoxesGroup.setLayout(spinBoxLayout)

    ___ createDateTimeEdits(self):
        self.editsGroup _ QGroupBox("Date and time spin boxes")

        dateLabel _ QLabel()
        dateEdit _ QDateEdit(QDate.currentDate())
        dateEdit.setDateRange(QDate(2005, 1, 1), QDate(2010, 12, 31))
        dateLabel.sT..("Appointment date (between %s and %s):" %
                    (dateEdit.minimumDate().toString(Qt.ISODate),
                    dateEdit.maximumDate().toString(Qt.ISODate)))

        timeLabel _ QLabel()
        timeEdit _ QTimeEdit(QTime.currentTime())
        timeEdit.setTimeRange(QTime(9, 0, 0, 0), QTime(16, 30, 0, 0))
        timeLabel.sT..("Appointment time (between %s and %s):" %
                    (timeEdit.minimumTime().toString(Qt.ISODate),
                    timeEdit.maximumTime().toString(Qt.ISODate)))

        self.meetingLabel _ QLabel()
        self.meetingEdit _ QDateTimeEdit(QDateTime.currentDateTime())

        formatLabel _ QLabel("Format string for the meeting date and time:")

        formatComboBox _ QComboBox()
        formatComboBox.addItem('yyyy-MM-dd hh:mm:ss (zzz \'ms\')')
        formatComboBox.addItem('hh:mm:ss MM/dd/yyyy')
        formatComboBox.addItem('hh:mm:ss dd/MM/yyyy')
        formatComboBox.addItem('hh:mm:ss')
        formatComboBox.addItem('hh:mm ap')

        formatComboBox.activated[str].c..(self.setFormatString)

        self.setFormatString(formatComboBox.currentText())

        editsLayout _ QVBoxLayout()
        editsLayout.addWidget(dateLabel)
        editsLayout.addWidget(dateEdit)
        editsLayout.addWidget(timeLabel)
        editsLayout.addWidget(timeEdit)
        editsLayout.addWidget(self.meetingLabel)
        editsLayout.addWidget(self.meetingEdit)
        editsLayout.addWidget(formatLabel)
        editsLayout.addWidget(formatComboBox)
        self.editsGroup.setLayout(editsLayout)

    ___ setFormatString  formatString):
        self.meetingEdit.setDisplayFormat(formatString)

        __ self.meetingEdit.displayedSections() & QDateTimeEdit.DateSections_Mask:
            self.meetingEdit.setDateRange(QDate(2004, 11, 1), QDate(2005, 11, 30))
            self.meetingLabel.sT..("Meeting date (between %s and %s):" %
                    (self.meetingEdit.minimumDate().toString(Qt.ISODate),
                    self.meetingEdit.maximumDate().toString(Qt.ISODate)))
        ____
            self.meetingEdit.setTimeRange(QTime(0, 7, 20, 0), QTime(21, 0, 0, 0))
            self.meetingLabel.sT..("Meeting time (between %s and %s):" %
                    (self.meetingEdit.minimumTime().toString(Qt.ISODate),
                    self.meetingEdit.maximumTime().toString(Qt.ISODate)))

    ___ createDoubleSpinBoxes(self):
        self.doubleSpinBoxesGroup _ QGroupBox("Double precision spinboxes")

        precisionLabel _ QLabel("Number of decimal places to show:")
        precisionSpinBox _ QSpinBox()
        precisionSpinBox.setRange(0, 100)
        precisionSpinBox.setValue(2)

        doubleLabel _ QLabel("Enter a value between %d and %d:" % (-20, 20))
        self.doubleSpinBox _ QDoubleSpinBox()
        self.doubleSpinBox.setRange(-20.0, 20.0)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setValue(0.0)

        scaleLabel _ QLabel("Enter a scale factor between %d and %d:" % (0, 1000))
        self.scaleSpinBox _ QDoubleSpinBox()
        self.scaleSpinBox.setRange(0.0, 1000.0)
        self.scaleSpinBox.setSingleStep(10.0)
        self.scaleSpinBox.setSuffix('%')
        self.scaleSpinBox.setSpecialValueText("No scaling")
        self.scaleSpinBox.setValue(100.0)

        priceLabel _ QLabel("Enter a price between %d and %d:" % (0, 1000))
        self.priceSpinBox _ QDoubleSpinBox()
        self.priceSpinBox.setRange(0.0, 1000.0)
        self.priceSpinBox.setSingleStep(1.0)
        self.priceSpinBox.setPrefix('$')
        self.priceSpinBox.setValue(99.99)

        precisionSpinBox.valueChanged.c..(self.changePrecision)

        spinBoxLayout _ QVBoxLayout()
        spinBoxLayout.addWidget(precisionLabel)
        spinBoxLayout.addWidget(precisionSpinBox)
        spinBoxLayout.addWidget(doubleLabel)
        spinBoxLayout.addWidget(self.doubleSpinBox)
        spinBoxLayout.addWidget(scaleLabel)
        spinBoxLayout.addWidget(self.scaleSpinBox)
        spinBoxLayout.addWidget(priceLabel)
        spinBoxLayout.addWidget(self.priceSpinBox)
        self.doubleSpinBoxesGroup.setLayout(spinBoxLayout)

    ___ changePrecision  decimals):
        self.doubleSpinBox.setDecimals(decimals)
        self.scaleSpinBox.setDecimals(decimals)
        self.priceSpinBox.setDecimals(decimals)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
