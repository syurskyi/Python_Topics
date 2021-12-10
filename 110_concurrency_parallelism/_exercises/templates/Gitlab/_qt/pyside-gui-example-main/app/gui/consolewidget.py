______ os

from PySide2.QtCore ______ Qt, Slot
from PySide2.QtWidgets ______ QTextEdit, QMenu, QAction
from PySide2.QtGui ______ QTextCursor, QKeySequence, QTextOption

from .. ______ g
from ..richtexthandler ______ RichTextHandlerObject, RichTextHandler
from ..loggers ______ ConsoleFormatter


class ConsoleWidget(QTextEdit):

    ___ __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setWordWrapMode(QTextOption.NoWrap)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet('''
            QTextEdit {
                background-color: #2b2b2b;
                font-family: "Consolas";
                font-size: 10pt;
                color: #bbbbbb;
                border: 0;
                white-space: pre;
            }''')

        self.handlerObj = RichTextHandlerObject()
        self.handler = RichTextHandler(self.handlerObj)
        self.handler.setFormatter(ConsoleFormatter())
        self.handlerObj.wroteLine.connect(self.write)
        g.log.addHandler(self.handler)

        self.actionCopy = QAction('&Copy', self, shortcut=QKeySequence.Copy, statusTip='Copy selected text to the clipboard', triggered=self.copy)
        self.actionSelectAll = QAction('Select &All', self, shortcut=QKeySequence.SelectAll, statusTip='Select all text in the output window', triggered=self.selectAll)
        self.actionScrollToEnd = QAction('Scroll to &End', self, statusTip='Move the cursor to the end of the output', triggered=self.scrollToEnd)
        self.actionWordWrap = QAction('&Word Wrap', self, statusTip='Toggle word wrap', checkable=True, triggered=self.toggleWordWrap)
        self.actionClear = QAction('C&lear', self, statusTip='Clear the output window', triggered=self.clear)

    @Slot(s..)
    ___ write(self, line):
        self.append(line)
        self.scrollToEnd()

    ___ scrollToEnd(self):
        self.moveCursor(QTextCursor.End)
        self.moveCursor(QTextCursor.StartOfLine)

    ___ toggleWordWrap(self):
        if self.wordWrapMode() == QTextOption.NoWrap:
            self.setWordWrapMode(QTextOption.WordWrap)
        else:
            self.setWordWrapMode(QTextOption.NoWrap)

    ___ clear(self):
        self.setText('')
        self.scrollToEnd()

    ___ contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.actionCopy)
        menu.addAction(self.actionSelectAll)
        menu.addAction(self.actionScrollToEnd)
        menu.addSeparator()
        self.actionWordWrap.setChecked(self.wordWrapMode() != QTextOption.NoWrap)
        menu.addAction(self.actionWordWrap)
        menu.addAction(self.actionClear)
        menu.exec_(event.globalPos())
