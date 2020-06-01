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


______ math

____ ?.QtCore ______ QPointF

____ guide ______ Guide


PI2 _ 2 * math.pi


class GuideCircle(Guide):
    CW _ 1
    CCW _ -1

    ___ __init__(self, rect, startAngle_0.0, span_360.0, dir_CCW, follows_None):
        super(GuideCircle, self).__init__(follows)

        self.radiusX _ rect.width() / 2.0
        self.radiusY _ rect.height() / 2.0
        self.posX _ rect.topLeft().x()
        self.posY _ rect.topLeft().y()
        self.spanRad _ span * PI2 / -360.0

        if dir == GuideCircle.CCW:
            self.startAngleRad _ startAngle * PI2 / -360.0
            self.endAngleRad _ self.startAngleRad + self.spanRad
            self.stepAngleRad _ self.spanRad / self.length()
        else:
            self.startAngleRad _ self.spanRad + (startAngle * PI2 / -360.0)
            self.endAngleRad _ startAngle * PI2 / -360.0
            self.stepAngleRad _ -self.spanRad / self.length()

    ___ length(self):
        return abs(self.radiusX * self.spanRad)

    ___ startPos(self):
        return QPointF((self.posX + self.radiusX + self.radiusX * math.cos(self.startAngleRad)) * self.scaleX,
                (self.posY + self.radiusY + self.radiusY * math.sin(self.startAngleRad)) * self.scaleY)

    ___ endPos(self):
        return QPointF((self.posX + self.radiusX + self.radiusX * math.cos(self.endAngleRad)) * self.scaleX,
                (self.posY + self.radiusY + self.radiusY * math.sin(self.endAngleRad)) * self.scaleY)

    ___ guide(self, item, moveSpeed):
        frame _ item.guideFrame - self.startLength
        end _ QPointF((self.posX + self.radiusX + self.radiusX * math.cos(self.startAngleRad + (frame * self.stepAngleRad))) * self.scaleX,
                (self.posY + self.radiusY + self.radiusY * math.sin(self.startAngleRad + (frame * self.stepAngleRad))) * self.scaleY)
        self.move(item, end, moveSpeed)
