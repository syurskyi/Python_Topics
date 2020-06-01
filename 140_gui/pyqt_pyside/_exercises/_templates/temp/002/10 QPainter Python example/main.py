____ ?.?W.. ______ *
____ ?.QtGui ______ *
____ ?.QtCore ______ *
____ ?.QtMultimedia ______ QSound

class PlainTextEdit(QPlainTextEdit):
    ___ __init__(self):
        super().__init__()
        self._holes _ []
        self._bullet _ QPixmap("bullet.png")
        size _ self._bullet.size()
        self._offset _ QPoint(size.width() / 2, size.height() / 2)
    ___ mousePressEvent(self, e):
        self._holes.append(e.pos())
        super().mousePressEvent(e)
        self.viewport().update()
        QSound.play("shot.wav")
    ___ paintEvent(self, e):
        super().paintEvent(e)
        painter _ QPainter(self.viewport())
        for hole in self._holes:
            painter.drawPixmap(hole - self._offset, self._bullet)

app _ ?
text _ PlainTextEdit()
text.setPlainText("Click with the mouse below to shoot ;-)")

# The rest of the code is as for the normal version of the text editor.

class MainWindow(QMainWindow):
    ___ closeEvent(self, e):
        if not text.document().isModified
            return
        answer _ QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

app.setApplicationName("Text Editor")
window _ MainWindow()
window.setCentralWidget(text)

file_path _ None

menu _ window.menuBar().addMenu("&File")
open_action _ QAction("&Open")
___ open_file
    global file_path
    path _ QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path _ path
open_action.triggered.c..(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.addAction(open_action)

save_action _ QAction("&Save")
___ save
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.triggered.c..(save)
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)

save_as_action _ QAction("Save &As...")
___ save_as
    global file_path
    path _ QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path _ path
        save()
save_as_action.triggered.c..(save_as)
menu.addAction(save_as_action)

close _ QAction("&Close")
close.triggered.c..(window.close)
menu.addAction(close)

help_menu _ window.menuBar().addMenu("&Help")
about_action _ QAction("&About")
help_menu.addAction(about_action)
___ show_about_dialog
    text _ "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)
about_action.triggered.c..(show_about_dialog)

window.s..
app.e..