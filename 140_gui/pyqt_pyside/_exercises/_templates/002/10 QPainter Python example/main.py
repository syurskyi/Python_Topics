____ ?.?W.. ______ *
____ ?.?G.. ______ *
____ ?.?C.. ______ *
____ ?.?M.. ______ QSound

c_ PlainTextEdit(?PTE..):
    ___  -
        s_. - ()
        _holes _   # list
        _bullet _ ?P..("bullet.png")
        size _ _bullet.size()
        _offset _ QPoint(size.width() / 2, size.height() / 2)
    ___ mousePressEvent  e):
        _holes.ap..(e.pos())
        s_.mousePressEvent(e)
        viewport().update()
        QSound.play("shot.wav")
    ___ paintEvent  e):
        s_.paintEvent(e)
        painter _ QPainter(viewport())
        ___ hole __ _holes:
            painter.drawPixmap(hole - _offset, _bullet)

app _ ?
t__ _ PlainTextEdit()
t__.sPT..("Click with the mouse below to shoot ;-)")

# The rest of the code is as for the normal version of the text editor.

c_ MainWindow ?MW..
    ___ closeEvent  e):
        __ no. t__.document().iM..
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
window.sCW..(t__)

file_path _ N..

menu _ window.mB.. .aM..("&File")
open_action _ ?A..("&Open")
___ open_file
    gl.. file_path
    pa__ _ ?FD...gOFN..(window, "Open")[0]
    __ pa__:
        t__.sPT..(o..(pa__).r..
        file_path _ pa__
open_action.t__.c..(open_file)
open_action.sS..(?KS...Open)
menu.aA..(open_action)

save_action _ ?A..("&Save")
___ save
    __ file_path __ N..:
        save_as()
    ____
        w__ o..(file_path, _  __ f:
            f.w..(t__.tPT..
        t__.document().setModified F..
save_action.t__.c..(save)
save_action.sS..(?KS...Save)
menu.aA..(save_action)

save_as_action _ ?A..("Save &As...")
___ save_as
    gl.. file_path
    pa__ _ ?FD...getSaveFileName(window, "Save As")[0]
    __ pa__:
        file_path _ pa__
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
    t__ _ "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    ?MB...about(window, "About Text Editor", t__)
about_action.t__.c..(show_about_dialog)

window.s..
app.e..