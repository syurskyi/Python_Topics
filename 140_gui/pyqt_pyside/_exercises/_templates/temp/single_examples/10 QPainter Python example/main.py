____ ?.QtWidgets ______ *
____ ?.QtGui ______ *
____ ?.?C.. ______ *
____ ?.QtMultimedia ______ QSound

c_ PlainTextEdit(QPlainTextEdit):
    ___  -
        super(). - ()
        _holes = []
        _bullet = QPixmap("bullet.png")
        size = _bullet.size()
        _offset = QPoint(size.width() / 2, size.height() / 2)
    ___ mousePressEvent(self, e):
        _holes.append(e.pos())
        super().mousePressEvent(e)
        viewport().update()
        QSound.play("shot.wav")
    ___ paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(viewport())
        for hole in _holes:
            painter.drawPixmap(hole - _offset, _bullet)

app = ?A..([])
text = PlainTextEdit()
text.setPlainText("Click with the mouse below to shoot ;-)")

# The rest of the code is as for the normal version of the text editor.

c_ MainWindow(?MW..):
    ___ closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

app.setApplicationName("Text Editor")
window = MainWindow()
window.setCentralWidget(text)

file_path = None

menu = window.menuBar().addMenu("&File")
open_action = ?A..("&Open")
___ open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path
open_action.t___.c__(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.aA..(open_action)

save_action = ?A..("&Save")
___ save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.t___.c__(save)
save_action.setShortcut(QKeySequence.Save)
menu.aA..(save_action)

save_as_action = ?A..("Save &As...")
___ save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()
save_as_action.t___.c__(save_as)
menu.aA..(save_as_action)

close = ?A..("&Close")
close.t___.c__(window.close)
menu.aA..(close)

help_menu = window.menuBar().addMenu("&Help")
about_action = ?A..("&About")
help_menu.aA..(about_action)
___ show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)
about_action.t___.c__(show_about_dialog)

window.s..
app.exec_()