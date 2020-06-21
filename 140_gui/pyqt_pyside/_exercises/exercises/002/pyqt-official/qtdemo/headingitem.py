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


____ ?.?C.. ______ __
____ ?.?G.. ______ (?C.., QFontMetrics, QImage, QLinearGradient,
        QPainter, ?P..)

____ colors ______ Colors
____ demoitem ______ DemoItem


c_ HeadingItem(DemoItem):
    ___  -   t__, parent_None):
        s__(HeadingItem, self). - (parent)

        t__ _ t__
        noSubPixeling _ T..

    ___ createImage  transform):
        sx _ min(transform.m11(), transform.m22())
        sy _ max(transform.m22(), sx)
        fm _ QFontMetrics(Colors.headingFont())

        w _ fm.width(t__) + 1
        h _ fm.height()
        xShadow _ 3.0
        yShadow _ 3.0

        image _ QImage(in.((w + xShadow) * sx), in.((h + yShadow) * sy),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.sF..(Colors.headingFont())
        painter.scale(sx, sy)

        # Draw shadow.
        brush_shadow _ QLinearGradient(xShadow, yShadow, w, yShadow)
        brush_shadow.setSpread(QLinearGradient.PadSpread)
        __ Colors.useEightBitPalette:
            brush_shadow.setColorAt(0.0, ?C..(0, 0, 0))
        ____
            brush_shadow.setColorAt(0.0, ?C..(0, 0, 0, 100))
        pen_shadow _ ?P..()
        pen_shadow.sB..(brush_shadow)
        painter.sP..(pen_shadow)
        painter.drawText(in.(xShadow), in.(yShadow), in.(w), in.(h),
                __.AlignLeft, t__)

        # Draw text.
        brush_text _ QLinearGradient(0, 0, w, w)
        brush_text.setSpread(QLinearGradient.PadSpread)
        brush_text.setColorAt(0.0, ?C..(255, 255, 255))
        brush_text.setColorAt(0.2, ?C..(255, 255, 255))
        brush_text.setColorAt(0.5, ?C..(190, 190, 190))
        pen_text _ ?P..()
        pen_text.sB..(brush_text)
        painter.sP..(pen_text)
        painter.drawText(0, 0, in.(w), in.(h), __.AlignLeft, t__)

        r_ image

    ___ animationStarted  id_0):
        noSubPixeling _ F..

    ___ animationStopped  id_0):
        noSubPixeling _ T..
