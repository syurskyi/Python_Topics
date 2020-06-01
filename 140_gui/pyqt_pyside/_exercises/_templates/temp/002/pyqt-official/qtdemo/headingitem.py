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


____ ?.QtCore ______ Qt
____ ?.QtGui ______ (QColor, QFontMetrics, QImage, QLinearGradient,
        QPainter, QPen)

____ colors ______ Colors
____ demoitem ______ DemoItem


class HeadingItem(DemoItem):
    ___ __init__(self, text, parent_None):
        super(HeadingItem, self).__init__(parent)

        self.text _ text
        self.noSubPixeling _ True

    ___ createImage(self, transform):
        sx _ min(transform.m11(), transform.m22())
        sy _ max(transform.m22(), sx)
        fm _ QFontMetrics(Colors.headingFont())

        w _ fm.width(self.text) + 1
        h _ fm.height()
        xShadow _ 3.0
        yShadow _ 3.0

        image _ QImage(int((w + xShadow) * sx), int((h + yShadow) * sy),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(QColor(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setFont(Colors.headingFont())
        painter.scale(sx, sy)

        # Draw shadow.
        brush_shadow _ QLinearGradient(xShadow, yShadow, w, yShadow)
        brush_shadow.setSpread(QLinearGradient.PadSpread)
        if Colors.useEightBitPalette:
            brush_shadow.setColorAt(0.0, QColor(0, 0, 0))
        else:
            brush_shadow.setColorAt(0.0, QColor(0, 0, 0, 100))
        pen_shadow _ QPen()
        pen_shadow.setBrush(brush_shadow)
        painter.setPen(pen_shadow)
        painter.drawText(int(xShadow), int(yShadow), int(w), int(h),
                Qt.AlignLeft, self.text)

        # Draw text.
        brush_text _ QLinearGradient(0, 0, w, w)
        brush_text.setSpread(QLinearGradient.PadSpread)
        brush_text.setColorAt(0.0, QColor(255, 255, 255))
        brush_text.setColorAt(0.2, QColor(255, 255, 255))
        brush_text.setColorAt(0.5, QColor(190, 190, 190))
        pen_text _ QPen()
        pen_text.setBrush(brush_text)
        painter.setPen(pen_text)
        painter.drawText(0, 0, int(w), int(h), Qt.AlignLeft, self.text)

        return image

    ___ animationStarted(self, id_0):
        self.noSubPixeling _ False

    ___ animationStopped(self, id_0):
        self.noSubPixeling _ True
