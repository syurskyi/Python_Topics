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


____ ?.QtCore ______ QDir, QPoint, QRect, QSize, Qt
____ ?.QtGui ______ QImage, QImageWriter, QPainter, QPen, qRgb
____ ?.?W.. ______ (QAction, ?A.., QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter


class ScribbleArea(QWidget):
    ___ __init__(self, parent_None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.modified _ False
        self.scribbling _ False
        self.myPenWidth _ 1
        self.myPenColor _ Qt.blue
        self.image _ QImage()
        self.lastPoint _ QPoint()

    ___ openImage(self, fileName):
        loadedImage _ QImage()
        if not loadedImage.load(fileName):
            return False

        newSize _ loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image _ loadedImage
        self.modified _ False
        self.update()
        return True

    ___ saveImage(self, fileName, fileFormat):
        visibleImage _ self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified _ False
            return True
        else:
            return False

    ___ setPenColor(self, newColor):
        self.myPenColor _ newColor

    ___ setPenWidth(self, newWidth):
        self.myPenWidth _ newWidth

    ___ clearImage(self):
        self.image.fill(qRgb(255, 255, 255))
        self.modified _ True
        self.update()

    ___ mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint _ event.pos()
            self.scribbling _ True

    ___ mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    ___ mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling _ False

    ___ paintEvent(self, event):
        painter _ QPainter(self)
        dirtyRect _ event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    ___ resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height
            newWidth _ max(self.width() + 128, self.image.width())
            newHeight _ max(self.height() + 128, self.image.height())
            self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    ___ drawLineTo(self, endPoint):
        painter _ QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified _ True

        rad _ self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint _ QPoint(endPoint)

    ___ resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage _ QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter _ QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        self.image _ newImage

    ___ print_(self):
        printer _ QPrinter(QPrinter.HighResolution)

        printDialog _ QPrintDialog(printer, self)
        if printDialog.e.. == QPrintDialog.Accepted:
            painter _ QPainter(printer)
            rect _ painter.viewport()
            size _ self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    ___ isModified(self):
        return self.modified

    ___ penColor(self):
        return self.myPenColor

    ___ penWidth(self):
        return self.myPenWidth


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs _ []

        self.scribbleArea _ ScribbleArea()
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Scribble")
        self.resize(500, 500)

    ___ closeEvent(self, event):
        if self.maybeSave
            event.accept()
        else:
            event.ignore()

    ___ open(self):
        if self.maybeSave
            fileName, _ _ QFileDialog.getOpenFileName(self, "Open File",
                    QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    ___ save(self):
        action _ self.sender()
        fileFormat _ action.data()
        self.saveFile(fileFormat)

    ___ penColor(self):
        newColor _ QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid
            self.scribbleArea.setPenColor(newColor)

    ___ penWidth(self):
        newWidth, ok _ QInputDialog.getInt(self, "Scribble",
                "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    ___ about(self):
        QMessageBox.about(self, "About Scribble",
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

    ___ createActions(self):
        self.openAct _ QAction("&Open...", self, shortcut_"Ctrl+O",
                triggered_self.open)

        for format in QImageWriter.supportedImageFormats
            format _ str(format)

            text _ format.upper() + "..."

            action _ QAction(text, self, triggered_self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct _ QAction("&Print...", self,
                triggered_self.scribbleArea.print_)

        self.exitAct _ QAction("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.penColorAct _ QAction("&Pen Color...", self,
                triggered_self.penColor)

        self.penWidthAct _ QAction("Pen &Width...", self,
                triggered_self.penWidth)

        self.clearScreenAct _ QAction("&Clear Screen", self, shortcut_"Ctrl+L",
                triggered_self.scribbleArea.clearImage)

        self.aboutAct _ QAction("&About", self, triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.saveAsMenu _ QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu _ QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu _ QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu _ QMenu("&Help", self)
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

    ___ maybeSave(self):
        if self.scribbleArea.isModified
            ret _ QMessageBox.warning(self, "Scribble",
                        "The image has been modified.\n"
                        "Do you want to save your changes?",
                        QMessageBox.Save | QMessageBox.Discard |
                        QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QMessageBox.Cancel:
                return False

        return True

    ___ saveFile(self, fileFormat):
        initialPath _ QDir.currentPath() + '/untitled.' + fileFormat

        fileName, _ _ QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())
