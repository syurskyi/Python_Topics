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


____ ?.?C.. ______ QRect
____ ?.?G.. ______ ?C.., QImage, QPainter, ?P..

____ colors ______ Colors
____ demoitem ______ DemoItem


c_ ScanItem(DemoItem):
    ITEM_WIDTH _ 16
    ITEM_HEIGHT _ 16

    ___  -   parent_None):
        s__(ScanItem, self). - (parent)

        useSharedImage(__file__)

    ___ createImage  transform):
        scaledRect _ transform.mapRect(QRect(0, 0, ScanItem.ITEM_WIDTH, ScanItem.ITEM_HEIGHT))
        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)

        __ Colors.useEightBitPalette:
            painter.sP..(?P..(?C..(100, 100, 100), 2))
            painter.sB..(?C..(206, 246, 117))
            painter.drawEllipse(1, 1, scaledRect.width() - 2,
                    scaledRect.height() - 2)
        ____
            painter.sP..(?P..(?C..(0, 0, 0, 15), 1))
            painter.sB..(?C..(0, 0, 0, 15))
            painter.drawEllipse(1, 1, scaledRect.width() - 2,
                    scaledRect.height() - 2)

        r_ image
