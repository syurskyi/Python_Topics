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


____ ?.?C.. ______ (?D.., ?DT__, QRegExp, QSortFilterProxyModel, __,
        ?T..)
____ ?.?G.. ______ ?SIM..
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, ?DE..,
        QGridLayout, ?GB.., ?HBL.., ?L.., QLineEdit, QTreeView,
        ?VBL.., ?W..)


c_ MySortFilterProxyModel(QSortFilterProxyModel):
    ___  -   parent_None):
        s__(MySortFilterProxyModel, self). - (parent)

        minDate _ ?D..()
        maxDate _ ?D..()

    ___ setFilterMinimumDate  date):
        minDate _ date
        invalidateFilter()

    ___ filterMinimumDate
        r_ minDate

    ___ setFilterMaximumDate  date):
        maxDate _ date
        invalidateFilter()
 
    ___ filterMaximumDate
        r_ maxDate

    ___ filterAcceptsRow  sourceRow, sourceParent):
        index0 _ sourceModel().i..(sourceRow, 0, sourceParent)
        index1 _ sourceModel().i..(sourceRow, 1, sourceParent)
        index2 _ sourceModel().i..(sourceRow, 2, sourceParent)

        r_ (   (filterRegExp().indexIn(sourceModel().data(index0)) >_ 0
                    or filterRegExp().indexIn(sourceModel().data(index1)) >_ 0)
                and dateInRange(sourceModel().data(index2)))

    ___ lessThan  left, right):
        leftData _ sourceModel().data(left)
        rightData _ sourceModel().data(right)

        __ no. isinstance(leftData, ?D..):
            emailPattern _ QRegExp("([\\w\\.]*@[\\w\\.]*)")

            __ left.column() __ 1 and emailPattern.indexIn(leftData) !_ -1:
                leftData _ emailPattern.cap(1)

            __ right.column() __ 1 and emailPattern.indexIn(rightData) !_ -1:
                rightData _ emailPattern.cap(1)

        r_ leftData < rightData

    ___ dateInRange  date):
        __ isinstance(date, ?DT__):
            date _ date.date()

        r_ (    (no. minDate.iV.. or date >_ minDate)
                and (no. maxDate.iV.. or date <_ maxDate))


