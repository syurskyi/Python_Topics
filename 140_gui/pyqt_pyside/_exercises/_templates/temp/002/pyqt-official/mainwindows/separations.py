#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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


____ ?.?C.. ______ (pyqtSignal, QBuffer, QByteArray, QFileInfo,
        QIODevice, QMimeData, QPoint, QSize, __)
____ ?.?G.. ______ (qBlue, ?C.., QDrag, qGreen, QImage, ?KS..,
        ?P.., QPixmap, qRed)
____ ?.?W.. ______ (?A.., QColorDialog, ?FD.., QFrame,
        QGridLayout, QLabel, QLayout, QMainWindow, QMenu, ?MB..,
        ?PB.., QVBoxLayout)


c_ FinalWidget(QFrame):

    ___ __init__  parent, name, labelSize):
        super(FinalWidget, self).__init__(parent)

        self.dragStartPosition _ QPoint()

        self.hasImage _ False
        self.imageLabel _ QLabel()
        self.imageLabel.setFrameShadow(QFrame.Sunken)
        self.imageLabel.setFrameShape(QFrame.StyledPanel)
        self.imageLabel.setMinimumSize(labelSize)
        self.nameLabel _ QLabel(name)

        layout _ ?VBL..
        layout.aW..(self.imageLabel, 1)
        layout.aW..(self.nameLabel, 0)
        self.sL..(layout)

    ___ mouseMoveEvent  event):
        """ If the mouse moves far enough when the left mouse button is held
            down, start a drag and drop operation.
        """
        __ no. event.buttons() & __.LeftButton:
            r_

        __ (event.pos() - self.dragStartPosition).manhattanLength() \
             < ?A...startDragDistance
            r_

        __ no. self.hasImage:
            r_

        drag _ QDrag(self)
        mimeData _ QMimeData()

        output _ QByteArray()
        outputBuffer _ QBuffer(output)
        outputBuffer.o..(QIODevice.WriteOnly)
        self.imageLabel.pixmap().toImage().save(outputBuffer, 'PNG')
        outputBuffer.close()
        mimeData.setData('image/png', output)

        drag.setMimeData(mimeData)
        drag.setPixmap(self.imageLabel.pixmap().scaled(64, 64, __.KeepAspectRatio))
        drag.setHotSpot(QPoint(drag.pixmap().width() / 2,
                                      drag.pixmap().height()))
        drag.start()

    ___ mousePressEvent  event):
        """ Check for left mouse button presses in order to enable drag and
            drop.
        """
        __ event.button() == __.LeftButton:
            self.dragStartPosition _ event.pos()

    ___ pixmap(self):
        r_ self.imageLabel.pixmap()

    ___ setPixmap  pixmap):
        self.imageLabel.setPixmap(pixmap)
        self.hasImage _ True


