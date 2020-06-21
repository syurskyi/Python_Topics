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


____ ?.?C.. ______ ?D.., QFile, __, QTextStream
____ ?.?G.. ______ (?F.., ?I.., ?KS.., QTextCharFormat,
        QTextCursor, QTextTableFormat)
____ ?.?PS.. ______ QPrintDialog, QPrinter
____ ?.?W.. ______ (?A.., ?A.., ?D.., QDockWidget,
        ?FD.., QListWidget, ?MW.., ?MB.., ?TE..)

______ dockwidgets_rc


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        textEdit _ ?TE..()
        sCW..(textEdit)

        createActions()
        createMenus()
        createToolBars()
        createStatusBar()
        createDockWindows()

        sWT..("Dock Widgets")

        newLetter()

    ___ newLetter
        textEdit.c..

        cursor _ textEdit.textCursor()
        cursor.movePosition(QTextCursor.Start)
        topFrame _ cursor.currentFrame()
        topFrameFormat _ topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat _ QTextCharFormat()
        boldFormat _ QTextCharFormat()
        boldFormat.setFontWeight(?F...Bold)
        italicFormat _ QTextCharFormat()
        italicFormat.setFontItalic( st.

        tableFormat _ QTextTableFormat()
        tableFormat.setBorder(1)
        tableFormat.setCellPadding(16)
        tableFormat.setAlignment(__.AlignRight)
        cursor.insertTable(1, 1, tableFormat)
        cursor.insertText("The Firm", boldFormat)
        cursor.insertBlock()
        cursor.insertText("321 City Street", textFormat)
        cursor.insertBlock()
        cursor.insertText("Industry Park")
        cursor.insertBlock()
        cursor.insertText("Some Country")
        cursor.setPosition(topFrame.lastPosition())
        cursor.insertText(?D...currentDate().toString("d MMMM yyyy"),
                textFormat)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText("Dear ", textFormat)
        cursor.insertText("NAME", italicFormat)   
        cursor.insertText(",", textFormat)
        ___ i __ ra..(3):
            cursor.insertBlock()
        cursor.insertText("Yours sincerely,", textFormat)
        ___ i __ ra..(3):
            cursor.insertBlock()
        cursor.insertText("The Boss", textFormat)
        cursor.insertBlock()
        cursor.insertText("ADDRESS", italicFormat)  

    ___ print_
        document _ textEdit.document()
        printer _ QPrinter()

        dlg _ QPrintDialog(printer, self)
        __ dlg.e.. !_ ?D...Accepted:
            r_

        document.print_(printer)

        sB.. .sM..("Ready", 2000)

    ___ save
        filename, _ _ ?FD...getSaveFileName
                "Choose a file name", '.', "HTML (*.html *.htm)")
        __ no. filename:
            r_

        file _ QFile(filename)
        __ no. file.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..  "Dock Widgets",
                    "Cannot write file %s:\n%s." % (filename, file.errorString()))
            r_

        out _ QTextStream(file)
        ?A...setOverrideCursor(__.WaitCursor)
        out << textEdit.toHtml()
        ?A...restoreOverrideCursor()

        sB.. .sM..("Saved '%s'" % filename, 2000)

    ___ undo
        document _ textEdit.document()
        document.undo()

    ___ insertCustomer  customer):
        __ no. customer:
            r_
        customerList _ customer.sp..(', ')
        document _ textEdit.document()
        cursor _ document.find('NAME')
        __ no. cursor.isNull
            cursor.beginEditBlock()
            cursor.insertText(customerList[0])
            oldcursor _ cursor
            cursor _ document.find('ADDRESS')
            __ no. cursor.isNull
                ___ i __ customerList[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            ____
                oldcursor.endEditBlock()

    ___ addParagraph  paragraph):
        __ no. paragraph:
            r_
        document _ textEdit.document()
        cursor _ document.find("Yours sincerely,")
        __ cursor.isNull
            r_
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.PreviousBlock, QTextCursor.MoveAnchor,
                2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    ___ about
        ?MB...about  "About Dock Widgets",
                "The <b>Dock Widgets</b> example demonstrates how to use "
                "Qt's dock widgets. You can enter your own text, click a "
                "customer to add a customer name and address, and click "
                "standard paragraphs to add them.")

    ___ createActions
        newLetterAct _ ?A..(?I..(':/images/new.png'), "&New Letter",
                self, shortcut_QKeySequence.New,
                statusTip_"Create a new form letter", triggered_self.newLetter)

        saveAct _ ?A..(?I..(':/images/save.png'), "&Save...", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the current form letter", triggered_self.save)

        printAct _ ?A..(?I..(':/images/print.png'), "&Print...", self,
                shortcut_QKeySequence.Print,
                statusTip_"Print the current form letter",
                triggered_self.print_)

        undoAct _ ?A..(?I..(':/images/undo.png'), "&Undo", self,
                shortcut_QKeySequence.Undo,
                statusTip_"Undo the last editing action", triggered_self.undo)

        quitAct _ ?A..("&Quit", self, shortcut_"Ctrl+Q",
                statusTip_"Quit the application", triggered_self.close)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(newLetterAct)
        fileMenu.aA..(saveAct)
        fileMenu.aA..(printAct)
        fileMenu.aS..)
        fileMenu.aA..(quitAct)

        editMenu _ mB.. .aM..("&Edit")
        editMenu.aA..(undoAct)

        viewMenu _ mB.. .aM..("&View")

        mB.. .aS..)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ createToolBars
        fileToolBar _ aTB..("File")
        fileToolBar.aA..(newLetterAct)
        fileToolBar.aA..(saveAct)
        fileToolBar.aA..(printAct)

        editToolBar _ aTB..("Edit")
        editToolBar.aA..(undoAct)

    ___ createStatusBar
        sB.. .sM..("Ready")

    ___ createDockWindows
        dock _ QDockWidget("Customers", self)
        dock.setAllowedAreas(__.LeftDockWidgetArea | __.RightDockWidgetArea)
        customerList _ QListWidget(dock)
        customerList.aI..((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(customerList)
        addDockWidget(__.RightDockWidgetArea, dock)
        viewMenu.aA..(dock.toggleViewAction())

        dock _ QDockWidget("Paragraphs", self)
        paragraphsList _ QListWidget(dock)
        paragraphsList.aI..((
            "Thank you for your payment which we have received today.",
            "Your order has been dispatched and should be with you within "
                "28 days.",
            "We have dispatched those items that were in stock. The rest of "
                "your order will be dispatched once all the remaining items "
                "have arrived at our warehouse. No additional shipping "
                "charges will be made.",
            "You made a small overpayment (less than $5) which we will keep "
                "on account for you, or return at your request.",
            "You made a small underpayment (less than $1), but we have sent "
                "your order anyway. We'll add this underpayment to your next "
                "bill.",
            "Unfortunately you did not send enough money. Please remit an "
                "additional $. Your order will be dispatched as soon as the "
                "complete amount has been received.",
            "You made an overpayment (more than $5). Do you wish to buy more "
                "items, or should we return the excess to you?"))
        dock.setWidget(paragraphsList)
        addDockWidget(__.RightDockWidgetArea, dock)
        viewMenu.aA..(dock.toggleViewAction())

        customerList.cTC...c..(insertCustomer)
        paragraphsList.cTC...c..(addParagraph)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
