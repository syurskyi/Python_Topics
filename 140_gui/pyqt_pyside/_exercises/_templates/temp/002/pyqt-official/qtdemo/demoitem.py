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


____ ?.QtCore ______ QPointF, QRectF, qRound
____ ?.QtGui ______ QColor, QPainter, QPixmap, QTransform
____ ?.?W.. ______ QGraphicsObject

____ colors ______ Colors


class SharedImage(object):
    ___ __init__(self):
        self.refCount _ 0
        self.image _ None
        self.pixmap _ None
        self.transform _ QTransform()
        self.unscaledBoundingRect _ QRectF()


class DemoItem(QGraphicsObject):
    _sharedImageHash _ {}

    _transform _ QTransform()

    ___ __init__(self, parent_None):
        super(DemoItem, self).__init__(parent)

        self.noSubPixeling _ False
        self.currentAnimation _ None
        self.currGuide _ None
        self.guideFrame _ 0.0

        self._sharedImage _ SharedImage()
        self._sharedImage.refCount +_ 1
        self._hashKey _ ''

    ___ __del__(self):
        self._sharedImage.refCount -_ 1
        if self._sharedImage.refCount == 0:
            if self._hashKey:
                del DemoItem._sharedImageHash[self._hashKey]

    ___ animationStarted(self, id_0):
        pass

    ___ animationStopped(self, id_0):
        pass

    ___ setRecursiveVisible(self, visible):
        self.setVisible(visible)
        for c in self.childItems
            c.setVisible(visible)

    ___ useGuide(self, guide, startFrame):
        self.guideFrame _ startFrame
        while self.guideFrame > guide.startLength + guide.length
            if guide.nextGuide == guide.firstGuide:
                break

            guide _ guide.nextGuide

        self.currGuide _ guide

    ___ guideAdvance(self, distance):
        self.guideFrame +_ distance
        while self.guideFrame > self.currGuide.startLength + self.currGuide.length
            self.currGuide _ self.currGuide.nextGuide
            if self.currGuide == self.currGuide.firstGuide:
                self.guideFrame -_ self.currGuide.lengthAll()

    ___ guideMove(self, moveSpeed):
        self.currGuide.guide(self, moveSpeed)

    ___ setPosUsingSheepDog(self, dest, sceneFence):
        self.setPos(dest)
        if sceneFence.isNull
            return

        itemWidth _ self.boundingRect().width()
        itemHeight _ self.boundingRect().height()
        fenceRight _ sceneFence.x() + sceneFence.width()
        fenceBottom _ sceneFence.y() + sceneFence.height()

        if self.scenePos().x() < sceneFence.x
            self.moveBy(self.mapFromScene(QPointF(sceneFence.x(), 0)).x(), 0)

        if self.scenePos().x() > fenceRight - itemWidth:
            self.moveBy(self.mapFromScene(QPointF(fenceRight - itemWidth, 0)).x(), 0)

        if self.scenePos().y() < sceneFence.y
            self.moveBy(0, self.mapFromScene(QPointF(0, sceneFence.y())).y())

        if self.scenePos().y() > fenceBottom - itemHeight:
            self.moveBy(0, self.mapFromScene(QPointF(0, fenceBottom - itemHeight)).y())

    ___ setGuidedPos(self, pos):
        # Make sure we have a copy.
        self.guidedPos _ QPointF(pos)

    ___ getGuidedPos(self):
        # Return a copy so that it can be changed.
        return QPointF(self.guidedPos)

    @staticmethod
    ___ setTransform(transform):
        DemoItem._transform _ transform

    ___ useSharedImage(self, hashKey):
        self._hashKey _ hashKey
        if hashKey not in DemoItem._sharedImageHash:
            DemoItem._sharedImageHash[hashKey] _ self._sharedImage
        else:
            self._sharedImage.refCount -_ 1
            self._sharedImage _ DemoItem._sharedImageHash[hashKey]
            self._sharedImage.refCount +_ 1

    ___ createImage(self, transform):
        return None

    ___ _validateImage(self):
        if (self._sharedImage.transform !_ DemoItem._transform and not Colors.noRescale) or (self._sharedImage.image is None and self._sharedImage.pixmap is None):
            # (Re)create image according to new transform.
            self._sharedImage.image _ None
            self._sharedImage.pixmap _ None
            self._sharedImage.transform _ DemoItem._transform

            # Let subclass create and draw a new image according to the new
            # transform.
            if Colors.noRescale:
                transform _ QTransform()
            else:
                transform _ DemoItem._transform
            image _ self.createImage(transform)
            if image is not None:
                if Colors.showBoundingRect:
                    # Draw red transparent rect.
                    painter _ QPainter(image)
                    painter.fillRect(image.rect(), QColor(255, 0, 0, 50))
                    painter.end()

                self._sharedImage.unscaledBoundingRect _ self._sharedImage.transform.inverted()[0].mapRect(QRectF(image.rect()))

                if Colors.usePixmaps:
                    if image.isNull
                        self._sharedImage.pixmap _ QPixmap(1, 1)
                    else:
                        self._sharedImage.pixmap _ QPixmap(image.size())

                    self._sharedImage.pixmap.fill(QColor(0, 0, 0, 0))
                    painter _ QPainter(self._sharedImage.pixmap)
                    painter.drawImage(0, 0, image)
                else:
                    self._sharedImage.image _ image

                return True
            else:
                return False

        return True

    ___ boundingRect(self):
        self._validateImage()
        return self._sharedImage.unscaledBoundingRect

    ___ paint(self, painter, option_None, widget_None):
        if self._validateImage
            wasSmoothPixmapTransform _ painter.testRenderHint(QPainter.SmoothPixmapTransform)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            if Colors.noRescale:
                # Let the painter scale the image for us.  This may degrade
                # both quality and performance.
                if self._sharedImage.image is not None:
                    painter.drawImage(self.pos(), self._sharedImage.image)
                else:
                    painter.drawPixmap(self.pos(), self._sharedImage.pixmap)
            else:
                m _ painter.worldTransform()
                painter.setWorldTransform(QTransform())

                x _ m.dx()
                y _ m.dy()
                if self.noSubPixeling:
                    x _ qRound(x)
                    y _ qRound(y)

                if self._sharedImage.image is not None:
                    painter.drawImage(QPointF(x, y), self._sharedImage.image)
                else:
                    painter.drawPixmap(QPointF(x, y), self._sharedImage.pixmap)

            if not wasSmoothPixmapTransform:
                painter.setRenderHint(QPainter.SmoothPixmapTransform,
                        False)

    ___ collidesWithItem(self, item, mode):
        return False
