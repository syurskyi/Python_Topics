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
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.currentPath _ ''

        self.view _ SvgView()

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        self.mB.. .aM..(fileMenu)

        viewMenu _ QMenu("&View", self)
        self.backgroundAction _ viewMenu.aA..("&Background")
        self.backgroundAction.setEnabled F..
        self.backgroundAction.setCheckable(True)
        self.backgroundAction.setChecked F..
        self.backgroundAction.toggled.c..(self.view.setViewBackground)

        self.outlineAction _ viewMenu.aA..("&Outline")
        self.outlineAction.setEnabled F..
        self.outlineAction.setCheckable(True)
        self.outlineAction.setChecked(True)
        self.outlineAction.toggled.c..(self.view.setViewOutline)

        self.mB.. .aM..(viewMenu)

        rendererMenu _ QMenu("&Renderer", self)
        self.nativeAction _ rendererMenu.aA..("&Native")
        self.nativeAction.setCheckable(True)
        self.nativeAction.setChecked(True)

        __ QGLFormat.hasOpenGL
            self.glAction _ rendererMenu.aA..("&OpenGL")
            self.glAction.setCheckable(True)

        self.imageAction _ rendererMenu.aA..("&Image")
        self.imageAction.setCheckable(True)

        __ QGLFormat.hasOpenGL
            rendererMenu.addSeparator()
            self.highQualityAntialiasingAction _ rendererMenu.aA..("&High Quality Antialiasing")
            self.highQualityAntialiasingAction.setEnabled F..
            self.highQualityAntialiasingAction.setCheckable(True)
            self.highQualityAntialiasingAction.setChecked F..
            self.highQualityAntialiasingAction.toggled.c..(self.view.setHighQualityAntialiasing)

        rendererGroup _ QActionGroup(self)
        rendererGroup.aA..(self.nativeAction)

        __ QGLFormat.hasOpenGL
            rendererGroup.aA..(self.glAction)

        rendererGroup.aA..(self.imageAction)

        self.mB.. .aM..(rendererMenu)

        openAction.t__.c..(self.openFile)
        quitAction.t__.c..(?A...instance().quit)
        rendererGroup.t__.c..(self.setRenderer)

        self.sCW..(self.view)
        self.setWindowTitle("SVG Viewer")

    ___ openFile  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Open SVG File",
                    self.currentPath, "SVG files (*.svg *.svgz *.svg.gz)")

        __ path:
            svg_file _ QFile(path)
            __ no. svg_file.exists
                ?MB...critical  "Open SVG File",
                        "Could not open file '%s'." % path)

                self.outlineAction.setEnabled F..
                self.backgroundAction.setEnabled F..
                r_

            self.view.openFile(svg_file)

            __ no. path.startswith(':/'):
                self.currentPath _ path
                self.setWindowTitle("%s - SVGViewer" % self.currentPath)

            self.outlineAction.setEnabled(True)
            self.backgroundAction.setEnabled(True)

            self.resize(self.view.sizeHint() + QSize(80, 80 + self.mB.. .height()))

    ___ setRenderer  action):
        __ QGLFormat.hasOpenGL
            self.highQualityAntialiasingAction.setEnabled F..

        __ action == self.nativeAction:
            self.view.setRenderer(SvgView.Native)
        ____ action == self.glAction:
            __ QGLFormat.hasOpenGL
                self.highQualityAntialiasingAction.setEnabled(True)
                self.view.setRenderer(SvgView.OpenGL)
        ____ action == self.imageAction:
            self.view.setRenderer(SvgView.Image)


c_ SvgView(QGraphicsView):
    Native, OpenGL, Image _ range(3)

    ___ __init__  parent_None):
        super(SvgView, self).__init__(parent)

        self.renderer _ SvgView.Native
        self.svgItem _ N..
        self.backgroundItem _ N..
        self.outlineItem _ N..
        self.image _ QImage()

        self.setScene(QGraphicsScene(self))
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Prepare background check-board pattern.
        tilePixmap _ QPixmap(64, 64)
        tilePixmap.fill(__.white)
        tilePainter _ QPainter(tilePixmap)
        color _ ?C..(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        self.setBackgroundBrush(QBrush(tilePixmap))

    ___ drawBackground  p, rect):
        p.save()
        p.resetTransform()
        p.drawTiledPixmap(self.viewport().rect(),
                self.backgroundBrush().texture())
        p.restore()

    ___ openFile  svg_file):
        __ no. svg_file.exists
            r_

        s _ self.scene()

        __ self.backgroundItem:
            drawBackground _ self.backgroundItem.isVisible()
        ____
            drawBackground _ False

        __ self.outlineItem:
            drawOutline _ self.outlineItem.isVisible()
        ____
            drawOutline _ True

        s.clear()
        self.resetTransform()

        self.svgItem _ QGraphicsSvgItem(svg_file.fileName())
        self.svgItem.setFlags(QGraphicsItem.ItemClipsToShape)
        self.svgItem.setCacheMode(QGraphicsItem.NoCache)
        self.svgItem.setZValue(0)

        self.backgroundItem _ QGraphicsRectItem(self.svgItem.boundingRect())
        self.backgroundItem.setBrush(__.white)
        self.backgroundItem.setPen(QPen(__.NoPen))
        self.backgroundItem.setVisible(drawBackground)
        self.backgroundItem.setZValue(-1)

        self.outlineItem _ QGraphicsRectItem(self.svgItem.boundingRect())
        outline _ QPen(__.black, 2, __.DashLine)
        outline.setCosmetic(True)
        self.outlineItem.setPen(outline)
        self.outlineItem.setBrush(QBrush(__.NoBrush))
        self.outlineItem.setVisible(drawOutline)
        self.outlineItem.setZValue(1)

        s.addItem(self.backgroundItem)
        s.addItem(self.svgItem)
        s.addItem(self.outlineItem)

        s.setSceneRect(self.outlineItem.boundingRect().adjusted(-10, -10, 10, 10))

    ___ setRenderer  renderer):
        self.renderer _ renderer

        __ self.renderer == SvgView.OpenGL:
            __ QGLFormat.hasOpenGL
                self.setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))
        ____
            self.setViewport(QWidget())

    ___ setHighQualityAntialiasing  highQualityAntialiasing):
        __ QGLFormat.hasOpenGL
            self.setRenderHint(QPainter.HighQualityAntialiasing,
                    highQualityAntialiasing)

    ___ setViewBackground  enable):
        __ self.backgroundItem:
            self.backgroundItem.setVisible(enable)

    ___ setViewOutline  enable):
        __ self.outlineItem:
            self.outlineItem.setVisible(enable)

    ___ paintEvent  event):
        __ self.renderer == SvgView.Image:
            __ self.image.size() !_ self.viewport().size
                self.image _ QImage(self.viewport().size(),
                        QImage.Format_ARGB32_Premultiplied)

            imagePainter _ QPainter(self.image)
            QGraphicsView.render  imagePainter)
            imagePainter.end()

            p _ QPainter(self.viewport())
            p.drawImage(0, 0, self.image)
        ____
            super(SvgView, self).paintEvent(event)

    ___ wheelEvent  event):
        factor _ pow(1.2, event.delta() / 240.0)
        self.scale(factor, factor)
        event.accept()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    window _ MainWindow()
    __ le.(sys.argv) == 2:
        window.openFile(sys.argv[1])
    ____
        window.openFile(':/files/bubbles.svg')
    window.s..
    sys.exit(app.exec_())
