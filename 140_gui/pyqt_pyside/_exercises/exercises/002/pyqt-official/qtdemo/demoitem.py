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


____ ?.?C.. ______ QPointF, QRectF, qRound
____ ?.?G.. ______ ?C.., QPainter, ?P.., QTransform
____ ?.?W.. ______ QGraphicsObject

____ colors ______ Colors


c_ SharedImage o..
    ___  -
        refCount _ 0
        image _ N..
        pixmap _ N..
        transform _ QTransform()
        unscaledBoundingRect _ QRectF()


c_ DemoItem(QGraphicsObject):
    _sharedImageHash _   # dict

    _transform _ QTransform()

    ___  -   parent_None):
        s__(DemoItem, self). - (parent)

        noSubPixeling _ F..
        currentAnimation _ N..
        currGuide _ N..
        guideFrame _ 0.0

        _sharedImage _ SharedImage()
        _sharedImage.refCount +_ 1
        _hashKey _ ''

    ___ __del__
        _sharedImage.refCount -_ 1
        __ _sharedImage.refCount __ 0:
            __ _hashKey:
                del DemoItem._sharedImageHash[_hashKey]

    ___ animationStarted  id_0):
        p..

    ___ animationStopped  id_0):
        p..

    ___ setRecursiveVisible  visible):
        setVisible(visible)
        ___ c __ childItems
            c.setVisible(visible)

    ___ useGuide  guide, startFrame):
        guideFrame _ startFrame
        w__ guideFrame > guide.startLength + guide.length
            __ guide.nextGuide __ guide.firstGuide:
                break

            guide _ guide.nextGuide

        currGuide _ guide

    ___ guideAdvance  distance):
        guideFrame +_ distance
        w__ guideFrame > currGuide.startLength + currGuide.length
            currGuide _ currGuide.nextGuide
            __ currGuide __ currGuide.firstGuide:
                guideFrame -_ currGuide.lengthAll()

    ___ guideMove  moveSpeed):
        currGuide.guide  moveSpeed)

    ___ setPosUsingSheepDog  dest, sceneFence):
        setPos(dest)
        __ sceneFence.isNull
            r_

        itemWidth _ boundingRect().width()
        itemHeight _ boundingRect().height()
        fenceRight _ sceneFence.x() + sceneFence.width()
        fenceBottom _ sceneFence.y() + sceneFence.height()

        __ scenePos().x() < sceneFence.x
            moveBy(mapFromScene(QPointF(sceneFence.x(), 0)).x(), 0)

        __ scenePos().x() > fenceRight - itemWidth:
            moveBy(mapFromScene(QPointF(fenceRight - itemWidth, 0)).x(), 0)

        __ scenePos().y() < sceneFence.y
            moveBy(0, mapFromScene(QPointF(0, sceneFence.y())).y())

        __ scenePos().y() > fenceBottom - itemHeight:
            moveBy(0, mapFromScene(QPointF(0, fenceBottom - itemHeight)).y())

    ___ setGuidedPos  pos):
        # Make sure we have a copy.
        guidedPos _ QPointF(pos)

    ___ getGuidedPos
        # Return a copy so that it can be changed.
        r_ QPointF(guidedPos)

    @staticmethod
    ___ setTransform(transform):
        DemoItem._transform _ transform

    ___ useSharedImage  hashKey):
        _hashKey _ hashKey
        __ hashKey no. __ DemoItem._sharedImageHash:
            DemoItem._sharedImageHash[hashKey] _ _sharedImage
        ____
            _sharedImage.refCount -_ 1
            _sharedImage _ DemoItem._sharedImageHash[hashKey]
            _sharedImage.refCount +_ 1

    ___ createImage  transform):
        r_ N..

    ___ _validateImage
        __ (_sharedImage.transform !_ DemoItem._transform and no. Colors.noRescale) or (_sharedImage.image __ N.. and _sharedImage.pixmap __ N..):
            # (Re)create image according to new transform.
            _sharedImage.image _ N..
            _sharedImage.pixmap _ N..
            _sharedImage.transform _ DemoItem._transform

            # Let subclass create and draw a new image according to the new
            # transform.
            __ Colors.noRescale:
                transform _ QTransform()
            ____
                transform _ DemoItem._transform
            image _ createImage(transform)
            __ image __ no. N..:
                __ Colors.showBoundingRect:
                    # Draw red transparent rect.
                    painter _ QPainter(image)
                    painter.fillRect(image.rect(), ?C..(255, 0, 0, 50))
                    painter.end()

                _sharedImage.unscaledBoundingRect _ _sharedImage.transform.inverted()[0].mapRect(QRectF(image.rect()))

                __ Colors.usePixmaps:
                    __ image.isNull
                        _sharedImage.pixmap _ ?P..(1, 1)
                    ____
                        _sharedImage.pixmap _ ?P..(image.size())

                    _sharedImage.pixmap.fill(?C..(0, 0, 0, 0))
                    painter _ QPainter(_sharedImage.pixmap)
                    painter.drawImage(0, 0, image)
                ____
                    _sharedImage.image _ image

                r_ T..
            ____
                r_ F..

        r_ T..

    ___ boundingRect
        _validateImage()
        r_ _sharedImage.unscaledBoundingRect

    ___ paint  painter, option_None, widget_None):
        __ _validateImage
            wasSmoothPixmapTransform _ painter.testRenderHint(QPainter.SmoothPixmapTransform)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            __ Colors.noRescale:
                # Let the painter scale the image for us.  This may degrade
                # both quality and performance.
                __ _sharedImage.image __ no. N..:
                    painter.drawImage(pos(), _sharedImage.image)
                ____
                    painter.drawPixmap(pos(), _sharedImage.pixmap)
            ____
                m _ painter.worldTransform()
                painter.setWorldTransform(QTransform())

                x _ m.dx()
                y _ m.dy()
                __ noSubPixeling:
                    x _ qRound(x)
                    y _ qRound(y)

                __ _sharedImage.image __ no. N..:
                    painter.drawImage(QPointF(x, y), _sharedImage.image)
                ____
                    painter.drawPixmap(QPointF(x, y), _sharedImage.pixmap)

            __ no. wasSmoothPixmapTransform:
                painter.setRenderHint(QPainter.SmoothPixmapTransform,
                        F..)

    ___ collidesWithItem  item, mode):
        r_ F..
