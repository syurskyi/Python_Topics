____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.?PS.. ______ *

______ __
______ ___


c_ MainWindow ?MW..

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)

        layout _ ?VBL..
        editor _ ?PTE..  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)


        # Setup the QTextEdit editor configuration
        fixedfont _ QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.sPS..(12)
        editor.sF..(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        pa__ _ N..

        layout.aW..(editor)

        container _ ?W..
        container.sL..(layout)
        sCW..(container)

        status _ ?SB..
        sSB..(status)

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
        cut_action.t__.c..(editor.cut)
        edit_toolbar.aA..(cut_action)
        edit_menu.aA..(cut_action)

        copy_action _ ?A..(?I..(__.p__ .join('images', 'document-copy.png')), "Copy", self)
        copy_action.sST..("Copy selected text")
        copy_action.t__.c..(editor.copy)
        edit_toolbar.aA..(copy_action)
        edit_menu.aA..(copy_action)

        paste_action _ ?A..(?I..(__.p__ .join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.sST..("Paste from clipboard")
        paste_action.t__.c..(editor.paste)
        edit_toolbar.aA..(paste_action)
        edit_menu.aA..(paste_action)

        select_action _ ?A..(?I..(__.p__ .join('images', 'selection-input.png')), "Select all", self)
        select_action.sST..("Select all text")
        select_action.t__.c..(editor.selectAll)
        edit_menu.aA..(select_action)

        edit_menu.aS..)

        wrap_action _ ?A..(?I..(__.p__ .join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.sST..("Toggle wrap text to window")
        wrap_action.setCheckable( st.
        wrap_action.sC__( st.
        wrap_action.t__.c..(edit_toggle_wrap)
        edit_menu.aA..(wrap_action)

        update_title()
        s..

    ___ dialog_critical  s):
        dlg _ ?MB..
        dlg.sT..(s)
        dlg.sI..(?MB...Critical)
        dlg.s..

    ___ file_open
        pa__, _ _ ?FD...gOFN..  "Open file", "", "Text documents (*.txt);All files (*.*)")

        __ pa__:
            ___
                w__ o..(pa__, 'rU') __ f:
                    t__ _ f.r..

            _____ E.. __ e:
                dialog_critical(st.(e))

            ____
                pa__ _ pa__
                editor.sPT..(t__)
                update_title()

    ___ file_save
        __ pa__ __ N..:
            # If we do not have a path, we need to use Save As.
            r_ file_saveas()

        _save_to_path(pa__)

    ___ file_saveas
        pa__, _ _ ?FD...getSaveFileName  "Save file", "", "Text documents (*.txt);All files (*.*)")

        __ no. pa__:
            # If dialog is cancelled, will return ''
            r_

        _save_to_path(pa__)

    ___ _save_to_path  pa__):
        t__ _ editor.toPlainText()
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
        sWT..("%s - No2Pads" % (__.p__ .basename(pa__) __ pa__ ____ "Untitled"))

    ___ edit_toggle_wrap
        editor.setLineWrapMode( 1 __ editor.lineWrapMode() __ 0 ____ 0 )


__ ______ __ ______

    app _ ?A..(___.a..
    app.sAN..("No2Pads")

    window _ MainWindow()
    app.e..