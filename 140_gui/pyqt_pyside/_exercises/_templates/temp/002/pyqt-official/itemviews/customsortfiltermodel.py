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


____ ?.?C.. ______ (QDate, QDateTime, QRegExp, QSortFilterProxyModel, __,
        QTime)
____ ?.?G.. ______ QStandardItemModel
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QDateEdit,
        QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView,
        QVBoxLayout, QWidget)


c_ MySortFilterProxyModel(QSortFilterProxyModel):
    ___ __init__  parent_None):
        super(MySortFilterProxyModel, self).__init__(parent)

        self.minDate _ QDate()
        self.maxDate _ QDate()

    ___ setFilterMinimumDate  date):
        self.minDate _ date
        self.invalidateFilter()

    ___ filterMinimumDate(self):
        r_ self.minDate

    ___ setFilterMaximumDate  date):
        self.maxDate _ date
        self.invalidateFilter()
 
    ___ filterMaximumDate(self):
        r_ self.maxDate

    ___ filterAcceptsRow  sourceRow, sourceParent):
        index0 _ self.sourceModel().index(sourceRow, 0, sourceParent)
        index1 _ self.sourceModel().index(sourceRow, 1, sourceParent)
        index2 _ self.sourceModel().index(sourceRow, 2, sourceParent)

        r_ (   (self.filterRegExp().indexIn(self.sourceModel().data(index0)) >_ 0
                    or self.filterRegExp().indexIn(self.sourceModel().data(index1)) >_ 0)
                and self.dateInRange(self.sourceModel().data(index2)))

    ___ lessThan  left, right):
        leftData _ self.sourceModel().data(left)
        rightData _ self.sourceModel().data(right)

        __ no. isinstance(leftData, QDate):
            emailPattern _ QRegExp("([\\w\\.]*@[\\w\\.]*)")

            __ left.column() == 1 and emailPattern.indexIn(leftData) !_ -1:
                leftData _ emailPattern.cap(1)

            __ right.column() == 1 and emailPattern.indexIn(rightData) !_ -1:
                rightData _ emailPattern.cap(1)

        r_ leftData < rightData

    ___ dateInRange  date):
        __ isinstance(date, QDateTime):
            date _ date.date()

        r_ (    (no. self.minDate.isValid() or date >_ self.minDate)
                and (no. self.maxDate.isValid() or date <_ self.maxDate))


