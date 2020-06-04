______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ ColorButton(qtw.?PB..):

    changed _ qtc.pS..()

    ___  -   default_color, changed_None):
        s_. - ()
        set_color(qtg.?C..(default_color))
        c__.c..(on_click)
        __ changed:
            changed.c..(changed)

    ___ set_color  color):
        _color _ color
        # update icon
        pixmap _ qtg.?P..(32, 32)
        pixmap.fill(_color)
        sI..(qtg.?I..(pixmap))

    ___ on_click
        color _ qtw.QColorDialog.getColor(_color)
        __ color:
            set_color(color)
            changed.e..()


c_ FontButton(qtw.?PB..):

    changed _ qtc.pS..()

    ___  -   default_family, default_size, changed_None):
        s_. - ()
        set_font(qtg.?F..(default_family, default_size))
        c__.c..(on_click)
        __ changed:
            changed.c..(changed)

    ___ set_font  font):
        _font _ font
        sF..(font)
        sT..(f'{font.family()} {font.pointSize()}')

    ___ on_click
        font, a___ _ qtw.QFontDialog.getFont(_font)
        __ a___:
            set_font(font)
            changed.e..()


c_ ImageFileButton(qtw.?PB..):

    changed _ qtc.pS..()

    ___  -   changed_None):
        s_. - ("Click to select…")
        _filename _ N..
        c__.c..(on_click)
        __ changed:
            changed.c..(changed)

    ___ on_click
        filename, _ _ qtw.?FD...gOFN..(
            N.., "Select an image to use",
            qtc.?D...homePath(), "Images (*.png *.xpm *.jpg)")
        __ filename:
            _filename _ filename
            # set button text to filename without path
            sT..(qtc.QFileInfo(filename).fileName())
            changed.e..()


c_ MemeEditForm ?.?W..

    changed _ qtc.pS..(dict)

    ___  -
        s_. - ()
        sL..(qtw.?FL..())

        # Image
        image_source _ ImageFileButton(changed_self.on_change)
        la__ .aR..('Image file', image_source)

        # Text entries
        top_text _ qtw.?PTE..(textChanged_self.on_change)
        bottom_text _ qtw.?PTE..(textChanged_self.on_change)
        la__ .aR..("Top Text", top_text)
        la__ .aR..("Bottom Text", bottom_text)

        # Text color and font
        text_color _ ColorButton('white', changed_self.on_change)
        la__ .aR..("Text Color", text_color)
        text_font _ FontButton('Impact', 32, changed_self.on_change)
        la__ .aR..("Text Font", text_font)

        # Background Boxes
        text_bg_color _ ColorButton('black', changed_self.on_change)
        la__ .aR..('Text Background', text_bg_color)
        top_bg_height _ qtw.SB..(
            minimum_0, maximum_32,
            valueChanged_self.on_change, suffix_' line(s)')
        la__ .aR..('Top BG height', top_bg_height)
        bottom_bg_height _ qtw.SB..(
            minimum_0, maximum_32,
            valueChanged_self.on_change, suffix_' line(s)')
        la__ .aR..('Bottom BG height', bottom_bg_height)
        bg_padding _ qtw.SB..(
            minimum_0, maximum_100, value_10,
            valueChanged_self.on_change, suffix_' px')
        la__ .aR..('BG Padding', bg_padding)

        # Deep Fryer
        deep_fry _ ?.?CB..('Deep Fry', stateChanged_self.on_change)
        la__ .aR..(deep_fry)

    ___ on_change
        data _ {
            'top_text': top_text.toPlainText(),
            'bottom_text': bottom_text.toPlainText(),
            'text_color': text_color._color,
            'text_font': text_font._font,
            'bg_color': text_bg_color._color,
            'top_bg_height': top_bg_height.v..,
            'bottom_bg_height': bottom_bg_height.v..,
            'bg_padding': bg_padding.v..,
            'deep_fry': deep_fry.isChecked()
        }

        changed.e..(data)


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        sWT..('Qt Meme Generator')

        # define some constants
        max_size _ qtc.?S..(800, 600)
        image _ qtg.QImage(
            max_size, qtg.QImage.Format_ARGB32)
        image.fill(qtg.?C..('black'))

        # Container widget
        mainwidget _ qtw.?W..
        sCW..(mainwidget)
        mainwidget.sL..(qtw.?HBL..

        # Image Previewer
        image_display _ ?.?L..(pixmap_qtg.?P..(image))
        mainwidget.la__ .aW..(image_display)

        # The editing form
        form _ MemeEditForm()
        mainwidget.la__ .aW..(form)
        form.changed.c..(build_image)

        # Create file loading and saving
        toolbar _ aTB..('File')
        toolbar.aA..("Save Image", save_image)

        # End main UI code
        s..

    ___ save_image
        save_file, _ _ qtw.?FD...getSaveFileName(
            N.., "Save your image",
            qtc.?D...homePath(), "PNG Images (*.png)")
        __ save_file:
            image.save(save_file, "PNG")

    ___ build_image  data):
        # Create a QImage file
        __ no. data.g..('image_source'):
            image.fill(qtg.?C..('black'))
        ____
            image.load(data.g..('image_source'))
            # Scale down the image if it's over the max_size
            __ no. (max_size - image.size()).isValid
                # isValid returns false if either dimension is negative
                image _ image.scaled(
                    max_size, qtc.__.KeepAspectRatio)

        # create the painter
        painter _ qtg.QPainter(image)

        # Paint the background blocks
        font_px _ qtg.QFontInfo(data['text_font']).pixelSize()
        top_px _ (data['top_bg_height'] * font_px) + data['bg_padding']
        top_block_rect _ qtc.QRect(
            0, 0, image.width(), top_px)
        bottom_px _ (
            image.height() - data['bg_padding']
            - (data['bottom_bg_height'] * font_px))
        bottom_block_rect _ qtc.QRect(
            0, bottom_px, image.width(), image.height())

        painter.sB..(qtg.?B..(data['bg_color']))
        painter.drawRect(top_block_rect)
        painter.drawRect(bottom_block_rect)

        # Paint the text
        painter.sP..(data['text_color'])
        painter.sF..(data['text_font'])
        flags _ qtc.__.AlignHCenter | qtc.__.TextWordWrap
        painter.drawText(
            image.rect(), flags | qtc.__.AlignTop, data['top_text'])
        painter.drawText(
            image.rect(), flags | qtc.__.AlignBottom,
            data['bottom_text'])

        # Deep fry
        __ data['deep_fry']:
            # To do image-level editing,
            # we need to explicitly end our painting first
            painter.end()

            # Now we can do things that overwrite the image
            # Swapping Red and Blue
            image _ image.rgbSwapped()

            # Convert to a 8-bit color
            image _ image.convertToFormat(qtg.QImage.Format_Indexed8)

            # We're going to grab all the colors from the color table
            # then alter the hue and saturation of each color
            colors _ image.colorTable()
            new_colors _   # list
            ___ color __ colors:
                qcolor _ qtg.?C..(color)
                qcolor.setHslF(
                    ((qcolor.hueF() * 200) % 100)/100,
                    min(1, qcolor.saturationF() * 2),
                    qcolor.lightnessF())
                new_colors.ap..(qcolor.rgba())
            image.setColorTable(new_colors)

            # Convert back to the original format
            image _ image.convertToFormat(qtg.QImage.Format_ARGB32)

        # show the image
        image_display.sP..(qtg.?P..(image))


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e.. ?.e..
