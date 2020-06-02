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


____ ?.?C.. ______ QByteArray, QFile, QRegExp, __
____ ?.?G.. ______ (?C.., ?F.., QSyntaxHighlighter, QTextCharFormat,
        QTextCursor, QTextFormat)
____ ?.?W.. ______ ?A.., ?MW.., ?TE..
____ ?.QtXmlPatterns ______ (QAbstractMessageHandler, QSourceLocation,
        QXmlSchema, QXmlSchemaValidator)

______ schema_rc
____ ui_schema ______ Ui_SchemaMainWindow


___ encode_utf8(ba):
    ___
        r_ unicode(ba, encoding_'utf8')
    _____ NameError:
        r_ st.(ba, encoding_'utf8')


___ decode_utf8(qs):
    ___
        r_ QByteArray(qs.d..(encoding_'utf8'))
    _____ AttributeError:
        r_ QByteArray(by..(qs, encoding_'utf8'))


c_ XmlSyntaxHighlighter(QSyntaxHighlighter):

    ___  -   parent_None):
        s__(XmlSyntaxHighlighter, self). - (parent)

        highlightingRules _   # list

        # Tag format.
        f.. _ QTextCharFormat()
        f...setForeground(__.darkBlue)
        f...setFontWeight(?F...Bold)
        pattern _ QRegExp("(<[a-zA-Z:]+\\b|<\\?[a-zA-Z:]+\\b|\\?>|>|/>|</[a-zA-Z:]+>)")
        highlightingRules.ap..((pattern, f..))

        # Attribute format.
        f.. _ QTextCharFormat()
        f...setForeground(__.darkGreen)
        pattern _ QRegExp("[a-zA-Z:]+=")
        highlightingRules.ap..((pattern, f..))

        # Attribute content format.
        f.. _ QTextCharFormat()
        f...setForeground(__.red)
        pattern _ QRegExp("(\"[^\"]*\"|'[^']*')")
        highlightingRules.ap..((pattern, f..))

        # Comment format.
        commentFormat _ QTextCharFormat()
        commentFormat.setForeground(__.lightGray)
        commentFormat.setFontItalic( st.

        commentStartExpression _ QRegExp("<!--")
        commentEndExpression _ QRegExp("-->")

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
                commentLength _ t__.length() - startIndex
            ____
                commentLength _ endIndex - startIndex + commentEndExpression.matchedLength()

            setFormat(startIndex, commentLength, commentFormat)
            startIndex _ commentStartExpression.indexIn(t__,
                    startIndex + commentLength)


c_ MessageHandler(QAbstractMessageHandler):

    ___  -
        s__(MessageHandler, self). - ()

        m_description _ ""
        m_sourceLocation _ QSourceLocation()

    ___ statusMessage
        r_ m_description

    ___ line
        r_ m_sourceLocation.line()

    ___ column
        r_ m_sourceLocation.column()

    ___ handleMessage  type, description, identifier, sourceLocation):
        m_description _ description
        m_sourceLocation _ sourceLocation


c_ MainWindow(?MW.., Ui_SchemaMainWindow):

    ___  -
        s__(MainWindow, self). - ()

        setupUi

        XmlSyntaxHighlighter(schemaView.document())
        XmlSyntaxHighlighter(instanceEdit.document())

        schemaSelection.aI..("Contact Schema")
        schemaSelection.aI..("Recipe Schema")
        schemaSelection.aI..("Order Schema")

        instanceSelection.aI..("Valid Contact Instance")
        instanceSelection.aI..("Invalid Contact Instance")

        schemaSelection.currentIndexChanged.c..(schemaSelected)
        instanceSelection.currentIndexChanged.c..(instanceSelected)
        validateButton.c__.c..(validate)
        instanceEdit.tC...c..(tC..)

        validationStatus.setAlignment(__.AlignCenter | __.AlignVCenter)

        schemaSelected(0)
        instanceSelected(0)

    ___ schemaSelected  index):
        instanceSelection.c..

        __ index __ 0:
            instanceSelection.aI..("Valid Contact Instance")
            instanceSelection.aI..("Invalid Contact Instance")
        ____ index __ 1:
            instanceSelection.aI..("Valid Recipe Instance")
            instanceSelection.aI..("Invalid Recipe Instance")
        ____ index __ 2:
            instanceSelection.aI..("Valid Order Instance")
            instanceSelection.aI..("Invalid Order Instance")

        tC..()

        schemaFile _ QFile(':/schema_%d.xsd' % index)
        schemaFile.o..(QFile.ReadOnly)
        schemaData _ schemaFile.rA..
        schemaView.sPT..(encode_utf8(schemaData))

        validate()

    ___ instanceSelected  index):
        index +_ 2 * schemaSelection.currentIndex()
        instanceFile _ QFile(':/instance_%d.xml' % index)
        instanceFile.o..(QFile.ReadOnly)
        instanceData _ instanceFile.rA..
        instanceEdit.sPT..(encode_utf8(instanceData))

        validate()

    ___ validate
        schemaData _ decode_utf8(schemaView.tPT..
        instanceData _ decode_utf8(instanceEdit.tPT..

        messageHandler _ MessageHandler()

        schema _ QXmlSchema()
        schema.setMessageHandler(messageHandler)
        schema.load(schemaData)

        errorOccurred _ F..
        __ no. schema.isValid
            errorOccurred _ T..
        ____
            validator _ QXmlSchemaValidator(schema)
            __ no. validator.validate(instanceData):
                errorOccurred _ T..

        __ errorOccurred:
            validationStatus.sT..(messageHandler.statusMessage())
            moveCursor(messageHandler.line(), messageHandler.column())
            background _ __.red
        ____
            validationStatus.sT..("validation successful")
            background _ __.green

        styleSheet _ 'QLabel {background: %s; padding: 3px}' % ?C..(background).lighter(160).name()
        validationStatus.sSS..(styleSheet)

    ___ tC..
        instanceEdit.setExtraSelections(  # list)

    ___ moveCursor  line, column):
        instanceEdit.moveCursor(QTextCursor.Start)

        ___ i __ ra..(1, line):
            instanceEdit.moveCursor(QTextCursor.Down)

        ___ i __ ra..(1, column):
            instanceEdit.moveCursor(QTextCursor.Right)

        extraSelections _   # list
        selection _ ?TE...ExtraSelection()

        lineColor _ ?C..(__.red).lighter(160)
        selection.f...setBackground(lineColor)
        selection.f...setProperty(QTextFormat.FullWidthSelection,  st.
        selection.cursor _ instanceEdit.textCursor()
        selection.cursor.clearSelection()
        extraSelections.ap..(selection)

        instanceEdit.setExtraSelections(extraSelections)

        instanceEdit.setFocus()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
