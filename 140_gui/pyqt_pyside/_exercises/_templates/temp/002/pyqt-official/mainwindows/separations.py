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


____ ?.?C.. ______ (pS.., QBuffer, QByteArray, QFileInfo,
        QIODevice, QMimeData, QPoint, ?S.., __)
____ ?.?G.. ______ (qBlue, ?C.., QDrag, qGreen, QImage, ?KS..,
        ?P.., ?P.., qRed)
____ ?.?W.. ______ (?A.., QColorDialog, ?FD.., QFrame,
        QGridLayout, ?L.., QLayout, ?MW.., ?M.., ?MB..,
        ?PB.., ?VBL..)


c_ FinalWidget(QFrame):

    ___  -   parent, name, labelSize):
        s__(FinalWidget, self). - (parent)

        dragStartPosition _ QPoint()

        hasImage _ F..
        imageLabel _ ?L..
        imageLabel.setFrameShadow(QFrame.Sunken)
        imageLabel.setFrameShape(QFrame.StyledPanel)
        imageLabel.sMS..(labelSize)
        nameLabel _ ?L..(name)

        layout _ ?VBL..
        layout.aW..(imageLabel, 1)
        layout.aW..(nameLabel, 0)
        sL..(layout)

    ___ mouseMoveEvent  event):
        """ If the mouse moves far enough when the left mouse button is held
            down, start a drag and drop operation.
        """
        __ no. event.buttons() & __.LeftButton:
            r_

        __ (event.pos() - dragStartPosition).manhattanLength() \
             < ?A...startDragDistance
            r_

        __ no. hasImage:
            r_

        drag _ QDrag
        mimeData _ QMimeData()

        output _ QByteArray()
        outputBuffer _ QBuffer(output)
        outputBuffer.o..(QIODevice.WriteOnly)
        imageLabel.pixmap().toImage().save(outputBuffer, 'PNG')
        outputBuffer.c..
        mimeData.setData('image/png', output)

        drag.setMimeData(mimeData)
        drag.sP..(imageLabel.pixmap().scaled(64, 64, __.KeepAspectRatio))
        drag.setHotSpot(QPoint(drag.pixmap().width() / 2,
                                      drag.pixmap().height()))
        drag.start()

    ___ mousePressEvent  event):
        """ Check for left mouse button presses in order to enable drag and
            drop.
        """
        __ event.button() __ __.LeftButton:
            dragStartPosition _ event.pos()

    ___ pixmap 
        r_ imageLabel.pixmap()

    ___ sP..  pixmap):
        imageLabel.sP..(pixmap)
        hasImage _ T..


