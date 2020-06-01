____ ?.?W.. ______ *
____ ?.?G.. ______ ?KS.., QPalette, QColor
____ ?.QtCore ______ Qt

app _ ?

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette _ QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

# The rest of the code is the same as for the "normal" text editor.

app.sAN..("Text Editor")

text _ ?PTE..

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