c_ ScreenWidget(QFrame):
    # Separation.
    Cyan, Magenta, Yellow _ range(3)

    convertMap _ {
        Cyan: qRed,
        Magenta: qGreen,
        Yellow: qBlue,
    }

    imageChanged _ pyqtSignal()

    ___ __init__  parent, initialColor, name, mask, labelSize):
        """ Initializes the paint color, the mask color (cyan, magenta, or
        yellow), connects the color selector and invert checkbox to functions,
        and creates a two-by-two grid layout.
        """
        super(ScreenWidget, self).__init__(parent)

        self.originalImage _ QImage()
        self.newImage _ QImage()

        self.paintColor _ initialColor
        self.maskColor _ mask
        self.inverted _ False

        self.imageLabel _ QLabel()
        self.imageLabel.setFrameShadow(QFrame.Sunken)
        self.imageLabel.setFrameShape(QFrame.StyledPanel)
        self.imageLabel.setMinimumSize(labelSize)

        self.nameLabel _ QLabel(name)
        self.colorButton _ ?PB..("Modify...")
        self.colorButton.setBackgroundRole(?P...Button)
        self.colorButton.setMinimumSize(32, 32)

        palette _ ?P..(self.colorButton.palette())
        palette.sC..(?P...Button, initialColor)
        self.colorButton.sP..(palette)

        self.invertButton _ ?PB..("Invert")
        self.invertButton.setEnabled F..

        self.colorButton.c__.c..(self.sC..)
        self.invertButton.c__.c..(self.invertImage)

        gridLayout _ QGridLayout()
        gridLayout.aW..(self.imageLabel, 0, 0, 1, 2)
        gridLayout.aW..(self.nameLabel, 1, 0)
        gridLayout.aW..(self.colorButton, 1, 1)
        gridLayout.aW..(self.invertButton, 2, 1, 1, 1)
        self.sL..(gridLayout)

    ___ createImage(self):
        """ Creates a new image by separating out the cyan, magenta, or yellow
            component, depending on the mask color specified in the constructor.
            The amount of the component found in each pixel of the image is used
            to determine how much of a user-selected ink is used for each pixel
            in the new image for the label widget.
        """
        self.newImage _ newImage _ self.originalImage.copy()

        # Create CMY components for the ink being used.
        cyanInk _ float(255 - ?C..(self.paintColor).red()) / 255.0
        magentaInk _ float(255 - ?C..(self.paintColor).green()) / 255.0
        yellowInk _ float(255 - ?C..(self.paintColor).blue()) / 255.0

        convert _ self.convertMap[self.maskColor]

        for y in range(newImage.height()):
            for x in range(newImage.width()):
                p _ self.originalImage.pixel(x, y)

                # Separate the source pixel into its cyan component.
                __ self.inverted:
                    amount _ convert(p)
                ____
                    amount _ 255 - convert(p)

                newColor _ ?C..(
                    255 - min(int(amount * cyanInk), 255),
                    255 - min(int(amount * magentaInk), 255),
                    255 - min(int(amount * yellowInk), 255))

                newImage.setPixel(x, y, newColor.rgb())

        self.imageLabel.setPixmap(QPixmap.fromImage(newImage))

    ___ image(self):
        """ Returns a reference to the modified image. """
        r_ self.newImage

    ___ invertImage(self):
        """ Sets whether the amount of ink applied to the canvas is to be
            inverted (subtracted from the maximum value) before the ink is
            applied.
        """
        self.inverted _ no. self.inverted
        self.createImage()
        self.imageChanged.emit()

    ___ sC..(self):
        """ Separate the current image into cyan, magenta, and yellow
            components.  Create a representation of how each component might
            appear when applied to a blank white piece of paper.
        """
        newColor _ QColorDialog.getColor(self.paintColor)

        __ newColor.isValid
            self.paintColor _ newColor
            palette _ ?P..(self.colorButton.palette())
            palette.sC..(?P...Button, self.paintColor)
            self.colorButton.sP..(palette)
            self.createImage()
            self.imageChanged.emit()

    ___ setImage  image):
        """ Records the original image selected by the user, creates a color
            separation, and enables the invert image checkbox.
        """
        self.originalImage _ image
        self.createImage()
        self.invertButton.setEnabled(True)


