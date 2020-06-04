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
###########################################################################


____ ?.?C.. ______ QFile, QIODevice, QTextStream, ?U..
____ ?.?G.. ______ ?KS..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., QInputDialog,
        QLineEdit, ?MW.., ?MB.., ?W..)

____ ui_previewer ______ Ui_Form


c_ Previewer(?W.., Ui_Form):
    ___  -   parent_None):
        s__(Previewer, self). - (parent)

        setupUi
        baseUrl _ ?U..()
 
    ___ setBaseUrl  url):
        baseUrl _ url

    ___ on_previewButton_clicked
        # Update the contents in the web viewer.
        t__ _ plainTextEdit.toPlainText()
        webView.setHtml(t__, baseUrl)


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        createActions()
        createMenus()
        centralWidget _ Previewer
        sCW..(centralWidget)
        centralWidget.webView.loadFinished.c..(updateTextEdit)
        setStartupText()

    ___ createActions
        openAct _ ?A..("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing HTML file", triggered_self.o..)

        openUrlAct _ ?A..("&Open URL...", self, shortcut_"Ctrl+U",
                statusTip_"Open a URL", triggered_self.openUrl)

        saveAct _ ?A..("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the HTML file to disk", triggered_self.save)

        exitAct _ ?A..("E&xit", self, shortcut_QKeySequence.Quit,
                statusTip_"Exit the application", triggered_self.close)

        aboutAct _ ?A..("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(openAct)
        fileMenu.aA..(openUrlAct)
        fileMenu.aA..(saveAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)
        mB.. .aS..)
        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ about
        ?MB...about  "About Previewer",
                "The <b>Previewer</b> example demonstrates how to view HTML "
                "documents using a QtWebKitWidgets.QWebView.")

    ___ o..
        fileName, _ _ ?FD...gOFN..
        __ fileName:
            fd _ QFile(fileName)
            __ no. fd.o..(QIODevice.ReadOnly):
                ?MB...i..  "Unable to open file",
                        fd.errorString())
                r_

            output _ QTextStream(fd).rA..

            # Display contents.
            centralWidget.plainTextEdit.sPT..(output)
            centralWidget.setBaseUrl(?U...fLF..(fileName))

    ___ openUrl
        url, ok _ QInputDialog.getText  "Enter a URL", "URL:",
                QLineEdit.Normal, "http://")

        __ ok and url:
            url _ ?U..(url)
            centralWidget.webView.setUrl(url)

    ___ save
        content _ centralWidget.plainTextEdit.toPlainText()
        fileName, _ _ ?FD...getSaveFileName
        __ fileName:
            fd _ QFile(fileName)
            __ no. fd.o..(QIODevice.WriteOnly):
                ?MB...i..  "Unable to open file",
                        fd.errorString())
                r_

            QTextStream(fd) << content
 
    ___ updateTextEdit
        mainFrame _ centralWidget.webView.page().mainFrame()
        frameText _ mainFrame.toHtml()
        centralWidget.plainTextEdit.sPT..(frameText)

    ___ setStartupText
        centralWidget.webView.setHtml("""
<html><body>
 <h1>HTML Previewer</h1>
  <p>This example shows you how to use QtWebKitWidgets.QWebView to
   preview HTML data written in a QtWidgets.QPlainTextEdit.
  </p>
</body></html>""")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    mainWindow _ MainWindow()
    mainWindow.s..

    ___.e.. ?.e..
