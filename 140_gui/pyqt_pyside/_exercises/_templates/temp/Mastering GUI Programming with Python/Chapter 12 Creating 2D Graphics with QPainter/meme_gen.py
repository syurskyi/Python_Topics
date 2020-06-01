______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ ColorButton(qtw.?PB..):

    changed _ qtc.pyqtSignal()

    ___ __init__  default_color, changed_None):
        super().__init__()
        self.set_color(qtg.?C..(default_color))
        self.c__.c..(self.on_click)
        __ changed:
            self.changed.c..(changed)

    ___ set_color  color):
        self._color _ color
        # update icon
        pixmap _ qtg.QPixmap(32, 32)
        pixmap.fill(self._color)
        self.setIcon(qtg.QIcon(pixmap))

    ___ on_click(self):
        color _ qtw.QColorDialog.getColor(self._color)
        __ color:
            self.set_color(color)
            self.changed.emit()


c_ FontButton(qtw.?PB..):

    changed _ qtc.pyqtSignal()

    ___ __init__  default_family, default_size, changed_None):
        super().__init__()
        self.set_font(qtg.QFont(default_family, default_size))
        self.c__.c..(self.on_click)
        __ changed:
            self.changed.c..(changed)

    ___ set_font  font):
        self._font _ font
        self.setFont(font)
        self.sT..(f'{font.family()} {font.pointSize()}')

    ___ on_click(self):
        font, accepted _ qtw.QFontDialog.getFont(self._font)
        __ accepted:
            self.set_font(font)
            self.changed.emit()


c_ ImageFileButton(qtw.?PB..):

    changed _ qtc.pyqtSignal()

    ___ __init__  changed_None):
        super().__init__("Click to select…")
        self._filename _ N..
        self.c__.c..(self.on_click)
        __ changed:
            self.changed.c..(changed)

    ___ on_click(self):
        filename, _ _ qtw.?FD...gOFN..(
            N.., "Select an image to use",
            qtc.QDir.homePath(), "Images (*.png *.xpm *.jpg)")
        __ filename:
            self._filename _ filename
            # set button text to filename without path
            self.sT..(qtc.QFileInfo(filename).fileName())
            self.changed.emit()


c_ MemeEditForm(qtw.QWidget):

    changed _ qtc.pyqtSignal(dict)

    ___ __init__(self):
        super().__init__()
        self.sL..(qtw.QFormLayout())

        # Image
        self.image_source _ ImageFileButton(changed_self.on_change)
        self.layout().addRow('Image file', self.image_source)

        # Text entries
        self.top_text _ qtw.QPlainTextEdit(textChanged_self.on_change)
        self.bottom_text _ qtw.QPlainTextEdit(textChanged_self.on_change)
        self.layout().addRow("Top Text", self.top_text)
        self.layout().addRow("Bottom Text", self.bottom_text)

        # Text color and font
        self.text_color _ ColorButton('white', changed_self.on_change)
        self.layout().addRow("Text Color", self.text_color)
        self.text_font _ FontButton('Impact', 32, changed_self.on_change)
        self.layout().addRow("Text Font", self.text_font)

        # Background Boxes
        self.text_bg_color _ ColorButton('black', changed_self.on_change)
        self.layout().addRow('Text Background', self.text_bg_color)
        self.top_bg_height _ qtw.QSpinBox(
            minimum_0, maximum_32,
            valueChanged_self.on_change, suffix_' line(s)')
        self.layout().addRow('Top BG height', self.top_bg_height)
        self.bottom_bg_height _ qtw.QSpinBox(
            minimum_0, maximum_32,
            valueChanged_self.on_change, suffix_' line(s)')
        self.layout().addRow('Bottom BG height', self.bottom_bg_height)
        self.bg_padding _ qtw.QSpinBox(
            minimum_0, maximum_100, value_10,
            valueChanged_self.on_change, suffix_' px')
        self.layout().addRow('BG Padding', self.bg_padding)

    ___ on_change(self):
        data _ {
            'image_source': self.image_source._filename,
            'top_text': self.top_text.toPlainText(),
            'bottom_text': self.bottom_text.toPlainText(),
            'text_color': self.text_color._color,
            'text_font': self.text_font._font,
            'bg_color': self.text_bg_color._color,
            'top_bg_height': self.top_bg_height.value(),
            'bottom_bg_height': self.bottom_bg_height.value(),
            'bg_padding': self.bg_padding.value()
        }
        self.changed.emit(data)


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.setWindowTitle('Qt Meme Generator')

        # define some constants
        self.max_size _ qtc.QSize(800, 600)
        self.image _ qtg.QImage(
            self.max_size, qtg.QImage.Format_ARGB32)
        self.image.fill(qtg.?C..('black'))

        # Container widget
        mainwidget _ qtw.?W..
        self.sCW..(mainwidget)
        mainwidget.sL..(qtw.QHBoxLayout())

        # Image Previewer
        self.image_display _ qtw.QLabel(pixmap_qtg.QPixmap(self.image))
        mainwidget.layout().aW..(self.image_display)

        # The editing form
        self.form _ MemeEditForm()
        mainwidget.layout().aW..(self.form)
        self.form.changed.c..(self.build_image)

        # Create file saving
        toolbar _ self.addToolBar('File')
        toolbar.aA..("Save Image", self.save_image)

        # End main UI code
        self.s..

    ___ save_image(self):
        save_file, _ _ qtw.?FD...getSaveFileName(
            N.., "Save your image",
            qtc.QDir.homePath(), "PNG Images (*.png)")
        __ save_file:
            self.image.save(save_file, "PNG")

    ___ build_image  data):
        # Create a QImage file
        __ no. data.g..('image_source'):
            self.image.fill(qtg.?C..('black'))
        ____
            self.image.load(data.g..('image_source'))
            # Scale down the image if it's over the max_size
            __ no. (self.max_size - self.image.size()).isValid
                # isValid returns false if either dimension is negative
                self.image _ self.image.scaled(
                    self.max_size, qtc.__.KeepAspectRatio)

        # create the painter
        painter _ qtg.QPainter(self.image)

        # Paint the background blocks
        font_px _ qtg.QFontInfo(data['text_font']).pixelSize()
        top_px _ (data['top_bg_height'] * font_px) + data['bg_padding']
        top_block_rect _ qtc.QRect(
            0, 0, self.image.width(), top_px)
        bottom_px _ (
            self.image.height() - data['bg_padding']
            - (data['bottom_bg_height'] * font_px))
        bottom_block_rect _ qtc.QRect(
            0, bottom_px, self.image.width(), self.image.height())

        painter.setBrush(qtg.QBrush(data['bg_color']))
        painter.drawRect(top_block_rect)
        painter.drawRect(bottom_block_rect)

        # Paint the text
        painter.setPen(data['text_color'])
        painter.setFont(data['text_font'])
        flags _ qtc.__.AlignHCenter | qtc.__.TextWordWrap
        painter.drawText(
            self.image.rect(), flags | qtc.__.AlignTop, data['top_text'])
        painter.drawText(
            self.image.rect(), flags | qtc.__.AlignBottom,
            data['bottom_text'])

        # show the image
        self.image_display.setPixmap(qtg.QPixmap(self.image))


__ __name__ == '__main__':
    app _ qtw.?A..(___.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
