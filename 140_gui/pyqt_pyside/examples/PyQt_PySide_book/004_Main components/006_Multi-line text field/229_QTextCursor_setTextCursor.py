# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    cur.deleteChar()
    textEdit.setTextCursor(cur)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение по умолчанию")
button = QtGui.QPushButton("Удалить выделенный фрагмент или символ справа")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

230_QTextDocument_Signals.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.document().setModified(False)

def on_block_count_changed(cnt):
    print("on_block_count_changed", cnt)

def on_undo(status):
    print("on_undo", status)

def on_redo(status):
    print("on_redo", status)

def on_contents_changed():
    print("on_contents_changed")

def on_contents_change(x, y, z):
    print("on_contents_change", x, y, z)

def on_position_changed(cur):
    print("on_position_changed")

def on_modification_changed(status):
    print("on_modification_changed", status)

def on_undo_command_added():
    print("on_undo_command_added")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.blockCountChanged["int"].connect(on_block_count_changed)
document.undoAvailable["bool"].connect(on_undo)
document.redoAvailable["bool"].connect(on_redo)
document.contentsChanged.connect(on_contents_changed)
document.contentsChange["int","int","int"].connect(on_contents_change)
document.cursorPositionChanged["const QTextCursor&"].connect(on_position_changed)
document.modificationChanged["bool"].connect(on_modification_changed)
document.undoCommandAdded.connect(on_undo_command_added)
textEdit.setDocument(document)
button = QtGui.QPushButton("Изменить статус документа")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

231_QTextDocument_block.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.document().firstBlock().text())
    print(textEdit.document().lastBlock().text())
    print(textEdit.document().findBlock(0).text())
    print(textEdit.document().findBlockByNumber(4).text())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

232_QTextDocument_clear.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.document().clear()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("Текст внутри поля")
textEdit.setDocument(document)
button = QtGui.QPushButton("Очистить")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

233_QTextDocument_find.py
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    rx = QtCore.QRegExp("Т[А-Я]+Т")
    rx.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    cursor = textEdit.document().find(rx, position=0)
    if not cursor.isNull():
        textEdit.setTextCursor(cursor)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\n")
textEdit.setDocument(document)
button = QtGui.QPushButton("Поиск фрагмента")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

234_QTextDocument_print_.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    printer = QtGui.QPrinter()
    printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
    printer.setOutputFileName("mypdf.pdf")
    textEdit.document().print_(printer)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\n")
textEdit.setDocument(document)
button = QtGui.QPushButton("Печать в PDF")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 235. QTextDocument_setDefaultFont.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.document().setDefaultFont(QtGui.QFont("Tahoma",
             pointSize=12, weight=QtGui.QFont.Normal, italic=False))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setDefaultFont(QtGui.QFont("Tahoma", 30, QtGui.QFont.Bold))
