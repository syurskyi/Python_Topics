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


____ ?.QtCore ______ QPropertyAnimation, QTimer

____ colors ______ Colors


c_ DemoItemAnimation(QPropertyAnimation):
    ANIM_IN, ANIM_OUT, ANIM_UNSPECIFIED _ range(3)

    ___ __init__  item, inOrOut_ANIM_UNSPECIFIED):
        super(DemoItemAnimation, self).__init__(item, b'pos')

        self._startDelay _ 0
        self._inOrOut _ inOrOut
        self._hideOnFinished _ False

    ___ prepare(self):
        self.targetObject().prepare()

    ___ setHideOnFinished  hide):
        self._hideOnFinshed _ hide

    ___ setStartDelay  delay):
        self._startDelay _ delay

    ___ setDuration  duration):
        duration _ int(duration * Colors.animSpeed)
        super(DemoItemAnimation, self).setDuration(duration)

    ___ notOwnerOfItem(self):
        r_ self __ no. self.targetObject().currentAnimation

    ___ play  fromStart_True, force_False):
        item _ self.targetObject()

        # If the item that this animation controls in currently under the
        # control of another animation, stop that animation first.
        __ item.currentAnimation __ no. N..:
            item.currentAnimation.stop()

        item.currentAnimation _ self

        __ Colors.noAnimations and no. force:
            # If animations are disabled just move to the end position.
            item.setPos(self.endValue())
        ____
            __ self.isVisible
                # If the item is already visible, start the animation from the
                # item's current position rather than from the start.
                self.setStartValue(item.pos())

            __ fromStart:
                self.setCurrentTime(0)
                item.setPos(self.startValue())

        __ self._inOrOut == DemoItemAnimation.ANIM_IN:
            item.setRecursiveVisible(True)

        __ no. Colors.noAnimations or force:
            __ self._startDelay:
                QTimer.singleShot(self._startDelay, self.start)
            ____
                self.start()

    ___ setCurveShape  shape):
        self.setEasingCurve(shape)

    ___ setEnabled  enabled):
        self.targetObject().setEnabled(enabled)

    ___ isVisible(self):
        r_ self.targetObject().isVisible()

    ___ updateState  new, old):
        item _ self.targetObject()

        __ new == QPropertyAnimation.Running:
            item.animationStarted(self._inOrOut)
        ____ new == QPropertyAnimation.Stopped:
            __ self._hideOnFinished:
                item.setRecursiveVisible F..

            item.animationStopped(self._inOrOut)
