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


____ ?.?C.. ______ QRect, __
____ ?.?G.. ______ ?C.., QImage, QLinearGradient, QPainter

____ colors ______ Colors
____ demoitem ______ DemoItem


c_ LetterItem(DemoItem):
    ___  -   letter, parent_None):
        s__(LetterItem, self). - (parent)

        letter _ letter

        useSharedImage(__file__ + letter)

    ___ createImage  transform):
        scaledRect _ transform.mapRect(QRect(0, 0, 25, 25))
        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(0)
        painter _ QPainter(image)
        painter.scale(transform.m11(), transform.m22())
        painter.setRenderHints(QPainter.TextAntialiasing | QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        painter.sP..(__.NoPen)

        __ Colors.useEightBitPalette:
            painter.sB..(?C..(102, 175, 54))
            painter.drawEllipse(0, 0, 25, 25)
            painter.sF..(Colors.tickerFont())
            painter.sP..(?C..(255, 255, 255))
            painter.drawText(10, 15, letter)
        ____
            brush _ QLinearGradient(0, 0, 0, 25)
            brush.setSpread(QLinearGradient.PadSpread)
            brush.setColorAt(0.0, ?C..(102, 175, 54, 200))
            brush.setColorAt(1.0, ?C..(102, 175, 54, 60))
            painter.sB..(brush)
            painter.drawEllipse(0, 0, 25, 25)
            painter.sF..(Colors.tickerFont())
            painter.sP..(?C..(255, 255, 255, 255))
            painter.drawText(10, 15, letter)

        r_ image
