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
____ ?.?G.. ______ ?F.., QSyntaxHighlighter, QTextCharFormat
____ ?.?W.. ______ (?A.., ?FD.., ?MW.., ?M..,
        ?MB.., ?TE..)


c_ MainWindow ?MW..
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        setupFileMenu()
        setupHelpMenu()
        setupEditor()

        sCW..(editor)
        sWT..("Syntax Highlighter")

    ___ about
        ?MB...about  "About Syntax Highlighter",
                "<p>The <b>Syntax Highlighter</b> example shows how to " \
                "perform simple syntax highlighting by subclassing the " \
                "QSyntaxHighlighter class and describing highlighting " \
                "rules using regular expressions.</p>")

    ___ newFile
        editor.c..

    ___ openFile  path_None):
        __ no. pa__:
            pa__, _ _ ?FD...gOFN..  "Open File", '',
                    "C++ Files (*.cpp *.h)")

        __ pa__:
            inFile _ QFile(pa__)
            __ inFile.o..(QFile.ReadOnly | QFile.Text):
                t__ _ inFile.rA..

                ___
                    # Python v3.
                    t__ _ st.(t__, encoding_'ascii')
                _____ TypeError:
                    # Python v2.
                    t__ _ st.(t__)

                editor.sPT..(t__)

    ___ setupEditor
        font _ ?F..()
        font.sF..('Courier')
        font.setFixedPitch( st.
        font.sPS..(10)

        editor _ ?TE..()
        editor.sF..(font)

        highlighter _ Highlighter(editor.document())

    ___ setupFileMenu
        fileMenu _ ?M..("&File", self)
        mB.. .aM..(fileMenu)

        fileMenu.aA..("&New...", newFile, "Ctrl+N")
        fileMenu.aA..("&Open...", openFile, "Ctrl+O")
        fileMenu.aA..("E&xit", ?A...i.. .quit, "Ctrl+Q")

    ___ setupHelpMenu
        helpMenu _ ?M..("&Help", self)
        mB.. .aM..(helpMenu)

        helpMenu.aA..("&About", about)
        helpMenu.aA..("About &Qt", ?A...i.. .aboutQt)


c_ Highlighter(QSyntaxHighlighter):
    ___  -   parent_None):
        s__(Highlighter, self). - (parent)

        keywordFormat _ QTextCharFormat()
        keywordFormat.setForeground(__.darkBlue)
        keywordFormat.setFontWeight(?F...Bold)

        keywordPatterns _ ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b"]

        highlightingRules _ [(QRegExp(pattern), keywordFormat)
                ___ pattern __ keywordPatterns]

        classFormat _ QTextCharFormat()
        classFormat.setFontWeight(?F...Bold)
        classFormat.setForeground(__.darkMagenta)
        highlightingRules.ap..((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat _ QTextCharFormat()
        singleLineCommentFormat.setForeground(__.red)
        highlightingRules.ap..((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        multiLineCommentFormat _ QTextCharFormat()
        multiLineCommentFormat.setForeground(__.red)

        quotationFormat _ QTextCharFormat()
        quotationFormat.setForeground(__.darkGreen)
        highlightingRules.ap..((QRegExp("\".*\""), quotationFormat))

        functionFormat _ QTextCharFormat()
        functionFormat.setFontItalic( st.
        functionFormat.setForeground(__.blue)
        highlightingRules.ap..((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        commentStartExpression _ QRegExp("/\\*")
        commentEndExpression _ QRegExp("\\*/")

    ___ highlightBlock  t__):
        ___ pattern, f.. __ highlightingRules:
            expression _ QRegExp(pattern)
            index _ expression.indexIn(t__)
            w__ index >_ 0:
                length _ expression.matchedLength()
                setFormat(index, length, f..)
                index _ expression.indexIn(t__, index + length)

        setCurrentBlockState(0)

        startIndex _ 0
        __ previousBlockState() !_ 1:
            startIndex _ commentStartExpression.indexIn(t__)

        w__ startIndex >_ 0:
            endIndex _ commentEndExpression.indexIn(t__, startIndex)

            __ endIndex __ -1:
                setCurrentBlockState(1)
                commentLength _ le.(t__) - startIndex
            ____
                commentLength _ endIndex - startIndex + commentEndExpression.matchedLength()

            setFormat(startIndex, commentLength,
                    multiLineCommentFormat)
            startIndex _ commentStartExpression.indexIn(t__,
                    startIndex + commentLength);


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.r..(640, 512)
    window.s..
    ___.e.. ?.e..
