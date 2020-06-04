#############################################################################
##
## Copyright (C) 2015 Riverbank Computing Limited.
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


____ ?.?C.. ______ QFileInfo, QPoint, QRect, qRound, __, ?T.., ?T..
____ ?.?G.. ______ (QFontMetricsF, QImage, QPainter, ?P.., QPolygon,
        QRegion)
____ ?.?W.. ______ (?A.., QFrame, QGraphicsScene,
        QGraphicsView, QGraphicsWidget, ?MB.., ?W..)

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demotextitem ______ DemoTextItem
____ imageitem ______ ImageItem
____ menumanager ______ MenuManager


c_ MainWindow(QGraphicsView):
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        imagesDir _ QFileInfo(__file__).absolutePath() + '/images'

        updateTimer _ ?T..
        demoStartTime _ ?T..()
        fpsTime _ ?T..()
        background _ ?P..()

        scene _ N..
        mainSceneRoot _ N..
        frameTimeList _   # list
        fpsHistory _   # list

        currentFps _ Colors.fps
        fpsMedian _ -1
        fpsLabel _ N..
        pausedLabel _ N..
        doneAdapt _ F..
        useTimer _ F..
        updateTimer.setSingleShot( st.
        companyLogo _ N..
        qtLogo _ N..

        setupWidget()
        setupScene()
        setupSceneItems()
        drawBackgroundToPixmap()

    ___ setupWidget
        desktop _ ?A...desktop()
        screenRect _ desktop.screenGeometry(desktop.primaryScreen())
        windowRect _ QRect(0, 0, 800, 600)

        __ screenRect.width() < 800:
            windowRect.sW..(screenRect.width())

        __ screenRect.height() < 600:
            windowRect.setHeight(screenRect.height())

        windowRect.moveCenter(screenRect.center())
        setGeometry(windowRect)
        sMS..(80, 60)

        sWT..("PyQt Examples")
        setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        setFrameStyle(QFrame.NoFrame)
        setRenderingSystem()
        updateTimer.timeout.c..(tick)

    ___ setRenderingSystem
        setCacheMode(QGraphicsView.CacheBackground)
        setViewport(?W..())

    ___ start
        switchTimerOnOff( st.
        demoStartTime.restart()
        MenuManager.i.. .itemSelected(MenuManager.ROOT,
                Colors.rootMenuName)
        Colors.debug("- starting demo")

    ___ enableMask  enable):
        __ no. enable or Colors.noWindowMask:
            clearMask()
        ____
            region _ QPolygon([
                    # North side.
                    0, 0,
                    800, 0,
                    # East side.
                    # 800, 70,
                    # 790, 90,
                    # 790, 480,
                    # 800, 500,
                    800, 600,
                    # South side.
                    700, 600,
                    670, 590,
                    130, 590,
                    100, 600,
                    0, 600,
                    # West side.
                    # 0, 550,
                    # 10, 530,
                    # 10, 520,
                    # 0, 520,
                    0, 0])

            setMask(QRegion(region))

    ___ setupScene
        scene _ QGraphicsScene
        scene.setSceneRect(0, 0, 800, 600)
        setScene(scene)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)

    ___ switchTimerOnOff  on):
        ticker _ MenuManager.i.. .ticker
        __ ticker and ticker.scene
            ticker.tickOnPaint _ no. on or Colors.noTimerUpdate

        __ on and no. Colors.noTimerUpdate:
            useTimer _ T..
            fpsTime _ ?T...currentTime()
            updateTimer.start(in.(1000 / Colors.fps))
            update_mode _ QGraphicsView.NoViewportUpdate
        ____
            useTimer _ F..
            updateTimer.s..

            __ Colors.noTicker:
                update_mode _ QGraphicsView.MinimalViewportUpdate
            ____
                update_mode _ QGraphicsView.SmartViewportUpdate

        setViewportUpdateMode(update_mode)

    ___ measureFps
        # Calculate time difference.
        t _ fpsTime.msecsTo(?T...currentTime())
        __ t __ 0:
            t _ 0.01

        currentFps _ (1000.0 / t)
        fpsHistory.ap..(currentFps)
        fpsTime _ ?T...currentTime()

        # Calculate median.
        size _ le.(fpsHistory)

        __ size __ 10:
            fpsHistory.s..()
            fpsMedian _ fpsHistory[in.(size / 2)]
            __ fpsMedian __ 0:
                fpsMedian _ 0.01

            fpsHistory _   # list

            r_ T..

        r_ F..

    ___ forceFpsMedianCalculation
        # Used for adaption in case things are so slow that no median has yet
        # been calculated.
        __ fpsMedian !_ -1:
            r_

        size _ le.(fpsHistory)

        __ size __ 0:
            fpsMedian _ 0.01
            r_

        fpsHistory.s..()
        fpsMedian _ fpsHistory[size // 2]
        __ fpsMedian __ 0:
            fpsMedian _ 0.01

    ___ tick
        medianChanged _ measureFps()
        checkAdapt()

        __ medianChanged and fpsLabel and Colors.showFps:
            fpsLabel.sT..("FPS: %d" % in.(currentFps))

        __ MenuManager.i.. .ticker:
            MenuManager.i.. .ticker.tick()

        viewport().update()

        __ useTimer:
            updateTimer.start(in.(1000 / Colors.fps))

    ___ setupSceneItems
        __ Colors.showFps:
            fpsLabel _ DemoTextItem("FPS: --", Colors.buttonFont(),
                    __.white, -1, N.., DemoTextItem.DYNAMIC_TEXT)
            fpsLabel.setZValue(1000)
            fpsLabel.setPos(Colors.stageStartX,
                    600 - QFontMetricsF(Colors.buttonFont()).height() - 5)

        mainSceneRoot _ QGraphicsWidget()
        scene.aI..(mainSceneRoot)

        companyLogo _ ImageItem(
                QImage(imagesDir + '/trolltech-logo.png'),
                1000, 1000, N.., T.., 0.5)
        qtLogo _ ImageItem(QImage(imagesDir + '/qtlogo_small.png'),
                1000, 1000, N.., T.., 0.5)
        companyLogo.setZValue(100)
        qtLogo.setZValue(100)
        pausedLabel _ DemoTextItem("PAUSED", Colors.buttonFont(),
                __.white, -1, N..)
        pausedLabel.setZValue(100)
        fm _ QFontMetricsF(Colors.buttonFont())
        pausedLabel.setPos(Colors.stageWidth - fm.width("PAUSED"),
                590 - fm.height())
        pausedLabel.setRecursiveVisible F..

    ___ checkAdapt
        __ doneAdapt or Colors.noTimerUpdate or demoStartTime.elapsed() < 2000:
            r_

        doneAdapt _ T..
        forceFpsMedianCalculation()
        Colors.benchmarkFps _ fpsMedian
        Colors.debug("- benchmark: %d FPS" % in.(Colors.benchmarkFps))

        __ Colors.noAdapt:
            r_

        __ fpsMedian < 30:
            ticker _ MenuManager.i.. .ticker
            __ ticker and ticker.scene
                scene.removeItem(ticker)
                Colors.noTimerUpdate _ T..
                switchTimerOnOff F..

                __ fpsLabel:
                    fpsLabel.sT..("FPS: (%d)" % in.(fpsMedian))

                Colors.debug("- benchmark adaption: removed ticker (fps < 30)")

            __ fpsMedian < 20:
                Colors.noAnimations _ T..
                Colors.debug("- benchmark adaption: animations switched off (fps < 20)")

            Colors.adapted _ T..

    ___ drawBackgroundToPixmap
        r _ scene.sceneRect()
        background _ ?P..(qRound(r.width()), qRound(r.height()))
        background.fill(__.black)
        painter _ QPainter(background)

        bg _ QImage(imagesDir + '/demobg.png')
        painter.drawImage(0, 0, bg)

    ___ drawBackground  painter, rect):
        painter.drawPixmap(QPoint(0, 0), background)

    ___ toggleFullscreen
        __ isFullScreen
            enableMask( st.
            showNormal()
            __ MenuManager.i.. .ticker:
                MenuManager.i.. .ticker.pause F..
        ____
            enableMask F..
            showFullScreen()

    ___ keyPressEvent  event):
        __ event.key() __ __.Key_Escape:
            ?A...quit()
        ____ event.key() __ __.Key_F1:
            s _ ""
            s +_ "\nAdapt: "
            s +_ ["on", "off"][Colors.noAdapt]
            s +_ "\nAdaption occured: "
            s +_ ["no", "yes"][Colors.adapted]
            w _ ?W..
            s +_ "\nColor bit depth: %d" % w.depth()
            s +_ "\nWanted FPS: %d" % Colors.fps
            s +_ "\nBenchmarked FPS: ";
            __ Colors.benchmarkFps !_ -1:
                s +_ "%d" % Colors.benchmarkFps
            ____
                s +_ "not calculated"
            s +_ "\nAnimations: ";
            s +_ ["on", "off"][Colors.noAnimations]
            s +_ "\nBlending: ";
            s +_ ["on", "off"][Colors.useEightBitPalette]
            s +_ "\nTicker: ";
            s +_ ["on", "off"][Colors.noTicker]
            s +_ "\nPixmaps: ";
            s +_ ["off", "on"][Colors.usePixmaps]
            s +_ "\nRescale images on resize: ";
            s +_ ["on", "off"][Colors.noRescale]
            s +_ "\nTimer based updates: ";
            s +_ ["on", "off"][Colors.noTimerUpdate]
            s +_ "\nSeparate loop: ";
            s +_ ["no", "yes"][Colors.useLoop]
            s +_ "\nScreen sync: ";
            s +_ ["yes", "no"][Colors.noScreenSync]
            ?MB...i..(N.., "Current configuration", s)

        s__(MainWindow, self).keyPressEvent(event)

    ___ focusInEvent  event):
        __ no. Colors.pause:
            r_

        __ MenuManager.i.. .ticker:
            MenuManager.i.. .ticker.pause F..

        code _ MenuManager.i.. .currentMenuCode
        __ code __ (MenuManager.ROOT, MenuManager.MENU1):
            switchTimerOnOff( st.

        pausedLabel.setRecursiveVisible F..

    ___ focusOutEvent  event):
        __ no. Colors.pause:
            r_

        __ MenuManager.i.. .ticker:
            MenuManager.i.. .ticker.pause( st.

        code _ MenuManager.i.. .currentMenuCode
        __ code __ (MenuManager.ROOT, MenuManager.MENU1):
            switchTimerOnOff F..

        pausedLabel.setRecursiveVisible( st.

    ___ resizeEvent  event):
        resetTransform()
        scale(event.size().width() / 800.0, event.size().height() / 600.0)

        s__(MainWindow, self).resizeEvent(event)

        DemoItem.setTransform(transform())

        __ companyLogo:
            r _ scene.sceneRect()
            ttb _ companyLogo.boundingRect()
            companyLogo.setPos(in.((r.width() - ttb.width()) / 2),
                    595 - ttb.height())
            qtb _ qtLogo.boundingRect()
            qtLogo.setPos(802 - qtb.width(), 0)

        # Changing size will almost always hurt FPS during the change so ignore
        # it.
        fpsHistory _   # list
