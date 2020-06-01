____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.QtCore ______ *
____ ?.QtPrintSupport ______ *

______ os
______ sys


c_ MainWindow ?MW..

    ___ __init__  *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout _ QVBoxLayout()
        self.editor _ ?PTE..  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)


        # Setup the QTextEdit editor configuration
        fixedfont _ QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path _ N..

        layout.addWidget(self.editor)

        container _ QWidget()
        container.setLayout(layout)
        self.sCW..(container)

        self.status _ QStatusBar()
        self.setStatusBar(self.status)

        file_toolbar _ QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu _ self.mB.. .aM..("&File")

        open_file_action _ ?A..(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.t__.c..(self.file_open)
        file_menu.aA..(open_file_action)
        file_toolbar.aA..(open_file_action)

        save_file_action _ ?A..(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.t__.c..(self.file_save)
        file_menu.aA..(save_file_action)
        file_toolbar.aA..(save_file_action)

        saveas_file_action _ ?A..(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.t__.c..(self.file_saveas)
        file_menu.aA..(saveas_file_action)
        file_toolbar.aA..(saveas_file_action)

        print_action _ ?A..(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.t__.c..(self.file_print)
        file_menu.aA..(print_action)
        file_toolbar.aA..(print_action)

        edit_toolbar _ QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu _ self.mB.. .aM..("&Edit")

        undo_action _ ?A..(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.t__.c..(self.editor.undo)
        edit_menu.aA..(undo_action)

        redo_action _ ?A..(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.t__.c..(self.editor.redo)
        edit_toolbar.aA..(redo_action)
        edit_menu.aA..(redo_action)

        edit_menu.addSeparator()

        cut_action _ ?A..(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.t__.c..(self.editor.cut)
        edit_toolbar.aA..(cut_action)
        edit_menu.aA..(cut_action)

        copy_action _ ?A..(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.t__.c..(self.editor.copy)
        edit_toolbar.aA..(copy_action)
        edit_menu.aA..(copy_action)

        paste_action _ ?A..(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.t__.c..(self.editor.paste)
        edit_toolbar.aA..(paste_action)
        edit_menu.aA..(paste_action)

        select_action _ ?A..(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.t__.c..(self.editor.selectAll)
        edit_menu.aA..(select_action)

        edit_menu.addSeparator()

        wrap_action _ ?A..(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.t__.c..(self.edit_toggle_wrap)
        edit_menu.aA..(wrap_action)

        self.update_title()
        self.s..

    ___ dialog_critical  s):
        dlg _ ?MB..(self)
        dlg.sT..(s)
        dlg.setIcon(?MB...Critical)
        dlg.s..

    ___ file_open(self):
        path, _ _ ?FD...gOFN..  "Open file", "", "Text documents (*.txt);All files (*.*)")

        __ path:
            try:
                w__ o..(path, 'rU') __ f:
                    text _ f.read()

            except Exception __ e:
                self.dialog_critical(str(e))

            ____
                self.path _ path
                self.editor.sPT..(text)
                self.update_title()

    ___ file_save(self):
        __ self.path __ N..:
            # If we do not have a path, we need to use Save As.
            r_ self.file_saveas()

        self._save_to_path(self.path)

    ___ file_saveas(self):
        path, _ _ ?FD...getSaveFileName  "Save file", "", "Text documents (*.txt);All files (*.*)")

        __ no. path:
            # If dialog is cancelled, will return ''
            r_

        self._save_to_path(path)

    ___ _save_to_path  path):
        text _ self.editor.toPlainText()
        try:
            w__ o..(path, 'w') __ f:
                f.w..(text)

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
        self.setWindowTitle("%s - No2Pads" % (os.path.basename(self.path) __ self.path else "Untitled"))

    ___ edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 __ self.editor.lineWrapMode() == 0 else 0 )


__ __name__ == '__main__':

    app _ ?A..(sys.argv)
    app.sAN..("No2Pads")

    window _ MainWindow()
    app.e..