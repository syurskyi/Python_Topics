#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ math

____ ?.?C.. ______ (pyqtProperty, QDirIterator, QEasingCurve, QEvent,
        QEventTransition, QHistoryState, QParallelAnimationGroup, QPointF,
        QPropertyAnimation, QRectF, QSequentialAnimationGroup, QSize, QState,
        QStateMachine, __)
____ ?.?G.. ______ (QBrush, ?C.., QFont, QLinearGradient, QPainter,
        ?P.., QPen, QPixmap, QTransform)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsProxyWidget, QGraphicsRotation, QGraphicsScene, QGraphicsView,
        QKeyEventTransition, QWidget)
____ ?.QtOpenGL ______ QGL, QGLFormat, QGLWidget

______ padnavigator_rc
____ ui_form ______ Ui_Form


c_ PadNavigator(QGraphicsView):
    ___  -   size, parent_None):
        super(PadNavigator, self). - (parent)

        form _ Ui_Form()

        splash _ SplashItem()
        splash.setZValue(1)

        pad _ FlippablePad(size)
        flipRotation _ QGraphicsRotation(pad)
        xRotation _ QGraphicsRotation(pad)
        yRotation _ QGraphicsRotation(pad)
        flipRotation.setAxis(__.YAxis)
        xRotation.setAxis(__.YAxis)
        yRotation.setAxis(__.XAxis)
        pad.setTransformations([flipRotation, xRotation, yRotation])

        backItem _ QGraphicsProxyWidget(pad)
        widget _ ?W..
        form.setupUi(widget)
        form.hostName.setFocus()
        backItem.setWidget(widget)
        backItem.setVisible F..
        backItem.setFocus()
        backItem.setCacheMode(QGraphicsItem.ItemCoordinateCache)
        r _ backItem.rect()
        backItem.setTransform(QTransform().rotate(180, __.YAxis).translate(-r.width()/2, -r.height()/2))

        selectionItem _ RoundRectItem(QRectF(-60, -60, 120, 120),
                ?C..(__.gray), pad)
        selectionItem.setZValue(0.5)

        smoothSplashMove _ QPropertyAnimation(splash, b'y')
        smoothSplashOpacity _ QPropertyAnimation(splash, b'opacity')
        smoothSplashMove.setEasingCurve(QEasingCurve.InQuad)
        smoothSplashMove.setDuration(250)
        smoothSplashOpacity.setDuration(250)

        smoothXSelection _ QPropertyAnimation(selectionItem, b'x')
        smoothYSelection _ QPropertyAnimation(selectionItem, b'y')
        smoothXRotation _ QPropertyAnimation(xRotation, b'angle')
        smoothYRotation _ QPropertyAnimation(yRotation, b'angle')
        smoothXSelection.setDuration(125)
        smoothYSelection.setDuration(125)
        smoothXRotation.setDuration(125)
        smoothYRotation.setDuration(125)
        smoothXSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYRotation.setEasingCurve(QEasingCurve.InOutQuad)

        smoothFlipRotation _ QPropertyAnimation(flipRotation, b'angle')
        smoothFlipScale _ QPropertyAnimation(pad, b'scale')
        smoothFlipXRotation _ QPropertyAnimation(xRotation, b'angle')
        smoothFlipYRotation _ QPropertyAnimation(yRotation, b'angle')
        flipAnimation _ QParallelAnimationGroup
        smoothFlipScale.setDuration(500)
        smoothFlipRotation.setDuration(500)
        smoothFlipXRotation.setDuration(500)
        smoothFlipYRotation.setDuration(500)
        smoothFlipScale.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipYRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipScale.setKeyValueAt(0, 1.0)
        smoothFlipScale.setKeyValueAt(0.5, 0.7)
        smoothFlipScale.setKeyValueAt(1, 1.0)
        flipAnimation.addAnimation(smoothFlipRotation)
        flipAnimation.addAnimation(smoothFlipScale)
        flipAnimation.addAnimation(smoothFlipXRotation)
        flipAnimation.addAnimation(smoothFlipYRotation)

        setVariablesSequence _ QSequentialAnimationGroup()
        setFillAnimation _ QPropertyAnimation(pad, b'fill')
        setBackItemVisibleAnimation _ QPropertyAnimation(backItem, b'visible')
        setSelectionItemVisibleAnimation _ QPropertyAnimation(selectionItem, b'visible')
        setFillAnimation.setDuration(0)
        setBackItemVisibleAnimation.setDuration(0)
        setSelectionItemVisibleAnimation.setDuration(0)
        setVariablesSequence.addPause(250)
        setVariablesSequence.addAnimation(setBackItemVisibleAnimation)
        setVariablesSequence.addAnimation(setSelectionItemVisibleAnimation)
        setVariablesSequence.addAnimation(setFillAnimation)
        flipAnimation.addAnimation(setVariablesSequence)

        stateMachine _ QStateMachine
        splashState _ QState(stateMachine)
        frontState _ QState(stateMachine)
        historyState _ QHistoryState(frontState)
        backState _ QState(stateMachine)

        frontState.assignProperty(pad, "fill", False)
        frontState.assignProperty(splash, "opacity", 0.0)
        frontState.assignProperty(backItem, "visible", False)
        frontState.assignProperty(flipRotation, "angle", 0.0)
        frontState.assignProperty(selectionItem, "visible", True)

        backState.assignProperty(pad, "fill", True)
        backState.assignProperty(backItem, "visible", True)
        backState.assignProperty(xRotation, "angle", 0.0)
        backState.assignProperty(yRotation, "angle", 0.0)
        backState.assignProperty(flipRotation, "angle", 180.0)
        backState.assignProperty(selectionItem, "visible", False)

        stateMachine.addDefaultAnimation(smoothXRotation)
        stateMachine.addDefaultAnimation(smoothYRotation)
        stateMachine.addDefaultAnimation(smoothXSelection)
        stateMachine.addDefaultAnimation(smoothYSelection)
        stateMachine.setInitialState(splashState)

        anyKeyTransition _ QEventTransition  QEvent.KeyPress, splashState)
        anyKeyTransition.setTargetState(frontState)
        anyKeyTransition.addAnimation(smoothSplashMove)
        anyKeyTransition.addAnimation(smoothSplashOpacity)

        enterTransition _ QKeyEventTransition  QEvent.KeyPress,
                __.Key_Enter, backState)
        returnTransition _ QKeyEventTransition  QEvent.KeyPress,
                __.Key_Return, backState)
        backEnterTransition _ QKeyEventTransition  QEvent.KeyPress,
                __.Key_Enter, frontState)
        backReturnTransition _ QKeyEventTransition  QEvent.KeyPress,
                __.Key_Return, frontState)
        enterTransition.setTargetState(historyState)
        returnTransition.setTargetState(historyState)
        backEnterTransition.setTargetState(backState)
        backReturnTransition.setTargetState(backState)
        enterTransition.addAnimation(flipAnimation)
        returnTransition.addAnimation(flipAnimation)
        backEnterTransition.addAnimation(flipAnimation)
        backReturnTransition.addAnimation(flipAnimation)

        columns _ size.width()
        rows _ size.height()
        stateGrid _   # list
        ___ y __ range(rows):
            stateGrid.ap..([QState(frontState) ___ _ __ range(columns)])

        frontState.setInitialState(stateGrid[0][0])
        selectionItem.setPos(pad.iconAt(0, 0).pos())

        ___ y __ range(rows):
            ___ x __ range(columns):
                state _ stateGrid[y][x]

                rightTransition _ QKeyEventTransition  QEvent.KeyPress,
                        __.Key_Right, state)
                leftTransition _ QKeyEventTransition  QEvent.KeyPress,
                        __.Key_Left, state)
                downTransition _ QKeyEventTransition  QEvent.KeyPress,
                        __.Key_Down, state)
                upTransition _ QKeyEventTransition  QEvent.KeyPress,
                        __.Key_Up, state)

                rightTransition.setTargetState(stateGrid[y][(x + 1) % columns])
                leftTransition.setTargetState(stateGrid[y][((x - 1) + columns) % columns])
                downTransition.setTargetState(stateGrid[(y + 1) % rows][x])
                upTransition.setTargetState(stateGrid[((y - 1) + rows) % rows][x])

                icon _ pad.iconAt(x, y)
                state.assignProperty(xRotation, "angle", -icon.x() / 6.0)
                state.assignProperty(yRotation, "angle", icon.y() / 6.0)
                state.assignProperty(selectionItem, "x", icon.x())
                state.assignProperty(selectionItem, "y", icon.y())
                frontState.assignProperty(icon, "visible", True)
                backState.assignProperty(icon, "visible", False)

                setIconVisibleAnimation _ QPropertyAnimation(icon, b'visible')
                setIconVisibleAnimation.setDuration(0)
                setVariablesSequence.addAnimation(setIconVisibleAnimation)

        scene _ QGraphicsScene
        scene.setBackgroundBrush(QBrush(QPixmap(":/images/blue_angle_swirl.jpg")))
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.addItem(pad)
        scene.setSceneRect(scene.itemsBoundingRect())
        setScene(scene)

        sbr _ splash.boundingRect()
        splash.setPos(-sbr.width() / 2, scene.sceneRect().top() - 2)
        frontState.assignProperty(splash, "y", splash.y() - 100.0)
        scene.addItem(splash)

        setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        setMinimumSize(50, 50)
        setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        setCacheMode(QGraphicsView.CacheBackground)
        setRenderHints(QPainter.Antialiasing |
                QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing)

        __ QGLFormat.hasOpenGL
            setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))

        stateMachine.start()

    ___ resizeEvent  event):
        super(PadNavigator, self).resizeEvent(event)
        fitInView(scene().sceneRect(), __.KeepAspectRatio)


