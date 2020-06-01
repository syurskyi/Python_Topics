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


____ ?.?C.. ______ QFile, QRegExp, __
____ ?.?G.. ______ QFont, QSyntaxHighlighter, QTextCharFormat
____ ?.?W.. ______ (?A.., ?FD.., QMainWindow, QMenu,
        ?MB.., QTextEdit)


c_ MainWindow ?MW..
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.setupFileMenu()
        self.setupHelpMenu()
        self.setupEditor()

        self.sCW..(self.editor)
        self.setWindowTitle("Syntax Highlighter")

    ___ about(self):
        ?MB...about  "About Syntax Highlighter",
                "<p>The <b>Syntax Highlighter</b> example shows how to " \
                "perform simple syntax highlighting by subclassing the " \
                "QSyntaxHighlighter class and describing highlighting " \
                "rules using regular expressions.</p>")

    ___ newFile(self):
        self.editor.clear()

    ___ openFile  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Open File", '',
                    "C++ Files (*.cpp *.h)")

        __ path:
            inFile _ QFile(path)
            __ inFile.o..(QFile.ReadOnly | QFile.Text):
                t__ _ inFile.readAll()

                try:
                    # Python v3.
                    t__ _ str(t__, encoding_'ascii')
                except TypeError:
                    # Python v2.
                    t__ _ str(t__)

                self.editor.sPT..(t__)

    ___ setupEditor(self):
        font _ QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)

        self.editor _ QTextEdit()
        self.editor.setFont(font)

        self.highlighter _ Highlighter(self.editor.document())

    ___ setupFileMenu(self):
        fileMenu _ QMenu("&File", self)
        self.mB.. .aM..(fileMenu)

        fileMenu.aA..("&New...", self.newFile, "Ctrl+N")
        fileMenu.aA..("&Open...", self.openFile, "Ctrl+O")
        fileMenu.aA..("E&xit", ?A...instance().quit, "Ctrl+Q")

    ___ setupHelpMenu(self):
        helpMenu _ QMenu("&Help", self)
        self.mB.. .aM..(helpMenu)

        helpMenu.aA..("&About", self.about)
        helpMenu.aA..("About &Qt", ?A...instance().aboutQt)


c_ Highlighter(QSyntaxHighlighter):
    ___ __init__  parent_None):
        super(Highlighter, self).__init__(parent)

        keywordFormat _ QTextCharFormat()
        keywordFormat.setForeground(__.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns _ ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b"]

        self.highlightingRules _ [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat _ QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(__.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat _ QTextCharFormat()
        singleLineCommentFormat.setForeground(__.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat _ QTextCharFormat()
        self.multiLineCommentFormat.setForeground(__.red)

        quotationFormat _ QTextCharFormat()
        quotationFormat.setForeground(__.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat _ QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(__.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression _ QRegExp("/\\*")
        self.commentEndExpression _ QRegExp("\\*/")

    ___ highlightBlock  t__):
        for pattern, format in self.highlightingRules:
            expression _ QRegExp(pattern)
            index _ expression.indexIn(t__)
            while index >_ 0:
                length _ expression.matchedLength()
                self.setFormat(index, length, format)
                index _ expression.indexIn(t__, index + length)

        self.setCurrentBlockState(0)

        startIndex _ 0
        __ self.previousBlockState() !_ 1:
            startIndex _ self.commentStartExpression.indexIn(t__)

        while startIndex >_ 0:
            endIndex _ self.commentEndExpression.indexIn(t__, startIndex)

            __ endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength _ len(t__) - startIndex
            ____
                commentLength _ endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex _ self.commentStartExpression.indexIn(t__,
                    startIndex + commentLength);


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.resize(640, 512)
    window.s..
    sys.exit(app.exec_())
