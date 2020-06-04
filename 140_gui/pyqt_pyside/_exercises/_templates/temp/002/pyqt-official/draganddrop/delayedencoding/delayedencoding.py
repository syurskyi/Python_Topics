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
#############################################################################


____ ?.?C.. ______ (pS.., QBuffer, QByteArray, QFile, QIODevice,
        QMimeData, __)
____ ?.?G.. ______ QDrag, ?I.., QImage, QPainter, ?P..
____ ?.?W.. ______ (?A.., QGridLayout, ?L.., ?PB..,
        QScrollArea, ?W..)
____ ?.QtSvg ______ QSvgWidget

______ delayedencoding_rc


c_ MimeData(QMimeData):

    dataRequested _ pS.. st.

    ___ formats
        formats _ QMimeData.formats
        formats.ap..('image/png')

        r_ formats

    ___ retrieveData  mimeType, qvtype):
        dataRequested.e..(mimeType)

        r_ QMimeData.retrieveData  mimeType, qvtype)


c_ SourceWidget(?W..):
    ___  -   parent_None):
        s__(SourceWidget, self). - (parent)

        mimeData _ N..

        imageFile _ QFile(':/images/example.svg')
        imageFile.o..(QIODevice.ReadOnly)
        imageData _ imageFile.rA..
        imageFile.c..

        imageArea _ QScrollArea()
        imageLabel _ QSvgWidget()
        imageLabel.renderer().load(imageData)
        imageArea.setWidget(imageLabel)

        instructTopLabel _ ?L..("This is an SVG drawing:")
        instructBottomLabel _ ?L..("Drag the icon to copy the drawing as a PNG file:")
        dragIcon _ ?PB..("Export")
        dragIcon.sI..(?I..(':/images/drag.png'))
        dragIcon.pressed.c..(startDrag)

        layout _ QGridLayout()
        layout.aW..(instructTopLabel, 0, 0, 1, 2)
        layout.aW..(imageArea, 1, 0, 2, 2)
        layout.aW..(instructBottomLabel, 3, 0)
        layout.aW..(dragIcon, 3, 1)
        sL..(layout)
        sWT..("Delayed Encoding")

    ___ createData  mimeType):
        __ mimeType !_ 'image/png':
            r_

        image _ QImage(imageLabel.size(), QImage.Format_RGB32)
        painter _ QPainter()
        painter.begin(image)
        imageLabel.renderer().render(painter)
        painter.end()

        data _ QByteArray()
        buffer _ QBuffer(data)
        buffer.o..(QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        buffer.c..
        mimeData.setData('image/png', data)

    ___ startDrag
        mimeData _ MimeData()
        mimeData.dataRequested.c..(createData, __.DirectConnection)

        drag _ QDrag
        drag.setMimeData(mimeData)
        drag.sP..(?P..(':/images/drag.png'))
        drag.e..(__.CopyAction)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ SourceWidget()
    window.s..
    ___.e.. ?.e..