c_ Window(QWidget):
    ___ __init__(self):
        super(Window, self).__init__()

        self.proxyModel _ MySortFilterProxyModel(self)
        self.proxyModel.setDynamicSortFilter(True)

        self.sourceView _ QTreeView()
        self.sourceView.setRootIsDecorated F..
        self.sourceView.setAlternatingRowColors(True)

        sourceLayout _ QHBoxLayout()
        sourceLayout.addWidget(self.sourceView)
        sourceGroupBox _ QGroupBox("Original Model")
        sourceGroupBox.setLayout(sourceLayout)

        self.filterCaseSensitivityCheckBox _ QCheckBox("Case sensitive filter")
        self.filterCaseSensitivityCheckBox.setChecked(True)
        self.filterPatternLineEdit _ QLineEdit()
        self.filterPatternLineEdit.sT..("Grace|Sports")
        filterPatternLabel _ QLabel("&Filter pattern:")
        filterPatternLabel.setBuddy(self.filterPatternLineEdit)
        self.filterSyntaxComboBox _ QComboBox()
        self.filterSyntaxComboBox.addItem("Regular expression", QRegExp.RegExp)
        self.filterSyntaxComboBox.addItem("Wildcard", QRegExp.Wildcard)
        self.filterSyntaxComboBox.addItem("Fixed string", QRegExp.FixedString)
        self.fromDateEdit _ QDateEdit()
        self.fromDateEdit.setDate(QDate(2006, 12, 22))
        self.fromDateEdit.setCalendarPopup(True)
        fromLabel _ QLabel("F&rom:")
        fromLabel.setBuddy(self.fromDateEdit)
        self.toDateEdit _ QDateEdit()
        self.toDateEdit.setDate(QDate(2007, 1, 5))
        self.toDateEdit.setCalendarPopup(True)
        toLabel _ QLabel("&To:")
        toLabel.setBuddy(self.toDateEdit)

        self.filterPatternLineEdit.textChanged.c..(self.textFilterChanged)
        self.filterSyntaxComboBox.currentIndexChanged.c..(self.textFilterChanged)
        self.filterCaseSensitivityCheckBox.toggled.c..(self.textFilterChanged)
        self.fromDateEdit.dateChanged.c..(self.dateFilterChanged)
        self.toDateEdit.dateChanged.c..(self.dateFilterChanged)

        self.proxyView _ QTreeView()
        self.proxyView.setRootIsDecorated F..
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)
        self.proxyView.sortByColumn(1, __.AscendingOrder)

        self.textFilterChanged()
        self.dateFilterChanged()

        proxyLayout _ QGridLayout()
        proxyLayout.addWidget(self.proxyView, 0, 0, 1, 3)
        proxyLayout.addWidget(filterPatternLabel, 1, 0)
        proxyLayout.addWidget(self.filterPatternLineEdit, 1, 1)
        proxyLayout.addWidget(self.filterSyntaxComboBox, 1, 2)
        proxyLayout.addWidget(self.filterCaseSensitivityCheckBox, 2, 0, 1, 3)
        proxyLayout.addWidget(fromLabel, 3, 0)
        proxyLayout.addWidget(self.fromDateEdit, 3, 1, 1, 2)
        proxyLayout.addWidget(toLabel, 4, 0)
        proxyLayout.addWidget(self.toDateEdit, 4, 1, 1, 2)
        proxyGroupBox _ QGroupBox("Sorted/Filtered Model")
        proxyGroupBox.setLayout(proxyLayout)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(sourceGroupBox)
        mainLayout.addWidget(proxyGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Custom Sort/Filter Model")
        self.resize(500, 450)

    ___ setSourceModel  model):
        self.proxyModel.setSourceModel(model)
        self.sourceView.setModel(model)

    ___ textFilterChanged(self):
        syntax _ QRegExp.PatternSyntax(
            self.filterSyntaxComboBox.itemData(
                self.filterSyntaxComboBox.currentIndex()))
        caseSensitivity _ (
            self.filterCaseSensitivityCheckBox.isChecked()
            and __.CaseSensitive or __.CaseInsensitive)
        regExp _ QRegExp(self.filterPatternLineEdit.text(), caseSensitivity, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    ___ dateFilterChanged(self):
        self.proxyModel.setFilterMinimumDate(self.fromDateEdit.date())
        self.proxyModel.setFilterMaximumDate(self.toDateEdit.date())


___ addMail(model, subject, sender, date):
    model.insertRow(0)
    model.setData(model.index(0, 0), subject)
    model.setData(model.index(0, 1), sender)
    model.setData(model.index(0, 2), date)


___ createMailModel(parent):
    model _ QStandardItemModel(0, 3, parent)

    model.setHeaderData(0, __.Horizontal, "Subject")
    model.setHeaderData(1, __.Horizontal, "Sender")
    model.setHeaderData(2, __.Horizontal, "Date")

    addMail(model, "Happy New Year!", "Grace K. <grace@software-inc.com>",
            QDateTime(QDate(2006, 12, 31), QTime(17, 3)))
    addMail(model, "Radically new concept", "Grace K. <grace@software-inc.com>",
            QDateTime(QDate(2006, 12, 22), QTime(9, 44)))
    addMail(model, "Accounts", "pascale@nospam.com",
            QDateTime(QDate(2006, 12, 31), QTime(12, 50)))
    addMail(model, "Expenses", "Joe Bloggs <joe@bloggs.com>",
            QDateTime(QDate(2006, 12, 25), QTime(11, 39)))
    addMail(model, "Re: Expenses", "Andy <andy@nospam.com>",
            QDateTime(QDate(2007, 1, 2), QTime(16, 5)))
    addMail(model, "Re: Accounts", "Joe Bloggs <joe@bloggs.com>",
            QDateTime(QDate(2007, 1, 3), QTime(14, 18)))
    addMail(model, "Re: Accounts", "Andy <andy@nospam.com>",
            QDateTime(QDate(2007, 1, 3), QTime(14, 26)))
    addMail(model, "Sports", "Linda Smith <linda.smith@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(11, 33)))
    addMail(model, "AW: Sports", "Rolf Newschweinstein <rolfn@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(12, 0)))
    addMail(model, "RE: Sports", "Petra Schmidt <petras@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(12, 1)))

    r_ model


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)

    window _ Window()
    window.setSourceModel(createMailModel(window))
    window.s..

    sys.exit(app.exec_())
