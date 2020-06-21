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


____ ?.?C.. ______ QPointF, QRect, QRectF, ?S.., __
____ ?.?G.. ______ (?C.., QImage, QLinearGradient, QPainter,
        QPainterPath, ?P..)

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ demotextitem ______ DemoTextItem
____ scanitem ______ ScanItem


c_ ButtonBackground(DemoItem):
    ___  -   type, highlighted, pressed, logicalSize, parent):
        s__(ButtonBackground, self). - (parent)

        type _ type
        highlighted _ highlighted
        pressed _ pressed
        logicalSize _ logicalSize
        useSharedImage('%s%d%d%d' % (__file__, type, highlighted, pressed))

    ___ createImage  transform):
        __ type __ (TextButton.SIDEBAR, TextButton.PANEL):
            r_ createRoundButtonBackground(transform)
        ____
            r_ createArrowBackground(transform)

    ___ createRoundButtonBackground  transform):
        scaledRect _ transform.mapRect(QRect(0, 0,
                logicalSize.width(), logicalSize.height()))

        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.sP..(__.NoPen)

        __ Colors.useEightBitPalette:
            painter.sP..(?C..(120, 120, 120))
            __ pressed:
                painter.sB..(?C..(60, 60, 60))
            ____ highlighted:
                painter.sB..(?C..(100, 100, 100))
            ____
                painter.sB..(?C..(80, 80, 80))
        ____
            outlinebrush _ QLinearGradient(0, 0, 0, scaledRect.height())
            brush _ QLinearGradient(0, 0, 0, scaledRect.height())

            brush.setSpread(QLinearGradient.PadSpread)
            highlight _ ?C..(255, 255, 255, 70)
            shadow _ ?C..(0, 0, 0, 70)
            sunken _ ?C..(220, 220, 220, 30)

            __ type __ TextButton.PANEL:
                normal1 _ ?C..(200, 170, 160, 50)
                normal2 _ ?C..(50, 10, 0, 50)
            ____
                normal1 _ ?C..(255, 255, 245, 60)
                normal2 _ ?C..(255, 255, 235, 10)

            __ pressed:
                outlinebrush.setColorAt(0, shadow)
                outlinebrush.setColorAt(1, highlight)
                brush.setColorAt(0, sunken)
                painter.sP..(__.NoPen)
            ____
                outlinebrush.setColorAt(1, shadow)
                outlinebrush.setColorAt(0, highlight)
                brush.setColorAt(0, normal1)
                __ no. highlighted:
                    brush.setColorAt(1, normal2)
                painter.sP..(?P..(outlinebrush, 1))

            painter.sB..(brush)

        __ type __ TextButton.PANEL:
            painter.drawRect(0, 0, scaledRect.width(), scaledRect.height())
        ____
            painter.dRR..(0, 0, scaledRect.width(),
                    scaledRect.height(), 10, 90, __.RelativeSize)

        r_ image

    ___ createArrowBackground  transform):
        scaledRect _ transform.mapRect(QRect(0, 0,
                logicalSize.width(), logicalSize.height()))

        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(?C..(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.sP..(__.NoPen)

        __ Colors.useEightBitPalette:
            painter.sP..(?C..(120, 120, 120))
            __ pressed:
                painter.sB..(?C..(60, 60, 60))
            ____ highlighted:
                painter.sB..(?C..(100, 100, 100))
            ____
                painter.sB..(?C..(80, 80, 80))
        ____
            outlinebrush _ QLinearGradient(0, 0, 0, scaledRect.height())
            brush _ QLinearGradient(0, 0, 0, scaledRect.height())

            brush.setSpread(QLinearGradient.PadSpread)
            highlight _ ?C..(255, 255, 255, 70)
            shadow _ ?C..(0, 0, 0, 70)
            sunken _ ?C..(220, 220, 220, 30)
            normal1 _ ?C..(200, 170, 160, 50)
            normal2 _ ?C..(50, 10, 0, 50)

            __ pressed:
                outlinebrush.setColorAt(0, shadow)
                outlinebrush.setColorAt(1, highlight)
                brush.setColorAt(0, sunken)
                painter.sP..(__.NoPen)
            ____
                outlinebrush.setColorAt(1, shadow)
                outlinebrush.setColorAt(0, highlight)
                brush.setColorAt(0, normal1)
                __ no. highlighted:
                    brush.setColorAt(1, normal2)
                painter.sP..(?P..(outlinebrush, 1))

            painter.sB..(brush);

        painter.drawRect(0, 0, scaledRect.width(), scaledRect.height())

        xOff _ scaledRect.width() / 2
        yOff _ scaledRect.height() / 2
        sizex _ 3.0 * transform.m11()
        sizey _ 1.5 * transform.m22()
        __ type __ TextButton.UP:
            sizey *_ -1
        pa__ _ QPainterPath()
        pa__.moveTo(xOff, yOff + (5 * sizey))
        pa__.lineTo(xOff - (4 * sizex), yOff - (3 * sizey))
        pa__.lineTo(xOff + (4 * sizex), yOff - (3 * sizey))
        pa__.lineTo(xOff, yOff + (5 * sizey))
        painter.drawPath(pa__)

        r_ image


c_ TextButton(DemoItem):
    BUTTON_WIDTH _ 180
    BUTTON_HEIGHT _ 19

    LEFT, RIGHT _ ra..(2)

    SIDEBAR, PANEL, UP, DOWN _ ra..(4)

    ON, OFF, HIGHLIGHT, DISABLED _ ra..(4)

    ___  -   t__, align_LEFT, userCode_0, parent_None, type_SIDEBAR):
        s__(TextButton, self). - (parent)

        # Prevent a circular import.
        ____ menumanager ______ MenuManager
        _menu_manager _ MenuManager.i.. 

        menuString _ t__
        buttonLabel _ t__
        alignment _ align
        buttonType _ type
        userCode _ userCode
        scanAnim _ N..
        bgOn _ N..
        bgOff _ N..
        bgHighlight _ N..
        bgDisabled _ N..
        state _ TextButton.OFF

        setAcceptHoverEvents( st.
        setCursor(__.PointingHandCursor)

        # Calculate the button size.
        __ type __ (TextButton.SIDEBAR, TextButton.PANEL):
            logicalSize _ ?S..(TextButton.BUTTON_WIDTH, TextButton.BUTTON_HEIGHT)
        ____
            logicalSize _ ?S..(in.((TextButton.BUTTON_WIDTH / 2.0) - 5), in.(TextButton.BUTTON_HEIGHT * 1.5))

        _prepared _ F..

    ___ setMenuString  menu):
        menuString _ menu

    ___ prepare 
        __ no. _prepared:
            setupHoverText()
            setupScanItem()
            setupButtonBg()
            _prepared _ T..

    ___ boundingRect 
        r_ QRectF(0, 0, logicalSize.width(),
                logicalSize.height())

    ___ setupHoverText 
        __ no. buttonLabel:
            r_

        textItem _ DemoTextItem(buttonLabel, Colors.buttonFont(),
                Colors.buttonText, -1, self)
        textItem.setZValue(zValue() + 2)
        textItem.setPos(16, 0)

    ___ setupScanItem 
        __ Colors.useButtonBalls:
            scanItem _ ScanItem
            scanItem.setZValue(zValue() + 1)

            scanAnim _ DemoItemAnimation(scanItem)

            x _ 1.0
            y _ 1.5
            stop _ TextButton.BUTTON_WIDTH - scanItem.boundingRect().width() - x
            __ alignment __ TextButton.LEFT:
                scanAnim.sD..(2500)
                scanAnim.sKVA..(0.0, QPointF(x, y))
                scanAnim.sKVA..(0.5, QPointF(x, y))
                scanAnim.sKVA..(0.7, QPointF(stop, y))
                scanAnim.sKVA..(1.0, QPointF(x, y))
                scanItem.setPos(QPointF(x, y))
            ____
                scanAnim.sKVA..(0.0, QPointF(stop, y))
                scanAnim.sKVA..(0.5, QPointF(x, y))
                scanAnim.sKVA..(1.0, QPointF(stop, y))
                scanItem.setPos(QPointF(stop, y))

    ___ setState  state):
        state _ state
        bgOn.setRecursiveVisible(state __ TextButton.ON)
        bgOff.setRecursiveVisible(state __ TextButton.OFF)
        bgHighlight.setRecursiveVisible(state __ TextButton.HIGHLIGHT)
        bgDisabled.setRecursiveVisible(state __ TextButton.DISABLED)
        __ state __ TextButton.DISABLED:
            setCursor(__.ArrowCursor)
        ____
            setCursor(__.PointingHandCursor)

    ___ setupButtonBg 
        bgOn _ ButtonBackground(buttonType, T.., T..,
                logicalSize, self)
        bgOff _ ButtonBackground(buttonType, F.., F..,
                logicalSize, self)
        bgHighlight _ ButtonBackground(buttonType, T.., F..,
                logicalSize, self)
        bgDisabled _ ButtonBackground(buttonType, T.., T..,
                logicalSize, self)
        setState(TextButton.OFF)

    ___ hoverEnterEvent  event):
        __ no. isEnabled() or state __ TextButton.DISABLED:
            r_

        __ state __ TextButton.OFF:
            setState(TextButton.HIGHLIGHT)

            __ Colors.noAnimations and Colors.useButtonBalls:
                # Wait a bit in the beginning to enhance the effect.  We have
                # to do this here so that the adaption can be dynamic.
                scanAnim.sD..(1000)
                scanAnim.sKVA..(0.2, scanAnim.posAt(0))

            __ (_menu_manager.window.fpsMedian > 10 or Colors.noAdapt or
                    Colors.noTimerUpdate):
                __ Colors.useButtonBalls:
                    scanAnim.play(T..,  st.

    ___ hoverLeaveEvent  event):
        __ state __ TextButton.DISABLED:
            r_

        setState(TextButton.OFF)

        __ Colors.noAnimations and Colors.useButtonBalls:
            scanAnim.s..

    ___ mousePressEvent  event):
        __ state __ TextButton.DISABLED:
            r_

        __ state __ TextButton.HIGHLIGHT or state __ TextButton.OFF:
            setState(TextButton.ON)

    ___ mouseReleaseEvent  event):
        __ state __ TextButton.ON:
            setState(TextButton.OFF)
            __ isEnabled() and boundingRect().contains(event.pos()):
                _menu_manager.itemSelected(userCode, menuString)

    ___ animationStarted  _):
        __ state __ TextButton.DISABLED:
            r_

        setState(TextButton.OFF)
