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


____ ?.?C.. ______ QFile, QIODevice, ?O.., QSizeF
____ ?.?G.. ______ QTextCharFormat, QTextFormat, QTextObjectInterface
____ ?.?W.. ______ (?A.., ?HBL.., ?L.., QLineEdit,
        ?MB.., ?PB.., ?TE.., ?VBL.., ?W..)
____ ?.QtSvg ______ QSvgRenderer


c_ SvgTextObject(?O.., QTextObjectInterface):
    ___ intrinsicSize  doc, posInDocument, f..):
        renderer _ QSvgRenderer(f...property(Window.SvgData))
        size _ renderer.defaultSize()

        __ size.height() > 25:
            size *_ 25.0 / size.height()

        r_ QSizeF(size)

    ___ drawObject  painter, rect, doc, posInDocument, f..):
        renderer _ QSvgRenderer(f...property(Window.SvgData))
        renderer.render(painter, rect)


c_ Window(?W..):

    SvgTextFormat _ QTextFormat.UserObject + 1

    SvgData _ 1

    ___  -
        s__(Window, self). - ()

        setupGui()
        setupTextObject()

        sWT..("Text Object Example")

    ___ insertTextObject
        fileName _ fileNameLineEdit.t__()
        file _ QFile(fileName)

        __ no. file.o..(QIODevice.ReadOnly):
            ?MB...w..  "Error Opening File",
                    "Could not open '%s'" % fileName)

        svgData _ file.rA..

        svgCharFormat _ QTextCharFormat()
        svgCharFormat.setObjectType(Window.SvgTextFormat)
        svgCharFormat.setProperty(Window.SvgData, svgData)

        ___
            # Python v2.
            orc _ unichr(0xfffc)
        _____ NameError:
            # Python v3.
            orc _ chr(0xfffc)

        cursor _ textEdit.textCursor()
        cursor.insertText(orc, svgCharFormat)
        textEdit.setTextCursor(cursor)

    ___ setupTextObject
        svgInterface _ SvgTextObject
        textEdit.document().documentLayout().registerHandler(Window.SvgTextFormat, svgInterface)

    ___ setupGui
        fileNameLabel _ ?L..("Svg File Name:")
        fileNameLineEdit _ ?LE..
        insertTextObjectButton _ ?PB..("Insert Image")

        fileNameLineEdit.sT..('./files/heart.svg')
        insertTextObjectButton.c__.c..(insertTextObject)

        bottomLayout _ ?HBL..
        bottomLayout.aW..(fileNameLabel)
        bottomLayout.aW..(fileNameLineEdit)
        bottomLayout.aW..(insertTextObjectButton)

        textEdit _ ?TE..()

        mainLayout _ ?VBL..
        mainLayout.aW..(textEdit)
        mainLayout.aL..(bottomLayout)

        sL..(mainLayout)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Window()
    window.s..
    ___.e.. ?.e..