c_ Viewer ?MW..
    # Brightness.
    Gloom, Quarter, Half, ThreeQuarters, Full _ range(5)

    # Brightness value map.
    brightnessValueMap _ {
        Gloom: 0,
        Quarter: 64,
        Half: 128,
        ThreeQuarters: 191,
        Full: 255,
    }

    ___ __init__(self):
        """ Constructor initializes a default value for the brightness, creates
            the main menu entries, and constructs a central widget that contains
            enough space for images to be displayed.
        """
        super(Viewer, self).__init__()

        self.scaledImage _ QImage()
        self.menuMap _ {}
        self.path _ ''
        self.brightness _ 255

        self.setWindowTitle("QImage Color Separations")

        self.createMenus()
        self.sCW..(self.createCentralWidget())

    ___ createMenus(self):
        """ Creates a main menu with two entries: a File menu, to allow the image
            to be selected, and a Brightness menu to allow the brightness of the
            separations to be changed.
            Initially, the Brightness menu items are disabled, but the first entry in
            the menu is checked to reflect the default brightness.
        """
        self.fileMenu _ QMenu("&File", self)
        self.brightnessMenu _ QMenu("&Brightness", self)

        self.openAction _ self.fileMenu.aA..("&Open...")
        self.openAction.sS..(?KS..('Ctrl+O'))
        self.saveAction _ self.fileMenu.aA..("&Save...")
        self.saveAction.sS..(?KS..('Ctrl+S'))
        self.saveAction.setEnabled F..
        self.quitAction _ self.fileMenu.aA..("E&xit")
        self.quitAction.sS..(?KS..('Ctrl+Q'))

        self.noBrightness _ self.brightnessMenu.aA..("&0%")
        self.noBrightness.setCheckable(True)
        self.quarterBrightness _ self.brightnessMenu.aA..("&25%")
        self.quarterBrightness.setCheckable(True)
        self.halfBrightness _ self.brightnessMenu.aA..("&50%")
        self.halfBrightness.setCheckable(True)
        self.threeQuartersBrightness _ self.brightnessMenu.aA..("&75%")
        self.threeQuartersBrightness.setCheckable(True)
        self.fullBrightness _ self.brightnessMenu.aA..("&100%")
        self.fullBrightness.setCheckable(True)

        self.menuMap[self.noBrightness] _ self.Gloom
        self.menuMap[self.quarterBrightness] _ self.Quarter
        self.menuMap[self.halfBrightness] _ self.Half
        self.menuMap[self.threeQuartersBrightness] _ self.ThreeQuarters
        self.menuMap[self.fullBrightness] _ self.Full

        self.currentBrightness _ self.fullBrightness
        self.currentBrightness.setChecked(True)
        self.brightnessMenu.setEnabled F..

        self.mB.. .aM..(self.fileMenu)
        self.mB.. .aM..(self.brightnessMenu)

        self.openAction.t__.c..(self.chooseFile)
        self.saveAction.t__.c..(self.saveImage)
        self.quitAction.t__.c..(?A...instance().quit)
        self.brightnessMenu.t__.c..(self.setBrightness)

    ___ createCentralWidget(self):
        """ Constructs a central widget for the window consisting of a two-by-two
            grid of labels, each of which will contain an image. We restrict the
            size of the labels to 256 pixels, and ensure that the window cannot
            be resized.
        """
        frame _ QFrame(self)
        grid _ QGridLayout(frame)
        grid.setSpacing(8)
        grid.setContentsMargins(4, 4, 4, 4)

        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        labelSize _ QSize(256, 256)

        self.finalWidget _ FinalWidget(frame, "Final image", labelSize)

        self.cyanWidget _ ScreenWidget(frame, __.cyan, "Cyan",
                ScreenWidget.Cyan, labelSize)
        self.magentaWidget _ ScreenWidget(frame, __.magenta, "Magenta",
                ScreenWidget.Magenta, labelSize)
        self.yellowWidget _ ScreenWidget(frame, __.yellow, "Yellow",
                ScreenWidget.Yellow, labelSize)

        self.cyanWidget.imageChanged.c..(self.createImage)
        self.magentaWidget.imageChanged.c..(self.createImage)
        self.yellowWidget.imageChanged.c..(self.createImage)

        grid.aW..(self.finalWidget, 0, 0, __.AlignTop | __.AlignHCenter)
        grid.aW..(self.cyanWidget, 0, 1, __.AlignTop | __.AlignHCenter)
        grid.aW..(self.magentaWidget, 1, 0, __.AlignTop | __.AlignHCenter)
        grid.aW..(self.yellowWidget, 1, 1, __.AlignTop | __.AlignHCenter)

        r_ frame

    ___ chooseFile(self):
        """ Provides a dialog window to allow the user to specify an image file.
            If a file is selected, the appropriate function is called to process
            and display it.
        """
        imageFile, _ _ ?FD...gOFN..
                "Choose an image file to open", self.path, "Images (*.*)")

        __ imageFile !_ '':
            self.openImageFile(imageFile)
            self.path _ imageFile

    ___ setBrightness  action):
        """ Changes the value of the brightness according to the entry selected in the
            Brightness menu. The selected entry is checked, and the previously selected
            entry is unchecked.
            The color separations are updated to use the new value for the brightness.
        """
        __ action no. in self.menuMap or self.scaledImage.isNull
            r_

        self.brightness _ self.brightnessValueMap.g..(self.menuMap[action])
        __ self.brightness __ N..:
            r_

        self.currentBrightness.setChecked F..
        self.currentBrightness _ action
        self.currentBrightness.setChecked(True)

        self.createImage()

    ___ openImageFile  imageFile):
        """ Load the image from the file given, and create four pixmaps based
            on the original image.
            The window caption is set, and the Brightness menu enabled if the image file
            can be loaded.
        """
        originalImage _ QImage()

        __ originalImage.load(imageFile):
            self.setWindowTitle(imageFile)
            self.saveAction.setEnabled(True)
            self.brightnessMenu.setEnabled(True)

            self.scaledImage _ originalImage.scaled(256, 256, __.KeepAspectRatio)

            self.cyanWidget.setImage(self.scaledImage)
            self.magentaWidget.setImage(self.scaledImage)
            self.yellowWidget.setImage(self.scaledImage)
            self.createImage()
        ____
            ?MB...warning  "Cannot open file",
                    "The selected file could not be opened.",
                    ?MB...Cancel, ?MB...NoButton,
                    ?MB...NoButton)

    ___ createImage(self):
        """ Creates an image by combining the contents of the three screens
            to present a page preview.
            The image associated with each screen is separated into cyan,
            magenta, and yellow components. We add up the values for each
            component from the three screen images, and subtract the totals
            from the maximum value for each corresponding primary color.
        """
        newImage _ self.scaledImage.copy()

        image1 _ self.cyanWidget.image()
        image2 _ self.magentaWidget.image()
        image3 _ self.yellowWidget.image()
        darkness _ 255 - self.brightness

        for y in range(newImage.height()):
            for x in range(newImage.width()):
                # Create three screens, using the quantities of the source CMY
                # components to determine how much of each of the inks are to
                # be put on each screen.
                p1 _ image1.pixel(x, y)
                cyan1 _ float(255 - qRed(p1))
                magenta1 _ float(255 - qGreen(p1))
                yellow1 _ float(255 - qBlue(p1))

                p2 _ image2.pixel(x, y)
                cyan2 _ float(255 - qRed(p2))
                magenta2 _ float(255 - qGreen(p2))
                yellow2 _ float(255 - qBlue(p2))

                p3 _ image3.pixel(x, y)
                cyan3 _ float(255 - qRed(p3))
                magenta3 _ float(255 - qGreen(p3))
                yellow3 _ float(255 - qBlue(p3))

                newColor _ ?C..(
                    max(255 - int(cyan1 + cyan2 + cyan3) - darkness, 0),
                    max(255 - int(magenta1 + magenta2 + magenta3) - darkness, 0),
                    max(255 - int(yellow1 + yellow2 + yellow3) - darkness, 0))

                newImage.setPixel(x, y, newColor.rgb())

        self.finalWidget.setPixmap(QPixmap.fromImage(newImage))

    ___ saveImage(self):
        """ Provides a dialog window to allow the user to save the image file.
        """
        imageFile, _ _ ?FD...getSaveFileName
                "Choose a filename to save the image", "", "Images (*.png)")

        info _ QFileInfo(imageFile)

        __ info.baseName() !_ '':
            newImageFile _ QFileInfo(info.absoluteDir(),
                    info.baseName() + '.png').absoluteFilePath()

            __ no. self.finalWidget.pixmap().save(newImageFile, 'PNG'):
                ?MB...warning  "Cannot save file",
                        "The file could not be saved.",
                        ?MB...Cancel, ?MB...NoButton,
                        ?MB...NoButton)
        ____
            ?MB...warning  "Cannot save file",
                    "Please enter a valid filename.", ?MB...Cancel,
                    ?MB...NoButton, ?MB...NoButton)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ Viewer()
    window.s..
    sys.exit(app.exec_())
