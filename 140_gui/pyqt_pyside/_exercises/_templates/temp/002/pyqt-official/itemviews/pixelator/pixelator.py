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


____ ?.QtCore ______ (QAbstractTableModel, QDir, QModelIndex, QRect,
        QRectF, QSize, Qt)
____ ?.QtGui ______ QBrush, qGray, QImage, QPainter
____ ?.QtPrintSupport ______ QPrintDialog, QPrinter
____ ?.?W.. ______ (QAbstractItemDelegate, QApplication, QDialog,
        QFileDialog, QHBoxLayout, QLabel, QMainWindow, QMessageBox, QMenu,
        QProgressDialog, QSpinBox, QStyle, QStyleOptionViewItem, QTableView,
        QVBoxLayout, QWidget)

______ pixelator_rc


ItemSize _ 256


class PixelDelegate(QAbstractItemDelegate):
    ___ __init__(self, parent_None):
        super(PixelDelegate, self).__init__(parent)

        self.pixelSize _ 12

    ___ paint(self, painter, option, index):
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        size _ min(option.rect.width(), option.rect.height())
        brightness _ index.model().data(index, Qt.DisplayRole)
        radius _ (size/2.0) - (brightness/255.0 * size/2.0)
        if radius == 0.0:
            return

        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        if option.state & QStyle.State_Selected:
            painter.setBrush(option.palette.highlightedText())
        else:
            painter.setBrush(QBrush(Qt.black))

        painter.drawEllipse(QRectF(
                            option.rect.x() + option.rect.width()/2 - radius,
                            option.rect.y() + option.rect.height()/2 - radius,
                            2*radius, 2*radius))

        painter.restore()

    ___ sizeHint(self, option, index):
        return QSize(self.pixelSize, self.pixelSize)

    ___ setPixelSize(self, size):
        self.pixelSize _ size


class ImageModel(QAbstractTableModel):
    ___ __init__(self, parent_None):
        super(ImageModel, self).__init__(parent)

        self.modelImage _ QImage()

    ___ setImage(self, image):
        self.beginResetModel()
        self.modelImage _ QImage(image)
        self.endResetModel()

    ___ rowCount(self, parent):
        return self.modelImage.height()

    ___ columnCount(self, parent):
        return self.modelImage.width()

    ___ data(self, index, role):
        if not index.isValid() or role !_ Qt.DisplayRole:
            return None

        return qGray(self.modelImage.pixel(index.column(), index.row()))

    ___ headerData(self, section, orientation, role):
        if role == Qt.SizeHintRole:
            return QSize(1, 1)

        return None