c_ RoundRectItem(QGraphicsObject):
    ___  -   bounds, color, parent_None):
        super(RoundRectItem, self). - (parent)

        fillRect _ False
        bounds _ QRectF(bounds)
        pix _ QPixmap()

        gradient _ QLinearGradient()
        gradient.setStart(bounds.topLeft())
        gradient.setFinalStop(bounds.bottomRight())
        gradient.setColorAt(0, color)
        gradient.setColorAt(1, color.darker(200))

        setCacheMode(QGraphicsItem.ItemCoordinateCache)

    ___ setFill  fill):
        fillRect _ fill
        update()

    ___ fill
        r_ fillRect

    fill _ pyqtProperty(bool, fill, setFill)

    ___ paint  painter, option, widget):
        painter.setPen(__.NoPen)
        painter.setBrush(?C..(0, 0, 0, 64))
        painter.drawRoundedRect(bounds.translated(2, 2), 25.0, 25.0)

        __ fillRect:
            painter.setBrush(?A...palette().brush(?P...Window))
        ____
            painter.setBrush(gradient)

        painter.setPen(QPen(__.black, 1))
        painter.drawRoundedRect(bounds, 25.0, 25.0)
        __ no. pix.isNull
            painter.scale(1.95, 1.95)
            painter.drawPixmap(-pix.width() / 2, -pix.height() / 2, pix)

    ___ boundingRect
        r_ bounds.adjusted(0, 0, 2, 2)

    ___ pixmap
        r_ QPixmap(pix)

    ___ setPixmap  pixmap):
        pix _ QPixmap(pixmap)
        update()


