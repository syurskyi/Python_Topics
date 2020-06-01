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


____ ?.QtCore ______ QFile, QIODevice, QTextStream, QUrl
____ ?.QtGui ______ QKeySequence
____ ?.?W.. ______ (QAction, ?A.., QFileDialog, QInputDialog,
        QLineEdit, QMainWindow, QMessageBox, QWidget)

____ ui_previewer ______ Ui_Form


class Previewer(QWidget, Ui_Form):
    ___ __init__(self, parent_None):
        super(Previewer, self).__init__(parent)

        self.setupUi(self)
        self.baseUrl _ QUrl()
 
    ___ setBaseUrl(self, url):
        self.baseUrl _ url

    ___ on_previewButton_clicked(self):
        # Update the contents in the web viewer.
        text _ self.plainTextEdit.toPlainText()
        self.webView.setHtml(text, self.baseUrl)


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.centralWidget _ Previewer(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.webView.loadFinished.c..(self.updateTextEdit)
        self.setStartupText()

    ___ createActions(self):
        self.openAct _ QAction("&Open...", self, shortcut_QKeySequence.Open,
                statusTip_"Open an existing HTML file", triggered_self.open)

        self.openUrlAct _ QAction("&Open URL...", self, shortcut_"Ctrl+U",
                statusTip_"Open a URL", triggered_self.openUrl)

        self.saveAct _ QAction("&Save", self, shortcut_QKeySequence.Save,
                statusTip_"Save the HTML file to disk", triggered_self.save)

        self.exitAct _ QAction("E&xit", self, shortcut_QKeySequence.Quit,
                statusTip_"Exit the application", triggered_self.close)

        self.aboutAct _ QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.openUrlAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)
        self.menuBar().addSeparator()
        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    ___ about(self):
        QMessageBox.about(self, "About Previewer",
                "The <b>Previewer</b> example demonstrates how to view HTML "
                "documents using a QtWebKitWidgets.QWebView.")

    ___ open(self):
        fileName, _ _ QFileDialog.getOpenFileName(self)
        if fileName:
            fd _ QFile(fileName)
            if not fd.open(QIODevice.ReadOnly):
                QMessageBox.information(self, "Unable to open file",
                        fd.errorString())
                return

            output _ QTextStream(fd).readAll()

            # Display contents.
            self.centralWidget.plainTextEdit.setPlainText(output)
            self.centralWidget.setBaseUrl(QUrl.fromLocalFile(fileName))

    ___ openUrl(self):
        url, ok _ QInputDialog.getText(self, "Enter a URL", "URL:",
                QLineEdit.Normal, "http://")

        if ok and url:
            url _ QUrl(url)
            self.centralWidget.webView.setUrl(url)

    ___ save(self):
        content _ self.centralWidget.plainTextEdit.toPlainText()
        fileName, _ _ QFileDialog.getSaveFileName(self)
        if fileName:
            fd _ QFile(fileName)
            if not fd.open(QIODevice.WriteOnly):
                QMessageBox.information(self, "Unable to open file",
                        fd.errorString())
                return

            QTextStream(fd) << content
 
    ___ updateTextEdit(self):
        mainFrame _ self.centralWidget.webView.page().mainFrame()
        frameText _ mainFrame.toHtml()
        self.centralWidget.plainTextEdit.setPlainText(frameText)

    ___ setStartupText(self):
        self.centralWidget.webView.setHtml("""
<html><body>
 <h1>HTML Previewer</h1>
  <p>This example shows you how to use QtWebKitWidgets.QWebView to
   preview HTML data written in a QtWidgets.QPlainTextEdit.
  </p>
</body></html>""")


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    mainWindow _ MainWindow()
    mainWindow.s..

    sys.exit(app.exec_())
