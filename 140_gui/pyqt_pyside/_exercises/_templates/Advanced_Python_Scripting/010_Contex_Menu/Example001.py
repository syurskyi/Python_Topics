____ PySide _____ ?C.., ?G..


c_ MainWindow(?G...QMainWindow
    ___  -  
        super(MainWindow, self). - ()

        widget _ ?G...?W..()
        setCentralWidget(widget)

        topFiller _ ?G...?W..()
        topFiller.setSizePolicy(?G...QSizePolicy.Expanding,
                ?G...QSizePolicy.Expanding)

        infoLabel _ ?G...QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment_?C...Qt.AlignCenter)
        infoLabel.setFrameStyle(?G...QFrame.StyledPanel | ?G...QFrame.Sunken)

        bottomFiller _ ?G...?W..()
        bottomFiller.setSizePolicy(?G...QSizePolicy.Expanding,
                ?G...QSizePolicy.Expanding)

        vbox _ ?G...QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(topFiller)
        vbox.addWidget(infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        createActions()
        createMenus()

        message _ "A context menu is available by right-clicking"
        statusBar().showMessage(message)

        setWindowTitle("Menus")
        setMinimumSize(160,160)
        resize(480,320)

    ___ contextMenuEvent , event
        menu _ ?G...QMenu
        menu.addAction(cutAct)
        menu.addAction(copyAct)
        menu.addAction(pasteAct)
        menu.exec_(event.globalPos())

    ___ newFile 
        infoLabel.sT..("Invoked <b>File|New</b>")

    ___ open 
        infoLabel.sT..("Invoked <b>File|Open</b>")

    ___ save 
        infoLabel.sT..("Invoked <b>File|Save</b>")

    ___ print_ 
        infoLabel.sT..("Invoked <b>File|Print</b>")

    ___ undo 
        infoLabel.sT..("Invoked <b>Edit|Undo</b>")

    ___ redo 
        infoLabel.sT..("Invoked <b>Edit|Redo</b>")

    ___ cut 
        infoLabel.sT..("Invoked <b>Edit|Cut</b>")

    ___ copy 
        infoLabel.sT..("Invoked <b>Edit|Copy</b>")

    ___ paste 
        infoLabel.sT..("Invoked <b>Edit|Paste</b>")

    ___ bold 
        infoLabel.sT..("Invoked <b>Edit|Format|Bold</b>")

    ___ italic 
        infoLabel.sT..("Invoked <b>Edit|Format|Italic</b>")

    ___ leftAlign 
        infoLabel.sT..("Invoked <b>Edit|Format|Left Align</b>")

    ___ rightAlign 
        infoLabel.sT..("Invoked <b>Edit|Format|Right Align</b>")

    ___ justify 
        infoLabel.sT..("Invoked <b>Edit|Format|Justify</b>")

    ___ center 
        infoLabel.sT..("Invoked <b>Edit|Format|Center</b>")

    ___ setLineSpacing 
        infoLabel.sT..("Invoked <b>Edit|Format|Set Line Spacing</b>")

    ___ setParagraphSpacing 
        infoLabel.sT..("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    ___ about 
        infoLabel.sT..("Invoked <b>Help|About</b>")
        ?G...QMessageBox.about , "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    ___ aboutQt 
        infoLabel.sT..("Invoked <b>Help|About Qt</b>")

    ___ createActions 
        newAct _ ?G...QAction("&New", self,
                shortcut_?G...QKeySequence.New,
                statusTip_"Create a new file", triggered_newFile)

        openAct _ ?G...QAction("&Open...", self,
                shortcut_?G...QKeySequence.Open,
                statusTip_"Open an existing file", triggered_open)

        saveAct _ ?G...QAction("&Save", self,
                shortcut_?G...QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_save)

        printAct _ ?G...QAction("&Print...", self,
                shortcut_?G...QKeySequence.Print,
                statusTip_"Print the document", triggered_print_)

        exitAct _ ?G...QAction("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_close)

        undoAct _ ?G...QAction("&Undo", self,
                shortcut_?G...QKeySequence.Undo,
                statusTip_"Undo the last operation", triggered_undo)

        redoAct _ ?G...QAction("&Redo", self,
                shortcut_?G...QKeySequence.Redo,
                statusTip_"Redo the last operation", triggered_redo)

        cutAct _ ?G...QAction("Cu&t", self,
                shortcut_?G...QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_cut)

        copyAct _ ?G...QAction("&Copy", self,
                shortcut_?G...QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_copy)

        pasteAct _ ?G...QAction("&Paste", self,
                shortcut_?G...QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_paste)

        boldAct _ ?G...QAction("&Bold", self, checkable_T..,
                shortcut_"Ctrl+B", statusTip_"Make the text bold",
                triggered_bold)

        boldFont _ boldAct.font()
        boldFont.setBold(T..)
        boldAct.sF..(boldFont)

        italicAct _ ?G...QAction("&Italic", self, checkable_T..,
                shortcut_"Ctrl+I", statusTip_"Make the text italic",
                triggered_italic)

        italicFont _ italicAct.font()
        italicFont.setItalic(T..)
        italicAct.sF..(italicFont)

        setLineSpacingAct _ ?G...QAction("Set &Line Spacing...", self,
                statusTip_"Change the gap between the lines of a paragraph",
                triggered_setLineSpacing)

        setParagraphSpacingAct _ ?G...QAction(
                "Set &Paragraph Spacing...", self,
                statusTip_"Change the gap between paragraphs",
                triggered_setParagraphSpacing)

        aboutAct _ ?G...QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_about)

        aboutQtAct _ ?G...QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_aboutQt)
        aboutQtAct.triggered.c..(?G...qApp.aboutQt)

        leftAlignAct _ ?G...QAction("&Left Align", self, checkable_T..,
                shortcut_"Ctrl+L", statusTip_"Left align the selected text",
                triggered_leftAlign)

        rightAlignAct _ ?G...QAction("&Right Align", self,
                checkable_T.., shortcut_"Ctrl+R",
                statusTip_"Right align the selected text",
                triggered_rightAlign)

        justifyAct _ ?G...QAction("&Justify", self, checkable_T..,
                shortcut_"Ctrl+J", statusTip_"Justify the selected text",
                triggered_justify)

        centerAct _ ?G...QAction("&Center", self, checkable_T..,
                shortcut_"Ctrl+C", statusTip_"Center the selected text",
                triggered_center)

        alignmentGroup _ ?G...QActionGroup
        alignmentGroup.addAction(leftAlignAct)
        alignmentGroup.addAction(rightAlignAct)
        alignmentGroup.addAction(justifyAct)
        alignmentGroup.addAction(centerAct)
        leftAlignAct.setChecked(T..)

    ___ createMenus 
        fileMenu _ menuBar().addMenu("&File")
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        editMenu _ menuBar().addMenu("&Edit")
        editMenu.addAction(undoAct)
        editMenu.addAction(redoAct)
        editMenu.addSeparator()
        editMenu.addAction(cutAct)
        editMenu.addAction(copyAct)
        editMenu.addAction(pasteAct)
        editMenu.addSeparator()

        helpMenu _ menuBar().addMenu("&Help")
        helpMenu.addAction(aboutAct)
        helpMenu.addAction(aboutQtAct)

        formatMenu _ editMenu.addMenu("&Format")
        formatMenu.addAction(boldAct)
        formatMenu.addAction(italicAct)
        formatMenu.addSeparator().sT..("Alignment")
        formatMenu.addAction(leftAlignAct)
        formatMenu.addAction(rightAlignAct)
        formatMenu.addAction(justifyAct)
        formatMenu.addAction(centerAct)
        formatMenu.addSeparator()
        formatMenu.addAction(setLineSpacingAct)
        formatMenu.addAction(setParagraphSpacingAct)


__ __name__ __ '__main__':

    _____ ___

    app _ ?G...?A..(___.argv)
    window _ MainWindow()
    window.s..
___.e..(app.e