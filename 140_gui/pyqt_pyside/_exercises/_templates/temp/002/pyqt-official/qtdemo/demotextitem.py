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


____ ?.?C.. ______ QRectF
____ ?.?G.. ______ ?C.., QImage, QPainter
____ ?.?W.. ______ QGraphicsTextItem, QStyleOptionGraphicsItem

____ demoitem ______ DemoItem


c_ DemoTextItem(DemoItem):
    STATIC_TEXT, DYNAMIC_TEXT _ ra..(2)

    ___  -   t__, font, textColor, textWidth, parent_None, type_STATIC_TEXT, bgColor_QColor()):
        s__(DemoTextItem, self). - (parent)

        type _ type
        t__ _ t__
        font _ font
        textColor _ textColor
        bgColor _ bgColor
        textWidth _ textWidth
        noSubPixeling _ T..

    ___ sT..  t__):
        t__ _ t__
        update()

    ___ createImage  transform):
        __ type __ DemoTextItem.DYNAMIC_TEXT:
            r_ N..

        sx _ min(transform.m11(), transform.m22())
        sy _ max(transform.m22(), sx)

        textItem _ QGraphicsTextItem()
        textItem.setHtml(t__)
        textItem.setTextWidth(textWidth)
        textItem.sF..(font)
        textItem.setDefaultTextColor(textColor)
        textItem.document().setDocumentMargin(2)

        w _ textItem.boundingRect().width()
        h _ textItem.boundingRect().height()
        image _ QImage(in.(w * sx), in.(h * sy),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.scale(sx, sy)
        style _ QStyleOptionGraphicsItem()
        textItem.paint(painter, style, N..)

        r_ image

    ___ animationStarted  id_0):
        noSubPixeling _ F..

    ___ animationStopped  id_0):
        noSubPixeling _ T..

    ___ boundingRect
        __ type __ DemoTextItem.STATIC_TEXT:
            r_ s__(DemoTextItem, self).boundingRect()

        # Sorry for using magic number.
        r_ QRectF(0, 0, 50, 20)

    ___ paint  painter, option, widget):
        __ type __ DemoTextItem.STATIC_TEXT:
            s__(DemoTextItem, self).paint(painter, option, widget)
            r_

        painter.sP..(textColor)
        painter.drawText(0, 0, t__)
