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


____ ?.QtCore ______ QFile, QRegExp, Qt
____ ?.QtGui ______ QFont, QSyntaxHighlighter, QTextCharFormat
____ ?.?W.. ______ (QApplication, QFileDialog, QMainWindow, QMenu,
        QMessageBox, QTextEdit)


class MainWindow(QMainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.setupFileMenu()
        self.setupHelpMenu()
        self.setupEditor()

        self.setCentralWidget(self.editor)
        self.setWindowTitle("Syntax Highlighter")

    ___ about(self):
        QMessageBox.about(self, "About Syntax Highlighter",
                "<p>The <b>Syntax Highlighter</b> example shows how to " \
                "perform simple syntax highlighting by subclassing the " \
                "QSyntaxHighlighter class and describing highlighting " \
                "rules using regular expressions.</p>")

    ___ newFile(self):
        self.editor.clear()

    ___ openFile(self, path_None):
        if not path:
            path, _ _ QFileDialog.getOpenFileName(self, "Open File", '',
                    "C++ Files (*.cpp *.h)")

        if path:
            inFile _ QFile(path)
            if inFile.open(QFile.ReadOnly | QFile.Text):
                text _ inFile.readAll()

                try:
                    # Python v3.
                    text _ str(text, encoding_'ascii')
                except TypeError:
                    # Python v2.
                    text _ str(text)

                self.editor.setPlainText(text)

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
        self.menuBar().addMenu(fileMenu)

        fileMenu.addAction("&New...", self.newFile, "Ctrl+N")
        fileMenu.addAction("&Open...", self.openFile, "Ctrl+O")
        fileMenu.addAction("E&xit", QApplication.instance().quit, "Ctrl+Q")

    ___ setupHelpMenu(self):
        helpMenu _ QMenu("&Help", self)
        self.menuBar().addMenu(helpMenu)

        helpMenu.addAction("&About", self.about)
        helpMenu.addAction("About &Qt", QApplication.instance().aboutQt)


class Highlighter(QSyntaxHighlighter):
    ___ __init__(self, parent_None):
        super(Highlighter, self).__init__(parent)

        keywordFormat _ QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
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
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat _ QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat _ QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat _ QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat _ QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression _ QRegExp("/\\*")
        self.commentEndExpression _ QRegExp("\\*/")

    ___ highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression _ QRegExp(pattern)
            index _ expression.indexIn(text)
            while index >_ 0:
                length _ expression.matchedLength()
                self.setFormat(index, length, format)
                index _ expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex _ 0
        if self.previousBlockState() !_ 1:
            startIndex _ self.commentStartExpression.indexIn(text)

        while startIndex >_ 0:
            endIndex _ self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength _ len(text) - startIndex
            else:
                commentLength _ endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex _ self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.resize(640, 512)
    window.s..
    sys.exit(app.exec_())
