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


____ ?.QtCore ______ QFile, QIODevice, Qt, QTextStream, QUrl
____ ?.?W.. ______ (?A.., ?A.., QLineEdit, QMainWindow,
        QSizePolicy, QStyle, QTextEdit)
____ ?.QtNetwork ______ QNetworkProxyFactory, QNetworkRequest
____ ?.QtWebKitWidgets ______ QWebPage, QWebView

______ jquery_rc


c_ MainWindow ?MW..
    ___ __init__  url):
        super(MainWindow, self).__init__()

        self.progress _ 0

        fd _ QFile(":/jquery.min.js")

        __ fd.o..(QIODevice.ReadOnly | QFile.Text):
            self.jQuery _ QTextStream(fd).readAll()
            fd.close()
        ____
            self.jQuery _ ''

        QNetworkProxyFactory.setUseSystemConfiguration(True)

        self.view _ QWebView(self)
        self.view.load(url)
        self.view.loadFinished.c..(self.adjustLocation)
        self.view.titleChanged.c..(self.adjustTitle)
        self.view.loadProgress.c..(self.setProgress)
        self.view.loadFinished.c..(self.finishLoading)

        self.locationEdit _ QLineEdit(self)
        self.locationEdit.setSizePolicy(QSizePolicy.Expanding,
                self.locationEdit.sizePolicy().verticalPolicy())
        self.locationEdit.returnPressed.c..(self.changeLocation)

        toolBar _ self.addToolBar("Navigation")
        toolBar.aA..(self.view.pageAction(QWebPage.Back))
        toolBar.aA..(self.view.pageAction(QWebPage.Forward))
        toolBar.aA..(self.view.pageAction(QWebPage.Reload))
        toolBar.aA..(self.view.pageAction(QWebPage.Stop))
        toolBar.addWidget(self.locationEdit)

        viewMenu _ self.mB.. .aM..("&View")
        viewSourceAction _ ?A..("Page Source", self)
        viewSourceAction.t__.c..(self.viewSource)
        viewMenu.aA..(viewSourceAction)

        effectMenu _ self.mB.. .aM..("&Effect")
        effectMenu.aA..("Highlight all links", self.highlightAllLinks)

        self.rotateAction _ ?A..(
                self.style().standardIcon(QStyle.SP_FileDialogDetailedView),
                "Turn images upside down", self, checkable_True,
                toggled_self.rotateImages)
        effectMenu.aA..(self.rotateAction)

        toolsMenu _ self.mB.. .aM..("&Tools")
        toolsMenu.aA..("Remove GIF images", self.removeGifImages)
        toolsMenu.aA..("Remove all inline frames",
                self.removeInlineFrames)
        toolsMenu.aA..("Remove all object elements",
                self.removeObjectElements)
        toolsMenu.aA..("Remove all embedded elements",
                self.removeEmbeddedElements)
        self.sCW..(self.view)

    ___ viewSource(self):
        accessManager _ self.view.page().networkAccessManager()
        request _ QNetworkRequest(self.view.url())
        reply _ accessManager.get(request)
        reply.finished.c..(self.slotSourceDownloaded)

    ___ slotSourceDownloaded(self):
        reply _ self.sender()
        self.textEdit _ QTextEdit()
        self.textEdit.setAttribute(Qt.WA_DeleteOnClose)
        self.textEdit.s..
        self.textEdit.sPT..(QTextStream(reply).readAll())
        self.textEdit.resize(600, 400)
        reply.deleteLater()

    ___ adjustLocation(self):
        self.locationEdit.sT..(self.view.url().toString())

    ___ changeLocation(self):
        url _ QUrl.fromUserInput(self.locationEdit.text())
        self.view.load(url)
        self.view.setFocus()

    ___ adjustTitle(self):
        __ 0 < self.progress < 100:
            self.setWindowTitle("%s (%s%%)" % (self.view.title(), self.progress))
        ____
            self.setWindowTitle(self.view.title())

    ___ setProgress  p):
        self.progress _ p
        self.adjustTitle()

    ___ finishLoading(self):
        self.progress _ 100
        self.adjustTitle()
        self.view.page().mainFrame().evaluateJavaScript(self.jQuery)
        self.rotateImages(self.rotateAction.isChecked())

    ___ highlightAllLinks(self):
        code _ """$('a').each(
                    function () {
                        $(this).css('background-color', 'yellow') 
                    } 
                  )"""
        self.view.page().mainFrame().evaluateJavaScript(code)

    ___ rotateImages  invert):
        __ invert:
            code _ """
                $('img').each(
                    function () {
                        $(this).css('-webkit-transition', '-webkit-transform 2s'); 
                        $(this).css('-webkit-transform', 'rotate(180deg)') 
                    } 
                )"""
        ____
            code _ """
                $('img').each(
                    function () { 
                        $(this).css('-webkit-transition', '-webkit-transform 2s'); 
                        $(this).css('-webkit-transform', 'rotate(0deg)') 
                    } 
                )"""

        self.view.page().mainFrame().evaluateJavaScript(code)

    ___ removeGifImages(self):
        code _ "$('[src*=gif]').remove()"
        self.view.page().mainFrame().evaluateJavaScript(code)

    ___ removeInlineFrames(self):
        code _ "$('iframe').remove()"
        self.view.page().mainFrame().evaluateJavaScript(code)

    ___ removeObjectElements(self):
        code _ "$('object').remove()"
        self.view.page().mainFrame().evaluateJavaScript(code)

    ___ removeEmbeddedElements(self):
        code _ "$('embed').remove()"
        self.view.page().mainFrame().evaluateJavaScript(code)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    __ len(sys.argv) > 1:
        url _ QUrl(sys.argv[1])
    ____
        url _ QUrl('http://www.google.com/ncr')

    browser _ MainWindow(url)
    browser.s..

    sys.exit(app.exec_())
