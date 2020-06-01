____ ?.?W.. ______ *
____ ?.?G.. ______ *
____ ?.QtCore ______ *
____ ?.QtMultimedia ______ QSound

c_ PlainTextEdit(QPlainTextEdit):
    ___ __init__(self):
        super().__init__()
        self._holes _ []
        self._bullet _ QPixmap("bullet.png")
        size _ self._bullet.size()
        self._offset _ QPoint(size.width() / 2, size.height() / 2)
    ___ mousePressEvent  e):
        self._holes.append(e.pos())
        super().mousePressEvent(e)
        self.viewport().update()
        QSound.play("shot.wav")
    ___ paintEvent  e):
        super().paintEvent(e)
        painter _ QPainter(self.viewport())
        for hole in self._holes:
            painter.drawPixmap(hole - self._offset, self._bullet)

app _ ?
text _ PlainTextEdit()
text.sPT..("Click with the mouse below to shoot ;-)")

# The rest of the code is as for the normal version of the text editor.

c_ MainWindow ?MW..
    ___ closeEvent  e):
        __ no. text.document().iM..
            r_
        answer _ ?MB...q..(
            window, N..,
            "You have unsaved changes. Save before closing?",
            ?MB...Save | ?MB...Discard | ?MB...Cancel
        )
        __ answer & ?MB...Save:
            save()
        ____ answer & ?MB...Cancel:
            e.ignore()

app.sAN..("Text Editor")
window _ MainWindow()
window.sCW..(text)

file_path _ N..

menu _ window.mB.. .aM..("&File")
open_action _ ?A..("&Open")
___ open_file
    gl.. file_path
    path _ ?FD...gOFN..(window, "Open")[0]
    __ path:
        text.sPT..(o..(path).r..
        file_path _ path
open_action.t__.c..(open_file)
open_action.sS..(?KS...Open)
menu.aA..(open_action)

save_action _ ?A..("&Save")
___ save
    __ file_path __ N..:
        save_as()
    ____
        w__ o..(file_path, _  __ f:
            f.w..(text.tPT..
        text.document().setModified F..
save_action.t__.c..(save)
save_action.sS..(?KS...Save)
menu.aA..(save_action)

save_as_action _ ?A..("Save &As...")
___ save_as
    gl.. file_path
    path _ ?FD...getSaveFileName(window, "Save As")[0]
    __ path:
        file_path _ path
        save()
save_as_action.t__.c..(save_as)
menu.aA..(save_as_action)

close _ ?A..("&Close")
close.t__.c..(window.close)
menu.aA..(close)

help_menu _ window.mB.. .aM..("&Help")
about_action _ ?A..("&About")
help_menu.aA..(about_action)
___ show_about_dialog
    text _ "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    ?MB...about(window, "About Text Editor", text)
about_action.t__.c..(show_about_dialog)

window.s..
app.e..