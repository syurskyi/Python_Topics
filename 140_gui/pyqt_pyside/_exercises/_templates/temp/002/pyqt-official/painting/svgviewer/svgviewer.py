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


____ ?.?C.. ______ QFile, QSize, __
____ ?.?G.. ______ QBrush, ?C.., QImage, QPainter, QPixmap, QPen
____ ?.?W.. ______ (QActionGroup, ?A.., ?FD..,
        QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView,
        QMainWindow, QMenu, ?MB.., QWidget)
____ ?.QtOpenGL ______ QGL, QGLFormat, QGLWidget
____ ?.QtSvg ______ QGraphicsSvgItem

______ svgviewer_rc


c_ MainWindow ?MW..
    ___  -
        super(MainWindow, self). - ()

        currentPath _ ''

        view _ SvgView()

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        mB.. .aM..(fileMenu)

        viewMenu _ QMenu("&View", self)
        backgroundAction _ viewMenu.aA..("&Background")
        backgroundAction.setEnabled F..
        backgroundAction.setCheckable(True)
        backgroundAction.setChecked F..
        backgroundAction.toggled.c..(view.setViewBackground)

        outlineAction _ viewMenu.aA..("&Outline")
        outlineAction.setEnabled F..
        outlineAction.setCheckable(True)
        outlineAction.setChecked(True)
        outlineAction.toggled.c..(view.setViewOutline)

        mB.. .aM..(viewMenu)

        rendererMenu _ QMenu("&Renderer", self)
        nativeAction _ rendererMenu.aA..("&Native")
        nativeAction.setCheckable(True)
        nativeAction.setChecked(True)

        __ QGLFormat.hasOpenGL
            glAction _ rendererMenu.aA..("&OpenGL")
            glAction.setCheckable(True)

        imageAction _ rendererMenu.aA..("&Image")
        imageAction.setCheckable(True)

        __ QGLFormat.hasOpenGL
            rendererMenu.addSeparator()
            highQualityAntialiasingAction _ rendererMenu.aA..("&High Quality Antialiasing")
            highQualityAntialiasingAction.setEnabled F..
            highQualityAntialiasingAction.setCheckable(True)
            highQualityAntialiasingAction.setChecked F..
            highQualityAntialiasingAction.toggled.c..(view.setHighQualityAntialiasing)

        rendererGroup _ QActionGroup
        rendererGroup.aA..(nativeAction)

        __ QGLFormat.hasOpenGL
            rendererGroup.aA..(glAction)

        rendererGroup.aA..(imageAction)

        mB.. .aM..(rendererMenu)

        openAction.t__.c..(openFile)
        quitAction.t__.c..(?A...instance().quit)
        rendererGroup.t__.c..(setRenderer)

        sCW..(view)
        setWindowTitle("SVG Viewer")

    ___ openFile  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Open SVG File",
                    currentPath, "SVG files (*.svg *.svgz *.svg.gz)")

        __ path:
            svg_file _ QFile(path)
            __ no. svg_file.exists
                ?MB...critical  "Open SVG File",
                        "Could not open file '%s'." % path)

                outlineAction.setEnabled F..
                backgroundAction.setEnabled F..
                r_

            view.openFile(svg_file)

            __ no. path.startswith(':/'):
                currentPath _ path
                setWindowTitle("%s - SVGViewer" % currentPath)

            outlineAction.setEnabled(True)
            backgroundAction.setEnabled(True)

            resize(view.sizeHint() + QSize(80, 80 + mB.. .height()))

    ___ setRenderer  action):
        __ QGLFormat.hasOpenGL
            highQualityAntialiasingAction.setEnabled F..

        __ action == nativeAction:
            view.setRenderer(SvgView.Native)
        ____ action == glAction:
            __ QGLFormat.hasOpenGL
                highQualityAntialiasingAction.setEnabled(True)
                view.setRenderer(SvgView.OpenGL)
        ____ action == imageAction:
            view.setRenderer(SvgView.Image)


