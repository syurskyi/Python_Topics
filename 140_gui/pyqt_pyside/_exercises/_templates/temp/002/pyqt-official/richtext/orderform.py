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


____ ?.?C.. ______ ?D.., __
____ ?.?G.. ______ (?F.., QTextCharFormat, QTextCursor, QTextFrameFormat,
        QTextLength, QTextTableFormat)
____ ?.?W.. ______ (?A.., QCheckBox, ?D..,
        ?DBB..., QGridLayout, ?L.., QLineEdit, ?MW..,
        ?MB.., ?M.., ?TW.., ?TWI.., ?TW..,
        ?TE..)
____ ?.?PS.. ______ QAbstractPrintDialog, QPrintDialog, QPrinter


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        fileMenu _ ?M..("&File", self)
        newAction _ fileMenu.aA..("&New...")
        newAction.sS..("Ctrl+N")
        printAction _ fileMenu.aA..("&Print...", printFile)
        printAction.sS..("Ctrl+P")
        printAction.sE.. F..
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")
        mB.. .aM..(fileMenu)

        letters _ ?TW..()

        newAction.t__.c..(openDialog)
        quitAction.t__.c..(close)

        sCW..(letters)
        sWT..("Order Form")

    ___ createLetter  name, address, orderItems, sendOffers):
        editor _ ?TE..()
        tabIndex _ letters.aT..(editor, name)
        letters.sCI..(tabIndex)

        cursor _ editor.textCursor()
        cursor.movePosition(QTextCursor.Start)
        topFrame _ cursor.currentFrame()
        topFrameFormat _ topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat _ QTextCharFormat()
        boldFormat _ QTextCharFormat()
        boldFormat.setFontWeight(?F...Bold)

        referenceFrameFormat _ QTextFrameFormat()
        referenceFrameFormat.setBorder(1)
        referenceFrameFormat.setPadding(8)
        referenceFrameFormat.setPosition(QTextFrameFormat.FloatRight)
        referenceFrameFormat.sW..(QTextLength(QTextLength.PercentageLength, 40))
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
        ___ line __ address.sp..("\n"):
            cursor.insertBlock()
            cursor.insertText(line)

        cursor.insertBlock()
        cursor.insertBlock()

        date _ ?D...currentDate()
        cursor.insertText("Date: %s" % date.toString('d MMMM yyyy'),
                textFormat)
        cursor.insertBlock()

        bodyFrameFormat _ QTextFrameFormat()
        bodyFrameFormat.sW..(QTextLength(QTextLength.PercentageLength, 100))
        cursor.insertFrame(bodyFrameFormat)

        cursor.insertText("I would like to place an order for the following "
                "items:", textFormat)
        cursor.insertBlock()
        cursor.insertBlock()

        orderTableFormat _ QTextTableFormat()
        orderTableFormat.setAlignment(__.AlignHCenter)
        orderTable _ cursor.insertTable(1, 2, orderTableFormat)

        orderFrameFormat _ cursor.currentFrame().frameFormat()
        orderFrameFormat.setBorder(1)
        cursor.currentFrame().setFrameFormat(orderFrameFormat)

        cursor _ orderTable.cellAt(0, 0).firstCursorPosition()
        cursor.insertText("Product", boldFormat)
        cursor _ orderTable.cellAt(0, 1).firstCursorPosition()
        cursor.insertText("Quantity", boldFormat)

        ___ t__, quantity __ orderItems:
            row _ orderTable.rows()

            orderTable.insertRows(row, 1)
            cursor _ orderTable.cellAt(row, 0).firstCursorPosition()
            cursor.insertText(t__, textFormat)
            cursor _ orderTable.cellAt(row, 1).firstCursorPosition()
            cursor.insertText(st.(quantity), textFormat)

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

        __ sendOffers:
            cursor _ offersTable.cellAt(0, 0).firstCursorPosition()
        ____
            cursor _ offersTable.cellAt(1, 0).firstCursorPosition()

        cursor.insertText('X', boldFormat)

        cursor.setPosition(topFrame.lastPosition())
        cursor.insertBlock()
        cursor.insertText("Sincerely,", textFormat)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText(name)

        printAction.sE..( st.

    ___ createSample
        dialog _ DetailsDialog('Dialog with default values', self)
        createLetter('Mr Smith',
                '12 High Street\nSmall Town\nThis country',
                dialog.orderItems(),  st.

    ___ openDialog
        dialog _ DetailsDialog("Enter Customer Details", self)

        __ dialog.e.. __ ?D...Accepted:
            createLetter(dialog.senderName(), dialog.senderAddress(),
                    dialog.orderItems(), dialog.sendOffers())

    ___ printFile
        editor _ letters.currentWidget()
        printer _ QPrinter()

        dialog _ QPrintDialog(printer, self)
        dialog.sWT..("Print Document")

        __ editor.textCursor().hasSelection
            dialog.addEnabledOption(QAbstractPrintDialog.PrintSelection)

        __ dialog.e.. !_ ?D...Accepted:
            r_

        editor.print_(printer)


c_ DetailsDialog(?D..):
    ___  -   title, parent):
        s__(DetailsDialog, self). - (parent)

        i.. _ ("T-shirt", "Badge", "Reference book", "Coffee cup")

        nameLabel _ ?L..("Name:")
        addressLabel _ ?L..("Address:")
        addressLabel.setAlignment(__.AlignLeft | __.AlignTop)

        nameEdit _ ?LE..
        addressEdit _ ?TE..()
        offersCheckBox _ QCheckBox(
                "Send information about products and special offers:")

        setupItemsTable()

        buttonBox _ ?DBB...(?DBB....Ok | ?DBB....Cancel)

        buttonBox.a___.c..(verify)
        buttonBox.r___.c..(reject)

        mainLayout _ QGridLayout()
        mainLayout.aW..(nameLabel, 0, 0)
        mainLayout.aW..(nameEdit, 0, 1)
        mainLayout.aW..(addressLabel, 1, 0)
        mainLayout.aW..(addressEdit, 1, 1)
        mainLayout.aW..(itemsTable, 0, 2, 2, 1)
        mainLayout.aW..(offersCheckBox, 2, 1, 1, 2)
        mainLayout.aW..(buttonBox, 3, 0, 1, 3)
        sL..(mainLayout)

        sWT..(title)

    ___ setupItemsTable
        itemsTable _ ?TW..(le.(i..), 2)

        ___ row, item __ en..(i..):
            name _ ?TWI..(item)
            name.setFlags(__.ItemIsEnabled | __.ItemIsSelectable)
            itemsTable.setItem(row, 0, name)
            quantity _ ?TWI..('1')
            itemsTable.setItem(row, 1, quantity)

    ___ orderItems
        orderList _   # list

        ___ row __ ra..(le.(i..)):
            t__ _ itemsTable.item(row, 0).t__()
            quantity _ in.(itemsTable.item(row, 1).data(__.DR..))
            orderList.ap..((t__, max(0, quantity)))

        r_ orderList

    ___ senderName
        r_ nameEdit.t__()

    ___ senderAddress
        r_ addressEdit.toPlainText()

    ___ sendOffers
        r_ offersCheckBox.isChecked()

    ___ verify
        __ nameEdit.t__() and addressEdit.toPlainText
            accept()
            r_

        answer _ ?MB...w..  "Incomplete Form",
                "The form does not contain all the necessary information.\n"
                "Do you want to discard it?",
                ?MB...Yes, ?MB...No)

        __ answer __ ?MB...Yes:
            reject()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.r..(640, 480)
    window.s..
    window.createSample()
    ___.e.. ?.e..
