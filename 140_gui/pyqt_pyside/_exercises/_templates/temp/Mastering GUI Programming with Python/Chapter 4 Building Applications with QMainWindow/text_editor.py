______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc


class SettingsDialog(qtw.QDialog):
    """Dialog for setting the settings"""

    ___ __init__(self, settings, parent_None):
        super().__init__(parent, modal_True)
        self.setLayout(qtw.QFormLayout())
        self.settings _ settings
        self.layout().addRow(
            qtw.QLabel('<h1>Application Settings</h1>'),
        )
        self.show_warnings_cb _ qtw.QCheckBox(
            #checked=settings.get('show_warnings')
            checked_settings.value('show_warnings', type_bool)
        )
        self.layout().addRow("Show Warnings", self.show_warnings_cb)

        self.accept_btn _ qtw.?PB..('Ok', c___self.accept)
        self.cancel_btn _ qtw.?PB..('Cancel', c___self.reject)
        self.layout().addRow(self.accept_btn, self.cancel_btn)

    ___ accept(self):
        #self.settings['show_warnings'] = self.show_warnings_cb.isChecked()
        self.settings.setValue(
            'show_warnings',
            self.show_warnings_cb.isChecked()
        )
        print(self.settings.value('show_warnings'))
        super().accept()


class MainWindow(qtw.QMainWindow): # change to mainwindow

    #settings = {'show_warnings': True}
    settings _ qtc.QSettings('Alan D Moore', 'text editor')

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        ######################
        # The central widget #
        ######################
        self.textedit _ qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        #################
        # The Statusbar #
        #################

        # The long way 'round
        #status_bar = qtw.QStatusBar()
        #self.setStatusBar(status_bar)
        #status_bar.showMessage('Welcome to text_editor.py')

        # The short way 'round
        self.statusBar().showMessage('Welcome to text_editor.py')

        # add widgets to statusbar
        charcount_label _ qtw.QLabel("chars: 0")
        self.textedit.textChanged.c..(
            lambda: charcount_label.sT..(
                "chars: " +
                str(len(self.textedit.toPlainText()))
                )
            )
        self.statusBar().addPermanentWidget(charcount_label)

        ###############j
        # The menubar #
        ###############
        menubar _ self.menuBar()

        # add submenus to a menu
        file_menu _ menubar.addMenu('File')
        edit_menu _ menubar.addMenu('Edit')
        help_menu _ menubar.addMenu('Help')

        # add actions
        open_action _ file_menu.addAction('Open')
        save_action _ file_menu.addAction('Save')

        # add separator
        file_menu.addSeparator()

        # add an action with a callback
        quit_action _ file_menu.addAction('Quit', self.destroy)

        # connect to a Qt Slot
        edit_menu.addAction('Undo', self.textedit.undo)

        # create a QAction manually

        redo_action _ qtw.QAction('Redo', self)
        redo_action.triggered.c..(self.textedit.redo)
        edit_menu.addAction(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################

        toolbar _ self.addToolBar('File')
        #toolbar.addAction(open_action)
        #toolbar.addAction("Save")

        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setAllowedAreas(
            qtc.Qt.TopToolBarArea |
            qtc.Qt.BottomToolBarArea
        )

        # Add with icons
        open_icon _ self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon _ self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        toolbar.addAction(open_action)
        toolbar.addAction(
            save_icon,
            'Save',
            lambda: self.statusBar().showMessage('File Saved!')
        )

        # create a custom QAction

        help_action _ qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
            'Help',
            self,  # important to pass the parent!
            triggered_lambda: self.statusBar().showMessage(
                'Sorry, no help yet!'
            )
        )
        toolbar.addAction(help_action)

        # create a toolbar in another part of the screen:
        toolbar2 _ qtw.QToolBar('Edit')
        self.addToolBar(qtc.Qt.RightToolBarArea, toolbar2)
        toolbar2.addAction('Copy', self.textedit.copy)
        toolbar2.addAction('Cut', self.textedit.cut)
        toolbar2.addAction('Paste', self.textedit.paste)


        ################
        # Dock Widgets #
        ################

        dock _ qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)

        # make it not closable
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        replace_widget _ qtw.QWidget()
        replace_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(replace_widget)

        self.search_text_inp _ qtw.QLineEdit(placeholderText_'search')
        self.replace_text_inp _ qtw.QLineEdit(placeholderText_'replace')
        search_and_replace_btn _ qtw.?PB..(
            "Search and Replace",
            c___self.search_and_replace
            )
        replace_widget.layout().addWidget(self.search_text_inp)
        replace_widget.layout().addWidget(self.replace_text_inp)
        replace_widget.layout().addWidget(search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################

        # QMessageBox
        help_menu.addAction('About', self.showAboutDialog)

        if self.settings.value('show_warnings', False, type_bool):
            response _ qtw.QMessageBox.question(
                self,
                'My Text Editor',
                'This is beta software, do you want to continue?',
                qtw.QMessageBox.Yes | qtw.QMessageBox.Abort
            )
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

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
            splash_screen.setWindowModality(qtc.Qt.WindowModal)
            splash_screen.addButton(qtw.QMessageBox.Yes)
            splash_screen.addButton(qtw.QMessageBox.Abort)
            response _ splash_screen.e..
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

        # QFileDialog
        open_action.triggered.c..(self.openFile)
        save_action.triggered.c..(self.saveFile)

        # QFontDialog

        edit_menu.addAction('Set Font…', self.set_font)

        # Custom dialog
        edit_menu.addAction('Settings…', self.show_settings)

        ###################
        # Saving Settings #
        ###################


        # End main UI code
        self.s..

    ___ search_and_replace(self):
        s_text _ self.search_text_inp.text()
        r_text _ self.replace_text_inp.text()

        if s_text:
            self.textedit.sT..(
                self.textedit.toPlainText().replace(s_text, r_text)
                )

    ___ showAboutDialog(self):
        qtw.QMessageBox.about(
            self,
            "About text_editor.py",
            "This is a text editor written in PyQt5."
        )

    ___ openFile(self):
        filename, _ _ qtw.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)',
            'Python Files (*.py)',
            qtw.QFileDialog.DontUseNativeDialog |
            qtw.QFileDialog.DontResolveSymlinks
        )
        if filename:
            try:
                with open(filename, 'r') as fh:
                    self.textedit.sT..(fh.read())
            except Exception as e:
                qtw.QMessageBox.critical(f"Could not load file: {e}")

    ___ saveFile(self):
        filename, _ _ qtw.QFileDialog.getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)'
        )
        if filename:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.textedit.toPlainText())
            except Exception as e:
                qtw.QMessageBox.critical(f"Could not save file: {e}")

    ___ set_font(self):
        current _ self.textedit.currentFont()
        font, accepted _ qtw.QFontDialog.getFont(
            current,
            self,
            options_(
                qtw.QFontDialog.DontUseNativeDialog |
                qtw.QFontDialog.MonospacedFonts
            )
        )
        if accepted:
            self.textedit.setCurrentFont(font)

    ___ show_settings(self):

        settings_dialog _ SettingsDialog(self.settings, self)
        settings_dialog.exec()


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
