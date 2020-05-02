____ PySide _____ ?C.., QtGui


c_ MainWindow(QtGui.QMainWindow
    ___  -  
        super(MainWindow, self). - ()

        widget = QtGui.?W..()
        setCentralWidget(widget)

        topFiller = QtGui.?W..()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        infoLabel = QtGui.QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment=?C...Qt.AlignCenter)
        infoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)

        bottomFiller = QtGui.?W..()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(topFiller)
        vbox.addWidget(infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        createActions()
        createMenus()

        message = "A context menu is available by right-clicking"
        statusBar().showMessage(message)

        setWindowTitle("Menus")
        setMinimumSize(160,160)
        resize(480,320)

    ___ contextMenuEvent , event
        menu = QtGui.QMenu
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
        newAct = QtGui.QAction("&New", self,
                shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=newFile)

        openAct = QtGui.QAction("&Open...", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing file", triggered=open)

        saveAct = QtGui.QAction("&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the document to disk", triggered=save)

        printAct = QtGui.QAction("&Print...", self,
                shortcut=QtGui.QKeySequence.Print,
                statusTip="Print the document", triggered=print_)

        exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=close)

        undoAct = QtGui.QAction("&Undo", self,
                shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last operation", triggered=undo)

        redoAct = QtGui.QAction("&Redo", self,
                shortcut=QtGui.QKeySequence.Redo,
                statusTip="Redo the last operation", triggered=redo)

        cutAct = QtGui.QAction("Cu&t", self,
                shortcut=QtGui.QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=cut)

        copyAct = QtGui.QAction("&Copy", self,
                shortcut=QtGui.QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=copy)

        pasteAct = QtGui.QAction("&Paste", self,
                shortcut=QtGui.QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=paste)

        boldAct = QtGui.QAction("&Bold", self, checkable=T..,
                shortcut="Ctrl+B", statusTip="Make the text bold",
                triggered=bold)

        boldFont = boldAct.font()
        boldFont.setBold(T..)
        boldAct.setFont(boldFont)

        italicAct = QtGui.QAction("&Italic", self, checkable=T..,
                shortcut="Ctrl+I", statusTip="Make the text italic",
                triggered=italic)

        italicFont = italicAct.font()
        italicFont.setItalic(T..)
        italicAct.setFont(italicFont)

        setLineSpacingAct = QtGui.QAction("Set &Line Spacing...", self,
                statusTip="Change the gap between the lines of a paragraph",
                triggered=setLineSpacing)

        setParagraphSpacingAct = QtGui.QAction(
                "Set &Paragraph Spacing...", self,
                statusTip="Change the gap between paragraphs",
                triggered=setParagraphSpacing)

        aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=about)

        aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=aboutQt)
        aboutQtAct.triggered.c..(QtGui.qApp.aboutQt)

        leftAlignAct = QtGui.QAction("&Left Align", self, checkable=T..,
                shortcut="Ctrl+L", statusTip="Left align the selected text",
                triggered=leftAlign)

        rightAlignAct = QtGui.QAction("&Right Align", self,
                checkable=T.., shortcut="Ctrl+R",
                statusTip="Right align the selected text",
                triggered=rightAlign)

        justifyAct = QtGui.QAction("&Justify", self, checkable=T..,
                shortcut="Ctrl+J", statusTip="Justify the selected text",
                triggered=justify)

        centerAct = QtGui.QAction("&Center", self, checkable=T..,
                shortcut="Ctrl+C", statusTip="Center the selected text",
                triggered=center)

        alignmentGroup = QtGui.QActionGroup
        alignmentGroup.addAction(leftAlignAct)
        alignmentGroup.addAction(rightAlignAct)
        alignmentGroup.addAction(justifyAct)
        alignmentGroup.addAction(centerAct)
        leftAlignAct.setChecked(T..)

    ___ createMenus 
        fileMenu = menuBar().addMenu("&File")
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        editMenu = menuBar().addMenu("&Edit")
        editMenu.addAction(undoAct)
        editMenu.addAction(redoAct)
        editMenu.addSeparator()
        editMenu.addAction(cutAct)
        editMenu.addAction(copyAct)
        editMenu.addAction(pasteAct)
        editMenu.addSeparator()

        helpMenu = menuBar().addMenu("&Help")
        helpMenu.addAction(aboutAct)
        helpMenu.addAction(aboutQtAct)

        formatMenu = editMenu.addMenu("&Format")
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

    app = QtGui.?A..(___.argv)
    window = MainWindow()
    window.s..
___.e..(app.exec_())