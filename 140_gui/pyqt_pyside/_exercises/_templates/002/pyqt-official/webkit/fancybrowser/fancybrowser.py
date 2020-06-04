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


____ ?.?C.. ______ QFile, QIODevice, __, QTextStream, ?U..
____ ?.?W.. ______ (?A.., ?A.., QLineEdit, ?MW..,
        ?SP.., ?S.., ?TE..)
____ ?.?N.. ______ QNetworkProxyFactory, ?NR..
____ ?.QtWebKitWidgets ______ QWebPage, QWebView

______ jquery_rc


c_ MainWindow ?MW..
    ___  -   url):
        s__(MainWindow, self). - ()

        progress _ 0

        fd _ QFile(":/jquery.min.js")

        __ fd.o..(QIODevice.ReadOnly | QFile.Text):
            jQuery _ QTextStream(fd).rA..
            fd.c..
        ____
            jQuery _ ''

        QNetworkProxyFactory.setUseSystemConfiguration( st.

        view _ QWebView
        view.load(url)
        view.loadFinished.c..(adjustLocation)
        view.titleChanged.c..(adjustTitle)
        view.loadProgress.c..(setProgress)
        view.loadFinished.c..(finishLoading)

        locationEdit _ QLineEdit
        locationEdit.sSP..(?SP...E..,
                locationEdit.sizePolicy().verticalPolicy())
        locationEdit.rP__.c..(changeLocation)

        toolBar _ aTB..("Navigation")
        toolBar.aA..(view.pageAction(QWebPage.Back))
        toolBar.aA..(view.pageAction(QWebPage.Forward))
        toolBar.aA..(view.pageAction(QWebPage.Reload))
        toolBar.aA..(view.pageAction(QWebPage.Stop))
        toolBar.aW..(locationEdit)

        viewMenu _ mB.. .aM..("&View")
        viewSourceAction _ ?A..("Page Source", self)
        viewSourceAction.t__.c..(viewSource)
        viewMenu.aA..(viewSourceAction)

        effectMenu _ mB.. .aM..("&Effect")
        effectMenu.aA..("Highlight all links", highlightAllLinks)

        rotateAction _ ?A..(
                style().standardIcon(?S...SP_FileDialogDetailedView),
                "Turn images upside down", self, checkable_True,
                toggled_self.rotateImages)
        effectMenu.aA..(rotateAction)

        toolsMenu _ mB.. .aM..("&Tools")
        toolsMenu.aA..("Remove GIF images", removeGifImages)
        toolsMenu.aA..("Remove all inline frames",
                removeInlineFrames)
        toolsMenu.aA..("Remove all object elements",
                removeObjectElements)
        toolsMenu.aA..("Remove all embedded elements",
                removeEmbeddedElements)
        sCW..(view)

    ___ viewSource 
        accessManager _ view.page().networkAccessManager()
        request _ ?NR..(view.url())
        reply _ accessManager.g..(request)
        reply.finished.c..(slotSourceDownloaded)

    ___ slotSourceDownloaded 
        reply _ sender()
        textEdit _ ?TE..()
        textEdit.setAttribute(__.WA_DeleteOnClose)
        textEdit.s..
        textEdit.sPT..(QTextStream(reply).readAll())
        textEdit.r..(600, 400)
        reply.deleteLater()

    ___ adjustLocation 
        locationEdit.sT..(view.u.. .toString())

    ___ changeLocation 
        url _ ?U...fromUserInput(locationEdit.t__())
        view.load(url)
        view.setFocus()

    ___ adjustTitle 
        __ 0 < progress < 100:
            sWT..("%s (%s%%)" % (view.title(), progress))
        ____
            sWT..(view.title())

    ___ setProgress  p):
        progress _ p
        adjustTitle()

    ___ finishLoading 
        progress _ 100
        adjustTitle()
        view.page().mainFrame().evaluateJavaScript(jQuery)
        rotateImages(rotateAction.isChecked())

    ___ highlightAllLinks 
        code _ """$('a').each(
                    function () {
                        $(this).css('background-color', 'yellow') 
                    } 
                  )"""
        view.page().mainFrame().evaluateJavaScript(code)

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

        view.page().mainFrame().evaluateJavaScript(code)

    ___ removeGifImages 
        code _ "$('[src*=gif]').remove()"
        view.page().mainFrame().evaluateJavaScript(code)

    ___ removeInlineFrames 
        code _ "$('iframe').remove()"
        view.page().mainFrame().evaluateJavaScript(code)

    ___ removeObjectElements 
        code _ "$('object').remove()"
        view.page().mainFrame().evaluateJavaScript(code)

    ___ removeEmbeddedElements 
        code _ "$('embed').remove()"
        view.page().mainFrame().evaluateJavaScript(code)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    __ le.(___.a.. > 1:
        url _ ?U..(___.argv[1])
    ____
        url _ ?U..('http://www.google.com/ncr')

    browser _ MainWindow(url)
    browser.s..

    ___.e.. ?.e..
