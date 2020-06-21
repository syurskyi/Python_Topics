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


______ m__

____ ?.?C.. ______ (pP.., QDirIterator, QEasingCurve, QEvent,
        QEventTransition, QHistoryState, QParallelAnimationGroup, QPointF,
        ?PA.., QRectF, QSequentialAnimationGroup, ?S.., QState,
        QStateMachine, __)
____ ?.?G.. ______ (?B.., ?C.., ?F.., QLinearGradient, QPainter,
        ?P.., ?P.., ?P.., QTransform)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsProxyWidget, QGraphicsRotation, QGraphicsScene, QGraphicsView,
        QKeyEventTransition, ?W..)
____ ?.QtOpenGL ______ QGL, QGLFormat, QGLWidget

______ padnavigator_rc
____ ui_form ______ Ui_Form


c_ PadNavigator(QGraphicsView):
    ___  -   size, parent_None):
        s__(PadNavigator, self). - (parent)

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

        smoothSplashMove _ ?PA..(splash, b'y')
        smoothSplashOpacity _ ?PA..(splash, b'opacity')
        smoothSplashMove.setEasingCurve(QEasingCurve.InQuad)
        smoothSplashMove.sD..(250)
        smoothSplashOpacity.sD..(250)

        smoothXSelection _ ?PA..(selectionItem, b'x')
        smoothYSelection _ ?PA..(selectionItem, b'y')
        smoothXRotation _ ?PA..(xRotation, b'angle')
        smoothYRotation _ ?PA..(yRotation, b'angle')
        smoothXSelection.sD..(125)
        smoothYSelection.sD..(125)
        smoothXRotation.sD..(125)
        smoothYRotation.sD..(125)
        smoothXSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYSelection.setEasingCurve(QEasingCurve.InOutQuad)
        smoothXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothYRotation.setEasingCurve(QEasingCurve.InOutQuad)

        smoothFlipRotation _ ?PA..(flipRotation, b'angle')
        smoothFlipScale _ ?PA..(pad, b'scale')
        smoothFlipXRotation _ ?PA..(xRotation, b'angle')
        smoothFlipYRotation _ ?PA..(yRotation, b'angle')
        flipAnimation _ QParallelAnimationGroup
        smoothFlipScale.sD..(500)
        smoothFlipRotation.sD..(500)
        smoothFlipXRotation.sD..(500)
        smoothFlipYRotation.sD..(500)
        smoothFlipScale.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipXRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipYRotation.setEasingCurve(QEasingCurve.InOutQuad)
        smoothFlipScale.sKVA..(0, 1.0)
        smoothFlipScale.sKVA..(0.5, 0.7)
        smoothFlipScale.sKVA..(1, 1.0)
        flipAnimation.addAnimation(smoothFlipRotation)
        flipAnimation.addAnimation(smoothFlipScale)
        flipAnimation.addAnimation(smoothFlipXRotation)
        flipAnimation.addAnimation(smoothFlipYRotation)

        setVariablesSequence _ QSequentialAnimationGroup()
        setFillAnimation _ ?PA..(pad, b'fill')
        setBackItemVisibleAnimation _ ?PA..(backItem, b'visible')
        setSelectionItemVisibleAnimation _ ?PA..(selectionItem, b'visible')
        setFillAnimation.sD..(0)
        setBackItemVisibleAnimation.sD..(0)
        setSelectionItemVisibleAnimation.sD..(0)
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

        frontState.assignProperty(pad, "fill", F..)
        frontState.assignProperty(splash, "opacity", 0.0)
        frontState.assignProperty(backItem, "visible", F..)
        frontState.assignProperty(flipRotation, "angle", 0.0)
        frontState.assignProperty(selectionItem, "visible",  st.

        backState.assignProperty(pad, "fill",  st.
        backState.assignProperty(backItem, "visible",  st.
        backState.assignProperty(xRotation, "angle", 0.0)
        backState.assignProperty(yRotation, "angle", 0.0)
        backState.assignProperty(flipRotation, "angle", 180.0)
        backState.assignProperty(selectionItem, "visible", F..)

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
        ___ y __ ra..(rows):
            stateGrid.ap..([QState(frontState) ___ _ __ ra..(columns)])

        frontState.setInitialState(stateGrid[0][0])
        selectionItem.setPos(pad.iconAt(0, 0).pos())

        ___ y __ ra..(rows):
            ___ x __ ra..(columns):
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
                frontState.assignProperty(icon, "visible",  st.
                backState.assignProperty(icon, "visible", F..)

                setIconVisibleAnimation _ ?PA..(icon, b'visible')
                setIconVisibleAnimation.sD..(0)
                setVariablesSequence.addAnimation(setIconVisibleAnimation)

        scene _ QGraphicsScene
        scene.setBackgroundBrush(?B..(?P..(":/images/blue_angle_swirl.jpg")))
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.aI..(pad)
        scene.setSceneRect(scene.itemsBoundingRect())
        setScene(scene)

        sbr _ splash.boundingRect()
        splash.setPos(-sbr.width() / 2, scene.sceneRect().top() - 2)
        frontState.assignProperty(splash, "y", splash.y() - 100.0)
        scene.aI..(splash)

        setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        sMS..(50, 50)
        setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        setCacheMode(QGraphicsView.CacheBackground)
        setRenderHints(QPainter.Antialiasing |
                QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing)

        __ QGLFormat.hasOpenGL
            setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))

        stateMachine.start()

    ___ resizeEvent  event):
        s__(PadNavigator, self).resizeEvent(event)
        fitInView(scene().sceneRect(), __.KeepAspectRatio)


c_ RoundRectItem(QGraphicsObject):
    ___  -   bounds, color, parent_None):
        s__(RoundRectItem, self). - (parent)

        fillRect _ F..
        bounds _ QRectF(bounds)
        pix _ ?P..()

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

    fill _ pP..(bool, fill, setFill)

    ___ paint  painter, option, widget):
        painter.sP..(__.NoPen)
        painter.sB..(?C..(0, 0, 0, 64))
        painter.dRR..(bounds.translated(2, 2), 25.0, 25.0)

        __ fillRect:
            painter.sB..(?A...p...brush(?P...Window))
        ____
            painter.sB..(gradient)

        painter.sP..(?P..(__.black, 1))
        painter.dRR..(bounds, 25.0, 25.0)
        __ no. pix.isNull
            painter.scale(1.95, 1.95)
            painter.drawPixmap(-pix.width() / 2, -pix.height() / 2, pix)

    ___ boundingRect
        r_ bounds.adjusted(0, 0, 2, 2)

    ___ pixmap
        r_ ?P..(pix)

    ___ sP..  pixmap):
        pix _ ?P..(pixmap)
        update()


