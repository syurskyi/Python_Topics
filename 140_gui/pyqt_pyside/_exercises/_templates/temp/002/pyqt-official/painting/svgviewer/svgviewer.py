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


____ ?.QtCore ______ QFile, QSize, Qt
____ ?.QtGui ______ QBrush, QColor, QImage, QPainter, QPixmap, QPen
____ ?.?W.. ______ (QActionGroup, QApplication, QFileDialog,
        QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView,
        QMainWindow, QMenu, QMessageBox, QWidget)
____ ?.QtOpenGL ______ QGL, QGLFormat, QGLWidget
____ ?.QtSvg ______ QGraphicsSvgItem

______ svgviewer_rc


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.currentPath _ ''

        self.view _ SvgView()

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.addAction("&Open...")
        openAction.setShortcut("Ctrl+O")
        quitAction _ fileMenu.addAction("E&xit")
        quitAction.setShortcut("Ctrl+Q")

        self.menuBar().addMenu(fileMenu)

        viewMenu _ QMenu("&View", self)
        self.backgroundAction _ viewMenu.addAction("&Background")
        self.backgroundAction.setEnabled(False)
        self.backgroundAction.setCheckable(True)
        self.backgroundAction.setChecked(False)
        self.backgroundAction.toggled.c..(self.view.setViewBackground)

        self.outlineAction _ viewMenu.addAction("&Outline")
        self.outlineAction.setEnabled(False)
        self.outlineAction.setCheckable(True)
        self.outlineAction.setChecked(True)
        self.outlineAction.toggled.c..(self.view.setViewOutline)

        self.menuBar().addMenu(viewMenu)

        rendererMenu _ QMenu("&Renderer", self)
        self.nativeAction _ rendererMenu.addAction("&Native")
        self.nativeAction.setCheckable(True)
        self.nativeAction.setChecked(True)

        if QGLFormat.hasOpenGL
            self.glAction _ rendererMenu.addAction("&OpenGL")
            self.glAction.setCheckable(True)

        self.imageAction _ rendererMenu.addAction("&Image")
        self.imageAction.setCheckable(True)

        if QGLFormat.hasOpenGL
            rendererMenu.addSeparator()
            self.highQualityAntialiasingAction _ rendererMenu.addAction("&High Quality Antialiasing")
            self.highQualityAntialiasingAction.setEnabled(False)
            self.highQualityAntialiasingAction.setCheckable(True)
            self.highQualityAntialiasingAction.setChecked(False)
            self.highQualityAntialiasingAction.toggled.c..(self.view.setHighQualityAntialiasing)

        rendererGroup _ QActionGroup(self)
        rendererGroup.addAction(self.nativeAction)

        if QGLFormat.hasOpenGL
            rendererGroup.addAction(self.glAction)

        rendererGroup.addAction(self.imageAction)

        self.menuBar().addMenu(rendererMenu)

        openAction.triggered.c..(self.openFile)
        quitAction.triggered.c..(QApplication.instance().quit)
        rendererGroup.triggered.c..(self.setRenderer)

        self.setCentralWidget(self.view)
        self.setWindowTitle("SVG Viewer")

    ___ openFile(self, path_None):
        if not path:
            path, _ _ QFileDialog.getOpenFileName(self, "Open SVG File",
                    self.currentPath, "SVG files (*.svg *.svgz *.svg.gz)")

        if path:
            svg_file _ QFile(path)
            if not svg_file.exists
                QMessageBox.critical(self, "Open SVG File",
                        "Could not open file '%s'." % path)

                self.outlineAction.setEnabled(False)
                self.backgroundAction.setEnabled(False)
                return

            self.view.openFile(svg_file)

            if not path.startswith(':/'):
                self.currentPath _ path
                self.setWindowTitle("%s - SVGViewer" % self.currentPath)

            self.outlineAction.setEnabled(True)
            self.backgroundAction.setEnabled(True)

            self.resize(self.view.sizeHint() + QSize(80, 80 + self.menuBar().height()))

    ___ setRenderer(self, action):
        if QGLFormat.hasOpenGL
            self.highQualityAntialiasingAction.setEnabled(False)

        if action == self.nativeAction:
            self.view.setRenderer(SvgView.Native)
        elif action == self.glAction:
            if QGLFormat.hasOpenGL
                self.highQualityAntialiasingAction.setEnabled(True)
                self.view.setRenderer(SvgView.OpenGL)
        elif action == self.imageAction:
            self.view.setRenderer(SvgView.Image)


