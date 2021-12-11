______ __

____ PySide2.QtCore ______ Qt, Slot
____ PySide2.QtWidgets ______ QTextEdit, QMenu, QAction
____ PySide2.QtGui ______ QTextCursor, QKeySequence, QTextOption

____ .. ______ g
____ ..richtexthandler ______ RichTextHandlerObject, RichTextHandler
____ ..loggers ______ ConsoleFormatter


c_ ConsoleWidget(QTextEdit):

    ___ - 
        s__().- ()

        setReadOnly(T..)
        setWordWrapMode(QTextOption.NoWrap)
        setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        setStyleSheet('''
            QTextEdit {
                background-color: #2b2b2b;
                font-family: "Consolas";
                font-size: 10pt;
                color: #bbbbbb;
                border: 0;
                white-space: pre;
            }''')

        handlerObj = RichTextHandlerObject()
        handler = RichTextHandler(handlerObj)
        handler.setFormatter(ConsoleFormatter())
        handlerObj.wroteLine.connect(w..)
        g.log.addHandler(handler)

        actionCopy = QAction('&Copy', self, shortcut=QKeySequence.Copy, statusTip='Copy selected text to the clipboard', triggered=copy)
        actionSelectAll = QAction('Select &All', self, shortcut=QKeySequence.SelectAll, statusTip='Select all text in the output window', triggered=selectAll)
        actionScrollToEnd = QAction('Scroll to &End', self, statusTip='Move the cursor to the end of the output', triggered=scrollToEnd)
        actionWordWrap = QAction('&Word Wrap', self, statusTip='Toggle word wrap', checkable=T.., triggered=toggleWordWrap)
        actionClear = QAction('C&lear', self, statusTip='Clear the output window', triggered=clear)

    @Slot(s..)
    ___ w.. line):
        a.. (line)
        scrollToEnd()

    ___ scrollToEnd
        moveCursor(QTextCursor.End)
        moveCursor(QTextCursor.StartOfLine)

    ___ toggleWordWrap
        __ wordWrapMode() == QTextOption.NoWrap:
            setWordWrapMode(QTextOption.WordWrap)
        ____
            setWordWrapMode(QTextOption.NoWrap)

    ___ clear
        setText('')
        scrollToEnd()

    ___ contextMenuEvent event):
        menu = QMenu
        menu.addAction(actionCopy)
        menu.addAction(actionSelectAll)
        menu.addAction(actionScrollToEnd)
        menu.addSeparator()
        actionWordWrap.setChecked(wordWrapMode() != QTextOption.NoWrap)
        menu.addAction(actionWordWrap)
        menu.addAction(actionClear)
        menu.exec_(event.globalPos())
