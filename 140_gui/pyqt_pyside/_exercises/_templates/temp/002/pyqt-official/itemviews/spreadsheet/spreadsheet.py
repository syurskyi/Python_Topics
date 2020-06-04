#!/usr/bin/env python


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


____ ?.?C.. ______ ?D.., QPoint, __
____ ?.?G.. ______ ?C.., ?I.., ?KS.., QPainter, ?P..
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QColorDialog,
        ?CB, ?D.., QFontDialog, ?GB.., ?HBL.., ?L..,
        QLineEdit, ?MW.., ?MB.., ?PB.., ?TW..,
        ?TWI.., QToolBar, ?VBL..)
____ ?.?PS.. ______ QPrinter, QPrintPreviewDialog

______ spreadsheet_rc

____ spreadsheetdelegate ______ SpreadSheetDelegate
____ spreadsheetitem ______ SpreadSheetItem
____ printview ______ PrintView
____ util ______ decode_pos, encode_pos


c_ SpreadSheet ?MW..

    dateFormats _ ["dd/M/yyyy", "yyyy/M/dd", "dd.MM.yyyy"]

    currentDateFormat _ dateFormats[0]

    ___  -   rows, cols, parent _ N..):
        s__(SpreadSheet, self). - (parent)

        toolBar _ ?TB..
        aTB..(toolBar)
        formulaInput _ ?LE..
        cellLabel _ ?L..(toolBar)
        cellLabel.sMS..(80, 0)
        toolBar.aW..(cellLabel)
        toolBar.aW..(formulaInput)
        table _ ?TW..(rows, cols, self)
        ___ c __ ra..(cols):
            character _ chr(ord('A') + c)
            table.setHorizontalHeaderItem(c, ?TWI..(character))

        table.setItemPrototype(table.item(rows - 1, cols - 1))
        table.sID..(SpreadSheetDelegate(self))
        createActions()
        updateColor(0)
        setupMenuBar()
        setupContents()
        setupContextMenu()
        sCW..(table)
        sB..
        table.currentItemChanged.c..(updateStatus)
        table.currentItemChanged.c..(updateColor)
        table.currentItemChanged.c..(updateLineEdit)
        table.itemChanged.c..(updateStatus)
        formulaInput.rP__.c..(rP__)
        table.itemChanged.c..(updateLineEdit)
        sWT..("Spreadsheet")

    ___ createActions 
        cell_sumAction _ ?A..("Sum", self)
        cell_sumAction.t__.c..(actionSum)

        cell_addAction _ ?A..("&Add", self)
        cell_addAction.sS..(__.CTRL | __.Key_Plus)
        cell_addAction.t__.c..(actionAdd)

        cell_subAction _ ?A..("&Subtract", self)
        cell_subAction.sS..(__.CTRL | __.Key_Minus)
        cell_subAction.t__.c..(actionSubtract)

        cell_mulAction _ ?A..("&Multiply", self)
        cell_mulAction.sS..(__.CTRL | __.Key_multiply)
        cell_mulAction.t__.c..(actionMultiply)

        cell_divAction _ ?A..("&Divide", self)
        cell_divAction.sS..(__.CTRL | __.Key_division)
        cell_divAction.t__.c..(actionDivide)

        fontAction _ ?A..("Font...", self)
        fontAction.sS..(__.CTRL | __.Key_F)
        fontAction.t__.c..(selectFont)

        colorAction _ ?A..(?I..(?P..(16, 16)), "Background &Color...", self)
        colorAction.t__.c..(selectColor)

        clearAction _ ?A..("Clear", self)
        clearAction.sS..(__.Key_Delete)
        clearAction.t__.c..(clear)

        aboutSpreadSheet _ ?A..("About Spreadsheet", self)
        aboutSpreadSheet.t__.c..(showAbout)

        exitAction _ ?A..("E&xit", self)
        exitAction.sS..(?KS...Quit)
        exitAction.t__.c..(?A...i.. .quit)

        printAction _ ?A..("&Print", self)
        printAction.sS..(?KS...Print)
        printAction.t__.c..(print_)

        firstSeparator _ ?A..
        firstSeparator.setSeparator( st.

        secondSeparator _ ?A..
        secondSeparator.setSeparator( st.

    ___ setupMenuBar 
        fileMenu _ mB.. .aM..("&File")
        dateFormatMenu _ fileMenu.aM..("&Date format")
        dateFormatGroup _ QActionGroup
        ___ f __ dateFormats:
            action _ ?A..(f, self, checkable_True,
                    triggered_self.changeDateFormat)
            dateFormatGroup.aA..(action)
            dateFormatMenu.aA..(action)
            __ f __ currentDateFormat:
                action.sC__( st.
                
        fileMenu.aA..(printAction)
        fileMenu.aA..(exitAction)
        cellMenu _ mB.. .aM..("&Cell")
        cellMenu.aA..(cell_addAction)
        cellMenu.aA..(cell_subAction)
        cellMenu.aA..(cell_mulAction)
        cellMenu.aA..(cell_divAction)
        cellMenu.aA..(cell_sumAction)
        cellMenu.aS..)
        cellMenu.aA..(colorAction)
        cellMenu.aA..(fontAction)
        mB.. .aS..)
        aboutMenu _ mB.. .aM..("&Help")
        aboutMenu.aA..(aboutSpreadSheet)

    ___ changeDateFormat 
        action _ sender()
        oldFormat _ currentDateFormat
        newFormat _ currentDateFormat _ action.t__()
        ___ row __ ra..(table.rowCount()):
            item _ table.item(row, 1)
            date _ ?D...fromString(item.t__(), oldFormat)
            item.sT..(date.toString(newFormat))

    ___ updateStatus  item):
        __ item and item __ table.currentItem
            sB.. .sM..(item.data(__.StatusTipRole), 1000)
            cellLabel.sT..("Cell: (%s)" % encode_pos(table.row(item),
                                                                     table.column(item)))

    ___ updateColor  item):
        pixmap _ ?P..(16, 16)
        color _ ?C..()
        __ item:
            color _ item.backgroundColor()
        __ no. color.isValid
            color _ p...base().color()
        painter _ QPainter(pixmap)
        painter.fillRect(0, 0, 16, 16, color)
        lighter _ color.lighter()
        painter.sP..(lighter)
        # light frame
        painter.drawPolyline(QPoint(0, 15), QPoint(0, 0), QPoint(15, 0))
        painter.sP..(color.darker())
        # dark frame
        painter.drawPolyline(QPoint(1, 15), QPoint(15, 15), QPoint(15, 1))
        painter.end()
        colorAction.sI..(?I..(pixmap))

    ___ updateLineEdit  item):
        __ item !_ table.currentItem
            r_
        __ item:
            formulaInput.sT..(item.data(__.ER..))
        ____
            formulaInput.c..

    ___ rP__ 
        t__ _ formulaInput.t__()
        row _ table.cR..
        col _ table.currentColumn()
        item _ table.item(row, col)
        __ no. item:
            table.setItem(row, col, SpreadSheetItem(t__))
        ____
            item.setData(__.ER.., t__)
        table.viewport().update()

    ___ selectColor 
        item _ table.currentItem()
        color _ item and ?C..(item.background()) or table.p...base().color()
        color _ QColorDialog.getColor(color, self)
        __ no. color.isValid
            r_
        selected _ table.selectedItems()
        __ no. selected:
            r_
        ___ i __ selected:
            i and i.setBackground(color)
        updateColor(table.currentItem())

    ___ selectFont 
        selected _ table.selectedItems()
        __ no. selected:
            r_
        font, ok _ QFontDialog.getFont(font(), self)
        __ no. ok:
            r_
        ___ i __ selected:
            i and i.sF..(font)

    ___ runInputDialog  title, c1Text, c2Text, opText,
                       outText, cell1, cell2, outCell):
        rows _   # list
        cols _   # list
        ___ r __ ra..(table.rowCount()):
            rows.ap..(st.(r + 1))
        ___ c __ ra..(table.columnCount()):
            cols.ap..(chr(ord('A') + c))
        addDialog _ ?D..
        addDialog.sWT..(title)
        group _ ?GB..(title, addDialog)
        group.sMS..(250, 100)
        cell1Label _ ?L..(c1Text, group)
        cell1RowInput _ ?CB(group)
        c1Row, c1Col _ decode_pos(cell1)
        cell1RowInput.aI..(rows)
        cell1RowInput.sCI..(c1Row)
        cell1ColInput _ ?CB(group)
        cell1ColInput.aI..(cols)
        cell1ColInput.sCI..(c1Col)
        operatorLabel _ ?L..(opText, group)
        operatorLabel.setAlignment(__.AlignHCenter)
        cell2Label _ ?L..(c2Text, group)
        cell2RowInput _ ?CB(group)
        c2Row, c2Col _ decode_pos(cell2)
        cell2RowInput.aI..(rows)
        cell2RowInput.sCI..(c2Row)
        cell2ColInput _ ?CB(group)
        cell2ColInput.aI..(cols)
        cell2ColInput.sCI..(c2Col)
        equalsLabel _ ?L..("=", group)
        equalsLabel.setAlignment(__.AlignHCenter)
        outLabel _ ?L..(outText, group)
        outRowInput _ ?CB(group)
        outRow, outCol _ decode_pos(outCell)
        outRowInput.aI..(rows)
        outRowInput.sCI..(outRow)
        outColInput _ ?CB(group)
        outColInput.aI..(cols)
        outColInput.sCI..(outCol)

        cancelButton _ ?PB..("Cancel", addDialog)
        cancelButton.c__.c..(addDialog.reject)
        okButton _ ?PB..("OK", addDialog)
        okButton.setDefault( st.
        okButton.c__.c..(addDialog.accept)
        buttonsLayout _ ?HBL..
        buttonsLayout.addStretch(1)
        buttonsLayout.aW..(okButton)
        buttonsLayout.addSpacing(10)
        buttonsLayout.aW..(cancelButton)

        dialogLayout _ ?VBL..(addDialog)
        dialogLayout.aW..(group)
        dialogLayout.addStretch(1)
        dialogLayout.aI..(buttonsLayout)

        cell1Layout _ ?HBL..
        cell1Layout.aW..(cell1Label)
        cell1Layout.addSpacing(10)
        cell1Layout.aW..(cell1ColInput)
        cell1Layout.addSpacing(10)
        cell1Layout.aW..(cell1RowInput)

        cell2Layout _ ?HBL..
        cell2Layout.aW..(cell2Label)
        cell2Layout.addSpacing(10)
        cell2Layout.aW..(cell2ColInput)
        cell2Layout.addSpacing(10)
        cell2Layout.aW..(cell2RowInput)
        outLayout _ ?HBL..
        outLayout.aW..(outLabel)
        outLayout.addSpacing(10)
        outLayout.aW..(outColInput)
        outLayout.addSpacing(10)
        outLayout.aW..(outRowInput)
        vLayout _ ?VBL..(group)
        vLayout.aI..(cell1Layout)
        vLayout.aW..(operatorLabel)
        vLayout.aI..(cell2Layout)
        vLayout.aW..(equalsLabel)
        vLayout.addStretch(1)
        vLayout.aI..(outLayout)
        __ addDialog.e..
            cell1 _ cell1ColInput.currentText() + cell1RowInput.currentText()
            cell2 _ cell2ColInput.currentText() + cell2RowInput.currentText()
            outCell _ outColInput.currentText() + outRowInput.currentText()
            r_ T.., cell1, cell2, outCell

        r_ F.., N.., N.., N..

    ___ actionSum 
        row_first _ 0
        row_last _ 0
        row_cur _ 0
        col_first _ 0
        col_last _ 0
        col_cur _ 0
        selected _ table.selectedItems()
        __ selected:
            first _ selected[0]
            last _ selected[-1]
            row_first _ table.row(first)
            row_last _ table.row(last)
            col_first _ table.column(first)
            col_last _ table.column(last)

        current _ table.currentItem()
        __ current:
            row_cur _ table.row(current)
            col_cur _ table.column(current)

        cell1 _ encode_pos(row_first, col_first)
        cell2 _ encode_pos(row_last, col_last)
        out _ encode_pos(row_cur, col_cur)
        ok, cell1, cell2, out _ runInputDialog("Sum cells", "First cell:",
                "Last cell:", u"\N{GREEK CAPITAL LETTER SIGMA}", "Output to:",
                cell1, cell2, out)
        __ ok:
            row, col _ decode_pos(out)
            table.item(row, col).sT..("sum %s %s" % (cell1, cell2))

    ___ actionMath_helper  title, op):
        cell1 _ "C1"
        cell2 _ "C2"
        out _ "C3"
        current _ table.currentItem()
        __ current:
            out _ encode_pos(table.cR.., table.currentColumn())
        ok, cell1, cell2, out _ runInputDialog(title, "Cell 1", "Cell 2",
                op, "Output to:", cell1, cell2, out)
        __ ok:
            row, col _ decode_pos(out)
            table.item(row, col).sT..("%s %s %s" % (op, cell1, cell2))

    ___ actionAdd 
        actionMath_helper("Addition", "+")

    ___ actionSubtract 
        actionMath_helper("Subtraction", "-")

    ___ actionMultiply 
        actionMath_helper("Multiplication", "*")

    ___ actionDivide 
        actionMath_helper("Division", "/")

    ___ clear 
        ___ i __ table.selectedItems
            i.sT..("")

    ___ setupContextMenu 
        aA..(cell_addAction)
        aA..(cell_subAction)
        aA..(cell_mulAction)
        aA..(cell_divAction)
        aA..(cell_sumAction)
        aA..(firstSeparator)
        aA..(colorAction)
        aA..(fontAction)
        aA..(secondSeparator)
        aA..(clearAction)
        sCMP..(__.ACM..)

    ___ setupContents 
        titleBackground _ ?C..(__.lightGray)
        titleFont _ table.font()
        titleFont.setBold( st.
        # column 0
        table.setItem(0, 0, SpreadSheetItem("Item"))
        table.item(0, 0).setBackground(titleBackground)
        table.item(0, 0).sTT..("This column shows the purchased item/service")
        table.item(0, 0).sF..(titleFont)
        table.setItem(1, 0, SpreadSheetItem("AirportBus"))
        table.setItem(2, 0, SpreadSheetItem("Flight (Munich)"))
        table.setItem(3, 0, SpreadSheetItem("Lunch"))
        table.setItem(4, 0, SpreadSheetItem("Flight (LA)"))
        table.setItem(5, 0, SpreadSheetItem("Taxi"))
        table.setItem(6, 0, SpreadSheetItem("Dinner"))
        table.setItem(7, 0, SpreadSheetItem("Hotel"))
        table.setItem(8, 0, SpreadSheetItem("Flight (Oslo)"))
        table.setItem(9, 0, SpreadSheetItem("Total:"))
        table.item(9, 0).sF..(titleFont)
        table.item(9, 0).setBackground(__.lightGray)
        # column 1
        table.setItem(0, 1, SpreadSheetItem("Date"))
        table.item(0, 1).setBackground(titleBackground)
        table.item(0, 1).sTT..("This column shows the purchase date, double click to change")
        table.item(0, 1).sF..(titleFont)
        table.setItem(1, 1, SpreadSheetItem("15/6/2006"))
        table.setItem(2, 1, SpreadSheetItem("15/6/2006"))
        table.setItem(3, 1, SpreadSheetItem("15/6/2006"))
        table.setItem(4, 1, SpreadSheetItem("21/5/2006"))
        table.setItem(5, 1, SpreadSheetItem("16/6/2006"))
        table.setItem(6, 1, SpreadSheetItem("16/6/2006"))
        table.setItem(7, 1, SpreadSheetItem("16/6/2006"))
        table.setItem(8, 1, SpreadSheetItem("18/6/2006"))
        table.setItem(9, 1, SpreadSheetItem())
        table.item(9, 1).setBackground(__.lightGray)
        # column 2
        table.setItem(0, 2, SpreadSheetItem("Price"))
        table.item(0, 2).setBackground(titleBackground)
        table.item(0, 2).sTT..("This column shows the price of the purchase")
        table.item(0, 2).sF..(titleFont)
        table.setItem(1, 2, SpreadSheetItem("150"))
        table.setItem(2, 2, SpreadSheetItem("2350"))
        table.setItem(3, 2, SpreadSheetItem("-14"))
        table.setItem(4, 2, SpreadSheetItem("980"))
        table.setItem(5, 2, SpreadSheetItem("5"))
        table.setItem(6, 2, SpreadSheetItem("120"))
        table.setItem(7, 2, SpreadSheetItem("300"))
        table.setItem(8, 2, SpreadSheetItem("1240"))
        table.setItem(9, 2, SpreadSheetItem())
        table.item(9, 2).setBackground(__.lightGray)
        # column 3
        table.setItem(0, 3, SpreadSheetItem("Currency"))
        table.item(0, 3).setBackgroundColor(titleBackground)
        table.item(0, 3).sTT..("This column shows the currency")
        table.item(0, 3).sF..(titleFont)
        table.setItem(1, 3, SpreadSheetItem("NOK"))
        table.setItem(2, 3, SpreadSheetItem("NOK"))
        table.setItem(3, 3, SpreadSheetItem("EUR"))
        table.setItem(4, 3, SpreadSheetItem("EUR"))
        table.setItem(5, 3, SpreadSheetItem("USD"))
        table.setItem(6, 3, SpreadSheetItem("USD"))
        table.setItem(7, 3, SpreadSheetItem("USD"))
        table.setItem(8, 3, SpreadSheetItem("USD"))
        table.setItem(9, 3, SpreadSheetItem())
        table.item(9,3).setBackground(__.lightGray)
        # column 4
        table.setItem(0, 4, SpreadSheetItem("Ex. Rate"))
        table.item(0, 4).setBackground(titleBackground)
        table.item(0, 4).sTT..("This column shows the exchange rate to NOK")
        table.item(0, 4).sF..(titleFont)
        table.setItem(1, 4, SpreadSheetItem("1"))
        table.setItem(2, 4, SpreadSheetItem("1"))
        table.setItem(3, 4, SpreadSheetItem("8"))
        table.setItem(4, 4, SpreadSheetItem("8"))
        table.setItem(5, 4, SpreadSheetItem("7"))
        table.setItem(6, 4, SpreadSheetItem("7"))
        table.setItem(7, 4, SpreadSheetItem("7"))
        table.setItem(8, 4, SpreadSheetItem("7"))
        table.setItem(9, 4, SpreadSheetItem())
        table.item(9,4).setBackground(__.lightGray)
        # column 5
        table.setItem(0, 5, SpreadSheetItem("NOK"))
        table.item(0, 5).setBackground(titleBackground)
        table.item(0, 5).sTT..("This column shows the expenses in NOK")
        table.item(0, 5).sF..(titleFont)
        table.setItem(1, 5, SpreadSheetItem("* C2 E2"))
        table.setItem(2, 5, SpreadSheetItem("* C3 E3"))
        table.setItem(3, 5, SpreadSheetItem("* C4 E4"))
        table.setItem(4, 5, SpreadSheetItem("* C5 E5"))
        table.setItem(5, 5, SpreadSheetItem("* C6 E6"))
        table.setItem(6, 5, SpreadSheetItem("* C7 E7"))
        table.setItem(7, 5, SpreadSheetItem("* C8 E8"))
        table.setItem(8, 5, SpreadSheetItem("* C9 E9"))
        table.setItem(9, 5, SpreadSheetItem("sum F2 F9"))
        table.item(9,5).setBackground(__.lightGray)

    ___ showAbout 
        ?MB...about  "About Spreadsheet", """
            <HTML>
            <p><b>This demo shows use of <c>QTableWidget</c> with custom handling for
             individual cells.</b></p>
            <p>Using a customized table item we make it possible to have dynamic
             output in different cells. The content that is implemented for this
             particular demo is:
            <ul>
            <li>Adding two cells.</li>
            <li>Subtracting one cell from another.</li>
            <li>Multiplying two cells.</li>
            <li>Dividing one cell with another.</li>
            <li>Summing the contents of an arbitrary number of cells.</li>
            </HTML>
        """)

    ___ print_ 
        printer _ QPrinter(QPrinter.ScreenResolution)
        dlg _ QPrintPreviewDialog(printer)
        view _ PrintView()
        view.sM..(table.model())
        dlg.paintRequested.c..(view.print_)
        dlg.e..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    sheet _ SpreadSheet(10, 6)
    sheet.sWI..(?I..(?P..(":/images/interview.png")))
    sheet.r..(640, 420)
    sheet.s..
    ___.e.. ?.e..