c_ FlippablePad(RoundRectItem):
    ___  -   size, parent_None):
        s__(FlippablePad, self). - (boundsFromSize(size),
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

        ___ y __ ra..(size.height()):
            row _   # list

            ___ x __ ra..(size.width()):
                rect _ RoundRectItem(iconRect, iconColor, self)
                rect.setZValue(1)
                rect.setPos(posForLocation(x, y, size))
                rect.sP..(pixmaps[n % le.(pixmaps)])
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
        s__(SplashItem, self). - (parent)

        t__ _ "Welcome to the Pad Navigator Example. You can use the " \
                "keyboard arrows to navigate the icons, and press enter to " \
                "activate an item. Press any key to begin."

        setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    ___ boundingRect
        r_ QRectF(0, 0, 400, 175)

    ___ paint  painter, option, widget):
        painter.sP..(?P..(__.black, 2))
        painter.sB..(?C..(245, 245, 255, 220))
        painter.setClipRect(boundingRect())
        painter.dRR..(3, -100 + 3, 400 - 6, 250 - 6, 25.0, 25.0)

        textRect _ boundingRect().adjusted(10, 10, -10, -10)
        flags _ in.(__.AlignTop | __.AlignLeft) | __.TextWordWrap

        font _ ?F..()
        font.setPixelSize(18)
        painter.sP..(__.black)
        painter.sF..(font)
        painter.drawText(textRect, flags, t__)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    navigator _ PadNavigator(?S..(3, 3))
    navigator.s..

    ___.e.. ?.e..