document.setPlainText("Текст внутри поля")
textEdit.setDocument(document)
button = QtGui.QPushButton("Изменить шрифт")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 236. QTextDocument_setDefaultStyleSheet.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.document().toHtml())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setDefaultStyleSheet("""
body { color:#FFFFFF; background-color:#000000; font-family: Tahoma;
    font-size: 30pt;}
""")
document.setHtml("<html><body><p>Текст внутри поля</p></body></html>")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить HTML-текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 237. QTextDocument_setDocument.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.document().toPlainText())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument("Текст по умолчанию")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 238. QTextDocument_setDocumentMargin.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.document().setDocumentMargin(5)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setDocumentMargin(10)
document.setHtml("<html><body><p>Текст внутри поля</p></body></html>")
textEdit.setDocument(document)
button = QtGui.QPushButton("Изменить отступ")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 239. QTextDocument_setHtml.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.document().toHtml(bytes("utf-8", "ascii")))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setHtml("<p><font color=red>Текст в формате <b>HTML</b></font></p>")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 240. QTextDocument_setMaximumBlockCount.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.document().maximumBlockCount())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setMaximumBlockCount(5)
document.setPlainText("Текст внутри поля")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 241. QTextDocument_setPlainText.py
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print(textEdit.document().toPlainText())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("Новый текст")
textEdit.setDocument(document)
button = QtGui.QPushButton("Получить текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 242. QTextEdit.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.toPlainText())
    print(textEdit.toHtml())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 243. Signals.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    f = QtGui.QTextCharFormat()
    f.setFontUnderline(True)
    textEdit.setCurrentCharFormat(f)

def on_copy(status):
    print("on_copy", status)

def on_undo(status):
    print("on_undo", status)

def on_redo(status):
    print("on_redo", status)

def on_format_changed(s):
    print("on_format_changed")

def on_position_changed():
    print("on_position_changed")

def on_selection_changed():
    print("on_selection_changed")

def on_text_changed():
    print("on_text_changed")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение по умолчанию")
textEdit.copyAvailable["bool"].connect(on_copy)
textEdit.undoAvailable["bool"].connect(on_undo)
textEdit.redoAvailable["bool"].connect(on_redo)
textEdit.currentCharFormatChanged["const QTextCharFormat&"].connect(on_format_changed)
textEdit.cursorPositionChanged.connect(on_position_changed)
textEdit.selectionChanged.connect(on_selection_changed)
textEdit.tC...connect(on_text_changed)
button = QtGui.QPushButton("Подчеркнуть текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 244. append.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.append("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 245. clear.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.clear()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Удалить текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 246. createStandardContextMenu.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_mypaste():
    textEdit.insertPlainText("мой текст")

class MyTextEdit(QtGui.QTextEdit):
    def __init__(self, text, parent=None):
        QtGui.QTextEdit.__init__(self, text, parent)

    def contextMenuEvent(self, e):
        menu = self.createStandardContextMenu()
        menu.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        menu.addSeparator()
        menu.addAction("Новый пункт", on_mypaste, "Ctrl+M")
        menu.exec_(e.globalPos())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = MyTextEdit("Значение по умолчанию")
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 247. ensureCursorVisible.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    textEdit.ensureCursorVisible()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nЗначение по умолчанию")
button = QtGui.QPushButton("Показать позицию с курсором")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 248. find.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    textEdit.find("текст",
                  QtGui.QTextDocument.FindCaseSensitively |
                  QtGui.QTextDocument.FindBackward)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\n")
button = QtGui.QPushButton("Найти в обратном порядке с учетом регистра")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 249. insertHtml.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.insertHtml("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 250. insertPlainText.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.insertPlainText("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 251. print_.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    printer = QtGui.QPrinter()
    printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
    printer.setOutputFileName("mypdf.pdf")
    textEdit.print_(printer)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\nтекст\n")
button = QtGui.QPushButton("Печать в PDF")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 252. selectAll.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.selectAll()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Выделить все")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 253. setAcceptRichText.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setAcceptRichText(not textEdit.acceptRichText())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setAcceptRichText(True)
button = QtGui.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 254. setAlignment.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    textEdit.setAlignment(QtCore.Qt.AlignRight)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setAlignment(QtCore.Qt.AlignRight)
textEdit.setPlainText("абзац 1\nабзац 2")
button = QtGui.QPushButton("Выравнивание по правому краю")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 255. setAutoFormatting.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.toHtml())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setAutoFormatting(QtGui.QTextEdit.AutoBulletList)
button = QtGui.QPushButton("Вывести текст")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 256. setCurrentFont.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setCurrentFont(QtGui.QFont("Tahoma", pointSize=12,
                            weight=QtGui.QFont.Normal, italic=True))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setCurrentFont(QtGui.QFont("Tahoma", 30, QtGui.QFont.Bold))
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить шрифт")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 257. setCursorWidth.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение по умолчанию")
textEdit.setCursorWidth(3)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 258. setDocumentTitle.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.documentTitle())
    print(textEdit.toHtml())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setDocumentTitle("Это заголовок документа")
