____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.?PS.. ______ *

______ __
______ ___
______ uuid

FONT_SIZES _ [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS _ ['.jpg','.png','.bmp']
HTML_EXTENSIONS _ ['.htm', '.html']

___ hexuuid
    r_ uuid.uuid4().hex

___ splitext(p):
    r_ __.p__ .splitext(p)[1].lower()

c_ TextEdit(?TE..):

    ___ canInsertFromMimeData  source):

        __ source.hasImage
            r_ T..
        ____
            r_ s__(TextEdit, self).canInsertFromMimeData(source)

    ___ insertFromMimeData  source):

        cursor _ textCursor()
        document _ document()

        __ source.hasUrls

            ___ u __ source.urls
                file_ext _ splitext(st.(u.toLocalFile()))
                __ u.isLocalFile() and file_ext __ IMAGE_EXTENSIONS:
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

        s__(TextEdit, self).insertFromMimeData(source)


c_ MainWindow ?MW..

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)

        layout _ ?VBL..
        editor _ TextEdit()
        # Setup the QTextEdit editor configuration
        editor.setAutoFormatting(?TE...AutoAll)
        editor.sC__.c..(update_format)
        # Initialize default font size.
        font _ ?F..('Times', 12)
        editor.sF..(font)
        # We need to repeat the size to init the current format.
        editor.setFontPointSize(12)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        pa__ _ N..

        layout.aW..(editor)

        container _ ?W..
        container.sL..(layout)
        sCW..(container)

        status _ ?SB..
        sSB..(status)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_toolbar _ QToolBar("File")
        file_toolbar.setIconSize(?S..(14, 14))
        aTB..(file_toolbar)
        file_menu _ mB.. .aM..("&File")

        open_file_action _ ?A..(?I..(__.p__ .join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.sST..("Open file")
        open_file_action.t__.c..(file_open)
        file_menu.aA..(open_file_action)
        file_toolbar.aA..(open_file_action)

        save_file_action _ ?A..(?I..(__.p__ .join('images', 'disk.png')), "Save", self)
        save_file_action.sST..("Save current page")
        save_file_action.t__.c..(file_save)
        file_menu.aA..(save_file_action)
        file_toolbar.aA..(save_file_action)

        saveas_file_action _ ?A..(?I..(__.p__ .join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.sST..("Save current page to specified file")
        saveas_file_action.t__.c..(file_saveas)
        file_menu.aA..(saveas_file_action)
        file_toolbar.aA..(saveas_file_action)

        print_action _ ?A..(?I..(__.p__ .join('images', 'printer.png')), "Print...", self)
        print_action.sST..("Print current page")
        print_action.t__.c..(file_print)
        file_menu.aA..(print_action)
        file_toolbar.aA..(print_action)

        edit_toolbar _ QToolBar("Edit")
        edit_toolbar.setIconSize(?S..(16, 16))
        aTB..(edit_toolbar)
        edit_menu _ mB.. .aM..("&Edit")

        undo_action _ ?A..(?I..(__.p__ .join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.sST..("Undo last change")
        undo_action.t__.c..(editor.undo)
        edit_menu.aA..(undo_action)

        redo_action _ ?A..(?I..(__.p__ .join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.sST..("Redo last change")
        redo_action.t__.c..(editor.redo)
        edit_toolbar.aA..(redo_action)
        edit_menu.aA..(redo_action)

        edit_menu.aS..)

        cut_action _ ?A..(?I..(__.p__ .join('images', 'scissors.png')), "Cut", self)
        cut_action.sST..("Cut selected text")
        cut_action.sS..(?KS...Cut)
        cut_action.t__.c..(editor.cut)
        edit_toolbar.aA..(cut_action)
        edit_menu.aA..(cut_action)

        copy_action _ ?A..(?I..(__.p__ .join('images', 'document-copy.png')), "Copy", self)
        copy_action.sST..("Copy selected text")
        cut_action.sS..(?KS...Copy)
        copy_action.t__.c..(editor.copy)
        edit_toolbar.aA..(copy_action)
        edit_menu.aA..(copy_action)

        paste_action _ ?A..(?I..(__.p__ .join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.sST..("Paste from clipboard")
        cut_action.sS..(?KS...Paste)
        paste_action.t__.c..(editor.paste)
        edit_toolbar.aA..(paste_action)
        edit_menu.aA..(paste_action)

        select_action _ ?A..(?I..(__.p__ .join('images', 'selection-input.png')), "Select all", self)
        select_action.sST..("Select all text")
        cut_action.sS..(?KS...SelectAll)
        select_action.t__.c..(editor.selectAll)
        edit_menu.aA..(select_action)

        edit_menu.aS..)

        wrap_action _ ?A..(?I..(__.p__ .join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.sST..("Toggle wrap text to window")
        wrap_action.setCheckable( st.
        wrap_action.sC__( st.
        wrap_action.t__.c..(edit_toggle_wrap)
        edit_menu.aA..(wrap_action)

        format_toolbar _ QToolBar("Format")
        format_toolbar.setIconSize(?S..(16, 16))
        aTB..(format_toolbar)
        format_menu _ mB.. .aM..("&Format")

        # We need references to these actions/settings to update as selection changes, so attach to self.
        fonts _ QFontComboBox()
        fonts.currentFontChanged.c..(editor.setCurrentFont)
        format_toolbar.aW..(fonts)

        fontsize _ ?CB()
        fontsize.aI..([st.(s) ___ s __ FONT_SIZES])

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        fontsize.currentIndexChanged[st.].c..(l___ s: editor.setFontPointSize(fl..(s)) )
        format_toolbar.aW..(fontsize)

        bold_action _ ?A..(?I..(__.p__ .join('images', 'edit-bold.png')), "Bold", self)
        bold_action.sST..("Bold")
        bold_action.sS..(?KS...Bold)
        bold_action.setCheckable( st.
        bold_action.t__.c..(l___ x: editor.setFontWeight(?F...Bold __ x ____ ?F...Normal))
        format_toolbar.aA..(bold_action)
        format_menu.aA..(bold_action)

        italic_action _ ?A..(?I..(__.p__ .join('images', 'edit-italic.png')), "Italic", self)
        italic_action.sST..("Italic")
        italic_action.sS..(?KS...Italic)
        italic_action.setCheckable( st.
        italic_action.t__.c..(editor.setFontItalic)
        format_toolbar.aA..(italic_action)
        format_menu.aA..(italic_action)

        underline_action _ ?A..(?I..(__.p__ .join('images', 'edit-underline.png')), "Underline", self)
        underline_action.sST..("Underline")
        underline_action.sS..(?KS...Underline)
        underline_action.setCheckable( st.
        underline_action.t__.c..(editor.setFontUnderline)
        format_toolbar.aA..(underline_action)
        format_menu.aA..(underline_action)

        format_menu.aS..)

        alignl_action _ ?A..(?I..(__.p__ .join('images', 'edit-alignment.png')), "Align left", self)
        alignl_action.sST..("Align text left")
        alignl_action.setCheckable( st.
        alignl_action.t__.c..(l___: editor.setAlignment(__.AlignLeft))
        format_toolbar.aA..(alignl_action)
        format_menu.aA..(alignl_action)

        alignc_action _ ?A..(?I..(__.p__ .join('images', 'edit-alignment-center.png')), "Align center", self)
        alignc_action.sST..("Align text center")
        alignc_action.setCheckable( st.
        alignc_action.t__.c..(l___: editor.setAlignment(__.AlignCenter))
        format_toolbar.aA..(alignc_action)
        format_menu.aA..(alignc_action)

        alignr_action _ ?A..(?I..(__.p__ .join('images', 'edit-alignment-right.png')), "Align right", self)
        alignr_action.sST..("Align text right")
        alignr_action.setCheckable( st.
        alignr_action.t__.c..(l___: editor.setAlignment(__.AlignRight))
        format_toolbar.aA..(alignr_action)
        format_menu.aA..(alignr_action)

        alignj_action _ ?A..(?I..(__.p__ .join('images', 'edit-alignment-justify.png')), "Justify", self)
        alignj_action.sST..("Justify text")
        alignj_action.setCheckable( st.
        alignj_action.t__.c..(l___: editor.setAlignment(__.AlignJustify))
        format_toolbar.aA..(alignj_action)
        format_menu.aA..(alignj_action)

        format_group _ QActionGroup
        format_group.setExclusive( st.
        format_group.aA..(alignl_action)
        format_group.aA..(alignc_action)
        format_group.aA..(alignr_action)
        format_group.aA..(alignj_action)

        format_menu.aS..)

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        _format_actions _ [
            fonts,
            fontsize,
            bold_action,
            italic_action,
            underline_action,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        # Initialize.
        update_format()
        update_title()
        s..

    ___ block_signals  objects, b):
        ___ o __ objects:
            o.blockSignals(b)

    ___ update_format
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        block_signals(_format_actions,  st.

        fonts.setCurrentFont(editor.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        fontsize.sCT..(st.(in.(editor.fontPointSize())))

        italic_action.sC__(editor.fontItalic())
        underline_action.sC__(editor.fontUnderline())
        bold_action.sC__(editor.fontWeight() __ ?F...Bold)

        alignl_action.sC__(editor.alignment() __ __.AlignLeft)
        alignc_action.sC__(editor.alignment() __ __.AlignCenter)
        alignr_action.sC__(editor.alignment() __ __.AlignRight)
        alignj_action.sC__(editor.alignment() __ __.AlignJustify)

        block_signals(_format_actions, F..)

    ___ dialog_critical  s):
        dlg _ ?MB..
        dlg.sT..(s)
        dlg.sI..(?MB...Critical)
        dlg.s..

    ___ file_open
        pa__, _ _ ?FD...gOFN..  "Open file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")

        ___
            w__ o..(pa__, 'rU') __ f:
                t__ _ f.r..

        _____ E.. __ e:
            dialog_critical(st.(e))

        ____
            pa__ _ pa__
            # Qt will automatically try and guess the format as txt/html
            editor.sT..(t__)
            update_title()

    ___ file_save
        __ pa__ __ N..:
            # If we do not have a path, we need to use Save As.
            r_ file_saveas()

        t__ _ editor.toHtml() __ splitext(pa__) __ HTML_EXTENSIONS ____ editor.toPlainText()

        ___
            w__ o..(pa__, 'w') __ f:
                f.w..(t__)

        _____ E.. __ e:
            dialog_critical(st.(e))

    ___ file_saveas
        pa__, _ _ ?FD...getSaveFileName  "Save file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")

        __ no. pa__:
            # If dialog is cancelled, will return ''
            r_

        t__ _ editor.toHtml() __ splitext(pa__) __ HTML_EXTENSIONS ____ editor.toPlainText()

        ___
            w__ o..(pa__, 'w') __ f:
                f.w..(t__)

        _____ E.. __ e:
            dialog_critical(st.(e))

        ____
            pa__ _ pa__
            update_title()

    ___ file_print
        dlg _ QPrintDialog()
        __ dlg.e..
            editor.print_(dlg.printer())

    ___ update_title
        sWT..("%s - Megasolid Idiom" % (__.p__ .basename(pa__) __ pa__ ____ "Untitled"))

    ___ edit_toggle_wrap
        editor.setLineWrapMode( 1 __ editor.lineWrapMode() __ 0 ____ 0 )


__ ______ __ ______

    app _ ?A..(___.a..
    app.sAN..("Megasolid Idiom")

    window _ MainWindow()
    app.e..