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


____ ?.QtCore ______ QRectF
____ ?.?G.. ______ QColor, QImage, QPainter
____ ?.?W.. ______ QGraphicsTextItem, QStyleOptionGraphicsItem

____ demoitem ______ DemoItem


c_ DemoTextItem(DemoItem):
    STATIC_TEXT, DYNAMIC_TEXT _ range(2)

    ___ __init__  text, font, textColor, textWidth, parent_None, type_STATIC_TEXT, bgColor_QColor()):
        super(DemoTextItem, self).__init__(parent)

        self.type _ type
        self.text _ text
        self.font _ font
        self.textColor _ textColor
        self.bgColor _ bgColor
        self.textWidth _ textWidth
        self.noSubPixeling _ True

    ___ sT..  text):
        self.text _ text
        self.update()

    ___ createImage  transform):
        __ self.type == DemoTextItem.DYNAMIC_TEXT:
            r_ N..

        sx _ min(transform.m11(), transform.m22())
        sy _ max(transform.m22(), sx)

        textItem _ QGraphicsTextItem()
        textItem.setHtml(self.text)
        textItem.setTextWidth(self.textWidth)
        textItem.setFont(self.font)
        textItem.setDefaultTextColor(self.textColor)
        textItem.document().setDocumentMargin(2)

        w _ textItem.boundingRect().width()
        h _ textItem.boundingRect().height()
        image _ QImage(int(w * sx), int(h * sy),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(QColor(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.scale(sx, sy)
        style _ QStyleOptionGraphicsItem()
        textItem.paint(painter, style, N..)

        r_ image

    ___ animationStarted  id_0):
        self.noSubPixeling _ False

    ___ animationStopped  id_0):
        self.noSubPixeling _ True

    ___ boundingRect(self):
        __ self.type == DemoTextItem.STATIC_TEXT:
            r_ super(DemoTextItem, self).boundingRect()

        # Sorry for using magic number.
        r_ QRectF(0, 0, 50, 20)

    ___ paint  painter, option, widget):
        __ self.type == DemoTextItem.STATIC_TEXT:
            super(DemoTextItem, self).paint(painter, option, widget)
            r_

        painter.setPen(self.textColor)
        painter.drawText(0, 0, self.text)
