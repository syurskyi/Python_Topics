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


____ ?.QtCore ______ QDate, Qt
____ ?.QtGui ______ (QFont, QTextCharFormat, QTextCursor, QTextFrameFormat,
        QTextLength, QTextTableFormat)
____ ?.?W.. ______ (?A.., QCheckBox, QDialog,
        QDialogButtonBox, QGridLayout, QLabel, QLineEdit, QMainWindow,
        QMessageBox, QMenu, QTableWidget, QTableWidgetItem, QTabWidget,
        QTextEdit)
____ ?.QtPrintSupport ______ QAbstractPrintDialog, QPrintDialog, QPrinter


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        fileMenu _ QMenu("&File", self)
        newAction _ fileMenu.addAction("&New...")
        newAction.setShortcut("Ctrl+N")
        self.printAction _ fileMenu.addAction("&Print...", self.printFile)
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.setEnabled(False)
        quitAction _ fileMenu.addAction("E&xit")
        quitAction.setShortcut("Ctrl+Q")
        self.menuBar().addMenu(fileMenu)

        self.letters _ QTabWidget()

        newAction.triggered.c..(self.openDialog)
        quitAction.triggered.c..(self.close)

        self.setCentralWidget(self.letters)
        self.setWindowTitle("Order Form")

    ___ createLetter(self, name, address, orderItems, sendOffers):
        editor _ QTextEdit()
        tabIndex _ self.letters.addTab(editor, name)
        self.letters.setCurrentIndex(tabIndex)

        cursor _ editor.textCursor()
        cursor.movePosition(QTextCursor.Start)
        topFrame _ cursor.currentFrame()
        topFrameFormat _ topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat _ QTextCharFormat()
        boldFormat _ QTextCharFormat()
        boldFormat.setFontWeight(QFont.Bold)

        referenceFrameFormat _ QTextFrameFormat()
        referenceFrameFormat.setBorder(1)
        referenceFrameFormat.setPadding(8)
        referenceFrameFormat.setPosition(QTextFrameFormat.FloatRight)
        referenceFrameFormat.setWidth(QTextLength(QTextLength.PercentageLength, 40))
        cursor.insertFrame(referenceFrameFormat)

        cursor.insertText("A company", boldFormat)
        cursor.insertBlock()
        cursor.insertText("321 City Street")
        cursor.insertBlock()
        cursor.insertText("Industry Park")
        cursor.insertBlock()
        cursor.insertText("Another country")

        cursor.setPosition(topFrame.lastPosition())

        cursor.insertText(name, textFormat)
        for line in address.split("\n"):
            cursor.insertBlock()
            cursor.insertText(line)

        cursor.insertBlock()
        cursor.insertBlock()

        date _ QDate.currentDate()
        cursor.insertText("Date: %s" % date.toString('d MMMM yyyy'),
                textFormat)
        cursor.insertBlock()

        bodyFrameFormat _ QTextFrameFormat()
        bodyFrameFormat.setWidth(QTextLength(QTextLength.PercentageLength, 100))
        cursor.insertFrame(bodyFrameFormat)

        cursor.insertText("I would like to place an order for the following "
                "items:", textFormat)
        cursor.insertBlock()
        cursor.insertBlock()

        orderTableFormat _ QTextTableFormat()
        orderTableFormat.setAlignment(Qt.AlignHCenter)
        orderTable _ cursor.insertTable(1, 2, orderTableFormat)

        orderFrameFormat _ cursor.currentFrame().frameFormat()
        orderFrameFormat.setBorder(1)
        cursor.currentFrame().setFrameFormat(orderFrameFormat)

        cursor _ orderTable.cellAt(0, 0).firstCursorPosition()
        cursor.insertText("Product", boldFormat)
        cursor _ orderTable.cellAt(0, 1).firstCursorPosition()
        cursor.insertText("Quantity", boldFormat)

        for text, quantity in orderItems:
            row _ orderTable.rows()

            orderTable.insertRows(row, 1)
            cursor _ orderTable.cellAt(row, 0).firstCursorPosition()
            cursor.insertText(text, textFormat)
            cursor _ orderTable.cellAt(row, 1).firstCursorPosition()
            cursor.insertText(str(quantity), textFormat)

        cursor.setPosition(topFrame.lastPosition())

        cursor.insertBlock()

        cursor.insertText("Please update my records to take account of the "
                "following privacy information:")
        cursor.insertBlock()

        offersTable _ cursor.insertTable(2, 2)

        cursor _ offersTable.cellAt(0, 1).firstCursorPosition()
        cursor.insertText("I want to receive more information about your "
                "company's products and special offers.", textFormat)
        cursor _ offersTable.cellAt(1, 1).firstCursorPosition()
        cursor.insertText("I do not want to receive any promotional "
                "information from your company.", textFormat)

        if sendOffers:
            cursor _ offersTable.cellAt(0, 0).firstCursorPosition()
        else:
            cursor _ offersTable.cellAt(1, 0).firstCursorPosition()

        cursor.insertText('X', boldFormat)

        cursor.setPosition(topFrame.lastPosition())
        cursor.insertBlock()
        cursor.insertText("Sincerely,", textFormat)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText(name)

        self.printAction.setEnabled(True)

    ___ createSample(self):
        dialog _ DetailsDialog('Dialog with default values', self)
        self.createLetter('Mr Smith',
                '12 High Street\nSmall Town\nThis country',
                dialog.orderItems(), True)

    ___ openDialog(self):
        dialog _ DetailsDialog("Enter Customer Details", self)

        if dialog.e.. == QDialog.Accepted:
            self.createLetter(dialog.senderName(), dialog.senderAddress(),
                    dialog.orderItems(), dialog.sendOffers())

    ___ printFile(self):
        editor _ self.letters.currentWidget()
        printer _ QPrinter()

        dialog _ QPrintDialog(printer, self)
        dialog.setWindowTitle("Print Document")

        if editor.textCursor().hasSelection
            dialog.addEnabledOption(QAbstractPrintDialog.PrintSelection)

        if dialog.e.. !_ QDialog.Accepted:
            return

        editor.print_(printer)