c_ Window(?W..):
    ___  -
        s__(Window, self). - ()

        proxyModel _ MySortFilterProxyModel
        proxyModel.setDynamicSortFilter( st.

        sourceView _ ?TV..
        sourceView.setRootIsDecorated F..
        sourceView.setAlternatingRowColors( st.

        sourceLayout _ ?HBL..
        sourceLayout.aW..(sourceView)
        sourceGroupBox _ ?GB..("Original Model")
        sourceGroupBox.sL..(sourceLayout)

        filterCaseSensitivityCheckBox _ QCheckBox("Case sensitive filter")
        filterCaseSensitivityCheckBox.sC__( st.
        filterPatternLineEdit _ ?LE..
        filterPatternLineEdit.sT..("Grace|Sports")
        filterPatternLabel _ ?L..("&Filter pattern:")
        filterPatternLabel.setBuddy(filterPatternLineEdit)
        filterSyntaxComboBox _ ?CB()
        filterSyntaxComboBox.aI..("Regular expression", QRegExp.RegExp)
        filterSyntaxComboBox.aI..("Wildcard", QRegExp.Wildcard)
        filterSyntaxComboBox.aI..("Fixed string", QRegExp.FixedString)
        fromDateEdit _ ?DE..()
        fromDateEdit.setDate(?D..(2006, 12, 22))
        fromDateEdit.setCalendarPopup( st.
        fromLabel _ ?L..("F&rom:")
        fromLabel.setBuddy(fromDateEdit)
        toDateEdit _ ?DE..()
        toDateEdit.setDate(?D..(2007, 1, 5))
        toDateEdit.setCalendarPopup( st.
        toLabel _ ?L..("&To:")
        toLabel.setBuddy(toDateEdit)

        filterPatternLineEdit.tC...c..(textFilterChanged)
        filterSyntaxComboBox.currentIndexChanged.c..(textFilterChanged)
        filterCaseSensitivityCheckBox.t__.c..(textFilterChanged)
        fromDateEdit.dateChanged.c..(dateFilterChanged)
        toDateEdit.dateChanged.c..(dateFilterChanged)

        proxyView _ ?TV..
        proxyView.setRootIsDecorated F..
        proxyView.setAlternatingRowColors( st.
        proxyView.sM..(proxyModel)
        proxyView.sSE.. st.
        proxyView.sortByColumn(1, __.AscendingOrder)

        textFilterChanged()
        dateFilterChanged()

        proxyLayout _ QGridLayout()
        proxyLayout.aW..(proxyView, 0, 0, 1, 3)
        proxyLayout.aW..(filterPatternLabel, 1, 0)
        proxyLayout.aW..(filterPatternLineEdit, 1, 1)
        proxyLayout.aW..(filterSyntaxComboBox, 1, 2)
        proxyLayout.aW..(filterCaseSensitivityCheckBox, 2, 0, 1, 3)
        proxyLayout.aW..(fromLabel, 3, 0)
        proxyLayout.aW..(fromDateEdit, 3, 1, 1, 2)
        proxyLayout.aW..(toLabel, 4, 0)
        proxyLayout.aW..(toDateEdit, 4, 1, 1, 2)
        proxyGroupBox _ ?GB..("Sorted/Filtered Model")
        proxyGroupBox.sL..(proxyLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(sourceGroupBox)
        mainLayout.aW..(proxyGroupBox)
        sL..(mainLayout)

        sWT..("Custom Sort/Filter Model")
        r..(500, 450)

    ___ setSourceModel  model):
        proxyModel.setSourceModel(model)
        sourceView.sM..(model)

    ___ textFilterChanged
        syntax _ QRegExp.PatternSyntax(
            filterSyntaxComboBox.itemData(
                filterSyntaxComboBox.currentIndex()))
        caseSensitivity _ (
            filterCaseSensitivityCheckBox.isChecked()
            and __.CaseSensitive or __.CaseInsensitive)
        regExp _ QRegExp(filterPatternLineEdit.t__(), caseSensitivity, syntax)
        proxyModel.setFilterRegExp(regExp)

    ___ dateFilterChanged
        proxyModel.setFilterMinimumDate(fromDateEdit.date())
        proxyModel.setFilterMaximumDate(toDateEdit.date())


___ addMail(model, subject, sender, date):
    model.insertRow(0)
    model.setData(model.i..(0, 0), subject)
    model.setData(model.i..(0, 1), sender)
    model.setData(model.index(0, 2), date)


___ createMailModel(parent):
    model _ ?SIM..(0, 3, parent)

    model.setHeaderData(0, __.H.., "Subject")
    model.setHeaderData(1, __.H.., "Sender")
    model.setHeaderData(2, __.H.., "Date")

    addMail(model, "Happy New Year!", "Grace K. <grace@software-inc.com>",
            ?DT__(?D..(2006, 12, 31), ?T..(17, 3)))
    addMail(model, "Radically new concept", "Grace K. <grace@software-inc.com>",
            ?DT__(?D..(2006, 12, 22), ?T..(9, 44)))
    addMail(model, "Accounts", "pascale@nospam.com",
            ?DT__(?D..(2006, 12, 31), ?T..(12, 50)))
    addMail(model, "Expenses", "Joe Bloggs <joe@bloggs.com>",
            ?DT__(?D..(2006, 12, 25), ?T..(11, 39)))
    addMail(model, "Re: Expenses", "Andy <andy@nospam.com>",
            ?DT__(?D..(2007, 1, 2), ?T..(16, 5)))
    addMail(model, "Re: Accounts", "Joe Bloggs <joe@bloggs.com>",
            ?DT__(?D..(2007, 1, 3), ?T..(14, 18)))
    addMail(model, "Re: Accounts", "Andy <andy@nospam.com>",
            ?DT__(?D..(2007, 1, 3), ?T..(14, 26)))
    addMail(model, "Sports", "Linda Smith <linda.smith@nospam.com>",
            ?DT__(?D..(2007, 1, 5), ?T..(11, 33)))
    addMail(model, "AW: Sports", "Rolf Newschweinstein <rolfn@nospam.com>",
            ?DT__(?D..(2007, 1, 5), ?T..(12, 0)))
    addMail(model, "RE: Sports", "Petra Schmidt <petras@nospam.com>",
            ?DT__(?D..(2007, 1, 5), ?T..(12, 1)))

    r_ model


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..

    window _ Window()
    window.setSourceModel(createMailModel(window))
    window.s..

    ___.e.. ?.e..