class SvgView(QGraphicsView):
    Native, OpenGL, Image _ range(3)

    ___ __init__(self, parent_None):
        super(SvgView, self).__init__(parent)

        self.renderer _ SvgView.Native
        self.svgItem _ None
        self.backgroundItem _ None
        self.outlineItem _ None
        self.image _ QImage()

        self.setScene(QGraphicsScene(self))
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Prepare background check-board pattern.
        tilePixmap _ QPixmap(64, 64)
        tilePixmap.fill(Qt.white)
        tilePainter _ QPainter(tilePixmap)
        color _ QColor(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        self.setBackgroundBrush(QBrush(tilePixmap))

    ___ drawBackground(self, p, rect):
        p.save()
        p.resetTransform()
        p.drawTiledPixmap(self.viewport().rect(),
                self.backgroundBrush().texture())
        p.restore()

    ___ openFile(self, svg_file):
        if not svg_file.exists
            return

        s _ self.scene()

        if self.backgroundItem:
            drawBackground _ self.backgroundItem.isVisible()
        else:
            drawBackground _ False

        if self.outlineItem:
            drawOutline _ self.outlineItem.isVisible()
        else:
            drawOutline _ True

        s.clear()
        self.resetTransform()

        self.svgItem _ QGraphicsSvgItem(svg_file.fileName())
        self.svgItem.setFlags(QGraphicsItem.ItemClipsToShape)
        self.svgItem.setCacheMode(QGraphicsItem.NoCache)
        self.svgItem.setZValue(0)

        self.backgroundItem _ QGraphicsRectItem(self.svgItem.boundingRect())
        self.backgroundItem.setBrush(Qt.white)
        self.backgroundItem.setPen(QPen(Qt.NoPen))
        self.backgroundItem.setVisible(drawBackground)
        self.backgroundItem.setZValue(-1)

        self.outlineItem _ QGraphicsRectItem(self.svgItem.boundingRect())
        outline _ QPen(Qt.black, 2, Qt.DashLine)
        outline.setCosmetic(True)
        self.outlineItem.setPen(outline)
        self.outlineItem.setBrush(QBrush(Qt.NoBrush))
        self.outlineItem.setVisible(drawOutline)
        self.outlineItem.setZValue(1)

        s.addItem(self.backgroundItem)
        s.addItem(self.svgItem)
        s.addItem(self.outlineItem)

        s.setSceneRect(self.outlineItem.boundingRect().adjusted(-10, -10, 10, 10))

    ___ setRenderer(self, renderer):
        self.renderer _ renderer

        if self.renderer == SvgView.OpenGL:
            if QGLFormat.hasOpenGL
                self.setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))
        else:
            self.setViewport(QWidget())

    ___ setHighQualityAntialiasing(self, highQualityAntialiasing):
        if QGLFormat.hasOpenGL
            self.setRenderHint(QPainter.HighQualityAntialiasing,
                    highQualityAntialiasing)

    ___ setViewBackground(self, enable):
        if self.backgroundItem:
            self.backgroundItem.setVisible(enable)

    ___ setViewOutline(self, enable):
        if self.outlineItem:
            self.outlineItem.setVisible(enable)

    ___ paintEvent(self, event):
        if self.renderer == SvgView.Image:
            if self.image.size() !_ self.viewport().size
                self.image _ QImage(self.viewport().size(),
                        QImage.Format_ARGB32_Premultiplied)

            imagePainter _ QPainter(self.image)
            QGraphicsView.render(self, imagePainter)
            imagePainter.end()

            p _ QPainter(self.viewport())
            p.drawImage(0, 0, self.image)
        else:
            super(SvgView, self).paintEvent(event)

    ___ wheelEvent(self, event):
        factor _ pow(1.2, event.delta() / 240.0)
        self.scale(factor, factor)
        event.accept()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)

    window _ MainWindow()
    if len(sys.argv) == 2:
        window.openFile(sys.argv[1])
    else:
        window.openFile(':/files/bubbles.svg')
    window.s..
    sys.exit(app.exec_())
