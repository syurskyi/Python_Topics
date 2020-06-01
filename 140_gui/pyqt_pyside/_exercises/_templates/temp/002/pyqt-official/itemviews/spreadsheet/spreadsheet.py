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


____ ?.QtCore ______ QDate, QPoint, Qt
____ ?.?G.. ______ QColor, QIcon, ?KS.., QPainter, QPixmap
____ ?.?W.. ______ (?A.., QActionGroup, ?A.., QColorDialog,
        QComboBox, QDialog, QFontDialog, QGroupBox, QHBoxLayout, QLabel,
        QLineEdit, QMainWindow, ?MB.., ?PB.., QTableWidget,
        QTableWidgetItem, QToolBar, QVBoxLayout)
____ ?.QtPrintSupport ______ QPrinter, QPrintPreviewDialog

______ spreadsheet_rc

____ spreadsheetdelegate ______ SpreadSheetDelegate
____ spreadsheetitem ______ SpreadSheetItem
____ printview ______ PrintView
____ util ______ decode_pos, encode_pos


c_ SpreadSheet ?MW..

    dateFormats _ ["dd/M/yyyy", "yyyy/M/dd", "dd.MM.yyyy"]

    currentDateFormat _ dateFormats[0]

    ___ __init__  rows, cols, parent _ N..):
        super(SpreadSheet, self).__init__(parent)

        self.toolBar _ QToolBar()
        self.addToolBar(self.toolBar)
        self.formulaInput _ QLineEdit()
        self.cellLabel _ QLabel(self.toolBar)
        self.cellLabel.setMinimumSize(80, 0)
        self.toolBar.addWidget(self.cellLabel)
        self.toolBar.addWidget(self.formulaInput)
        self.table _ QTableWidget(rows, cols, self)
        for c in range(cols):
            character _ chr(ord('A') + c)
            self.table.setHorizontalHeaderItem(c, QTableWidgetItem(character))

        self.table.setItemPrototype(self.table.item(rows - 1, cols - 1))
        self.table.setItemDelegate(SpreadSheetDelegate(self))
        self.createActions()
        self.updateColor(0)
        self.setupMenuBar()
        self.setupContents()
        self.setupContextMenu()
        self.sCW..(self.table)
        self.statusBar()
        self.table.currentItemChanged.c..(self.updateStatus)
        self.table.currentItemChanged.c..(self.updateColor)
        self.table.currentItemChanged.c..(self.updateLineEdit)
        self.table.itemChanged.c..(self.updateStatus)
        self.formulaInput.returnPressed.c..(self.returnPressed)
        self.table.itemChanged.c..(self.updateLineEdit)
        self.setWindowTitle("Spreadsheet")

    ___ createActions(self):
        self.cell_sumAction _ ?A..("Sum", self)
        self.cell_sumAction.t__.c..(self.actionSum)

        self.cell_addAction _ ?A..("&Add", self)
        self.cell_addAction.sS..(Qt.CTRL | Qt.Key_Plus)
        self.cell_addAction.t__.c..(self.actionAdd)

        self.cell_subAction _ ?A..("&Subtract", self)
        self.cell_subAction.sS..(Qt.CTRL | Qt.Key_Minus)
        self.cell_subAction.t__.c..(self.actionSubtract)

        self.cell_mulAction _ ?A..("&Multiply", self)
        self.cell_mulAction.sS..(Qt.CTRL | Qt.Key_multiply)
        self.cell_mulAction.t__.c..(self.actionMultiply)

        self.cell_divAction _ ?A..("&Divide", self)
        self.cell_divAction.sS..(Qt.CTRL | Qt.Key_division)
        self.cell_divAction.t__.c..(self.actionDivide)

        self.fontAction _ ?A..("Font...", self)
        self.fontAction.sS..(Qt.CTRL | Qt.Key_F)
        self.fontAction.t__.c..(self.selectFont)

        self.colorAction _ ?A..(QIcon(QPixmap(16, 16)), "Background &Color...", self)
        self.colorAction.t__.c..(self.selectColor)

        self.clearAction _ ?A..("Clear", self)
        self.clearAction.sS..(Qt.Key_Delete)
        self.clearAction.t__.c..(self.clear)

        self.aboutSpreadSheet _ ?A..("About Spreadsheet", self)
        self.aboutSpreadSheet.t__.c..(self.showAbout)

        self.exitAction _ ?A..("E&xit", self)
        self.exitAction.sS..(?KS...Quit)
        self.exitAction.t__.c..(?A...instance().quit)

        self.printAction _ ?A..("&Print", self)
        self.printAction.sS..(?KS...Print)
        self.printAction.t__.c..(self.print_)

        self.firstSeparator _ ?A..(self)
        self.firstSeparator.setSeparator(True)

        self.secondSeparator _ ?A..(self)
        self.secondSeparator.setSeparator(True)

    ___ setupMenuBar(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.dateFormatMenu _ self.fileMenu.aM..("&Date format")
        self.dateFormatGroup _ QActionGroup(self)
        for f in self.dateFormats:
            action _ ?A..(f, self, checkable_True,
                    triggered_self.changeDateFormat)
            self.dateFormatGroup.aA..(action)
            self.dateFormatMenu.aA..(action)
            __ f == self.currentDateFormat:
                action.setChecked(True)
                
        self.fileMenu.aA..(self.printAction)
        self.fileMenu.aA..(self.exitAction)
        self.cellMenu _ self.mB.. .aM..("&Cell")
        self.cellMenu.aA..(self.cell_addAction)
        self.cellMenu.aA..(self.cell_subAction)
        self.cellMenu.aA..(self.cell_mulAction)
        self.cellMenu.aA..(self.cell_divAction)
        self.cellMenu.aA..(self.cell_sumAction)
        self.cellMenu.addSeparator()
        self.cellMenu.aA..(self.colorAction)
        self.cellMenu.aA..(self.fontAction)
        self.mB.. .addSeparator()
        self.aboutMenu _ self.mB.. .aM..("&Help")
        self.aboutMenu.aA..(self.aboutSpreadSheet)

    ___ changeDateFormat(self):
        action _ self.sender()
        oldFormat _ self.currentDateFormat
        newFormat _ self.currentDateFormat _ action.text()
        for row in range(self.table.rowCount()):
            item _ self.table.item(row, 1)
            date _ QDate.fromString(item.text(), oldFormat)
            item.sT..(date.toString(newFormat))

    ___ updateStatus  item):
        __ item and item == self.table.currentItem
            self.statusBar().showMessage(item.data(Qt.StatusTipRole), 1000)
            self.cellLabel.sT..("Cell: (%s)" % encode_pos(self.table.row(item),
                                                                     self.table.column(item)))

    ___ updateColor  item):
        pixmap _ QPixmap(16, 16)
        color _ QColor()
        __ item:
            color _ item.backgroundColor()
        __ no. color.isValid
            color _ self.palette().base().color()
        painter _ QPainter(pixmap)
        painter.fillRect(0, 0, 16, 16, color)
        lighter _ color.lighter()
        painter.setPen(lighter)
        # light frame
        painter.drawPolyline(QPoint(0, 15), QPoint(0, 0), QPoint(15, 0))
        painter.setPen(color.darker())
        # dark frame
        painter.drawPolyline(QPoint(1, 15), QPoint(15, 15), QPoint(15, 1))
        painter.end()
        self.colorAction.setIcon(QIcon(pixmap))

    ___ updateLineEdit  item):
        __ item !_ self.table.currentItem
            r_
        __ item:
            self.formulaInput.sT..(item.data(Qt.EditRole))
        ____
            self.formulaInput.clear()

    ___ returnPressed(self):
        text _ self.formulaInput.text()
        row _ self.table.currentRow()
        col _ self.table.currentColumn()
        item _ self.table.item(row, col)
        __ no. item:
            self.table.setItem(row, col, SpreadSheetItem(text))
        ____
            item.setData(Qt.EditRole, text)
        self.table.viewport().update()

    ___ selectColor(self):
        item _ self.table.currentItem()
        color _ item and QColor(item.background()) or self.table.palette().base().color()
        color _ QColorDialog.getColor(color, self)
        __ no. color.isValid
            r_
        selected _ self.table.selectedItems()
        __ no. selected:
            r_
        for i in selected:
            i and i.setBackground(color)
        self.updateColor(self.table.currentItem())

    ___ selectFont(self):
        selected _ self.table.selectedItems()
        __ no. selected:
            r_
        font, ok _ QFontDialog.getFont(self.font(), self)
        __ no. ok:
            r_
        for i in selected:
            i and i.setFont(font)

    ___ runInputDialog  title, c1Text, c2Text, opText,
                       outText, cell1, cell2, outCell):
        rows _ []
        cols _ []
        for r in range(self.table.rowCount()):
            rows.append(str(r + 1))
        for c in range(self.table.columnCount()):
            cols.append(chr(ord('A') + c))
        addDialog _ QDialog(self)
        addDialog.setWindowTitle(title)
        group _ QGroupBox(title, addDialog)
        group.setMinimumSize(250, 100)
        cell1Label _ QLabel(c1Text, group)
        cell1RowInput _ QComboBox(group)
        c1Row, c1Col _ decode_pos(cell1)
        cell1RowInput.addItems(rows)
        cell1RowInput.setCurrentIndex(c1Row)
        cell1ColInput _ QComboBox(group)
        cell1ColInput.addItems(cols)
        cell1ColInput.setCurrentIndex(c1Col)
        operatorLabel _ QLabel(opText, group)
        operatorLabel.setAlignment(Qt.AlignHCenter)
        cell2Label _ QLabel(c2Text, group)
        cell2RowInput _ QComboBox(group)
        c2Row, c2Col _ decode_pos(cell2)
        cell2RowInput.addItems(rows)
        cell2RowInput.setCurrentIndex(c2Row)
        cell2ColInput _ QComboBox(group)
        cell2ColInput.addItems(cols)
        cell2ColInput.setCurrentIndex(c2Col)
        equalsLabel _ QLabel("=", group)
        equalsLabel.setAlignment(Qt.AlignHCenter)
        outLabel _ QLabel(outText, group)
        outRowInput _ QComboBox(group)
        outRow, outCol _ decode_pos(outCell)
        outRowInput.addItems(rows)
        outRowInput.setCurrentIndex(outRow)
        outColInput _ QComboBox(group)
        outColInput.addItems(cols)
        outColInput.setCurrentIndex(outCol)

        cancelButton _ ?PB..("Cancel", addDialog)
        cancelButton.c__.c..(addDialog.reject)
        okButton _ ?PB..("OK", addDialog)
        okButton.setDefault(True)
        okButton.c__.c..(addDialog.accept)
        buttonsLayout _ QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(okButton)
        buttonsLayout.addSpacing(10)
        buttonsLayout.addWidget(cancelButton)

        dialogLayout _ QVBoxLayout(addDialog)
        dialogLayout.addWidget(group)
        dialogLayout.addStretch(1)
        dialogLayout.addItem(buttonsLayout)

        cell1Layout _ QHBoxLayout()
        cell1Layout.addWidget(cell1Label)
        cell1Layout.addSpacing(10)
        cell1Layout.addWidget(cell1ColInput)
        cell1Layout.addSpacing(10)
        cell1Layout.addWidget(cell1RowInput)

        cell2Layout _ QHBoxLayout()
        cell2Layout.addWidget(cell2Label)
        cell2Layout.addSpacing(10)
        cell2Layout.addWidget(cell2ColInput)
        cell2Layout.addSpacing(10)
        cell2Layout.addWidget(cell2RowInput)
        outLayout _ QHBoxLayout()
        outLayout.addWidget(outLabel)
        outLayout.addSpacing(10)
        outLayout.addWidget(outColInput)
        outLayout.addSpacing(10)
        outLayout.addWidget(outRowInput)
        vLayout _ QVBoxLayout(group)
        vLayout.addItem(cell1Layout)
        vLayout.addWidget(operatorLabel)
        vLayout.addItem(cell2Layout)
        vLayout.addWidget(equalsLabel)
        vLayout.addStretch(1)
        vLayout.addItem(outLayout)
        __ addDialog.exec_
            cell1 _ cell1ColInput.currentText() + cell1RowInput.currentText()
            cell2 _ cell2ColInput.currentText() + cell2RowInput.currentText()
            outCell _ outColInput.currentText() + outRowInput.currentText()
            r_ True, cell1, cell2, outCell

        r_ False, N.., N.., N..

    ___ actionSum(self):
        row_first _ 0
        row_last _ 0
        row_cur _ 0
        col_first _ 0
        col_last _ 0
        col_cur _ 0
        selected _ self.table.selectedItems()
        __ selected:
            first _ selected[0]
            last _ selected[-1]
            row_first _ self.table.row(first)
            row_last _ self.table.row(last)
            col_first _ self.table.column(first)
            col_last _ self.table.column(last)

        current _ self.table.currentItem()
        __ current:
            row_cur _ self.table.row(current)
            col_cur _ self.table.column(current)

        cell1 _ encode_pos(row_first, col_first)
        cell2 _ encode_pos(row_last, col_last)
        out _ encode_pos(row_cur, col_cur)
        ok, cell1, cell2, out _ self.runInputDialog("Sum cells", "First cell:",
                "Last cell:", u"\N{GREEK CAPITAL LETTER SIGMA}", "Output to:",
                cell1, cell2, out)
        __ ok:
            row, col _ decode_pos(out)
            self.table.item(row, col).sT..("sum %s %s" % (cell1, cell2))

    ___ actionMath_helper  title, op):
        cell1 _ "C1"
        cell2 _ "C2"
        out _ "C3"
        current _ self.table.currentItem()
        __ current:
            out _ encode_pos(self.table.currentRow(), self.table.currentColumn())
        ok, cell1, cell2, out _ self.runInputDialog(title, "Cell 1", "Cell 2",
                op, "Output to:", cell1, cell2, out)
        __ ok:
            row, col _ decode_pos(out)
            self.table.item(row, col).sT..("%s %s %s" % (op, cell1, cell2))

    ___ actionAdd(self):
        self.actionMath_helper("Addition", "+")

    ___ actionSubtract(self):
        self.actionMath_helper("Subtraction", "-")

    ___ actionMultiply(self):
        self.actionMath_helper("Multiplication", "*")

    ___ actionDivide(self):
        self.actionMath_helper("Division", "/")

    ___ clear(self):
        for i in self.table.selectedItems
            i.sT..("")

    ___ setupContextMenu(self):
        self.aA..(self.cell_addAction)
        self.aA..(self.cell_subAction)
        self.aA..(self.cell_mulAction)
        self.aA..(self.cell_divAction)
        self.aA..(self.cell_sumAction)
        self.aA..(self.firstSeparator)
        self.aA..(self.colorAction)
        self.aA..(self.fontAction)
        self.aA..(self.secondSeparator)
        self.aA..(self.clearAction)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

    ___ setupContents(self):
        titleBackground _ QColor(Qt.lightGray)
        titleFont _ self.table.font()
        titleFont.setBold(True)
        # column 0
        self.table.setItem(0, 0, SpreadSheetItem("Item"))
        self.table.item(0, 0).setBackground(titleBackground)
        self.table.item(0, 0).setToolTip("This column shows the purchased item/service")
        self.table.item(0, 0).setFont(titleFont)
        self.table.setItem(1, 0, SpreadSheetItem("AirportBus"))
        self.table.setItem(2, 0, SpreadSheetItem("Flight (Munich)"))
        self.table.setItem(3, 0, SpreadSheetItem("Lunch"))
        self.table.setItem(4, 0, SpreadSheetItem("Flight (LA)"))
        self.table.setItem(5, 0, SpreadSheetItem("Taxi"))
        self.table.setItem(6, 0, SpreadSheetItem("Dinner"))
        self.table.setItem(7, 0, SpreadSheetItem("Hotel"))
        self.table.setItem(8, 0, SpreadSheetItem("Flight (Oslo)"))
        self.table.setItem(9, 0, SpreadSheetItem("Total:"))
        self.table.item(9, 0).setFont(titleFont)
        self.table.item(9, 0).setBackground(Qt.lightGray)
        # column 1
        self.table.setItem(0, 1, SpreadSheetItem("Date"))
        self.table.item(0, 1).setBackground(titleBackground)
        self.table.item(0, 1).setToolTip("This column shows the purchase date, double click to change")
        self.table.item(0, 1).setFont(titleFont)
        self.table.setItem(1, 1, SpreadSheetItem("15/6/2006"))
        self.table.setItem(2, 1, SpreadSheetItem("15/6/2006"))
        self.table.setItem(3, 1, SpreadSheetItem("15/6/2006"))
        self.table.setItem(4, 1, SpreadSheetItem("21/5/2006"))
        self.table.setItem(5, 1, SpreadSheetItem("16/6/2006"))
        self.table.setItem(6, 1, SpreadSheetItem("16/6/2006"))
        self.table.setItem(7, 1, SpreadSheetItem("16/6/2006"))
        self.table.setItem(8, 1, SpreadSheetItem("18/6/2006"))
        self.table.setItem(9, 1, SpreadSheetItem())
        self.table.item(9, 1).setBackground(Qt.lightGray)
        # column 2
        self.table.setItem(0, 2, SpreadSheetItem("Price"))
        self.table.item(0, 2).setBackground(titleBackground)
        self.table.item(0, 2).setToolTip("This column shows the price of the purchase")
        self.table.item(0, 2).setFont(titleFont)
        self.table.setItem(1, 2, SpreadSheetItem("150"))
        self.table.setItem(2, 2, SpreadSheetItem("2350"))
        self.table.setItem(3, 2, SpreadSheetItem("-14"))
        self.table.setItem(4, 2, SpreadSheetItem("980"))
        self.table.setItem(5, 2, SpreadSheetItem("5"))
        self.table.setItem(6, 2, SpreadSheetItem("120"))
        self.table.setItem(7, 2, SpreadSheetItem("300"))
        self.table.setItem(8, 2, SpreadSheetItem("1240"))
        self.table.setItem(9, 2, SpreadSheetItem())
        self.table.item(9, 2).setBackground(Qt.lightGray)
        # column 3
        self.table.setItem(0, 3, SpreadSheetItem("Currency"))
        self.table.item(0, 3).setBackgroundColor(titleBackground)
        self.table.item(0, 3).setToolTip("This column shows the currency")
        self.table.item(0, 3).setFont(titleFont)
        self.table.setItem(1, 3, SpreadSheetItem("NOK"))
        self.table.setItem(2, 3, SpreadSheetItem("NOK"))
        self.table.setItem(3, 3, SpreadSheetItem("EUR"))
        self.table.setItem(4, 3, SpreadSheetItem("EUR"))
        self.table.setItem(5, 3, SpreadSheetItem("USD"))
        self.table.setItem(6, 3, SpreadSheetItem("USD"))
        self.table.setItem(7, 3, SpreadSheetItem("USD"))
        self.table.setItem(8, 3, SpreadSheetItem("USD"))
        self.table.setItem(9, 3, SpreadSheetItem())
        self.table.item(9,3).setBackground(Qt.lightGray)
        # column 4
        self.table.setItem(0, 4, SpreadSheetItem("Ex. Rate"))
        self.table.item(0, 4).setBackground(titleBackground)
        self.table.item(0, 4).setToolTip("This column shows the exchange rate to NOK")
        self.table.item(0, 4).setFont(titleFont)
        self.table.setItem(1, 4, SpreadSheetItem("1"))
        self.table.setItem(2, 4, SpreadSheetItem("1"))
        self.table.setItem(3, 4, SpreadSheetItem("8"))
        self.table.setItem(4, 4, SpreadSheetItem("8"))
        self.table.setItem(5, 4, SpreadSheetItem("7"))
        self.table.setItem(6, 4, SpreadSheetItem("7"))
        self.table.setItem(7, 4, SpreadSheetItem("7"))
        self.table.setItem(8, 4, SpreadSheetItem("7"))
        self.table.setItem(9, 4, SpreadSheetItem())
        self.table.item(9,4).setBackground(Qt.lightGray)
        # column 5
        self.table.setItem(0, 5, SpreadSheetItem("NOK"))
        self.table.item(0, 5).setBackground(titleBackground)
        self.table.item(0, 5).setToolTip("This column shows the expenses in NOK")
        self.table.item(0, 5).setFont(titleFont)
        self.table.setItem(1, 5, SpreadSheetItem("* C2 E2"))
        self.table.setItem(2, 5, SpreadSheetItem("* C3 E3"))
        self.table.setItem(3, 5, SpreadSheetItem("* C4 E4"))
        self.table.setItem(4, 5, SpreadSheetItem("* C5 E5"))
        self.table.setItem(5, 5, SpreadSheetItem("* C6 E6"))
        self.table.setItem(6, 5, SpreadSheetItem("* C7 E7"))
        self.table.setItem(7, 5, SpreadSheetItem("* C8 E8"))
        self.table.setItem(8, 5, SpreadSheetItem("* C9 E9"))
        self.table.setItem(9, 5, SpreadSheetItem("sum F2 F9"))
        self.table.item(9,5).setBackground(Qt.lightGray)

    ___ showAbout(self):
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

    ___ print_(self):
        printer _ QPrinter(QPrinter.ScreenResolution)
        dlg _ QPrintPreviewDialog(printer)
        view _ PrintView()
        view.setModel(self.table.model())
        dlg.paintRequested.c..(view.print_)
        dlg.e..


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    sheet _ SpreadSheet(10, 6)
    sheet.setWindowIcon(QIcon(QPixmap(":/images/interview.png")))
    sheet.resize(640, 420)
    sheet.s..
    sys.exit(app.exec_())
