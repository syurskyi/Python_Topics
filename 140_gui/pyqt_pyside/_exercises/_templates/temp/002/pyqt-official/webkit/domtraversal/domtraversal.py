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


____ ?.QtCore ______ QUrl
____ ?.?W.. ______ QApplication, QMainWindow, QTreeWidgetItem

____ ui_window ______ Ui_Window


class Window(QMainWindow, Ui_Window):
    ___ __init__(self, parent_None):
        super(Window, self).__init__(parent)

        self.setupUi(self)
 
    ___ setUrl(self, url):
        self.webView.setUrl(url)
  
    ___ on_webView_loadFinished(self):
        # Begin document inspection.
        self.treeWidget.clear()
        frame _ self.webView.page().mainFrame()
        document _ frame.documentElement()
        self.examineChildElements(document, self.treeWidget.invisibleRootItem())
 
    ___ examineChildElements(self, parentElement, parentItem):
        # Traverse the document.
        element _ parentElement.firstChild()
        while not element.isNull
            item _ QTreeWidgetItem()
            item.sT..(0, element.tagName())
            parentItem.addChild(item)
            self.examineChildElements(element, item)
            element _ element.nextSibling()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    window _ Window()
    window.s..
    window.setUrl(QUrl('http://qt-project.org/'))

    sys.exit(app.exec_())
