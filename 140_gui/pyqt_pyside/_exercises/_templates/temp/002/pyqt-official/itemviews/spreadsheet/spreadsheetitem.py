#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2012 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
## Contact: Nokia Corporation (qt-info@nokia.com)
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## GNU Lesser General Public License Usage
## This file may be used under the terms of the GNU Lesser General Public
## License version 2.1 as published by the Free Software Foundation and
## appearing in the file LICENSE.LGPL included in the packaging of this
## file. Please review the following information to ensure the GNU Lesser
## General Public License version 2.1 requirements will be met:
## http:#www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights. These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU General
## Public License version 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of this
## file. Please review the following information to ensure the GNU General
## Public License version 3.0 requirements will be met:
## http:#www.gnu.org/copyleft/gpl.html.
##
## Other Usage
## Alternatively, this file may be used in accordance with the terms and
## conditions contained in a signed written agreement between you and Nokia.
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ __
____ ?.?G.. ______ ?C..
____ ?.?W.. ______ ?TWI..

____ util ______ decode_pos


c_ SpreadSheetItem(?TWI..):

    ___  -   text_None):
        __ t__ __ no. N..:
            s__(SpreadSheetItem, self). - (t__)
        ____
            s__(SpreadSheetItem, self). - ()

        isResolving _ F..

    ___ clone
        item _ s__(SpreadSheetItem, self).clone()
        item.isResolving _ isResolving

        r_ item

    ___ formula
        r_ s__(SpreadSheetItem, self).data(__.DR..)

    ___ data  role):
        __ role __ (__.ER.., __.StatusTipRole):
            r_ formula()
        __ role __ __.DR..:
            r_ display()
        t _ st.(display())
        ___
            number _ in.(t)
        _____ V..:
            number _ N..
        __ role __ __.TextColorRole:
            __ number __ N..:
                r_ ?C..(__.black)
            ____ number < 0:
                r_ ?C..(__.red)
            r_ ?C..(__.blue)

        __ role __ __.TextAlignmentRole:
            __ t and (t[0].i_d.. or t[0] __ '-'):
                r_ __.AlignRight | __.AlignVCenter
        r_ s__(SpreadSheetItem, self).data(role)

    ___ setData  role, value):
        s__(SpreadSheetItem, self).setData(role, value)
        __ tableWidget
            tableWidget().viewport().update()

    ___ display
        # avoid circular dependencies
        __ isResolving:
            r_ N..
        isResolving _ T..
        result _ computeFormula(formula(), tableWidget())
        isResolving _ F..
        r_ result

    ___ computeFormula  formula, widget):
        __ formula __ N..:
            r_ N..
        # check if the string is actually a formula or not
        slist _ formula.sp..(' ')
        __ no. slist or no. widget:
            # it is a normal string
            r_ formula
        op _ slist[0].lower()
        firstRow _ -1
        firstCol _ -1
        secondRow _ -1
        secondCol _ -1
        __ le.(slist) > 1:
            firstRow, firstCol _ decode_pos(slist[1])
        __ le.(slist) > 2:
            secondRow, secondCol _ decode_pos(slist[2])
        start _ widget.item(firstRow, firstCol)
        end _ widget.item(secondRow, secondCol)
        firstVal _ 0
        ___
            firstVal _ start and in.(start.t__()) or 0
        _____ V..:
            p..
        secondVal _ 0
        ___
            secondVal _ end and in.(end.t__()) or 0
        _____ V..:
            p..
        result _ N..
        __ op __ "sum":
            sum_ _ 0
            ___ r __ ra..(firstRow, secondRow + 1):
                ___ c __ ra..(firstCol, secondCol + 1):
                    tableItem _ widget.item(r, c)
                    __ tableItem and tableItem !_ self:
                        ___
                            sum_ +_ in.(tableItem.t__())
                        _____ V..:
                            p..
            result _ sum_
        ____ op __ "+":
            result _ (firstVal + secondVal)
        ____ op __ "-":
            result _ (firstVal - secondVal)
        ____ op __ "*":
            result _ (firstVal * secondVal)
        ____ op __ "/":
            __ secondVal __ 0:
                result _ "nan"
            ____
                result _ (firstVal / secondVal)
        ____ op __ "=":
            __ start:
                result _ start.t__()
        ____
            result _ formula
        r_ result