c_ FlippablePad(RoundRectItem):
    ___  -   size, parent_None):
        super(FlippablePad, self). - (boundsFromSize(size),
                ?C..(226, 255, 92, 64), parent)

        numIcons _ size.width() * size.height()
        pixmaps _   # list
        it _ QDirIterator(":/images", ["*.png"])
        w__ it.hasNext() and le.(pixmaps) < numIcons:
            pixmaps.ap..(it.next())

        iconRect _ QRectF(-54, -54, 108, 108)
        iconColor _ ?C..(214, 240, 110, 128)
        iconGrid _   # list
        n _ 0

        ___ y __ range(size.height()):
            row _   # list

            ___ x __ range(size.width()):
                rect _ RoundRectItem(iconRect, iconColor, self)
                rect.setZValue(1)
                rect.setPos(posForLocation(x, y, size))
                rect.setPixmap(pixmaps[n % le.(pixmaps)])
                n +_ 1

                row.ap..(rect)

            iconGrid.ap..(row)

    ___ iconAt  column, row):
        r_ iconGrid[row][column]

    @staticmethod
    ___ boundsFromSize(size):
        r_ QRectF((-size.width() / 2.0) * 150,
                (-size.height() / 2.0) * 150, size.width() * 150,
                size.height() * 150)

    @staticmethod
    ___ posForLocation(column, row, size):
        r_ QPointF(column * 150, row * 150) - QPointF((size.width() - 1) * 75, (size.height() - 1) * 75)


c_ SplashItem(QGraphicsObject):
    ___  -   parent_None):
        super(SplashItem, self). - (parent)

        t__ _ "Welcome to the Pad Navigator Example. You can use the " \
                "keyboard arrows to navigate the icons, and press enter to " \
                "activate an item. Press any key to begin."

        setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    ___ boundingRect
        r_ QRectF(0, 0, 400, 175)

    ___ paint  painter, option, widget):
        painter.setPen(QPen(__.black, 2))
        painter.setBrush(?C..(245, 245, 255, 220))
        painter.setClipRect(boundingRect())
        painter.drawRoundedRect(3, -100 + 3, 400 - 6, 250 - 6, 25.0, 25.0)

        textRect _ boundingRect().adjusted(10, 10, -10, -10)
        flags _ int(__.AlignTop | __.AlignLeft) | __.TextWordWrap

        font _ QFont()
        font.setPixelSize(18)
        painter.setPen(__.black)
        painter.setFont(font)
        painter.drawText(textRect, flags, t__)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    navigator _ PadNavigator(QSize(3, 3))
    navigator.s..

    ___.exit(app.exec_())
