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


____ ?.?C.. ______ QDir, __
____ ?.?G.. ______ QImage, QPainter, ?P.., QPixmap
____ ?.?W.. ______ (?A.., ?A.., ?FD.., QLabel,
        QMainWindow, QMenu, ?MB.., QScrollArea, QSizePolicy)
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter


c_ ImageViewer ?MW..
    ___ __init__(self):
        super(ImageViewer, self).__init__()

        self.printer _ QPrinter()
        self.scaleFactor _ 0.0

        self.imageLabel _ QLabel()
        self.imageLabel.setBackgroundRole(?P...Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea _ QScrollArea()
        self.scrollArea.setBackgroundRole(?P...Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.sCW..(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Image Viewer")
        self.resize(500, 400)

    ___ o..(self):
        fileName, _ _ ?FD...gOFN..  "Open File",
                QDir.currentPath())
        __ fileName:
            image _ QImage(fileName)
            __ image.isNull
                ?MB...information  "Image Viewer",
                        "Cannot load %s." % fileName)
                r_

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor _ 1.0

            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            __ no. self.fitToWindowAct.isChecked
                self.imageLabel.adjustSize()

    ___ print_(self):
        dialog _ QPrintDialog(self.printer, self)
        __ dialog.exec_
            painter _ QPainter(self.printer)
            rect _ painter.viewport()
            size _ self.imageLabel.pixmap().size()
            size.scale(rect.size(), __.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    ___ zoomIn(self):
        self.scaleImage(1.25)

    ___ zoomOut(self):
        self.scaleImage(0.8)

    ___ normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor _ 1.0

    ___ fitToWindow(self):
        fitToWindow _ self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        __ no. fitToWindow:
            self.normalSize()

        self.updateActions()

    ___ about(self):
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

    ___ createActions(self):
        self.openAct _ ?A..("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.o..)

        self.printAct _ ?A..("&Print...", self, shortcut_"Ctrl+P",
                enabled_False, triggered_self.print_)

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.zoomInAct _ ?A..("Zoom &In (25%)", self, shortcut_"Ctrl++",
                enabled_False, triggered_self.zoomIn)

        self.zoomOutAct _ ?A..("Zoom &Out (25%)", self, shortcut_"Ctrl+-",
                enabled_False, triggered_self.zoomOut)

        self.normalSizeAct _ ?A..("&Normal Size", self, shortcut_"Ctrl+S",
                enabled_False, triggered_self.normalSize)

        self.fitToWindowAct _ ?A..("&Fit to Window", self, enabled_False,
                checkable_True, shortcut_"Ctrl+F", triggered_self.fitToWindow)

        self.aboutAct _ ?A..("&About", self, triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ QMenu("&File", self)
        self.fileMenu.aA..(self.openAct)
        self.fileMenu.aA..(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)

        self.viewMenu _ QMenu("&View", self)
        self.viewMenu.aA..(self.zoomInAct)
        self.viewMenu.aA..(self.zoomOutAct)
        self.viewMenu.aA..(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.aA..(self.fitToWindowAct)

        self.helpMenu _ QMenu("&Help", self)
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

        self.mB.. .aM..(self.fileMenu)
        self.mB.. .aM..(self.viewMenu)
        self.mB.. .aM..(self.helpMenu)

    ___ updateActions(self):
        self.zoomInAct.setEnabled(no. self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(no. self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(no. self.fitToWindowAct.isChecked())

    ___ scaleImage  factor):
        self.scaleFactor *_ factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    ___ adjustScrollBar  scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    imageViewer _ ImageViewer()
    imageViewer.s..
    sys.exit(app.exec_())
