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


______ m__

____ ?.?C.. ______ QPointF

____ guide ______ Guide


PI2 _ 2 * m__.pi


c_ GuideCircle(Guide):
    CW _ 1
    CCW _ -1

    ___  -   rect, startAngle_0.0, span_360.0, dir_CCW, follows_None):
        s__(GuideCircle, self). - (follows)

        radiusX _ rect.width() / 2.0
        radiusY _ rect.height() / 2.0
        posX _ rect.topLeft().x()
        posY _ rect.topLeft().y()
        spanRad _ span * PI2 / -360.0

        __ dir __ GuideCircle.CCW:
            startAngleRad _ startAngle * PI2 / -360.0
            endAngleRad _ startAngleRad + spanRad
            stepAngleRad _ spanRad / length()
        ____
            startAngleRad _ spanRad + (startAngle * PI2 / -360.0)
            endAngleRad _ startAngle * PI2 / -360.0
            stepAngleRad _ -spanRad / length()

    ___ length
        r_ abs(radiusX * spanRad)

    ___ startPos
        r_ QPointF((posX + radiusX + radiusX * m__.cos(startAngleRad)) * scaleX,
                (posY + radiusY + radiusY * m__.sin(startAngleRad)) * scaleY)

    ___ endPos
        r_ QPointF((posX + radiusX + radiusX * m__.cos(endAngleRad)) * scaleX,
                (posY + radiusY + radiusY * m__.sin(endAngleRad)) * scaleY)

    ___ guide  item, moveSpeed):
        frame _ item.guideFrame - startLength
        end _ QPointF((posX + radiusX + radiusX * m__.cos(startAngleRad + (frame * stepAngleRad))) * scaleX,
                (posY + radiusY + radiusY * m__.sin(startAngleRad + (frame * stepAngleRad))) * scaleY)
        move(item, end, moveSpeed)
