#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited.
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


____ ?.?C.. ______ (?ATM.., ?D.., QModelIndex, QRect,
        QRectF, ?S.., __)
____ ?.?G.. ______ ?B.., qGray, QImage, QPainter
____ ?.?PS.. ______ QPrintDialog, QPrinter
____ ?.?W.. ______ (QAbstractItemDelegate, ?A.., ?D..,
        ?FD.., ?HBL.., ?L.., ?MW.., ?MB.., ?M..,
        QProgressDialog, SB.., ?S.., QStyleOptionViewItem, QTableView,
        ?VBL.., ?W..)

______ pixelator_rc


ItemSize _ 256


c_ PixelDelegate(QAbstractItemDelegate):
    ___  -   parent_None):
        s__(PixelDelegate, self). - (parent)

        pixelSize _ 12

    ___ paint  painter, option, index):
        __ option.state & ?S...State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        size _ min(option.rect.width(), option.rect.height())
        brightness _ index.model().data(index, __.DR..)
        radius _ (size/2.0) - (brightness/255.0 * size/2.0)
        __ radius __ 0.0:
            r_

        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.sP..(__.NoPen)

        __ option.state & ?S...State_Selected:
            painter.sB..(option.palette.highlightedText())
        ____
            painter.sB..(?B..(__.black))

        painter.drawEllipse(QRectF(
                            option.rect.x() + option.rect.width()/2 - radius,
                            option.rect.y() + option.rect.height()/2 - radius,
                            2*radius, 2*radius))

        painter.restore()

    ___ sH..  option, index):
        r_ ?S..(pixelSize, pixelSize)

    ___ setPixelSize  size):
        pixelSize _ size


c_ ImageModel ?ATM..
    ___  -   parent_None):
        s__(ImageModel, self). - (parent)

        modelImage _ QImage()

    ___ setImage  image):
        beginResetModel()
        modelImage _ QImage(image)
        endResetModel()

    ___ rowCount  parent):
        r_ modelImage.height()

    ___ columnCount  parent):
        r_ modelImage.width()

    ___ data  index, role):
        __ no. index.iV.. or role !_ __.DR..:
            r_ N..

        r_ qGray(modelImage.pixel(index.column(), index.row()))

    ___ hD..  section, orientation, role):
        __ role __ __.SizeHintRole:
            r_ ?S..(1, 1)

        r_ N..


c_ MainWindow ?MW..
    ___  -
        s__(MainWindow, self). - ()

        currentPath _ ?D...homePath()
        model _ ImageModel

        centralWidget _ ?W..

        view _ ?TV..
        view.setShowGrid F..
        view.hH.. .hide()
        view.vH.. .hide()
        view.hH.. .setMinimumSectionSize(1)
        view.vH.. .setMinimumSectionSize(1)
        view.sM..(model)

        delegate _ PixelDelegate
        view.sID..(delegate)

        pixelSizeLabel _ ?L..("Pixel size:")
        pixelSizeSpinBox _ SB..()
        pixelSizeSpinBox.setMinimum(4)
        pixelSizeSpinBox.sM..(32)
        pixelSizeSpinBox.sV..(12)

        fileMenu _ ?M..("&File", self)
        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")

        printAction _ fileMenu.aA..("&Print...")
        printAction.sE.. F..
        printAction.sS..("Ctrl+P")

        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..("Ctrl+Q")

        helpMenu _ ?M..("&Help", self)
        aboutAction _ helpMenu.aA..("&About")

        mB.. .aM..(fileMenu)
        mB.. .aS..)
        mB.. .aM..(helpMenu)

        openAction.t__.c..(chooseImage)
        printAction.t__.c..(printImage)
        quitAction.t__.c..(?A...i.. .quit)
        aboutAction.t__.c..(showAboutBox)
        pixelSizeSpinBox.valueChanged.c..(delegate.setPixelSize)
        pixelSizeSpinBox.valueChanged.c..(updateView)

        controlsLayout _ ?HBL..
        controlsLayout.aW..(pixelSizeLabel)
        controlsLayout.aW..(pixelSizeSpinBox)
        controlsLayout.addStretch(1)

        mainLayout _ ?VBL..
        mainLayout.aW..(view)
        mainLayout.aL..(controlsLayout)
        centralWidget.sL..(mainLayout)

        sCW..(centralWidget)

        sWT..("Pixelator")
        r..(640, 480)

    ___ chooseImage 
        fileName, _ _ ?FD...gOFN..  "Choose an Image",
                currentPath, '*')

        __ fileName:
            openImage(fileName)

    ___ openImage  fileName):
        image _ QImage()

        __ image.load(fileName):
            model.setImage(image)

            __ no. fileName.s_w_(':/'):
                currentPath _ fileName
                sWT..("%s - Pixelator" % currentPath)

            printAction.sE..( st.
            updateView()

    ___ printImage 
        __ model.rowCount(QModelIndex()) * model.columnCount(QModelIndex()) > 90000:
            answer _ ?MB...q..  "Large Image Size",
                    "The printed image may be very large. Are you sure that "
                    "you want to print it?",
                    ?MB...Yes | ?MB...No)
            __ answer __ ?MB...No:
                r_

        printer _ QPrinter(QPrinter.HighResolution)

        dlg _ QPrintDialog(printer, self)
        dlg.sWT..("Print Image")

        __ dlg.e.. !_ ?D...Accepted:
            r_

        painter _ QPainter()
        painter.begin(printer)

        rows _ model.rowCount(QModelIndex())
        columns _ model.columnCount(QModelIndex())
        sourceWidth _ (columns+1) * ItemSize
        sourceHeight _ (rows+1) * ItemSize

        painter.save()

        xscale _ printer.pageRect().width() / fl..(sourceWidth)
        yscale _ printer.pageRect().height() / fl..(sourceHeight)
        scale _ min(xscale, yscale)

        painter.translate(printer.paperRect().x()+printer.pageRect().width()/2,
                          printer.paperRect().y()+printer.pageRect().height()/2)
        painter.scale(scale, scale)
        painter.translate(-sourceWidth/2, -sourceHeight/2)

        option _ QStyleOptionViewItem()
        parent _ QModelIndex()

        progress _ QProgressDialog("Printing...", "Cancel", 0, rows, self)
        progress.setWindowModality(__.ApplicationModal)
        y _ ItemSize / 2.0

        ___ row __ ra..(rows):
            progress.sV..(row)
            ?A...processEvents()
            __ progress.wasCanceled
                break

            x _ ItemSize / 2.0

            ___ column __ ra..(columns):
                option.rect _ QRect(x, y, ItemSize, ItemSize)
                view.itemDelegate().paint(painter, option,
                        model.index(row, column, parent))
                x +_ ItemSize

            y +_ ItemSize

        progress.sV..(rows)

        painter.restore()
        painter.end()

        __ progress.wasCanceled
            ?MB...i..  "Printing canceled",
                    "The printing process was canceled.", ?MB...Cancel)

    ___ showAboutBox 
        ?MB...about  "About the Pixelator example",
                "This example demonstrates how a standard view and a custom\n"
                "delegate can be used to produce a specialized "
                "representation\nof data in a simple custom model.")

    ___ updateView 
        view.rCTC..
        view.rRTC..)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    window.openImage(':/images/qt.png')
    ___.e.. ?.e..