button = QtGui.QPushButton("Вывести текст заголовка")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 259. setFontFamily.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFontFamily("Courier New")
    print(textEdit.fontFamily())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setFontFamily("Tahoma")
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить шрифт")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 260. setFontItalic.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFontItalic(True)
    print(textEdit.fontItalic())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setFontItalic(False)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Сделать шрифт курсивным")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 261. setFontPointSize.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFontPointSize(12)
    print(textEdit.fontPointSize())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setFontPointSize(30)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить размер шрифта")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 262. setFontUnderline.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFontUnderline(True)
    print(textEdit.fontUnderline())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setFontUnderline(False)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Сделать текст подчеркнутым")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 263. setFontWeight.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setFontWeight(QtGui.QFont.Normal)
    print(textEdit.fontWeight())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setFontWeight(QtGui.QFont.Bold)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить жирность шрифта")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 264. setHtml.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setHtml("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 265. setLineWrapMode.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

wrap = 1

def on_clicked():
    global wrap
    textEdit.setLineWrapMode(wrap)
    wrap += 1
    if wrap > 3:
        wrap = 0

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit(
"""setLineWrapMode() задает режим переноса строк. В качестве значения могут быть указаны следующие атрибуты из класса QTextEdit:""")
textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
textEdit.setLineWrapColumnOrWidth(70)
button = QtGui.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 266. setOverwriteMode.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setOverwriteMode(not textEdit.overwriteMode())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setOverwriteMode(True)
button = QtGui.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 267. setPlainText.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setPlainText("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 268. setReadOnly.py
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    print(textEdit.isReadOnly())

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
textEdit.setReadOnly(True)
button = QtGui.QPushButton("Проверить статус")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 269. setText.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked():
    textEdit.setText("Новый <font color=red>текст</font>")

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Установить новое значение")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 270. setTextBackgroundColor.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    textEdit.setTextBackgroundColor(QtGui.QColor("#FF0000"))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setTextColor(QtGui.QColor("#FFFFFF"))
textEdit.setTextBackgroundColor(QtCore.Qt.blue)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить цвет фона")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 271. setTextColor.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    textEdit.setTextColor(QtGui.QColor("#FF0000"))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit()
textEdit.setTextColor(QtCore.Qt.blue)
textEdit.setPlainText("Значение по умолчанию")
button = QtGui.QPushButton("Изменить цвет текста")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 272. setTextInteractionFlags.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

flag = 1
allFlags = [QtCore.Qt.NoTextInteraction,
            QtCore.Qt.TextSelectableByMouse,
            QtCore.Qt.TextSelectableByKeyboard,
            QtCore.Qt.LinksAccessibleByMouse,
            QtCore.Qt.LinksAccessibleByKeyboard,
            QtCore.Qt.TextEditable,
            QtCore.Qt.TextEditorInteraction,
            QtCore.Qt.TextBrowserInteraction]
def on_clicked():
    global flag
    textEdit.setTextInteractionFlags(allFlags[flag])
    flag += 1
    if flag > 7:
        flag = 0

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("""Значение по умолчанию <a href="http://google.ru/">ссылка</a>""")
textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
button = QtGui.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 273. setWordWrapMode.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

wrap = 1

def on_clicked():
    global wrap
    textEdit.setWordWrapMode(wrap)
    wrap += 1
    if wrap > 4:
        wrap = 0

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit(
"""setWordWrapMode() задает режим переноса строк. В качестве значения могут быть указаны следующие атрибуты из класса QTextOption:""")
textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)
button = QtGui.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())

Листинг 274. zoom.pyw
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

def on_clicked_button1():
    textEdit.zoomOut()

def on_clicked_button2():
    textEdit.zoomIn()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtGui.QTextEdit("Значение <b>по умолчанию</b>")
button = QtGui.QPushButton("Уменьшить")
button.clicked.connect(on_clicked_button1)
button2 = QtGui.QPushButton("Увеличить")
button2.clicked.connect(on_clicked_button2)
box = QtGui.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec_())