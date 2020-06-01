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


____ ?.QtCore ______ QFile, QIODevice, QObject, QSizeF
____ ?.QtGui ______ QTextCharFormat, QTextFormat, QTextObjectInterface
____ ?.?W.. ______ (QApplication, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, ?PB.., QTextEdit, QVBoxLayout, QWidget)
____ ?.QtSvg ______ QSvgRenderer


class SvgTextObject(QObject, QTextObjectInterface):
    ___ intrinsicSize(self, doc, posInDocument, format):
        renderer _ QSvgRenderer(format.property(Window.SvgData))
        size _ renderer.defaultSize()

        if size.height() > 25:
            size *_ 25.0 / size.height()

        return QSizeF(size)

    ___ drawObject(self, painter, rect, doc, posInDocument, format):
        renderer _ QSvgRenderer(format.property(Window.SvgData))
        renderer.render(painter, rect)


class Window(QWidget):

    SvgTextFormat _ QTextFormat.UserObject + 1

    SvgData _ 1

    ___ __init__(self):
        super(Window, self).__init__()

        self.setupGui()
        self.setupTextObject()

        self.setWindowTitle("Text Object Example")

    ___ insertTextObject(self):
        fileName _ self.fileNameLineEdit.text()
        file _ QFile(fileName)

        if not file.open(QIODevice.ReadOnly):
            QMessageBox.warning(self, "Error Opening File",
                    "Could not open '%s'" % fileName)

        svgData _ file.readAll()

        svgCharFormat _ QTextCharFormat()
        svgCharFormat.setObjectType(Window.SvgTextFormat)
        svgCharFormat.setProperty(Window.SvgData, svgData)

        try:
            # Python v2.
            orc _ unichr(0xfffc)
        except NameError:
            # Python v3.
            orc _ chr(0xfffc)

        cursor _ self.textEdit.textCursor()
        cursor.insertText(orc, svgCharFormat)
        self.textEdit.setTextCursor(cursor)

    ___ setupTextObject(self):
        svgInterface _ SvgTextObject(self)
        self.textEdit.document().documentLayout().registerHandler(Window.SvgTextFormat, svgInterface)

    ___ setupGui(self):
        fileNameLabel _ QLabel("Svg File Name:")
        self.fileNameLineEdit _ QLineEdit()
        insertTextObjectButton _ ?PB..("Insert Image")

        self.fileNameLineEdit.sT..('./files/heart.svg')
        insertTextObjectButton.c__.c..(self.insertTextObject)

        bottomLayout _ QHBoxLayout()
        bottomLayout.addWidget(fileNameLabel)
        bottomLayout.addWidget(self.fileNameLineEdit)
        bottomLayout.addWidget(insertTextObjectButton)

        self.textEdit _ QTextEdit()

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.textEdit)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ Window()
    window.s..
    sys.exit(app.exec_())
