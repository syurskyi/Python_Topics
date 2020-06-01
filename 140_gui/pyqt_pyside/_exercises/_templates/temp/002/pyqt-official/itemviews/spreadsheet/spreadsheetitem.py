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
____ ?.?W.. ______ QTableWidgetItem

____ util ______ decode_pos


c_ SpreadSheetItem(QTableWidgetItem):

    ___ __init__  text_None):
        __ t__ __ no. N..:
            super(SpreadSheetItem, self).__init__(t__)
        ____
            super(SpreadSheetItem, self).__init__()

        self.isResolving _ False

    ___ clone(self):
        item _ super(SpreadSheetItem, self).clone()
        item.isResolving _ self.isResolving

        r_ item

    ___ formula(self):
        r_ super(SpreadSheetItem, self).data(__.DisplayRole)

    ___ data  role):
        __ role in (__.EditRole, __.StatusTipRole):
            r_ self.formula()
        __ role == __.DisplayRole:
            r_ self.display()
        t _ str(self.display())
        try:
            number _ int(t)
        except ValueError:
            number _ N..
        __ role == __.TextColorRole:
            __ number __ N..:
                r_ ?C..(__.black)
            ____ number < 0:
                r_ ?C..(__.red)
            r_ ?C..(__.blue)

        __ role == __.TextAlignmentRole:
            __ t and (t[0].isdigit() or t[0] == '-'):
                r_ __.AlignRight | __.AlignVCenter
        r_ super(SpreadSheetItem, self).data(role)

    ___ setData  role, value):
        super(SpreadSheetItem, self).setData(role, value)
        __ self.tableWidget
            self.tableWidget().viewport().update()

    ___ display(self):
        # avoid circular dependencies
        __ self.isResolving:
            r_ N..
        self.isResolving _ True
        result _ self.computeFormula(self.formula(), self.tableWidget())
        self.isResolving _ False
        r_ result

    ___ computeFormula  formula, widget):
        __ formula __ N..:
            r_ N..
        # check if the string is actually a formula or not
        slist _ formula.split(' ')
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
        try:
            firstVal _ start and int(start.t__()) or 0
        except ValueError:
            pass
        secondVal _ 0
        try:
            secondVal _ end and int(end.t__()) or 0
        except ValueError:
            pass
        result _ N..
        __ op == "sum":
            sum_ _ 0
            for r in range(firstRow, secondRow + 1):
                for c in range(firstCol, secondCol + 1):
                    tableItem _ widget.item(r, c)
                    __ tableItem and tableItem !_ self:
                        try:
                            sum_ +_ int(tableItem.t__())
                        except ValueError:
                            pass
            result _ sum_
        ____ op == "+":
            result _ (firstVal + secondVal)
        ____ op == "-":
            result _ (firstVal - secondVal)
        ____ op == "*":
            result _ (firstVal * secondVal)
        ____ op == "/":
            __ secondVal == 0:
                result _ "nan"
            ____
                result _ (firstVal / secondVal)
        ____ op == "=":
            __ start:
                result _ start.t__()
        ____
            result _ formula
        r_ result
