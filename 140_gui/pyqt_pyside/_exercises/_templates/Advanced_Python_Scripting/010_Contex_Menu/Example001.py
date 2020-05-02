____ PySide _____ ?C.., QtGui


c_ MainWindow(QtGui.QMainWindow
    ___  -  
        super(MainWindow, self). - ()

        widget _ QtGui.?W..()
        setCentralWidget(widget)

        topFiller _ QtGui.?W..()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        infoLabel _ QtGui.QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment_?C...Qt.AlignCenter)
        infoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)

        bottomFiller _ QtGui.?W..()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        vbox _ QtGui.QVBoxLayout()
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
        menu _ QtGui.QMenu
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
        QtGui.QMessageBox.about , "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    ___ aboutQt 
        infoLabel.sT..("Invoked <b>Help|About Qt</b>")

    ___ createActions 
        newAct _ QtGui.QAction("&New", self,
                shortcut_QtGui.QKeySequence.New,
                statusTip_"Create a new file", triggered_newFile)

        openAct _ QtGui.QAction("&Open...", self,
                shortcut_QtGui.QKeySequence.Open,
                statusTip_"Open an existing file", triggered_open)

        saveAct _ QtGui.QAction("&Save", self,
                shortcut_QtGui.QKeySequence.Save,
                statusTip_"Save the document to disk", triggered_save)

        printAct _ QtGui.QAction("&Print...", self,
                shortcut_QtGui.QKeySequence.Print,
                statusTip_"Print the document", triggered_print_)

        exitAct _ QtGui.QAction("E&xit", self, shortcut_"Ctrl+Q",
                statusTip_"Exit the application", triggered_close)

        undoAct _ QtGui.QAction("&Undo", self,
                shortcut_QtGui.QKeySequence.Undo,
                statusTip_"Undo the last operation", triggered_undo)

        redoAct _ QtGui.QAction("&Redo", self,
                shortcut_QtGui.QKeySequence.Redo,
                statusTip_"Redo the last operation", triggered_redo)

        cutAct _ QtGui.QAction("Cu&t", self,
                shortcut_QtGui.QKeySequence.Cut,
                statusTip_"Cut the current selection's contents to the clipboard",
                triggered_cut)

        copyAct _ QtGui.QAction("&Copy", self,
                shortcut_QtGui.QKeySequence.Copy,
                statusTip_"Copy the current selection's contents to the clipboard",
                triggered_copy)

        pasteAct _ QtGui.QAction("&Paste", self,
                shortcut_QtGui.QKeySequence.Paste,
                statusTip_"Paste the clipboard's contents into the current selection",
                triggered_paste)

        boldAct _ QtGui.QAction("&Bold", self, checkable_T..,
                shortcut_"Ctrl+B", statusTip_"Make the text bold",
                triggered_bold)

        boldFont _ boldAct.font()
        boldFont.setBold(T..)
        boldAct.setFont(boldFont)

        italicAct _ QtGui.QAction("&Italic", self, checkable_T..,
                shortcut_"Ctrl+I", statusTip_"Make the text italic",
                triggered_italic)

        italicFont _ italicAct.font()
        italicFont.setItalic(T..)
        italicAct.setFont(italicFont)

        setLineSpacingAct _ QtGui.QAction("Set &Line Spacing...", self,
                statusTip_"Change the gap between the lines of a paragraph",
                triggered_setLineSpacing)

        setParagraphSpacingAct _ QtGui.QAction(
                "Set &Paragraph Spacing...", self,
                statusTip_"Change the gap between paragraphs",
                triggered_setParagraphSpacing)

        aboutAct _ QtGui.QAction("&About", self,
                statusTip_"Show the application's About box",
                triggered_about)

        aboutQtAct _ QtGui.QAction("About &Qt", self,
                statusTip_"Show the Qt library's About box",
                triggered_aboutQt)
        aboutQtAct.triggered.c..(QtGui.qApp.aboutQt)

        leftAlignAct _ QtGui.QAction("&Left Align", self, checkable_T..,
                shortcut_"Ctrl+L", statusTip_"Left align the selected text",
                triggered_leftAlign)

        rightAlignAct _ QtGui.QAction("&Right Align", self,
                checkable_T.., shortcut_"Ctrl+R",
                statusTip_"Right align the selected text",
                triggered_rightAlign)

        justifyAct _ QtGui.QAction("&Justify", self, checkable_T..,
                shortcut_"Ctrl+J", statusTip_"Justify the selected text",
                triggered_justify)

        centerAct _ QtGui.QAction("&Center", self, checkable_T..,
                shortcut_"Ctrl+C", statusTip_"Center the selected text",
                triggered_center)

        alignmentGroup _ QtGui.QActionGroup
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

    app _ QtGui.?A..(___.argv)
    window _ MainWindow()
    window.s..
___.e..(app.e