c_ SvgView(QGraphicsView):
    Native, OpenGL, Image _ range(3)

    ___  -   parent_None):
        super(SvgView, self). - (parent)

        renderer _ SvgView.Native
        svgItem _ N..
        backgroundItem _ N..
        outlineItem _ N..
        image _ QImage()

        setScene(QGraphicsScene(self))
        setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        setDragMode(QGraphicsView.ScrollHandDrag)
        setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Prepare background check-board pattern.
        tilePixmap _ QPixmap(64, 64)
        tilePixmap.fill(__.white)
        tilePainter _ QPainter(tilePixmap)
        color _ ?C..(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        setBackgroundBrush(QBrush(tilePixmap))

    ___ drawBackground  p, rect):
        p.save()
        p.resetTransform()
        p.drawTiledPixmap(viewport().rect(),
                backgroundBrush().texture())
        p.restore()

    ___ openFile  svg_file):
        __ no. svg_file.exists
            r_

        s _ scene()

        __ backgroundItem:
            drawBackground _ backgroundItem.isVisible()
        ____
            drawBackground _ False

        __ outlineItem:
            drawOutline _ outlineItem.isVisible()
        ____
            drawOutline _ True

        s.clear()
        resetTransform()

        svgItem _ QGraphicsSvgItem(svg_file.fileName())
        svgItem.setFlags(QGraphicsItem.ItemClipsToShape)
        svgItem.setCacheMode(QGraphicsItem.NoCache)
        svgItem.setZValue(0)

        backgroundItem _ QGraphicsRectItem(svgItem.boundingRect())
        backgroundItem.setBrush(__.white)
        backgroundItem.setPen(QPen(__.NoPen))
        backgroundItem.setVisible(drawBackground)
        backgroundItem.setZValue(-1)

        outlineItem _ QGraphicsRectItem(svgItem.boundingRect())
        outline _ QPen(__.black, 2, __.DashLine)
        outline.setCosmetic(True)
        outlineItem.setPen(outline)
        outlineItem.setBrush(QBrush(__.NoBrush))
        outlineItem.setVisible(drawOutline)
        outlineItem.setZValue(1)

        s.addItem(backgroundItem)
        s.addItem(svgItem)
        s.addItem(outlineItem)

        s.setSceneRect(outlineItem.boundingRect().adjusted(-10, -10, 10, 10))

    ___ setRenderer  renderer):
        renderer _ renderer

        __ renderer == SvgView.OpenGL:
            __ QGLFormat.hasOpenGL
                setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))
        ____
            setViewport(QWidget())

    ___ setHighQualityAntialiasing  highQualityAntialiasing):
        __ QGLFormat.hasOpenGL
            setRenderHint(QPainter.HighQualityAntialiasing,
                    highQualityAntialiasing)

    ___ setViewBackground  enable):
        __ backgroundItem:
            backgroundItem.setVisible(enable)

    ___ setViewOutline  enable):
        __ outlineItem:
            outlineItem.setVisible(enable)

    ___ paintEvent  event):
        __ renderer == SvgView.Image:
            __ image.size() !_ viewport().size
                image _ QImage(viewport().size(),
                        QImage.Format_ARGB32_Premultiplied)

            imagePainter _ QPainter(image)
            QGraphicsView.render  imagePainter)
            imagePainter.end()

            p _ QPainter(viewport())
            p.drawImage(0, 0, image)
        ____
            super(SvgView, self).paintEvent(event)

    ___ wheelEvent  event):
        factor _ pow(1.2, event.delta() / 240.0)
        scale(factor, factor)
        event.accept()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ MainWindow()
    __ le.(___.a.. == 2:
        window.openFile(___.argv[1])
    ____
        window.openFile(':/files/bubbles.svg')
    window.s..
    ___.exit(app.exec_())
