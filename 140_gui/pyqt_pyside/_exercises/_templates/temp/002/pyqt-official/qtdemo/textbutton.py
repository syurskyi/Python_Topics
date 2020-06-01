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


____ ?.QtCore ______ QPointF, QRect, QRectF, QSize, Qt
____ ?.QtGui ______ (QColor, QImage, QLinearGradient, QPainter,
        QPainterPath, QPen)

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ demotextitem ______ DemoTextItem
____ scanitem ______ ScanItem


class ButtonBackground(DemoItem):
    ___ __init__(self, type, highlighted, pressed, logicalSize, parent):
        super(ButtonBackground, self).__init__(parent)

        self.type _ type
        self.highlighted _ highlighted
        self.pressed _ pressed
        self.logicalSize _ logicalSize
        self.useSharedImage('%s%d%d%d' % (__file__, type, highlighted, pressed))

    ___ createImage(self, transform):
        if self.type in (TextButton.SIDEBAR, TextButton.PANEL):
            return self.createRoundButtonBackground(transform)
        else:
            return self.createArrowBackground(transform)

    ___ createRoundButtonBackground(self, transform):
        scaledRect _ transform.mapRect(QRect(0, 0,
                self.logicalSize.width(), self.logicalSize.height()))

        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(QColor(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        if Colors.useEightBitPalette:
            painter.setPen(QColor(120, 120, 120))
            if self.pressed:
                painter.setBrush(QColor(60, 60, 60))
            elif self.highlighted:
                painter.setBrush(QColor(100, 100, 100))
            else:
                painter.setBrush(QColor(80, 80, 80))
        else:
            outlinebrush _ QLinearGradient(0, 0, 0, scaledRect.height())
            brush _ QLinearGradient(0, 0, 0, scaledRect.height())

            brush.setSpread(QLinearGradient.PadSpread)
            highlight _ QColor(255, 255, 255, 70)
            shadow _ QColor(0, 0, 0, 70)
            sunken _ QColor(220, 220, 220, 30)

            if self.type == TextButton.PANEL:
                normal1 _ QColor(200, 170, 160, 50)
                normal2 _ QColor(50, 10, 0, 50)
            else:
                normal1 _ QColor(255, 255, 245, 60)
                normal2 _ QColor(255, 255, 235, 10)

            if self.pressed:
                outlinebrush.setColorAt(0, shadow)
                outlinebrush.setColorAt(1, highlight)
                brush.setColorAt(0, sunken)
                painter.setPen(Qt.NoPen)
            else:
                outlinebrush.setColorAt(1, shadow)
                outlinebrush.setColorAt(0, highlight)
                brush.setColorAt(0, normal1)
                if not self.highlighted:
                    brush.setColorAt(1, normal2)
                painter.setPen(QPen(outlinebrush, 1))

            painter.setBrush(brush)

        if self.type == TextButton.PANEL:
            painter.drawRect(0, 0, scaledRect.width(), scaledRect.height())
        else:
            painter.drawRoundedRect(0, 0, scaledRect.width(),
                    scaledRect.height(), 10, 90, Qt.RelativeSize)

        return image

    ___ createArrowBackground(self, transform):
        scaledRect _ transform.mapRect(QRect(0, 0,
                self.logicalSize.width(), self.logicalSize.height()))

        image _ QImage(scaledRect.width(), scaledRect.height(),
                QImage.Format_ARGB32_Premultiplied)
        image.fill(QColor(0, 0, 0, 0).rgba())
        painter _ QPainter(image)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        if Colors.useEightBitPalette:
            painter.setPen(QColor(120, 120, 120))
            if self.pressed:
                painter.setBrush(QColor(60, 60, 60))
            elif self.highlighted:
                painter.setBrush(QColor(100, 100, 100))
            else:
                painter.setBrush(QColor(80, 80, 80))
        else:
            outlinebrush _ QLinearGradient(0, 0, 0, scaledRect.height())
            brush _ QLinearGradient(0, 0, 0, scaledRect.height())

            brush.setSpread(QLinearGradient.PadSpread)
            highlight _ QColor(255, 255, 255, 70)
            shadow _ QColor(0, 0, 0, 70)
            sunken _ QColor(220, 220, 220, 30)
            normal1 _ QColor(200, 170, 160, 50)
            normal2 _ QColor(50, 10, 0, 50)

            if self.pressed:
                outlinebrush.setColorAt(0, shadow)
                outlinebrush.setColorAt(1, highlight)
                brush.setColorAt(0, sunken)
                painter.setPen(Qt.NoPen)
            else:
                outlinebrush.setColorAt(1, shadow)
                outlinebrush.setColorAt(0, highlight)
                brush.setColorAt(0, normal1)
                if not self.highlighted:
                    brush.setColorAt(1, normal2)
                painter.setPen(QPen(outlinebrush, 1))

            painter.setBrush(brush);

        painter.drawRect(0, 0, scaledRect.width(), scaledRect.height())

        xOff _ scaledRect.width() / 2
        yOff _ scaledRect.height() / 2
        sizex _ 3.0 * transform.m11()
        sizey _ 1.5 * transform.m22()
        if self.type == TextButton.UP:
            sizey *_ -1
        path _ QPainterPath()
        path.moveTo(xOff, yOff + (5 * sizey))
        path.lineTo(xOff - (4 * sizex), yOff - (3 * sizey))
        path.lineTo(xOff + (4 * sizex), yOff - (3 * sizey))
        path.lineTo(xOff, yOff + (5 * sizey))
        painter.drawPath(path)

        return image


class TextButton(DemoItem):
    BUTTON_WIDTH _ 180
    BUTTON_HEIGHT _ 19

    LEFT, RIGHT _ range(2)

    SIDEBAR, PANEL, UP, DOWN _ range(4)

    ON, OFF, HIGHLIGHT, DISABLED _ range(4)

    ___ __init__(self, text, align_LEFT, userCode_0, parent_None, type_SIDEBAR):
        super(TextButton, self).__init__(parent)

        # Prevent a circular import.
        ____ menumanager ______ MenuManager
        self._menu_manager _ MenuManager.instance()

        self.menuString _ text
        self.buttonLabel _ text
        self.alignment _ align
        self.buttonType _ type
        self.userCode _ userCode
        self.scanAnim _ None
        self.bgOn _ None
        self.bgOff _ None
        self.bgHighlight _ None
        self.bgDisabled _ None
        self.state _ TextButton.OFF

        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.PointingHandCursor)

        # Calculate the button size.
        if type in (TextButton.SIDEBAR, TextButton.PANEL):
            self.logicalSize _ QSize(TextButton.BUTTON_WIDTH, TextButton.BUTTON_HEIGHT)
        else:
            self.logicalSize _ QSize(int((TextButton.BUTTON_WIDTH / 2.0) - 5), int(TextButton.BUTTON_HEIGHT * 1.5))

        self._prepared _ False

    ___ setMenuString(self, menu):
        self.menuString _ menu

    ___ prepare(self):
        if not self._prepared:
            self.setupHoverText()
            self.setupScanItem()
            self.setupButtonBg()
            self._prepared _ True

    ___ boundingRect(self):
        return QRectF(0, 0, self.logicalSize.width(),
                self.logicalSize.height())

    ___ setupHoverText(self):
        if not self.buttonLabel:
            return

        textItem _ DemoTextItem(self.buttonLabel, Colors.buttonFont(),
                Colors.buttonText, -1, self)
        textItem.setZValue(self.zValue() + 2)
        textItem.setPos(16, 0)

    ___ setupScanItem(self):
        if Colors.useButtonBalls:
            scanItem _ ScanItem(self)
            scanItem.setZValue(self.zValue() + 1)

            self.scanAnim _ DemoItemAnimation(scanItem)

            x _ 1.0
            y _ 1.5
            stop _ TextButton.BUTTON_WIDTH - scanItem.boundingRect().width() - x
            if self.alignment == TextButton.LEFT:
                self.scanAnim.setDuration(2500)
                self.scanAnim.setKeyValueAt(0.0, QPointF(x, y))
                self.scanAnim.setKeyValueAt(0.5, QPointF(x, y))
                self.scanAnim.setKeyValueAt(0.7, QPointF(stop, y))
                self.scanAnim.setKeyValueAt(1.0, QPointF(x, y))
                scanItem.setPos(QPointF(x, y))
            else:
                self.scanAnim.setKeyValueAt(0.0, QPointF(stop, y))
                self.scanAnim.setKeyValueAt(0.5, QPointF(x, y))
                self.scanAnim.setKeyValueAt(1.0, QPointF(stop, y))
                scanItem.setPos(QPointF(stop, y))

    ___ setState(self, state):
        self.state _ state
        self.bgOn.setRecursiveVisible(state == TextButton.ON)
        self.bgOff.setRecursiveVisible(state == TextButton.OFF)
        self.bgHighlight.setRecursiveVisible(state == TextButton.HIGHLIGHT)
        self.bgDisabled.setRecursiveVisible(state == TextButton.DISABLED)
        if state == TextButton.DISABLED:
            self.setCursor(Qt.ArrowCursor)
        else:
            self.setCursor(Qt.PointingHandCursor)

    ___ setupButtonBg(self):
        self.bgOn _ ButtonBackground(self.buttonType, True, True,
                self.logicalSize, self)
        self.bgOff _ ButtonBackground(self.buttonType, False, False,
                self.logicalSize, self)
        self.bgHighlight _ ButtonBackground(self.buttonType, True, False,
                self.logicalSize, self)
        self.bgDisabled _ ButtonBackground(self.buttonType, True, True,
                self.logicalSize, self)
        self.setState(TextButton.OFF)

    ___ hoverEnterEvent(self, event):
        if not self.isEnabled() or self.state == TextButton.DISABLED:
            return

        if self.state == TextButton.OFF:
            self.setState(TextButton.HIGHLIGHT)

            if Colors.noAnimations and Colors.useButtonBalls:
                # Wait a bit in the beginning to enhance the effect.  We have
                # to do this here so that the adaption can be dynamic.
                self.scanAnim.setDuration(1000)
                self.scanAnim.setKeyValueAt(0.2, self.scanAnim.posAt(0))

            if (self._menu_manager.window.fpsMedian > 10 or Colors.noAdapt or
                    Colors.noTimerUpdate):
                if Colors.useButtonBalls:
                    self.scanAnim.play(True, True)

    ___ hoverLeaveEvent(self, event):
        if self.state == TextButton.DISABLED:
            return

        self.setState(TextButton.OFF)

        if Colors.noAnimations and Colors.useButtonBalls:
            self.scanAnim.stop()

    ___ mousePressEvent(self, event):
        if self.state == TextButton.DISABLED:
            return

        if self.state == TextButton.HIGHLIGHT or self.state == TextButton.OFF:
            self.setState(TextButton.ON)

    ___ mouseReleaseEvent(self, event):
        if self.state == TextButton.ON:
            self.setState(TextButton.OFF)
            if self.isEnabled() and self.boundingRect().contains(event.pos()):
                self._menu_manager.itemSelected(self.userCode, self.menuString)

    ___ animationStarted(self, _):
        if self.state == TextButton.DISABLED:
            return

        self.setState(TextButton.OFF)
