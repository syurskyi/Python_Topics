____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.QtPrintSupport ______ *

______ os
______ ___
______ uuid

FONT_SIZES _ [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS _ ['.jpg','.png','.bmp']
HTML_EXTENSIONS _ ['.htm', '.html']

___ hexuuid
    r_ uuid.uuid4().hex

___ splitext(p):
    r_ __.p__ .splitext(p)[1].lower()

c_ TextEdit(QTextEdit):

    ___ canInsertFromMimeData  source):

        __ source.hasImage
            r_ True
        ____
            r_ super(TextEdit, self).canInsertFromMimeData(source)

    ___ insertFromMimeData  source):

        cursor _ self.textCursor()
        document _ self.document()

        __ source.hasUrls

            for u in source.urls
                file_ext _ splitext(str(u.toLocalFile()))
                __ u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image _ QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                ____
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            ____
                # If all were valid images, finish here.
                r_


        ____ source.hasImage
            image _ source.imageData()
            uuid _ hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            r_

        super(TextEdit, self).insertFromMimeData(source)


c_ MainWindow ?MW..

    ___ __init__  *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout _ ?VBL..
        self.editor _ TextEdit()
        # Setup the QTextEdit editor configuration
        self.editor.setAutoFormatting(QTextEdit.AutoAll)
        self.editor.selectionChanged.c..(self.update_format)
        # Initialize default font size.
        font _ QFont('Times', 12)
        self.editor.setFont(font)
        # We need to repeat the size to init the current format.
        self.editor.setFontPointSize(12)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path _ N..

        layout.aW..(self.editor)

        container _ ?W..
        container.sL..(layout)
        self.sCW..(container)

        self.status _ QStatusBar()
        self.setStatusBar(self.status)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_toolbar _ QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu _ self.mB.. .aM..("&File")

        open_file_action _ ?A..(QIcon(__.p__ .join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.t__.c..(self.file_open)
        file_menu.aA..(open_file_action)
        file_toolbar.aA..(open_file_action)

        save_file_action _ ?A..(QIcon(__.p__ .join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.t__.c..(self.file_save)
        file_menu.aA..(save_file_action)
        file_toolbar.aA..(save_file_action)

        saveas_file_action _ ?A..(QIcon(__.p__ .join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.t__.c..(self.file_saveas)
        file_menu.aA..(saveas_file_action)
        file_toolbar.aA..(saveas_file_action)

        print_action _ ?A..(QIcon(__.p__ .join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.t__.c..(self.file_print)
        file_menu.aA..(print_action)
        file_toolbar.aA..(print_action)

        edit_toolbar _ QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu _ self.mB.. .aM..("&Edit")

        undo_action _ ?A..(QIcon(__.p__ .join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.t__.c..(self.editor.undo)
        edit_menu.aA..(undo_action)

        redo_action _ ?A..(QIcon(__.p__ .join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.t__.c..(self.editor.redo)
        edit_toolbar.aA..(redo_action)
        edit_menu.aA..(redo_action)

        edit_menu.addSeparator()

        cut_action _ ?A..(QIcon(__.p__ .join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.sS..(?KS...Cut)
        cut_action.t__.c..(self.editor.cut)
        edit_toolbar.aA..(cut_action)
        edit_menu.aA..(cut_action)

        copy_action _ ?A..(QIcon(__.p__ .join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        cut_action.sS..(?KS...Copy)
        copy_action.t__.c..(self.editor.copy)
        edit_toolbar.aA..(copy_action)
        edit_menu.aA..(copy_action)

        paste_action _ ?A..(QIcon(__.p__ .join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        cut_action.sS..(?KS...Paste)
        paste_action.t__.c..(self.editor.paste)
        edit_toolbar.aA..(paste_action)
        edit_menu.aA..(paste_action)

        select_action _ ?A..(QIcon(__.p__ .join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        cut_action.sS..(?KS...SelectAll)
        select_action.t__.c..(self.editor.selectAll)
        edit_menu.aA..(select_action)

        edit_menu.addSeparator()

        wrap_action _ ?A..(QIcon(__.p__ .join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.t__.c..(self.edit_toggle_wrap)
        edit_menu.aA..(wrap_action)

        format_toolbar _ QToolBar("Format")
        format_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(format_toolbar)
        format_menu _ self.mB.. .aM..("&Format")

        # We need references to these actions/settings to update as selection changes, so attach to self.
        self.fonts _ QFontComboBox()
        self.fonts.currentFontChanged.c..(self.editor.setCurrentFont)
        format_toolbar.aW..(self.fonts)

        self.fontsize _ QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        self.fontsize.currentIndexChanged[str].c..(lambda s: self.editor.setFontPointSize(float(s)) )
        format_toolbar.aW..(self.fontsize)

        self.bold_action _ ?A..(QIcon(__.p__ .join('images', 'edit-bold.png')), "Bold", self)
        self.bold_action.setStatusTip("Bold")
        self.bold_action.sS..(?KS...Bold)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.c..(lambda x: self.editor.setFontWeight(QFont.Bold __ x else QFont.Normal))
        format_toolbar.aA..(self.bold_action)
        format_menu.aA..(self.bold_action)

        self.italic_action _ ?A..(QIcon(__.p__ .join('images', 'edit-italic.png')), "Italic", self)
        self.italic_action.setStatusTip("Italic")
        self.italic_action.sS..(?KS...Italic)
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.c..(self.editor.setFontItalic)
        format_toolbar.aA..(self.italic_action)
        format_menu.aA..(self.italic_action)

        self.underline_action _ ?A..(QIcon(__.p__ .join('images', 'edit-underline.png')), "Underline", self)
        self.underline_action.setStatusTip("Underline")
        self.underline_action.sS..(?KS...Underline)
        self.underline_action.setCheckable(True)
        self.underline_action.toggled.c..(self.editor.setFontUnderline)
        format_toolbar.aA..(self.underline_action)
        format_menu.aA..(self.underline_action)

        format_menu.addSeparator()

        self.alignl_action _ ?A..(QIcon(__.p__ .join('images', 'edit-alignment.png')), "Align left", self)
        self.alignl_action.setStatusTip("Align text left")
        self.alignl_action.setCheckable(True)
        self.alignl_action.t__.c..(lambda: self.editor.setAlignment(__.AlignLeft))
        format_toolbar.aA..(self.alignl_action)
        format_menu.aA..(self.alignl_action)

        self.alignc_action _ ?A..(QIcon(__.p__ .join('images', 'edit-alignment-center.png')), "Align center", self)
        self.alignc_action.setStatusTip("Align text center")
        self.alignc_action.setCheckable(True)
        self.alignc_action.t__.c..(lambda: self.editor.setAlignment(__.AlignCenter))
        format_toolbar.aA..(self.alignc_action)
        format_menu.aA..(self.alignc_action)

        self.alignr_action _ ?A..(QIcon(__.p__ .join('images', 'edit-alignment-right.png')), "Align right", self)
        self.alignr_action.setStatusTip("Align text right")
        self.alignr_action.setCheckable(True)
        self.alignr_action.t__.c..(lambda: self.editor.setAlignment(__.AlignRight))
        format_toolbar.aA..(self.alignr_action)
        format_menu.aA..(self.alignr_action)

        self.alignj_action _ ?A..(QIcon(__.p__ .join('images', 'edit-alignment-justify.png')), "Justify", self)
        self.alignj_action.setStatusTip("Justify text")
        self.alignj_action.setCheckable(True)
        self.alignj_action.t__.c..(lambda: self.editor.setAlignment(__.AlignJustify))
        format_toolbar.aA..(self.alignj_action)
        format_menu.aA..(self.alignj_action)

        format_group _ QActionGroup(self)
        format_group.setExclusive(True)
        format_group.aA..(self.alignl_action)
        format_group.aA..(self.alignc_action)
        format_group.aA..(self.alignr_action)
        format_group.aA..(self.alignj_action)

        format_menu.addSeparator()

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions _ [
            self.fonts,
            self.fontsize,
            self.bold_action,
            self.italic_action,
            self.underline_action,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        # Initialize.
        self.update_format()
        self.update_title()
        self.s..

    ___ block_signals  objects, b):
        for o in objects:
            o.blockSignals(b)

    ___ update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        self.fonts.setCurrentFont(self.editor.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

        self.italic_action.setChecked(self.editor.fontItalic())
        self.underline_action.setChecked(self.editor.fontUnderline())
        self.bold_action.setChecked(self.editor.fontWeight() == QFont.Bold)

        self.alignl_action.setChecked(self.editor.alignment() == __.AlignLeft)
        self.alignc_action.setChecked(self.editor.alignment() == __.AlignCenter)
        self.alignr_action.setChecked(self.editor.alignment() == __.AlignRight)
        self.alignj_action.setChecked(self.editor.alignment() == __.AlignJustify)

        self.block_signals(self._format_actions, False)

    ___ dialog_critical  s):
        dlg _ ?MB..(self)
        dlg.sT..(s)
        dlg.setIcon(?MB...Critical)
        dlg.s..

    ___ file_open(self):
        path, _ _ ?FD...gOFN..  "Open file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")

        try:
            w__ o..(path, 'rU') __ f:
                t__ _ f.read()

        except Exception __ e:
            self.dialog_critical(str(e))

        ____
            self.path _ path
            # Qt will automatically try and guess the format as txt/html
            self.editor.sT..(t__)
            self.update_title()

    ___ file_save(self):
        __ self.path __ N..:
            # If we do not have a path, we need to use Save As.
            r_ self.file_saveas()

        t__ _ self.editor.toHtml() __ splitext(self.path) in HTML_EXTENSIONS else self.editor.toPlainText()

        try:
            w__ o..(self.path, 'w') __ f:
                f.w..(t__)

        except Exception __ e:
            self.dialog_critical(str(e))

    ___ file_saveas(self):
        path, _ _ ?FD...getSaveFileName  "Save file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")

        __ no. path:
            # If dialog is cancelled, will return ''
            r_

        t__ _ self.editor.toHtml() __ splitext(path) in HTML_EXTENSIONS else self.editor.toPlainText()

        try:
            w__ o..(path, 'w') __ f:
                f.w..(t__)

        except Exception __ e:
            self.dialog_critical(str(e))

        ____
            self.path _ path
            self.update_title()

    ___ file_print(self):
        dlg _ QPrintDialog()
        __ dlg.exec_
            self.editor.print_(dlg.printer())

    ___ update_title(self):
        self.setWindowTitle("%s - Megasolid Idiom" % (__.p__ .basename(self.path) __ self.path else "Untitled"))

    ___ edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 __ self.editor.lineWrapMode() == 0 else 0 )


__ __name__ == '__main__':

    app _ ?A..(___.argv)
    app.sAN..("Megasolid Idiom")

    window _ MainWindow()
    app.e..