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


____ ?.QtCore ______ QByteArray, QFile, QRegExp, Qt
____ ?.QtGui ______ (QColor, QFont, QSyntaxHighlighter, QTextCharFormat,
        QTextCursor, QTextFormat)
____ ?.?W.. ______ QApplication, QMainWindow, QTextEdit
____ ?.QtXmlPatterns ______ (QAbstractMessageHandler, QSourceLocation,
        QXmlSchema, QXmlSchemaValidator)

______ schema_rc
____ ui_schema ______ Ui_SchemaMainWindow


___ encode_utf8(ba):
    try:
        return unicode(ba, encoding_'utf8')
    except NameError:
        return str(ba, encoding_'utf8')


___ decode_utf8(qs):
    try:
        return QByteArray(qs.decode(encoding_'utf8'))
    except AttributeError:
        return QByteArray(bytes(qs, encoding_'utf8'))


class XmlSyntaxHighlighter(QSyntaxHighlighter):

    ___ __init__(self, parent_None):
        super(XmlSyntaxHighlighter, self).__init__(parent)

        self.highlightingRules _ []

        # Tag format.
        format _ QTextCharFormat()
        format.setForeground(Qt.darkBlue)
        format.setFontWeight(QFont.Bold)
        pattern _ QRegExp("(<[a-zA-Z:]+\\b|<\\?[a-zA-Z:]+\\b|\\?>|>|/>|</[a-zA-Z:]+>)")
        self.highlightingRules.append((pattern, format))

        # Attribute format.
        format _ QTextCharFormat()
        format.setForeground(Qt.darkGreen)
        pattern _ QRegExp("[a-zA-Z:]+=")
        self.highlightingRules.append((pattern, format))

        # Attribute content format.
        format _ QTextCharFormat()
        format.setForeground(Qt.red)
        pattern _ QRegExp("(\"[^\"]*\"|'[^']*')")
        self.highlightingRules.append((pattern, format))

        # Comment format.
        self.commentFormat _ QTextCharFormat()
        self.commentFormat.setForeground(Qt.lightGray)
        self.commentFormat.setFontItalic(True)

        self.commentStartExpression _ QRegExp("<!--")
        self.commentEndExpression _ QRegExp("-->")

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
                commentLength _ text.length() - startIndex
            else:
                commentLength _ endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength, self.commentFormat)
            startIndex _ self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)


class MessageHandler(QAbstractMessageHandler):

    ___ __init__(self):
        super(MessageHandler, self).__init__()

        self.m_description _ ""
        self.m_sourceLocation _ QSourceLocation()

    ___ statusMessage(self):
        return self.m_description

    ___ line(self):
        return self.m_sourceLocation.line()

    ___ column(self):
        return self.m_sourceLocation.column()

    ___ handleMessage(self, type, description, identifier, sourceLocation):
        self.m_description _ description
        self.m_sourceLocation _ sourceLocation


class MainWindow(QMainWindow, Ui_SchemaMainWindow):

    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        XmlSyntaxHighlighter(self.schemaView.document())
        XmlSyntaxHighlighter(self.instanceEdit.document())

        self.schemaSelection.addItem("Contact Schema")
        self.schemaSelection.addItem("Recipe Schema")
        self.schemaSelection.addItem("Order Schema")

        self.instanceSelection.addItem("Valid Contact Instance")
        self.instanceSelection.addItem("Invalid Contact Instance")

        self.schemaSelection.currentIndexChanged.c..(self.schemaSelected)
        self.instanceSelection.currentIndexChanged.c..(self.instanceSelected)
        self.validateButton.c__.c..(self.validate)
        self.instanceEdit.textChanged.c..(self.textChanged)

        self.validationStatus.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.schemaSelected(0)
        self.instanceSelected(0)

    ___ schemaSelected(self, index):
        self.instanceSelection.clear()

        if index == 0:
            self.instanceSelection.addItem("Valid Contact Instance")
            self.instanceSelection.addItem("Invalid Contact Instance")
        elif index == 1:
            self.instanceSelection.addItem("Valid Recipe Instance")
            self.instanceSelection.addItem("Invalid Recipe Instance")
        elif index == 2:
            self.instanceSelection.addItem("Valid Order Instance")
            self.instanceSelection.addItem("Invalid Order Instance")

        self.textChanged()

        schemaFile _ QFile(':/schema_%d.xsd' % index)
        schemaFile.open(QFile.ReadOnly)
        schemaData _ schemaFile.readAll()
        self.schemaView.setPlainText(encode_utf8(schemaData))

        self.validate()

    ___ instanceSelected(self, index):
        index +_ 2 * self.schemaSelection.currentIndex()
        instanceFile _ QFile(':/instance_%d.xml' % index)
        instanceFile.open(QFile.ReadOnly)
        instanceData _ instanceFile.readAll()
        self.instanceEdit.setPlainText(encode_utf8(instanceData))

        self.validate()

    ___ validate(self):
        schemaData _ decode_utf8(self.schemaView.toPlainText())
        instanceData _ decode_utf8(self.instanceEdit.toPlainText())

        messageHandler _ MessageHandler()

        schema _ QXmlSchema()
        schema.setMessageHandler(messageHandler)
        schema.load(schemaData)

        errorOccurred _ False
        if not schema.isValid
            errorOccurred _ True
        else:
            validator _ QXmlSchemaValidator(schema)
            if not validator.validate(instanceData):
                errorOccurred _ True

        if errorOccurred:
            self.validationStatus.sT..(messageHandler.statusMessage())
            self.moveCursor(messageHandler.line(), messageHandler.column())
            background _ Qt.red
        else:
            self.validationStatus.sT..("validation successful")
            background _ Qt.green

        styleSheet _ 'QLabel {background: %s; padding: 3px}' % QColor(background).lighter(160).name()
        self.validationStatus.setStyleSheet(styleSheet)

    ___ textChanged(self):
        self.instanceEdit.setExtraSelections([])

    ___ moveCursor(self, line, column):
        self.instanceEdit.moveCursor(QTextCursor.Start)

        for i in range(1, line):
            self.instanceEdit.moveCursor(QTextCursor.Down)

        for i in range(1, column):
            self.instanceEdit.moveCursor(QTextCursor.Right)

        extraSelections _ []
        selection _ QTextEdit.ExtraSelection()

        lineColor _ QColor(Qt.red).lighter(160)
        selection.format.setBackground(lineColor)
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor _ self.instanceEdit.textCursor()
        selection.cursor.clearSelection()
        extraSelections.append(selection)

        self.instanceEdit.setExtraSelections(extraSelections)

        self.instanceEdit.setFocus()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
