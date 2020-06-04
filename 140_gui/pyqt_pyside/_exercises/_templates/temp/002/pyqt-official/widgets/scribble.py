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


____ ?.?C.. ______ ?D.., QPoint, QRect, ?S.., __
____ ?.?G.. ______ QImage, QImageWriter, QPainter, ?P.., qRgb
____ ?.?W.. ______ (?A.., ?A.., QColorDialog, ?FD..,
        QInputDialog, ?MW.., ?M.., ?MB.., ?W..)
____ ?.?PS.. ______ QPrintDialog, QPrinter


c_ ScribbleArea(?W..):
    ___  -   parent_None):
        s__(ScribbleArea, self). - (parent)

        setAttribute(__.WA_StaticContents)
        modified _ F..
        scribbling _ F..
        myPenWidth _ 1
        myPenColor _ __.blue
        image _ QImage()
        lastPoint _ QPoint()

    ___ openImage  fileName):
        loadedImage _ QImage()
        __ no. loadedImage.load(fileName):
            r_ F..

        newSize _ loadedImage.size().expandedTo(size())
        resizeImage(loadedImage, newSize)
        image _ loadedImage
        modified _ F..
        update()
        r_ T..

    ___ saveImage  fileName, fileFormat):
        visibleImage _ image
        resizeImage(visibleImage, size())

        __ visibleImage.save(fileName, fileFormat):
            modified _ F..
            r_ T..
        ____
            r_ F..

    ___ setPenColor  newColor):
        myPenColor _ newColor

    ___ setPenWidth  newWidth):
        myPenWidth _ newWidth

    ___ clearImage
        image.fill(qRgb(255, 255, 255))
        modified _ T..
        update()

    ___ mousePressEvent  event):
        __ event.button() __ __.LeftButton:
            lastPoint _ event.pos()
            scribbling _ T..

    ___ mouseMoveEvent  event):
        __ (event.buttons() & __.LeftButton) and scribbling:
            drawLineTo(event.pos())

    ___ mouseReleaseEvent  event):
        __ event.button() __ __.LeftButton and scribbling:
            drawLineTo(event.pos())
            scribbling _ F..

    ___ paintEvent  event):
        painter _ QPainter
        dirtyRect _ event.rect()
        painter.drawImage(dirtyRect, image, dirtyRect)

    ___ resizeEvent  event):
        __ width() > image.width() or height() > image.height
            newWidth _ max(width() + 128, image.width())
            newHeight _ max(height() + 128, image.height())
            resizeImage(image, ?S..(newWidth, newHeight))
            update()

        s__(ScribbleArea, self).resizeEvent(event)

    ___ drawLineTo  endPoint):
        painter _ QPainter(image)
        painter.sP..(?P..(myPenColor, myPenWidth, __.SolidLine,
                __.RoundCap, __.RoundJoin))
        painter.drawLine(lastPoint, endPoint)
        modified _ T..

        rad _ myPenWidth / 2 + 2
        update(QRect(lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        lastPoint _ QPoint(endPoint)

    ___ resizeImage  image, newSize):
        __ image.size() __ newSize:
            r_

        newImage _ QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter _ QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        image _ newImage

    ___ print_
        printer _ QPrinter(QPrinter.HighResolution)

        printDialog _ QPrintDialog(printer, self)
        __ printDialog.e.. __ QPrintDialog.Accepted:
            painter _ QPainter(printer)
            rect _ painter.viewport()
            size _ image.size()
            size.scale(rect.size(), __.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(image.rect())
            painter.drawImage(0, 0, image)
            painter.end()

    ___ iM..
        r_ modified

    ___ penColor
        r_ myPenColor

    ___ penWidth
        r_ myPenWidth


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        saveAsActs _   # list

        scribbleArea _ ScribbleArea()
        sCW..(scribbleArea)

        createActions()
        createMenus()

        sWT..("Scribble")
        r..(500, 500)

    ___ closeEvent  event):
        __ maybeSave
            event.accept()
        ____
            event.ignore()

    ___ o..
        __ maybeSave
            fileName, _ _ ?FD...gOFN..  "Open File",
                    ?D...currentPath())
            __ fileName:
                scribbleArea.openImage(fileName)

    ___ save
        action _ sender()
        fileFormat _ action.data()
        saveFile(fileFormat)

    ___ penColor
        newColor _ QColorDialog.getColor(scribbleArea.penColor())
        __ newColor.isValid
            scribbleArea.setPenColor(newColor)

    ___ penWidth
        newWidth, ok _ QInputDialog.getInt  "Scribble",
                "Select pen width:", scribbleArea.penWidth(), 1, 50, 1)
        __ ok:
            scribbleArea.setPenWidth(newWidth)

    ___ about
        ?MB...about  "About Scribble",
                "<p>The <b>Scribble</b> example shows how to use "
                "QMainWindow as the base widget for an application, and how "
                "to reimplement some of QWidget's event handlers to receive "
                "the events generated for the application's widgets:</p>"
                "<p> We reimplement the mouse event handlers to facilitate "
                "drawing, the paint event handler to update the application "
                "and the resize event handler to optimize the application's "
                "appearance. In addition we reimplement the close event "
                "handler to intercept the close events before terminating "
                "the application.</p>"
                "<p> The example also demonstrates how to use QPainter to "
                "draw an image in real time, as well as to repaint "
                "widgets.</p>")

    ___ createActions
        openAct _ ?A..("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.o..)

        ___ f.. __ QImageWriter.supportedImageFormats
            f.. _ st.(f..)

            t__ _ f...upper() + "..."

            action _ ?A..(t__, self, triggered_self.save)
            action.setData(f..)
            saveAsActs.ap..(action)

        printAct _ ?A..("&Print...", self,
                triggered_self.scribbleArea.print_)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        penColorAct _ ?A..("&Pen Color...", self,
                triggered_self.penColor)

        penWidthAct _ ?A..("Pen &Width...", self,
                triggered_self.penWidth)

        clearScreenAct _ ?A..("&Clear Screen", self, shortcut_"Ctrl+L",
                triggered_self.scribbleArea.clearImage)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        saveAsMenu _ ?M..("&Save As", self)
        ___ action __ saveAsActs:
            saveAsMenu.aA..(action)

        fileMenu _ ?M..("&File", self)
        fileMenu.aA..(openAct)
        fileMenu.aM..(saveAsMenu)
        fileMenu.aA..(printAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        optionMenu _ ?M..("&Options", self)
        optionMenu.aA..(penColorAct)
        optionMenu.aA..(penWidthAct)
        optionMenu.aS..)
        optionMenu.aA..(clearScreenAct)

        helpMenu _ ?M..("&Help", self)
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

        mB.. .aM..(fileMenu)
        mB.. .aM..(optionMenu)
        mB.. .aM..(helpMenu)

    ___ maybeSave
        __ scribbleArea.iM..
            ret _ ?MB...w..  "Scribble",
                        "The image has been modified.\n"
                        "Do you want to save your changes?",
                        ?MB...Save | ?MB...Discard |
                        ?MB...Cancel)
            __ ret __ ?MB...Save:
                r_ saveFile('png')
            ____ ret __ ?MB...Cancel:
                r_ F..

        r_ T..

    ___ saveFile  fileFormat):
        initialPath _ ?D...currentPath() + '/untitled.' + fileFormat

        fileName, _ _ ?FD...getSaveFileName  "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        __ fileName:
            r_ scribbleArea.saveImage(fileName, fileFormat)

        r_ F..


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..
