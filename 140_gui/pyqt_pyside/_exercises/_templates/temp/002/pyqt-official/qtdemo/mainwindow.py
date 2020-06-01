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


____ ?.?C.. ______ QFileInfo, QPoint, QRect, qRound, __, QTime, QTimer
____ ?.?G.. ______ (QFontMetricsF, QImage, QPainter, QPixmap, QPolygon,
        QRegion)
____ ?.?W.. ______ (?A.., QFrame, QGraphicsScene,
        QGraphicsView, QGraphicsWidget, ?MB.., QWidget)

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demotextitem ______ DemoTextItem
____ imageitem ______ ImageItem
____ menumanager ______ MenuManager


c_ MainWindow(QGraphicsView):
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.imagesDir _ QFileInfo(__file__).absolutePath() + '/images'

        self.updateTimer _ QTimer(self)
        self.demoStartTime _ QTime()
        self.fpsTime _ QTime()
        self.background _ QPixmap()

        self.scene _ N..
        self.mainSceneRoot _ N..
        self.frameTimeList _   # list
        self.fpsHistory _   # list

        self.currentFps _ Colors.fps
        self.fpsMedian _ -1
        self.fpsLabel _ N..
        self.pausedLabel _ N..
        self.doneAdapt _ False
        self.useTimer _ False
        self.updateTimer.setSingleShot(True)
        self.companyLogo _ N..
        self.qtLogo _ N..

        self.setupWidget()
        self.setupScene()
        self.setupSceneItems()
        self.drawBackgroundToPixmap()

    ___ setupWidget(self):
        desktop _ ?A...desktop()
        screenRect _ desktop.screenGeometry(desktop.primaryScreen())
        windowRect _ QRect(0, 0, 800, 600)

        __ screenRect.width() < 800:
            windowRect.setWidth(screenRect.width())

        __ screenRect.height() < 600:
            windowRect.setHeight(screenRect.height())

        windowRect.moveCenter(screenRect.center())
        self.setGeometry(windowRect)
        self.setMinimumSize(80, 60)

        self.setWindowTitle("PyQt Examples")
        self.setHorizontalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(__.ScrollBarAlwaysOff)
        self.setFrameStyle(QFrame.NoFrame)
        self.setRenderingSystem()
        self.updateTimer.timeout.c..(self.tick)

    ___ setRenderingSystem(self):
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewport(QWidget())

    ___ start(self):
        self.switchTimerOnOff(True)
        self.demoStartTime.restart()
        MenuManager.instance().itemSelected(MenuManager.ROOT,
                Colors.rootMenuName)
        Colors.debug("- starting demo")

    ___ enableMask  enable):
        __ no. enable or Colors.noWindowMask:
            self.clearMask()
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

            self.setMask(QRegion(region))

    ___ setupScene(self):
        self.scene _ QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 800, 600)
        self.setScene(self.scene)
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)

    ___ switchTimerOnOff  on):
        ticker _ MenuManager.instance().ticker
        __ ticker and ticker.scene
            ticker.tickOnPaint _ no. on or Colors.noTimerUpdate

        __ on and no. Colors.noTimerUpdate:
            self.useTimer _ True
            self.fpsTime _ QTime.currentTime()
            self.updateTimer.start(int(1000 / Colors.fps))
            update_mode _ QGraphicsView.NoViewportUpdate
        ____
            self.useTimer _ False
            self.updateTimer.stop()

            __ Colors.noTicker:
                update_mode _ QGraphicsView.MinimalViewportUpdate
            ____
                update_mode _ QGraphicsView.SmartViewportUpdate

        self.setViewportUpdateMode(update_mode)

    ___ measureFps(self):
        # Calculate time difference.
        t _ self.fpsTime.msecsTo(QTime.currentTime())
        __ t == 0:
            t _ 0.01

        self.currentFps _ (1000.0 / t)
        self.fpsHistory.ap..(self.currentFps)
        self.fpsTime _ QTime.currentTime()

        # Calculate median.
        size _ le.(self.fpsHistory)

        __ size == 10:
            self.fpsHistory.sort()
            self.fpsMedian _ self.fpsHistory[int(size / 2)]
            __ self.fpsMedian == 0:
                self.fpsMedian _ 0.01

            self.fpsHistory _   # list

            r_ True

        r_ False

    ___ forceFpsMedianCalculation(self):
        # Used for adaption in case things are so slow that no median has yet
        # been calculated.
        __ self.fpsMedian !_ -1:
            r_

        size _ le.(self.fpsHistory)

        __ size == 0:
            self.fpsMedian _ 0.01
            r_

        self.fpsHistory.sort()
        self.fpsMedian _ self.fpsHistory[size // 2]
        __ self.fpsMedian == 0:
            self.fpsMedian _ 0.01

    ___ tick(self):
        medianChanged _ self.measureFps()
        self.checkAdapt()

        __ medianChanged and self.fpsLabel and Colors.showFps:
            self.fpsLabel.sT..("FPS: %d" % int(self.currentFps))

        __ MenuManager.instance().ticker:
            MenuManager.instance().ticker.tick()

        self.viewport().update()

        __ self.useTimer:
            self.updateTimer.start(int(1000 / Colors.fps))

    ___ setupSceneItems(self):
        __ Colors.showFps:
            self.fpsLabel _ DemoTextItem("FPS: --", Colors.buttonFont(),
                    __.white, -1, N.., DemoTextItem.DYNAMIC_TEXT)
            self.fpsLabel.setZValue(1000)
            self.fpsLabel.setPos(Colors.stageStartX,
                    600 - QFontMetricsF(Colors.buttonFont()).height() - 5)

        self.mainSceneRoot _ QGraphicsWidget()
        self.scene.addItem(self.mainSceneRoot)

        self.companyLogo _ ImageItem(
                QImage(self.imagesDir + '/trolltech-logo.png'),
                1000, 1000, N.., True, 0.5)
        self.qtLogo _ ImageItem(QImage(self.imagesDir + '/qtlogo_small.png'),
                1000, 1000, N.., True, 0.5)
        self.companyLogo.setZValue(100)
        self.qtLogo.setZValue(100)
        self.pausedLabel _ DemoTextItem("PAUSED", Colors.buttonFont(),
                __.white, -1, N..)
        self.pausedLabel.setZValue(100)
        fm _ QFontMetricsF(Colors.buttonFont())
        self.pausedLabel.setPos(Colors.stageWidth - fm.width("PAUSED"),
                590 - fm.height())
        self.pausedLabel.setRecursiveVisible F..

    ___ checkAdapt(self):
        __ self.doneAdapt or Colors.noTimerUpdate or self.demoStartTime.elapsed() < 2000:
            r_

        self.doneAdapt _ True
        self.forceFpsMedianCalculation()
        Colors.benchmarkFps _ self.fpsMedian
        Colors.debug("- benchmark: %d FPS" % int(Colors.benchmarkFps))

        __ Colors.noAdapt:
            r_

        __ self.fpsMedian < 30:
            ticker _ MenuManager.instance().ticker
            __ ticker and ticker.scene
                self.scene.removeItem(ticker)
                Colors.noTimerUpdate _ True
                self.switchTimerOnOff F..

                __ self.fpsLabel:
                    self.fpsLabel.sT..("FPS: (%d)" % int(self.fpsMedian))

                Colors.debug("- benchmark adaption: removed ticker (fps < 30)")

            __ self.fpsMedian < 20:
                Colors.noAnimations _ True
                Colors.debug("- benchmark adaption: animations switched off (fps < 20)")

            Colors.adapted _ True

    ___ drawBackgroundToPixmap(self):
        r _ self.scene.sceneRect()
        self.background _ QPixmap(qRound(r.width()), qRound(r.height()))
        self.background.fill(__.black)
        painter _ QPainter(self.background)

        bg _ QImage(self.imagesDir + '/demobg.png')
        painter.drawImage(0, 0, bg)

    ___ drawBackground  painter, rect):
        painter.drawPixmap(QPoint(0, 0), self.background)

    ___ toggleFullscreen(self):
        __ self.isFullScreen
            self.enableMask(True)
            self.showNormal()
            __ MenuManager.instance().ticker:
                MenuManager.instance().ticker.pause F..
        ____
            self.enableMask F..
            self.showFullScreen()

    ___ keyPressEvent  event):
        __ event.key() == __.Key_Escape:
            ?A...quit()
        ____ event.key() == __.Key_F1:
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
            ?MB...information(N.., "Current configuration", s)

        super(MainWindow, self).keyPressEvent(event)

    ___ focusInEvent  event):
        __ no. Colors.pause:
            r_

        __ MenuManager.instance().ticker:
            MenuManager.instance().ticker.pause F..

        code _ MenuManager.instance().currentMenuCode
        __ code in (MenuManager.ROOT, MenuManager.MENU1):
            self.switchTimerOnOff(True)

        self.pausedLabel.setRecursiveVisible F..

    ___ focusOutEvent  event):
        __ no. Colors.pause:
            r_

        __ MenuManager.instance().ticker:
            MenuManager.instance().ticker.pause(True)

        code _ MenuManager.instance().currentMenuCode
        __ code in (MenuManager.ROOT, MenuManager.MENU1):
            self.switchTimerOnOff F..

        self.pausedLabel.setRecursiveVisible(True)

    ___ resizeEvent  event):
        self.resetTransform()
        self.scale(event.size().width() / 800.0, event.size().height() / 600.0)

        super(MainWindow, self).resizeEvent(event)

        DemoItem.setTransform(self.transform())

        __ self.companyLogo:
            r _ self.scene.sceneRect()
            ttb _ self.companyLogo.boundingRect()
            self.companyLogo.setPos(int((r.width() - ttb.width()) / 2),
                    595 - ttb.height())
            qtb _ self.qtLogo.boundingRect()
            self.qtLogo.setPos(802 - qtb.width(), 0)

        # Changing size will almost always hurt FPS during the change so ignore
        # it.
        self.fpsHistory _   # list