class DetailsDialog(QDialog):
    ___ __init__(self, title, parent):
        super(DetailsDialog, self).__init__(parent)

        self.items _ ("T-shirt", "Badge", "Reference book", "Coffee cup")

        nameLabel _ QLabel("Name:")
        addressLabel _ QLabel("Address:")
        addressLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.nameEdit _ QLineEdit()
        self.addressEdit _ QTextEdit()
        self.offersCheckBox _ QCheckBox(
                "Send information about products and special offers:")

        self.setupItemsTable()

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.c..(self.verify)
        buttonBox.rejected.c..(self.reject)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameEdit, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0)
        mainLayout.addWidget(self.addressEdit, 1, 1)
        mainLayout.addWidget(self.itemsTable, 0, 2, 2, 1)
        mainLayout.addWidget(self.offersCheckBox, 2, 1, 1, 2)
        mainLayout.addWidget(buttonBox, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.setWindowTitle(title)

    ___ setupItemsTable(self):
        self.itemsTable _ QTableWidget(len(self.items), 2)

        for row, item in enumerate(self.items):
            name _ QTableWidgetItem(item)
            name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.itemsTable.setItem(row, 0, name)
            quantity _ QTableWidgetItem('1')
            self.itemsTable.setItem(row, 1, quantity)

    ___ orderItems(self):
        orderList _ []

        for row in range(len(self.items)):
            text _ self.itemsTable.item(row, 0).text()
            quantity _ int(self.itemsTable.item(row, 1).data(Qt.DisplayRole))
            orderList.append((text, max(0, quantity)))

        return orderList

    ___ senderName(self):
        return self.nameEdit.text()

    ___ senderAddress(self):
        return self.addressEdit.toPlainText()

    ___ sendOffers(self):
        return self.offersCheckBox.isChecked()

    ___ verify(self):
        if self.nameEdit.text() and self.addressEdit.toPlainText
            self.accept()
            return

        answer _ QMessageBox.warning(self, "Incomplete Form",
                "The form does not contain all the necessary information.\n"
                "Do you want to discard it?",
                QMessageBox.Yes, QMessageBox.No)

        if answer == QMessageBox.Yes:
            self.reject()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.resize(640, 480)
    window.s..
    window.createSample()
    sys.exit(app.exec_())
