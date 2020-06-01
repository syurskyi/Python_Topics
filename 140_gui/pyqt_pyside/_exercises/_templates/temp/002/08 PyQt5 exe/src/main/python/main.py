____ fbs_runtime.application_context.? ______ ApplicationContext
____ ?.?W.. ______ QMainWindow

______ sys

appctxt _ ApplicationContext()       # 1. Instantiate ApplicationContext

____ ?.?W.. ______ _
____ ?.QtGui ______ QKeySequence

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

text _ QPlainTextEdit()
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
       "<img src=%r>" \
       "</center>" \
       "<p>Version 31.4.159.265358<br/>" \
       "Copyright &copy; Company Inc.</p>" \
       % appctxt.get_resource("icon.svg")
    about_dialog _ QMessageBox(window)
    about_dialog.sT..(text)
    about_dialog.e..
about_action.triggered.c..(show_about_dialog)

window.s..

exit_code _ appctxt.app.e..      # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)