class MainWindow(QMainWindow):
    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.currentPath _ QDir.homePath()
        self.model _ ImageModel(self)

        centralWidget _ QWidget()

        self.view _ QTableView()
        self.view.setShowGrid(False)
        self.view.horizontalHeader().hide()
        self.view.verticalHeader().hide()
        self.view.horizontalHeader().setMinimumSectionSize(1)
        self.view.verticalHeader().setMinimumSectionSize(1)
        self.view.setModel(self.model)

        delegate _ PixelDelegate(self)
        self.view.setItemDelegate(delegate)

        pixelSizeLabel _ QLabel("Pixel size:")
        pixelSizeSpinBox _ QSpinBox()
        pixelSizeSpinBox.setMinimum(4)
        pixelSizeSpinBox.setMaximum(32)
        pixelSizeSpinBox.setValue(12)

        fileMenu _ QMenu("&File", self)
        openAction _ fileMenu.addAction("&Open...")
        openAction.setShortcut("Ctrl+O")

        self.printAction _ fileMenu.addAction("&Print...")
        self.printAction.setEnabled(False)
        self.printAction.setShortcut("Ctrl+P")

        quitAction _ fileMenu.addAction("E&xit")
        quitAction.setShortcut("Ctrl+Q")

        helpMenu _ QMenu("&Help", self)
        aboutAction _ helpMenu.addAction("&About")

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(helpMenu)

        openAction.triggered.c..(self.chooseImage)
        self.printAction.triggered.c..(self.printImage)
        quitAction.triggered.c..(QApplication.instance().quit)
        aboutAction.triggered.c..(self.showAboutBox)
        pixelSizeSpinBox.valueChanged.c..(delegate.setPixelSize)
        pixelSizeSpinBox.valueChanged.c..(self.updateView)

        controlsLayout _ QHBoxLayout()
        controlsLayout.addWidget(pixelSizeLabel)
        controlsLayout.addWidget(pixelSizeSpinBox)
        controlsLayout.addStretch(1)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.view)
        mainLayout.addLayout(controlsLayout)
        centralWidget.setLayout(mainLayout)

        self.setCentralWidget(centralWidget)

        self.setWindowTitle("Pixelator")
        self.resize(640, 480)

    ___ chooseImage(self):
        fileName, _ _ QFileDialog.getOpenFileName(self, "Choose an Image",
                self.currentPath, '*')

        if fileName:
            self.openImage(fileName)

    ___ openImage(self, fileName):
        image _ QImage()

        if image.load(fileName):
            self.model.setImage(image)

            if not fileName.startswith(':/'):
                self.currentPath _ fileName
                self.setWindowTitle("%s - Pixelator" % self.currentPath)

            self.printAction.setEnabled(True)
            self.updateView()

    ___ printImage(self):
        if self.model.rowCount(QModelIndex()) * self.model.columnCount(QModelIndex()) > 90000:
            answer _ QMessageBox.question(self, "Large Image Size",
                    "The printed image may be very large. Are you sure that "
                    "you want to print it?",
                    QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.No:
                return

        printer _ QPrinter(QPrinter.HighResolution)

        dlg _ QPrintDialog(printer, self)
        dlg.setWindowTitle("Print Image")

        if dlg.e.. !_ QDialog.Accepted:
            return

        painter _ QPainter()
        painter.begin(printer)

        rows _ self.model.rowCount(QModelIndex())
        columns _ self.model.columnCount(QModelIndex())
        sourceWidth _ (columns+1) * ItemSize
        sourceHeight _ (rows+1) * ItemSize

        painter.save()

        xscale _ printer.pageRect().width() / float(sourceWidth)
        yscale _ printer.pageRect().height() / float(sourceHeight)
        scale _ min(xscale, yscale)

        painter.translate(printer.paperRect().x()+printer.pageRect().width()/2,
                          printer.paperRect().y()+printer.pageRect().height()/2)
        painter.scale(scale, scale)
        painter.translate(-sourceWidth/2, -sourceHeight/2)

        option _ QStyleOptionViewItem()
        parent _ QModelIndex()

        progress _ QProgressDialog("Printing...", "Cancel", 0, rows, self)
        progress.setWindowModality(Qt.ApplicationModal)
        y _ ItemSize / 2.0

        for row in range(rows):
            progress.setValue(row)
            QApplication.processEvents()
            if progress.wasCanceled
                break

            x _ ItemSize / 2.0

            for column in range(columns):
                option.rect _ QRect(x, y, ItemSize, ItemSize)
                self.view.itemDelegate().paint(painter, option,
                        self.model.index(row, column, parent))
                x +_ ItemSize

            y +_ ItemSize

        progress.setValue(rows)

        painter.restore()
        painter.end()

        if progress.wasCanceled
            QMessageBox.information(self, "Printing canceled",
                    "The printing process was canceled.", QMessageBox.Cancel)

    ___ showAboutBox(self):
        QMessageBox.about(self, "About the Pixelator example",
                "This example demonstrates how a standard view and a custom\n"
                "delegate can be used to produce a specialized "
                "representation\nof data in a simple custom model.")

    ___ updateView(self):
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    window _ MainWindow()
    window.s..
    window.openImage(':/images/qt.png')
    sys.exit(app.exec_())
