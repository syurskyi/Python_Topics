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


____ ?.?C.. ______ (QDate, QDateTime, QRegExp, QSortFilterProxyModel, __,
        QTime)
____ ?.?G.. ______ QStandardItemModel
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget)


SUBJECT, SENDER, DATE _ range(3)

# Work around the fact that QSortFilterProxyModel always filters datetime
# values in QtCore.Qt.ISODate format, but the tree views display using
# QtCore.Qt.DefaultLocaleShortDate format.
c_ SortFilterProxyModel(QSortFilterProxyModel):
    ___ filterAcceptsRow  sourceRow, sourceParent):
        # Do we filter for the date column?
        __ filterKeyColumn() == DATE:
            # Fetch datetime value.
            index _ sourceModel().index(sourceRow, DATE, sourceParent)
            data _ sourceModel().data(index)

            # Return, if regExp match in displayed format.
            r_ (filterRegExp().indexIn(data.toString(__.DefaultLocaleShortDate)) >_ 0)

        # Not our business.
        r_ super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


c_ Window(QWidget):
    ___  -
        super(Window, self). - ()

        proxyModel _ SortFilterProxyModel()
        proxyModel.setDynamicSortFilter(True)

        sourceGroupBox _ QGroupBox("Original Model")
        proxyGroupBox _ QGroupBox("Sorted/Filtered Model")

        sourceView _ ?TV..
        sourceView.setRootIsDecorated F..
        sourceView.setAlternatingRowColors(True)

        proxyView _ ?TV..
        proxyView.setRootIsDecorated F..
        proxyView.setAlternatingRowColors(True)
        proxyView.sM..(proxyModel)
        proxyView.setSortingEnabled(True)

        sortCaseSensitivityCheckBox _ QCheckBox("Case sensitive sorting")
        filterCaseSensitivityCheckBox _ QCheckBox("Case sensitive filter")

        filterPatternLineEdit _ ?LE..
        filterPatternLabel _ QLabel("&Filter pattern:")
        filterPatternLabel.setBuddy(filterPatternLineEdit)

        filterSyntaxComboBox _ QComboBox()
        filterSyntaxComboBox.addItem("Regular expression", QRegExp.RegExp)
        filterSyntaxComboBox.addItem("Wildcard", QRegExp.Wildcard)
        filterSyntaxComboBox.addItem("Fixed string", QRegExp.FixedString)
        filterSyntaxLabel _ QLabel("Filter &syntax:")
        filterSyntaxLabel.setBuddy(filterSyntaxComboBox)

        filterColumnComboBox _ QComboBox()
        filterColumnComboBox.addItem("Subject")
        filterColumnComboBox.addItem("Sender")
        filterColumnComboBox.addItem("Date")
        filterColumnLabel _ QLabel("Filter &column:")
        filterColumnLabel.setBuddy(filterColumnComboBox)

        filterPatternLineEdit.textChanged.c..(filterRegExpChanged)
        filterSyntaxComboBox.currentIndexChanged.c..(filterRegExpChanged)
        filterColumnComboBox.currentIndexChanged.c..(filterColumnChanged)
        filterCaseSensitivityCheckBox.toggled.c..(filterRegExpChanged)
        sortCaseSensitivityCheckBox.toggled.c..(sortChanged)

        sourceLayout _ QHBoxLayout()
        sourceLayout.aW..(sourceView)
        sourceGroupBox.sL..(sourceLayout)

        proxyLayout _ QGridLayout()
        proxyLayout.aW..(proxyView, 0, 0, 1, 3)
        proxyLayout.aW..(filterPatternLabel, 1, 0)
        proxyLayout.aW..(filterPatternLineEdit, 1, 1, 1, 2)
        proxyLayout.aW..(filterSyntaxLabel, 2, 0)
        proxyLayout.aW..(filterSyntaxComboBox, 2, 1, 1, 2)
        proxyLayout.aW..(filterColumnLabel, 3, 0)
        proxyLayout.aW..(filterColumnComboBox, 3, 1, 1, 2)
        proxyLayout.aW..(filterCaseSensitivityCheckBox, 4, 0, 1, 2)
        proxyLayout.aW..(sortCaseSensitivityCheckBox, 4, 2)
        proxyGroupBox.sL..(proxyLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(sourceGroupBox)
        mainLayout.aW..(proxyGroupBox)
        sL..(mainLayout)

        sWT..("Basic Sort/Filter Model")
        r..(500, 450)

        proxyView.sortByColumn(SENDER, __.AscendingOrder)
        filterColumnComboBox.setCurrentIndex(SENDER)

        filterPatternLineEdit.sT..("Andy|Grace")
        filterCaseSensitivityCheckBox.setChecked(True)
        sortCaseSensitivityCheckBox.setChecked(True)

    ___ setSourceModel  model):
        proxyModel.setSourceModel(model)
        sourceView.sM..(model)

    ___ filterRegExpChanged
        syntax_nr _ filterSyntaxComboBox.itemData(filterSyntaxComboBox.currentIndex())
        syntax _ QRegExp.PatternSyntax(syntax_nr)

        __ filterCaseSensitivityCheckBox.isChecked
            caseSensitivity _ __.CaseSensitive
        ____
            caseSensitivity _ __.CaseInsensitive

        regExp _ QRegExp(filterPatternLineEdit.t__(),
                caseSensitivity, syntax)
        proxyModel.setFilterRegExp(regExp)

    ___ filterColumnChanged
        proxyModel.setFilterKeyColumn(filterColumnComboBox.currentIndex())

    ___ sortChanged
        __ sortCaseSensitivityCheckBox.isChecked
            caseSensitivity _ __.CaseSensitive
        ____
            caseSensitivity _ __.CaseInsensitive

        proxyModel.setSortCaseSensitivity(caseSensitivity)


___ addMail(model, subject, sender, date):
    model.insertRow(0)
    model.setData(model.index(0, SUBJECT), subject)
    model.setData(model.index(0, SENDER), sender)
    model.setData(model.index(0, DATE), date)


___ createMailModel(parent):
    model _ QStandardItemModel(0, 3, parent)

    model.setHeaderData(SUBJECT, __.Horizontal, "Subject")
    model.setHeaderData(SENDER, __.Horizontal, "Sender")
    model.setHeaderData(DATE, __.Horizontal, "Date")

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


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.setSourceModel(createMailModel(window))
    window.s..
    ___.e..(app.exec_())
