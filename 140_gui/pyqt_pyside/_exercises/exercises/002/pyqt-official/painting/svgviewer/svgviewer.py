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


____ ?.?C.. ______ QFile, ?S.., __
____ ?.?G.. ______ ?B.., ?C.., QImage, QPainter, ?P.., ?P..
____ ?.?W.. ______ (QActionGroup, ?A.., ?FD..,
        QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView,
        ?MW.., ?M.., ?MB.., ?W..)
____ ?.QtOpenGL ______ QGL, QGLFormat, QGLWidget
____ ?.QtSvg ______ QGraphicsSvgItem

______ svgviewer_rc


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        currentPath _ ''

        view _ SvgView()

        fileMenu _ ?M..("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        mB.. .aM..(fileMenu)

        viewMenu _ ?M..("&View", self)
        backgroundAction _ viewMenu.aA..("&Background")
        backgroundAction.sE.. F..
        backgroundAction.setCheckable( st.
        backgroundAction.sC__ F..
        backgroundAction.t__.c..(view.setViewBackground)

        outlineAction _ viewMenu.aA..("&Outline")
        outlineAction.sE.. F..
        outlineAction.setCheckable( st.
        outlineAction.sC__( st.
        outlineAction.t__.c..(view.setViewOutline)

        mB.. .aM..(viewMenu)

        rendererMenu _ ?M..("&Renderer", self)
        nativeAction _ rendererMenu.aA..("&Native")
        nativeAction.setCheckable( st.
        nativeAction.sC__( st.

        __ QGLFormat.hasOpenGL
            glAction _ rendererMenu.aA..("&OpenGL")
            glAction.setCheckable( st.

        imageAction _ rendererMenu.aA..("&Image")
        imageAction.setCheckable( st.

        __ QGLFormat.hasOpenGL
            rendererMenu.aS..)
            highQualityAntialiasingAction _ rendererMenu.aA..("&High Quality Antialiasing")
            highQualityAntialiasingAction.sE.. F..
            highQualityAntialiasingAction.setCheckable( st.
            highQualityAntialiasingAction.sC__ F..
            highQualityAntialiasingAction.t__.c..(view.setHighQualityAntialiasing)

        rendererGroup _ QActionGroup
        rendererGroup.aA..(nativeAction)

        __ QGLFormat.hasOpenGL
            rendererGroup.aA..(glAction)

        rendererGroup.aA..(imageAction)

        mB.. .aM..(rendererMenu)

        openAction.t__.c..(openFile)
        quitAction.t__.c..(?A...i.. .quit)
        rendererGroup.t__.c..(setRenderer)

        sCW..(view)
        sWT..("SVG Viewer")

    ___ openFile  path_None):
        __ no. pa__:
            pa__, _ _ ?FD...gOFN..  "Open SVG File",
                    currentPath, "SVG files (*.svg *.svgz *.svg.gz)")

        __ pa__:
            svg_file _ QFile(pa__)
            __ no. svg_file.e..
                ?MB...c..  "Open SVG File",
                        "Could not open file '%s'." % pa__)

                outlineAction.sE.. F..
                backgroundAction.sE.. F..
                r_

            view.openFile(svg_file)

            __ no. pa__.s_w_(':/'):
                currentPath _ pa__
                sWT..("%s - SVGViewer" % currentPath)

            outlineAction.sE..( st.
            backgroundAction.sE..( st.

            r..(view.sH..() + ?S..(80, 80 + mB.. .height()))

    ___ setRenderer  action):
        __ QGLFormat.hasOpenGL
            highQualityAntialiasingAction.sE.. F..

        __ action __ nativeAction:
            view.setRenderer(SvgView.Native)
        ____ action __ glAction:
            __ QGLFormat.hasOpenGL
                highQualityAntialiasingAction.sE..( st.
                view.setRenderer(SvgView.OpenGL)
        ____ action __ imageAction:
            view.setRenderer(SvgView.Image)


c_ SvgView(QGraphicsView):
    Native, OpenGL, Image _ ra..(3)

    ___  -   parent_None):
        s__(SvgView, self). - (parent)

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
        tilePixmap _ ?P..(64, 64)
        tilePixmap.fill(__.white)
        tilePainter _ QPainter(tilePixmap)
        color _ ?C..(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        setBackgroundBrush(?B..(tilePixmap))

    ___ drawBackground  p, rect):
        p.save()
        p.resetTransform()
        p.drawTiledPixmap(viewport().rect(),
                backgroundBrush().texture())
        p.restore()

    ___ openFile  svg_file):
        __ no. svg_file.e..
            r_

        s _ scene()

        __ backgroundItem:
            drawBackground _ backgroundItem.isVisible()
        ____
            drawBackground _ F..

        __ outlineItem:
            drawOutline _ outlineItem.isVisible()
        ____
            drawOutline _ T..

        s.c..
        resetTransform()

        svgItem _ QGraphicsSvgItem(svg_file.fileName())
        svgItem.setFlags(QGraphicsItem.ItemClipsToShape)
        svgItem.setCacheMode(QGraphicsItem.NoCache)
        svgItem.setZValue(0)

        backgroundItem _ QGraphicsRectItem(svgItem.boundingRect())
        backgroundItem.sB..(__.white)
        backgroundItem.sP..(?P..(__.NoPen))
        backgroundItem.setVisible(drawBackground)
        backgroundItem.setZValue(-1)

        outlineItem _ QGraphicsRectItem(svgItem.boundingRect())
        outline _ ?P..(__.black, 2, __.DashLine)
        outline.setCosmetic( st.
        outlineItem.sP..(outline)
        outlineItem.sB..(?B..(__.NoBrush))
        outlineItem.setVisible(drawOutline)
        outlineItem.setZValue(1)

        s.aI..(backgroundItem)
        s.aI..(svgItem)
        s.aI..(outlineItem)

        s.setSceneRect(outlineItem.boundingRect().adjusted(-10, -10, 10, 10))

    ___ setRenderer  renderer):
        renderer _ renderer

        __ renderer __ SvgView.OpenGL:
            __ QGLFormat.hasOpenGL
                setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))
        ____
            setViewport(?W..())

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
        __ renderer __ SvgView.Image:
            __ image.size() !_ viewport().size
                image _ QImage(viewport().size(),
                        QImage.Format_ARGB32_Premultiplied)

            imagePainter _ QPainter(image)
            QGraphicsView.render  imagePainter)
            imagePainter.end()

            p _ QPainter(viewport())
            p.drawImage(0, 0, image)
        ____
            s__(SvgView, self).paintEvent(event)

    ___ wheelEvent  event):
        factor _ pow(1.2, event.delta() / 240.0)
        scale(factor, factor)
        event.accept()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    window _ MainWindow()
    __ le.(___.a.. __ 2:
        window.openFile(___.argv[1])
    ____
        window.openFile(':/files/bubbles.svg')
    window.s..
    ___.e.. ?.e..
