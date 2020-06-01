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


____ ?.QtCore ______ QLineF, QPointF


c_ Guide(object):
    ___ __init__  follows_None):
        self.scaleX _ 1.0
        self.scaleY _ 1.0

        __ follows __ no. N..:
            while follows.nextGuide __ no. follows.firstGuide:
                follows _ follows.nextGuide

            follows.nextGuide _ self
            self.prevGuide _ follows
            self.firstGuide _ follows.firstGuide
            self.nextGuide _ follows.firstGuide
            self.startLength _ int(follows.startLength + follows.length()) + 1
        ____
            self.prevGuide _ self
            self.firstGuide _ self
            self.nextGuide _ self
            self.startLength _ 0

    ___ setScale  scaleX, scaleY, all_True):
        self.scaleX _ scaleX
        self.scaleY _ scaleY

        __ all:
            next _ self.nextGuide
            while next __ no. self:
                next.scaleX _ scaleX
                next.scaleY _ scaleY
                next _ next.nextGuide

    ___ setFence  fence, all_True):
        self.fence _ fence

        __ all:
            next _ self.nextGuide
            while next __ no. self:
                next.fence _ fence
                next _ next.nextGuide

    ___ lengthAll(self):
        len _ self.length()
        next _ self.nextGuide
        while next __ no. self:
            len +_ next.length()
            next _ next.nextGuide

        r_ len

    ___ move  item, dest, moveSpeed):
        walkLine _ QLineF(item.getGuidedPos(), dest)
        __ moveSpeed >_ 0 and walkLine.length() > moveSpeed:
            # The item is too far away from it's destination point so we move
            # it towards it instead.
            dx _ walkLine.dx()
            dy _ walkLine.dy()

            __ abs(dx) > abs(dy):
                # Walk along x-axis.
                __ dx !_ 0:
                    d _ moveSpeed * dy / abs(dx)

                    __ dx > 0:
                        s _ moveSpeed
                    ____
                        s _ -moveSpeed

                    dest.setX(item.getGuidedPos().x() + s)
                    dest.setY(item.getGuidedPos().y() + d)
            ____
                # Walk along y-axis.
                __ dy !_ 0:
                    d _ moveSpeed * dx / abs(dy)

                    __ dy > 0:
                        s _ moveSpeed
                    ____
                        s _ -moveSpeed

                    dest.setX(item.getGuidedPos().x() + d)
                    dest.setY(item.getGuidedPos().y() + s)

        item.setGuidedPos(dest)

    ___ startPos(self):
        r_ QPointF(0, 0)

    ___ endPos(self):
        r_ QPointF(0, 0)

    ___ length(self):
        r_ 1.0

    ___ guide  item, moveSpeed):
        raise NotImplementedError
