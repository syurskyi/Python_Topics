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
____ ?.?G.. ______ (?C.., QFont, QSyntaxHighlighter, QTextCharFormat,
        QTextCursor, QTextFormat)
____ ?.?W.. ______ ?A.., QMainWindow, QTextEdit
____ ?.QtXmlPatterns ______ (QAbstractMessageHandler, QSourceLocation,
        QXmlSchema, QXmlSchemaValidator)

______ schema_rc
____ ui_schema ______ Ui_SchemaMainWindow


___ encode_utf8(ba):
    try:
        r_ unicode(ba, encoding_'utf8')
    except NameError:
        r_ str(ba, encoding_'utf8')


___ decode_utf8(qs):
    try:
        r_ QByteArray(qs.decode(encoding_'utf8'))
    except AttributeError:
        r_ QByteArray(bytes(qs, encoding_'utf8'))


c_ XmlSyntaxHighlighter(QSyntaxHighlighter):

    ___  -   parent_None):
        super(XmlSyntaxHighlighter, self). - (parent)

        highlightingRules _   # list

        # Tag format.
        format _ QTextCharFormat()
        format.setForeground(__.darkBlue)
        format.setFontWeight(QFont.Bold)
        pattern _ QRegExp("(<[a-zA-Z:]+\\b|<\\?[a-zA-Z:]+\\b|\\?>|>|/>|</[a-zA-Z:]+>)")
        highlightingRules.ap..((pattern, format))

        # Attribute format.
        format _ QTextCharFormat()
        format.setForeground(__.darkGreen)
        pattern _ QRegExp("[a-zA-Z:]+=")
        highlightingRules.ap..((pattern, format))

        # Attribute content format.
        format _ QTextCharFormat()
        format.setForeground(__.red)
        pattern _ QRegExp("(\"[^\"]*\"|'[^']*')")
        highlightingRules.ap..((pattern, format))

        # Comment format.
        commentFormat _ QTextCharFormat()
        commentFormat.setForeground(__.lightGray)
        commentFormat.setFontItalic(True)

        commentStartExpression _ QRegExp("<!--")
        commentEndExpression _ QRegExp("-->")

    ___ highlightBlock  t__):
        ___ pattern, format __ highlightingRules:
            expression _ QRegExp(pattern)
            index _ expression.indexIn(t__)
            w__ index >_ 0:
                length _ expression.matchedLength()
                setFormat(index, length, format)
                index _ expression.indexIn(t__, index + length)

        setCurrentBlockState(0)

        startIndex _ 0
        __ previousBlockState() !_ 1:
            startIndex _ commentStartExpression.indexIn(t__)

        w__ startIndex >_ 0:
            endIndex _ commentEndExpression.indexIn(t__, startIndex)
            __ endIndex == -1:
                setCurrentBlockState(1)
                commentLength _ t__.length() - startIndex
            ____
                commentLength _ endIndex - startIndex + commentEndExpression.matchedLength()

            setFormat(startIndex, commentLength, commentFormat)
            startIndex _ commentStartExpression.indexIn(t__,
                    startIndex + commentLength)


c_ MessageHandler(QAbstractMessageHandler):

    ___  -
        super(MessageHandler, self). - ()

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


c_ MainWindow(QMainWindow, Ui_SchemaMainWindow):

    ___  -
        super(MainWindow, self). - ()

        setupUi

        XmlSyntaxHighlighter(schemaView.document())
        XmlSyntaxHighlighter(instanceEdit.document())

        schemaSelection.addItem("Contact Schema")
        schemaSelection.addItem("Recipe Schema")
        schemaSelection.addItem("Order Schema")

        instanceSelection.addItem("Valid Contact Instance")
        instanceSelection.addItem("Invalid Contact Instance")

        schemaSelection.currentIndexChanged.c..(schemaSelected)
        instanceSelection.currentIndexChanged.c..(instanceSelected)
        validateButton.c__.c..(validate)
        instanceEdit.textChanged.c..(textChanged)

        validationStatus.setAlignment(__.AlignCenter | __.AlignVCenter)

        schemaSelected(0)
        instanceSelected(0)

    ___ schemaSelected  index):
        instanceSelection.clear()

        __ index == 0:
            instanceSelection.addItem("Valid Contact Instance")
            instanceSelection.addItem("Invalid Contact Instance")
        ____ index == 1:
            instanceSelection.addItem("Valid Recipe Instance")
            instanceSelection.addItem("Invalid Recipe Instance")
        ____ index == 2:
            instanceSelection.addItem("Valid Order Instance")
            instanceSelection.addItem("Invalid Order Instance")

        textChanged()

        schemaFile _ QFile(':/schema_%d.xsd' % index)
        schemaFile.o..(QFile.ReadOnly)
        schemaData _ schemaFile.readAll()
        schemaView.sPT..(encode_utf8(schemaData))

        validate()

    ___ instanceSelected  index):
        index +_ 2 * schemaSelection.currentIndex()
        instanceFile _ QFile(':/instance_%d.xml' % index)
        instanceFile.o..(QFile.ReadOnly)
        instanceData _ instanceFile.readAll()
        instanceEdit.sPT..(encode_utf8(instanceData))

        validate()

    ___ validate
        schemaData _ decode_utf8(schemaView.tPT..
        instanceData _ decode_utf8(instanceEdit.tPT..

        messageHandler _ MessageHandler()

        schema _ QXmlSchema()
        schema.setMessageHandler(messageHandler)
        schema.load(schemaData)

        errorOccurred _ False
        __ no. schema.isValid
            errorOccurred _ True
        ____
            validator _ QXmlSchemaValidator(schema)
            __ no. validator.validate(instanceData):
                errorOccurred _ True

        __ errorOccurred:
            validationStatus.sT..(messageHandler.statusMessage())
            moveCursor(messageHandler.line(), messageHandler.column())
            background _ __.red
        ____
            validationStatus.sT..("validation successful")
            background _ __.green

        styleSheet _ 'QLabel {background: %s; padding: 3px}' % ?C..(background).lighter(160).name()
        validationStatus.setStyleSheet(styleSheet)

    ___ textChanged
        instanceEdit.setExtraSelections(  # list)

    ___ moveCursor  line, column):
        instanceEdit.moveCursor(QTextCursor.Start)

        ___ i __ range(1, line):
            instanceEdit.moveCursor(QTextCursor.Down)

        ___ i __ range(1, column):
            instanceEdit.moveCursor(QTextCursor.Right)

        extraSelections _   # list
        selection _ QTextEdit.ExtraSelection()

        lineColor _ ?C..(__.red).lighter(160)
        selection.format.setBackground(lineColor)
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
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
    ___.e..(app.exec_())
