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


____ ?.?C.. ______ ?PA.., ?T..

____ colors ______ Colors


c_ DemoItemAnimation(?PA..):
    ANIM_IN, ANIM_OUT, ANIM_UNSPECIFIED _ ra..(3)

    ___  -   item, inOrOut_ANIM_UNSPECIFIED):
        s__(DemoItemAnimation, self). - (item, b'pos')

        _startDelay _ 0
        _inOrOut _ inOrOut
        _hideOnFinished _ F..

    ___ prepare 
        targetObject().prepare()

    ___ setHideOnFinished  hide):
        _hideOnFinshed _ hide

    ___ setStartDelay  delay):
        _startDelay _ delay

    ___ sD..  duration):
        duration _ in.(duration * Colors.animSpeed)
        s__(DemoItemAnimation, self).sD..(duration)

    ___ notOwnerOfItem 
        r_ self __ no. targetObject().currentAnimation

    ___ play  fromStart_True, force_False):
        item _ targetObject()

        # If the item that this animation controls in currently under the
        # control of another animation, stop that animation first.
        __ item.currentAnimation __ no. N..:
            item.currentAnimation.s..

        item.currentAnimation _ self

        __ Colors.noAnimations and no. force:
            # If animations are disabled just move to the end position.
            item.setPos(endValue())
        ____
            __ isVisible
                # If the item is already visible, start the animation from the
                # item's current position rather than from the start.
                sSV..(item.pos())

            __ fromStart:
                setCurrentTime(0)
                item.setPos(startValue())

        __ _inOrOut __ DemoItemAnimation.ANIM_IN:
            item.setRecursiveVisible( st.

        __ no. Colors.noAnimations or force:
            __ _startDelay:
                ?T...sS..(_startDelay, start)
            ____
                start()

    ___ setCurveShape  shape):
        setEasingCurve(shape)

    ___ sE..  enabled):
        targetObject().sE..(enabled)

    ___ isVisible 
        r_ targetObject().isVisible()

    ___ updateState  new, old):
        item _ targetObject()

        __ new __ ?PA...Running:
            item.animationStarted(_inOrOut)
        ____ new __ ?PA...Stopped:
            __ _hideOnFinished:
                item.setRecursiveVisible F..

            item.animationStopped(_inOrOut)