c_ ScreenWidget(QFrame):
    # Separation.
    Cyan, Magenta, Yellow _ ra..(3)

    convertMap _ {
        Cyan: qRed,
        Magenta: qGreen,
        Yellow: qBlue,
    }

    imageChanged _ pS..()

    ___  -   parent, initialColor, name, mask, labelSize):
        """ Initializes the paint color, the mask color (cyan, magenta, or
        yellow), connects the color selector and invert checkbox to functions,
        and creates a two-by-two grid layout.
        """
        s__(ScreenWidget, self). - (parent)

        originalImage _ QImage()
        newImage _ QImage()

        paintColor _ initialColor
        maskColor _ mask
        inverted _ F..

        imageLabel _ ?L..
        imageLabel.setFrameShadow(QFrame.Sunken)
        imageLabel.setFrameShape(QFrame.StyledPanel)
        imageLabel.sMS..(labelSize)

        nameLabel _ ?L..(name)
        colorButton _ ?PB..("Modify...")
        colorButton.setBackgroundRole(?P...Button)
        colorButton.sMS..(32, 32)

        palette _ ?P..(colorButton.palette())
        palette.sC..(?P...Button, initialColor)
        colorButton.sP..(palette)

        invertButton _ ?PB..("Invert")
        invertButton.sE.. F..

        colorButton.c__.c..(sC..)
        invertButton.c__.c..(invertImage)

        gridLayout _ QGridLayout()
        gridLayout.aW..(imageLabel, 0, 0, 1, 2)
        gridLayout.aW..(nameLabel, 1, 0)
        gridLayout.aW..(colorButton, 1, 1)
        gridLayout.aW..(invertButton, 2, 1, 1, 1)
        sL..(gridLayout)

    ___ createImage 
        """ Creates a new image by separating out the cyan, magenta, or yellow
            component, depending on the mask color specified in the constructor.
            The amount of the component found in each pixel of the image is used
            to determine how much of a user-selected ink is used for each pixel
            in the new image for the label widget.
        """
        newImage _ newImage _ originalImage.copy()

        # Create CMY components for the ink being used.
        cyanInk _ fl..(255 - ?C..(paintColor).red()) / 255.0
        magentaInk _ fl..(255 - ?C..(paintColor).green()) / 255.0
        yellowInk _ fl..(255 - ?C..(paintColor).blue()) / 255.0

        convert _ convertMap[maskColor]

        ___ y __ ra..(newImage.height()):
            ___ x __ ra..(newImage.width()):
                p _ originalImage.pixel(x, y)

                # Separate the source pixel into its cyan component.
                __ inverted:
                    amount _ convert(p)
                ____
                    amount _ 255 - convert(p)

                newColor _ ?C..(
                    255 - min(in.(amount * cyanInk), 255),
                    255 - min(in.(amount * magentaInk), 255),
                    255 - min(in.(amount * yellowInk), 255))

                newImage.setPixel(x, y, newColor.rgb())

        imageLabel.sP..(?P...fromImage(newImage))

    ___ image 
        """ Returns a reference to the modified image. """
        r_ newImage

    ___ invertImage 
        """ Sets whether the amount of ink applied to the canvas is to be
            inverted (subtracted from the maximum value) before the ink is
            applied.
        """
        inverted _ no. inverted
        createImage()
        imageChanged.e..()

    ___ sC.. 
        """ Separate the current image into cyan, magenta, and yellow
            components.  Create a representation of how each component might
            appear when applied to a blank white piece of paper.
        """
        newColor _ QColorDialog.getColor(paintColor)

        __ newColor.isValid
            paintColor _ newColor
            palette _ ?P..(colorButton.palette())
            palette.sC..(?P...Button, paintColor)
            colorButton.sP..(palette)
            createImage()
            imageChanged.e..()

    ___ setImage  image):
        """ Records the original image selected by the user, creates a color
            separation, and enables the invert image checkbox.
        """
        originalImage _ image
        createImage()
        invertButton.sE..( st.


c_ Viewer ?MW..
    # Brightness.
    Gloom, Quarter, Half, ThreeQuarters, Full _ ra..(5)

    # Brightness value map.
    brightnessValueMap _ {
        Gloom: 0,
        Quarter: 64,
        Half: 128,
        ThreeQuarters: 191,
        Full: 255,
    }

    ___  -
        """ Constructor initializes a default value for the brightness, creates
            the main menu entries, and constructs a central widget that contains
            enough space for images to be displayed.
        """
        s__(Viewer, self). - ()

        scaledImage _ QImage()
        menuMap _   # dict
        pa__ _ ''
        brightness _ 255

        sWT..("QImage Color Separations")

        createMenus()
        sCW..(createCentralWidget())

    ___ createMenus 
        """ Creates a main menu with two entries: a File menu, to allow the image
            to be selected, and a Brightness menu to allow the brightness of the
            separations to be changed.
            Initially, the Brightness menu items are disabled, but the first entry in
            the menu is checked to reflect the default brightness.
        """
        fileMenu _ ?M..("&File", self)
        brightnessMenu _ ?M..("&Brightness", self)

        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..(?KS..('Ctrl+O'))
        saveAction _ fileMenu.aA..("&Save...")
        saveAction.sS..(?KS..('Ctrl+S'))
        saveAction.sE.. F..
        quitAction _ fileMenu.aA..("E&xit")
        quitAction.sS..(?KS..('Ctrl+Q'))

        noBrightness _ brightnessMenu.aA..("&0%")
        noBrightness.setCheckable( st.
        quarterBrightness _ brightnessMenu.aA..("&25%")
        quarterBrightness.setCheckable( st.
        halfBrightness _ brightnessMenu.aA..("&50%")
        halfBrightness.setCheckable( st.
        threeQuartersBrightness _ brightnessMenu.aA..("&75%")
        threeQuartersBrightness.setCheckable( st.
        fullBrightness _ brightnessMenu.aA..("&100%")
        fullBrightness.setCheckable( st.

        menuMap[noBrightness] _ Gloom
        menuMap[quarterBrightness] _ Quarter
        menuMap[halfBrightness] _ Half
        menuMap[threeQuartersBrightness] _ ThreeQuarters
        menuMap[fullBrightness] _ Full

        currentBrightness _ fullBrightness
        currentBrightness.sC__( st.
        brightnessMenu.sE.. F..

        mB.. .aM..(fileMenu)
        mB.. .aM..(brightnessMenu)

        openAction.t__.c..(chooseFile)
        saveAction.t__.c..(saveImage)
        quitAction.t__.c..(?A...i.. .quit)
        brightnessMenu.t__.c..(setBrightness)

    ___ createCentralWidget 
        """ Constructs a central widget for the window consisting of a two-by-two
            grid of labels, each of which will contain an image. We restrict the
            size of the labels to 256 pixels, and ensure that the window cannot
            be resized.
        """
        frame _ QFrame
        grid _ QGridLayout(frame)
        grid.setSpacing(8)
        grid.sCM..(4, 4, 4, 4)

        la__ .setSizeConstraint(QLayout.SetFixedSize)

        labelSize _ ?S..(256, 256)

        finalWidget _ FinalWidget(frame, "Final image", labelSize)

        cyanWidget _ ScreenWidget(frame, __.cyan, "Cyan",
                ScreenWidget.Cyan, labelSize)
        magentaWidget _ ScreenWidget(frame, __.magenta, "Magenta",
                ScreenWidget.Magenta, labelSize)
        yellowWidget _ ScreenWidget(frame, __.yellow, "Yellow",
                ScreenWidget.Yellow, labelSize)

        cyanWidget.imageChanged.c..(createImage)
        magentaWidget.imageChanged.c..(createImage)
        yellowWidget.imageChanged.c..(createImage)

        grid.aW..(finalWidget, 0, 0, __.AlignTop | __.AlignHCenter)
        grid.aW..(cyanWidget, 0, 1, __.AlignTop | __.AlignHCenter)
        grid.aW..(magentaWidget, 1, 0, __.AlignTop | __.AlignHCenter)
        grid.aW..(yellowWidget, 1, 1, __.AlignTop | __.AlignHCenter)

        r_ frame

    ___ chooseFile 
        """ Provides a dialog window to allow the user to specify an image file.
            If a file is selected, the appropriate function is called to process
            and display it.
        """
        imageFile, _ _ ?FD...gOFN..
                "Choose an image file to open", pa__, "Images (*.*)")

        __ imageFile !_ '':
            openImageFile(imageFile)
            pa__ _ imageFile

    ___ setBrightness  action):
        """ Changes the value of the brightness according to the entry selected in the
            Brightness menu. The selected entry is checked, and the previously selected
            entry is unchecked.
            The color separations are updated to use the new value for the brightness.
        """
        __ action no. __ menuMap or scaledImage.isNull
            r_

        brightness _ brightnessValueMap.g..(menuMap[action])
        __ brightness __ N..:
            r_

        currentBrightness.sC__ F..
        currentBrightness _ action
        currentBrightness.sC__( st.

        createImage()

    ___ openImageFile  imageFile):
        """ Load the image from the file given, and create four pixmaps based
            on the original image.
            The window caption is set, and the Brightness menu enabled if the image file
            can be loaded.
        """
        originalImage _ QImage()

        __ originalImage.load(imageFile):
            sWT..(imageFile)
            saveAction.sE..( st.
            brightnessMenu.sE..( st.

            scaledImage _ originalImage.scaled(256, 256, __.KeepAspectRatio)

            cyanWidget.setImage(scaledImage)
            magentaWidget.setImage(scaledImage)
            yellowWidget.setImage(scaledImage)
            createImage()
        ____
            ?MB...w..  "Cannot open file",
                    "The selected file could not be opened.",
                    ?MB...Cancel, ?MB...NoButton,
                    ?MB...NoButton)

    ___ createImage 
        """ Creates an image by combining the contents of the three screens
            to present a page preview.
            The image associated with each screen is separated into cyan,
            magenta, and yellow components. We add up the values for each
            component from the three screen images, and subtract the totals
            from the maximum value for each corresponding primary color.
        """
        newImage _ scaledImage.copy()

        image1 _ cyanWidget.image()
        image2 _ magentaWidget.image()
        image3 _ yellowWidget.image()
        darkness _ 255 - brightness

        ___ y __ ra..(newImage.height()):
            ___ x __ ra..(newImage.width()):
                # Create three screens, using the quantities of the source CMY
                # components to determine how much of each of the inks are to
                # be put on each screen.
                p1 _ image1.pixel(x, y)
                cyan1 _ fl..(255 - qRed(p1))
                magenta1 _ fl..(255 - qGreen(p1))
                yellow1 _ fl..(255 - qBlue(p1))

                p2 _ image2.pixel(x, y)
                cyan2 _ fl..(255 - qRed(p2))
                magenta2 _ fl..(255 - qGreen(p2))
                yellow2 _ fl..(255 - qBlue(p2))

                p3 _ image3.pixel(x, y)
                cyan3 _ fl..(255 - qRed(p3))
                magenta3 _ fl..(255 - qGreen(p3))
                yellow3 _ fl..(255 - qBlue(p3))

                newColor _ ?C..(
                    max(255 - in.(cyan1 + cyan2 + cyan3) - darkness, 0),
                    max(255 - in.(magenta1 + magenta2 + magenta3) - darkness, 0),
                    max(255 - in.(yellow1 + yellow2 + yellow3) - darkness, 0))

                newImage.setPixel(x, y, newColor.rgb())

        finalWidget.sP..(?P...fromImage(newImage))

    ___ saveImage 
        """ Provides a dialog window to allow the user to save the image file.
        """
        imageFile, _ _ ?FD...getSaveFileName
                "Choose a filename to save the image", "", "Images (*.png)")

        info _ QFileInfo(imageFile)

        __ i...baseName() !_ '':
            newImageFile _ QFileInfo(i...absoluteDir(),
                    i...baseName() + '.png').absoluteFilePath()

            __ no. finalWidget.pixmap().save(newImageFile, 'PNG'):
                ?MB...w..  "Cannot save file",
                        "The file could not be saved.",
                        ?MB...Cancel, ?MB...NoButton,
                        ?MB...NoButton)
        ____
            ?MB...w..  "Cannot save file",
                    "Please enter a valid filename.", ?MB...Cancel,
                    ?MB...NoButton, ?MB...NoButton)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    window _ Viewer()
    window.s..
    ___.e.. ?.e..
