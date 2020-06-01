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


____ ?.QtCore ______ QDate, QFile, Qt, QTextStream
____ ?.QtGui ______ (QFont, QIcon, QKeySequence, QTextCharFormat,
        QTextCursor, QTextTableFormat)
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter
____ ?.?W.. ______ (QAction, QApplication, QDialog, QDockWidget,
        QFileDialog, QListWidget, QMainWindow, QMessageBox, QTextEdit)

______ dockwidgets_rc


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.textEdit _ QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()

        self.setWindowTitle("Dock Widgets")

        self.newLetter()

    ___ newLetter(self):
        self.textEdit.clear()

        cursor _ self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.Start)
        topFrame _ cursor.currentFrame()
        topFrameFormat _ topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat _ QTextCharFormat()
        boldFormat _ QTextCharFormat()
        boldFormat.setFontWeight(QFont.Bold)
        italicFormat _ QTextCharFormat()
        italicFormat.setFontItalic(True)

        tableFormat _ QTextTableFormat()
        tableFormat.setBorder(1)
        tableFormat.setCellPadding(16)
        tableFormat.setAlignment(Qt.AlignRight)
        cursor.insertTable(1, 1, tableFormat)
        cursor.insertText("The Firm", boldFormat)
        cursor.insertBlock()
        cursor.insertText("321 City Street", textFormat)
        cursor.insertBlock()
        cursor.insertText("Industry Park")
        cursor.insertBlock()
        cursor.insertText("Some Country")
        cursor.setPosition(topFrame.lastPosition())
        cursor.insertText(QDate.currentDate().toString("d MMMM yyyy"),
                textFormat)
        cursor.insertBlock()
        cursor.insertBlock()
        cursor.insertText("Dear ", textFormat)
        cursor.insertText("NAME", italicFormat)   
        cursor.insertText(",", textFormat)
        for i in range(3):
            cursor.insertBlock()
        cursor.insertText("Yours sincerely,", textFormat)
        for i in range(3):
            cursor.insertBlock()
        cursor.insertText("The Boss", textFormat)
        cursor.insertBlock()
        cursor.insertText("ADDRESS", italicFormat)  

    ___ print_(self):
        document _ self.textEdit.document()
        printer _ QPrinter()

        dlg _ QPrintDialog(printer, self)
        if dlg.e.. !_ QDialog.Accepted:
            return

        document.print_(printer)

        self.statusBar().showMessage("Ready", 2000)

    ___ save(self):
        filename, _ _ QFileDialog.getSaveFileName(self,
                "Choose a file name", '.', "HTML (*.html *.htm)")
        if not filename:
            return

        file _ QFile(filename)
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "Dock Widgets",
                    "Cannot write file %s:\n%s." % (filename, file.errorString()))
            return

        out _ QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        out << self.textEdit.toHtml()
        QApplication.restoreOverrideCursor()

        self.statusBar().showMessage("Saved '%s'" % filename, 2000)

    ___ undo(self):
        document _ self.textEdit.document()
        document.undo()

    ___ insertCustomer(self, customer):
        if not customer:
            return
        customerList _ customer.split(', ')
        document _ self.textEdit.document()
        cursor _ document.find('NAME')
        if not cursor.isNull
            cursor.beginEditBlock()
            cursor.insertText(customerList[0])
            oldcursor _ cursor
            cursor _ document.find('ADDRESS')
            if not cursor.isNull
                for i in customerList[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            else:
                oldcursor.endEditBlock()

    ___ addParagraph(self, paragraph):
        if not paragraph:
            return
        document _ self.textEdit.document()
        cursor _ document.find("Yours sincerely,")
        if cursor.isNull
            return
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.PreviousBlock, QTextCursor.MoveAnchor,
                2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    ___ about(self):
        QMessageBox.about(self, "About Dock Widgets",
                "The <b>Dock Widgets</b> example demonstrates how to use "
                "Qt's dock widgets. You can enter your own text, click a "
                "customer to add a customer name and address, and click "
                "standard paragraphs to add them.")

    ___ createActions(self):
        self.newLetterAct _ QAction(QIcon(':/images/new.png'), "&New Letter",
                self, shortcut_QKeySequence.New,
                statusTip_"Create a new form letter", triggered_self.newLetter)

        self.saveAct _ QAction(QIcon(':/images/save.png'), "&Save...", self,
                shortcut_QKeySequence.Save,
                statusTip_"Save the current form letter", triggered_self.save)

        self.printAct _ QAction(QIcon(':/images/print.png'), "&Print...", self,
                shortcut_QKeySequence.Print,
                statusTip_"Print the current form letter",
                triggered_self.print_)

        self.undoAct _ QAction(QIcon(':/images/undo.png'), "&Undo", self,
                shortcut_QKeySequence.Undo,
                statusTip_"Undo the last editing action", triggered_self.undo)

        self.quitAct _ QAction("&Quit", self, shortcut_"Ctrl+Q",
                statusTip_"Quit the application", triggered_self.close)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newLetterAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAct)

        self.editMenu _ self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)

        self.viewMenu _ self.menuBar().addMenu("&View")

        self.menuBar().addSeparator()

        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    ___ createToolBars(self):
        self.fileToolBar _ self.addToolBar("File")
        self.fileToolBar.addAction(self.newLetterAct)
        self.fileToolBar.addAction(self.saveAct)
        self.fileToolBar.addAction(self.printAct)

        self.editToolBar _ self.addToolBar("Edit")
        self.editToolBar.addAction(self.undoAct)

    ___ createStatusBar(self):
        self.statusBar().showMessage("Ready")

    ___ createDockWindows(self):
        dock _ QDockWidget("Customers", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.customerList _ QListWidget(dock)
        self.customerList.addItems((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(self.customerList)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        dock _ QDockWidget("Paragraphs", self)
        self.paragraphsList _ QListWidget(dock)
        self.paragraphsList.addItems((
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
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        self.customerList.currentTextChanged.c..(self.insertCustomer)
        self.paragraphsList.currentTextChanged.c..(self.addParagraph)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
