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


____ ?.?C.. ______ ?D.., __
____ ?.?G.. ______ QImage, QPainter, ?P.., ?P..
____ ?.?W.. ______ (?A.., ?A.., ?FD.., ?L..,
        ?MW.., ?M.., ?MB.., QScrollArea, ?SP..)
____ ?.?PS.. ______ QPrintDialog, QPrinter


c_ ImageViewer ?MW..
    ___  -
        s__(ImageViewer, self). - ()

        printer _ QPrinter()
        scaleFactor _ 0.0

        imageLabel _ ?L..
        imageLabel.setBackgroundRole(?P...Base)
        imageLabel.sSP..(?SP...Ignored, ?SP...Ignored)
        imageLabel.setScaledContents( st.

        scrollArea _ QScrollArea()
        scrollArea.setBackgroundRole(?P...Dark)
        scrollArea.setWidget(imageLabel)
        sCW..(scrollArea)

        createActions()
        createMenus()

        sWT..("Image Viewer")
        r..(500, 400)

    ___ o..
        fileName, _ _ ?FD...gOFN..  "Open File",
                ?D...currentPath())
        __ fileName:
            image _ QImage(fileName)
            __ image.isNull
                ?MB...i..  "Image Viewer",
                        "Cannot load %s." % fileName)
                r_

            imageLabel.sP..(?P...fromImage(image))
            scaleFactor _ 1.0

            printAct.sE..( st.
            fitToWindowAct.sE..( st.
            updateActions()

            __ no. fitToWindowAct.isChecked
                imageLabel.adjustSize()

    ___ print_
        dialog _ QPrintDialog(printer, self)
        __ dialog.e..
            painter _ QPainter(printer)
            rect _ painter.viewport()
            size _ imageLabel.pixmap().size()
            size.scale(rect.size(), __.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, imageLabel.pixmap())

    ___ zoomIn
        scaleImage(1.25)

    ___ zoomOut
        scaleImage(0.8)

    ___ normalSize
        imageLabel.adjustSize()
        scaleFactor _ 1.0

    ___ fitToWindow
        fitToWindow _ fitToWindowAct.isChecked()
        scrollArea.setWidgetResizable(fitToWindow)
        __ no. fitToWindow:
            normalSize()

        updateActions()

    ___ about
        ?MB...about  "About Image Viewer",
                "<p>The <b>Image Viewer</b> example shows how to combine "
                "QLabel and QScrollArea to display an image. QLabel is "
                "typically used for displaying text, but it can also display "
                "an image. QScrollArea provides a scrolling view around "
                "another widget. If the child widget exceeds the size of the "
                "frame, QScrollArea automatically provides scroll bars.</p>"
                "<p>The example demonstrates how QLabel's ability to scale "
                "its contents (QLabel.scaledContents), and QScrollArea's "
                "ability to automatically resize its contents "
                "(QScrollArea.widgetResizable), can be used to implement "
                "zooming and scaling features.</p>"
                "<p>In addition the example shows how to use QPainter to "
                "print an image.</p>")

    ___ createActions
        openAct _ ?A..("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.o..)

        printAct _ ?A..("&Print...", self, shortcut_"Ctrl+P",
                enabled_False, triggered_self.print_)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        zoomInAct _ ?A..("Zoom &In (25%)", self, shortcut_"Ctrl++",
                enabled_False, triggered_self.zoomIn)

        zoomOutAct _ ?A..("Zoom &Out (25%)", self, shortcut_"Ctrl+-",
                enabled_False, triggered_self.zoomOut)

        normalSizeAct _ ?A..("&Normal Size", self, shortcut_"Ctrl+S",
                enabled_False, triggered_self.normalSize)

        fitToWindowAct _ ?A..("&Fit to Window", self, enabled_False,
                checkable_True, shortcut_"Ctrl+F", triggered_self.fitToWindow)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ ?M..("&File", self)
        fileMenu.aA..(openAct)
        fileMenu.aA..(printAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        viewMenu _ ?M..("&View", self)
        viewMenu.aA..(zoomInAct)
        viewMenu.aA..(zoomOutAct)
        viewMenu.aA..(normalSizeAct)
        viewMenu.aS..)
        viewMenu.aA..(fitToWindowAct)

        helpMenu _ ?M..("&Help", self)
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

        mB.. .aM..(fileMenu)
        mB.. .aM..(viewMenu)
        mB.. .aM..(helpMenu)

    ___ updateActions
        zoomInAct.sE..(no. fitToWindowAct.isChecked())
        zoomOutAct.sE..(no. fitToWindowAct.isChecked())
        normalSizeAct.sE..(no. fitToWindowAct.isChecked())

    ___ scaleImage  factor):
        scaleFactor *_ factor
        imageLabel.r..(scaleFactor * imageLabel.pixmap().size())

        adjustScrollBar(scrollArea.horizontalScrollBar(), factor)
        adjustScrollBar(scrollArea.verticalScrollBar(), factor)

        zoomInAct.sE..(scaleFactor < 3.0)
        zoomOutAct.sE..(scaleFactor > 0.333)

    ___ adjustScrollBar  scrollBar, factor):
        scrollBar.sV..(in.(factor * scrollBar.v..
                                + ((factor - 1) * scrollBar.pageStep()/2)))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    imageViewer _ ImageViewer()
    imageViewer.s..
    ___.e.. ?.e..
