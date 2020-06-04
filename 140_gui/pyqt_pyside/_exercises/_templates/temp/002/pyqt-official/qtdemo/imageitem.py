#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ QPoint
____ ?.?G.. ______ ?C.., QImage, QLinearGradient, QPainter

____ colors ______ Colors
____ demoitem ______ DemoItem


c_ ImageItem(DemoItem):
    ___  -   image, maxWidth, maxHeight, parent_None, adjustSize_False, scale_1.0):
        s__(ImageItem, self). - (parent)

        image _ image
        maxWidth _ maxWidth
        maxHeight _ maxHeight
        adjustSize _ adjustSize
        scale _ scale

    ___ createImage  transform):
        original _ QImage(image)
        __ original.isNull
            r_ original

        size _ transform.map(QPoint(maxWidth, maxHeight))
        w _ size.x()
        h _ size.y()

        # Optimization: if image is smaller than maximum allowed size, just
        # return the loaded image.
        __ original.size().height() <_ h and original.size().width() <_ w and no. adjustSize and scale __ 1:
            r_ original

        # Calculate what the size of the final image will be.
        w _ min(w, fl..(original.size().width()) * scale)
        h _ min(h, fl..(original.size().height()) * scale)

        adjustx _ 1.0
        adjusty _ 1.0
        __ adjustSize:
            adjustx _ min(transform.m11(), transform.m22())
            adjusty _ max(transform.m22(), adjustx)
            w *_ adjustx
            h *_ adjusty

        # Create a new image with correct size, and draw original on it.
        image _ QImage(in.(w + 2), in.(h + 2),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        __ adjustSize:
            painter.scale(adjustx, adjusty)
        __ scale !_ 1:
            painter.scale(scale, scale)
        painter.drawImage(0, 0, original)

        __ no. adjustSize:
            # Blur out edges.
            blur _ 30

            __ h < original.height
                brush1 _ QLinearGradient(0, h - blur, 0, h)
                brush1.setSpread(QLinearGradient.PadSpread)
                brush1.setColorAt(0.0, ?C..(0, 0, 0, 0))
                brush1.setColorAt(1.0, Colors.sceneBg1)
                painter.fillRect(0, in.(h) - blur, original.width(), in.(h),
                        brush1)

            __ w < original.width
                brush2 _ QLinearGradient(w - blur, 0, w, 0)
                brush2.setSpread(QLinearGradient.PadSpread)
                brush2.setColorAt(0.0, ?C..(0, 0, 0, 0))
                brush2.setColorAt(1.0, Colors.sceneBg1)
                painter.fillRect(in.(w) - blur, 0, in.(w), original.height(),
                        brush2)

        r_ image
