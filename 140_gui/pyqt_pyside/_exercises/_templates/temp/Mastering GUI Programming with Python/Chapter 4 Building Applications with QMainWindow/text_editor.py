______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ SettingsDialog(qtw.QDialog):
    """Dialog for setting the settings"""

    ___  -   settings, parent_None):
        s_. - (parent, modal_True)
        sL..(qtw.QFormLayout())
        settings _ settings
        layout().addRow(
            qtw.QLabel('<h1>Application Settings</h1>'),
        )
        show_warnings_cb _ qtw.QCheckBox(
            #checked=settings.get('show_warnings')
            checked_settings.value('show_warnings', type_bool)
        )
        layout().addRow("Show Warnings", show_warnings_cb)

        accept_btn _ qtw.?PB..('Ok', c___self.accept)
        cancel_btn _ qtw.?PB..('Cancel', c___self.reject)
        layout().addRow(accept_btn, cancel_btn)

    ___ accept
        #self.settings['show_warnings'] = self.show_warnings_cb.isChecked()
        settings.setValue(
            'show_warnings',
            show_warnings_cb.isChecked()
        )
        print(settings.value('show_warnings'))
        s_.accept()


c_ MainWindow(qtw.QMainWindow): # change to mainwindow

    #settings = {'show_warnings': True}
    settings _ qtc.QSettings('Alan D Moore', 'text editor')

    ___  - 
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here

        ######################
        # The central widget #
        ######################
        textedit _ qtw.QTextEdit()
        sCW..(textedit)

        #################
        # The Statusbar #
        #################

        # The long way 'round
        #status_bar = qtw.QStatusBar()
        #self.setStatusBar(status_bar)
        #status_bar.showMessage('Welcome to text_editor.py')

        # The short way 'round
        statusBar().showMessage('Welcome to text_editor.py')

        # add widgets to statusbar
        charcount_label _ qtw.QLabel("chars: 0")
        textedit.textChanged.c..(
            lambda: charcount_label.sT..(
                "chars: " +
                str(le.(textedit.toPlainText()))
                )
            )
        statusBar().addPermanentWidget(charcount_label)

        ###############j
        # The menubar #
        ###############
        menubar _ mB..

        # add submenus to a menu
        file_menu _ menubar.aM..('File')
        edit_menu _ menubar.aM..('Edit')
        help_menu _ menubar.aM..('Help')

        # add actions
        open_action _ file_menu.aA..('Open')
        save_action _ file_menu.aA..('Save')

        # add separator
        file_menu.addSeparator()

        # add an action with a callback
        quit_action _ file_menu.aA..('Quit', destroy)

        # connect to a Qt Slot
        edit_menu.aA..('Undo', textedit.undo)

        # create a QAction manually

        redo_action _ qtw.?A..('Redo', self)
        redo_action.t__.c..(textedit.redo)
        edit_menu.aA..(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################

        toolbar _ addToolBar('File')
        #toolbar.addAction(open_action)
        #toolbar.addAction("Save")

        toolbar.setMovable F..
        toolbar.setFloatable F..
        toolbar.setAllowedAreas(
            qtc.__.TopToolBarArea |
            qtc.__.BottomToolBarArea
        )

        # Add with icons
        open_icon _ style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon _ style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        toolbar.aA..(open_action)
        toolbar.aA..(
            save_icon,
            'Save',
            lambda: statusBar().showMessage('File Saved!')
        )

        # create a custom QAction

        help_action _ qtw.?A..(
            style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
            'Help',
            self,  # important to pass the parent!
            triggered_lambda: statusBar().showMessage(
                'Sorry, no help yet!'
            )
        )
        toolbar.aA..(help_action)

        # create a toolbar in another part of the screen:
        toolbar2 _ qtw.QToolBar('Edit')
        addToolBar(qtc.__.RightToolBarArea, toolbar2)
        toolbar2.aA..('Copy', textedit.copy)
        toolbar2.aA..('Cut', textedit.cut)
        toolbar2.aA..('Paste', textedit.paste)


        ################
        # Dock Widgets #
        ################

        dock _ qtw.QDockWidget("Replace")
        addDockWidget(qtc.__.LeftDockWidgetArea, dock)

        # make it not closable
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        replace_widget _ qtw.?W..
        replace_widget.sL.. ?.?VBL..
        dock.setWidget(replace_widget)

        search_text_inp _ ?.?LE..(placeholderText_'search')
        replace_text_inp _ ?.?LE..(placeholderText_'replace')
        search_and_replace_btn _ qtw.?PB..(
            "Search and Replace",
            c___self.search_and_replace
            )
        replace_widget.layout().aW..(search_text_inp)
        replace_widget.layout().aW..(replace_text_inp)
        replace_widget.layout().aW..(search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################

        # QMessageBox
        help_menu.aA..('About', showAboutDialog)

        __ settings.value('show_warnings', False, type_bool):
            response _ qtw.?MB...q..(
                self,
                'My Text Editor',
                'This is beta software, do you want to continue?',
                qtw.?MB...Yes | qtw.?MB...Abort
            )
            __ response == qtw.?MB...Abort:
                close()
                ___.e..

            # custom message box

            splash_screen _ qtw.?MB..
            splash_screen.setWindowTitle('My Text Editor')
            splash_screen.sT..('BETA SOFTWARE WARNING!')
            splash_screen.setInformativeText(
                'This is very, very beta, '
                'are you really sure you want to use it?'
            )
            splash_screen.setDetailedText(
                'This editor was written for pedagogical '
                'purposes, and probably is not fit for real work.'
            )
            splash_screen.setWindowModality(qtc.__.WindowModal)
            splash_screen.addButton(qtw.?MB...Yes)
            splash_screen.addButton(qtw.?MB...Abort)
            response _ splash_screen.e..
            __ response == qtw.?MB...Abort:
                close()
                ___.e..

        # QFileDialog
        open_action.t__.c..(openFile)
        save_action.t__.c..(saveFile)

        # QFontDialog

        edit_menu.aA..('Set Font…', set_font)

        # Custom dialog
        edit_menu.aA..('Settings…', show_settings)

        ###################
        # Saving Settings #
        ###################


        # End main UI code
        s..

    ___ search_and_replace
        s_text _ search_text_inp.t__()
        r_text _ replace_text_inp.t__()

        __ s_text:
            textedit.sT..(
                textedit.toPlainText().replace(s_text, r_text)
                )

    ___ showAboutDialog
        qtw.?MB...about(
            self,
            "About text_editor.py",
            "This is a text editor written in PyQt5."
        )

    ___ openFile
        filename, _ _ qtw.?FD...gOFN..(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)',
            'Python Files (*.py)',
            qtw.?FD...DontUseNativeDialog |
            qtw.?FD...DontResolveSymlinks
        )
        __ filename:
            try:
                w__ o..(filename, 'r') __ fh:
                    textedit.sT..(fh.r..
            except Exception __ e:
                qtw.?MB...critical(f"Could not load file: {e}")

    ___ saveFile
        filename, _ _ qtw.?FD...getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)'
        )
        __ filename:
            try:
                w__ o..(filename, 'w') __ fh:
                    fh.w..(textedit.tPT..
            except Exception __ e:
                qtw.?MB...critical(f"Could not save file: {e}")

    ___ set_font
        current _ textedit.currentFont()
        font, accepted _ qtw.QFontDialog.getFont(
            current,
            self,
            options_(
                qtw.QFontDialog.DontUseNativeDialog |
                qtw.QFontDialog.MonospacedFonts
            )
        )
        __ accepted:
            textedit.setCurrentFont(font)

    ___ show_settings

        settings_dialog _ SettingsDialog(settings, self)
        settings_dialog.exec()


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
