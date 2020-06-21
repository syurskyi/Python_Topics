# ____ ?.?W.. ______ *
# ____ ?.?G.. ______ *
# ____ ?.?C.. ______ *
# ____ ?.QtMultimedia ______ QSound
#
# c_ PlainTextEdit(?PTE..):
#     ___  -
#         s__(). - ()
#         _holes _   # list
#         _bullet _ ?P..("bullet.png")
#         size _ _bullet.size()
#         _offset _ QPoint(size.width() / 2, size.height() / 2)
#     ___ mousePressEvent  e):
#         _holes.ap..(e.pos())
#         s__().mousePressEvent(e)
#         viewport().update()
#         QSound.play("shot.wav")
#     ___ paintEvent  e):
#         s__().paintEvent(e)
#         painter _ QPainter(viewport())
#         ___ hole in _holes:
#             painter.drawPixmap(hole - _offset, _bullet)
#
# app _ ?A..([])
# text _ PlainTextEdit()
# text.setPlainText("Click with the mouse below to shoot ;-)")
#
# # The rest of the code is as for the normal version of the text editor.
#
# c_ MainWindow(?MW..):
#     ___ closeEvent  e):
#         __ not text.document().isModified():
#             r_
#         answer _ ?MB...question(
#             window, None,
#             "You have unsaved changes. Save before closing?",
#             ?MB...Save | ?MB...Discard | ?MB...Cancel
#         )
#         __ answer & ?MB...Save:
#             save()
#         elif answer & ?MB...Cancel:
#             e.ignore()
#
# app.setApplicationName("Text Editor")
# window _ MainWindow()
# window.setCentralWidget(text)
#
# file_path _ None
#
# menu _ window.mB...aM..("&File")
# open_action _ ?A..("&Open")
# ___ open_file():
#     g__ file_path
#     path _ QFileDialog.getOpenFileName(window, "Open")[0]
#     __ path:
#         text.setPlainText(open(path).read())
#         file_path _ path
# open_action.t___.c__(open_file)
# open_action.setShortcut(QKeySequence.Open)
# menu.aA..(open_action)
#
# save_action _ ?A..("&Save")
# ___ save():
#     __ file_path is N..
#         save_as()
#     ____
#         w__ open(file_path, "w") __ f:
#             f.write(text.toPlainText())
#         text.document().setModified F..
# save_action.t___.c__(save)
# save_action.setShortcut(QKeySequence.Save)
# menu.aA..(save_action)
#
# save_as_action _ ?A..("Save &As...")
# ___ save_as():
#     g__ file_path
#     path _ QFileDialog.getSaveFileName(window, "Save As")[0]
#     __ path:
#         file_path _ path
#         save()
# save_as_action.t___.c__(save_as)
# menu.aA..(save_as_action)
#
# close _ ?A..("&Close")
# close.t___.c__(window.close)
# menu.aA..(close)
#
# help_menu _ window.mB...aM..("&Help")
# about_action _ ?A..("&About")
# help_menu.aA..(about_action)
# ___ show_about_dialog():
#     text _ "<center>" \
#            "<h1>Text Editor</h1>" \
#            "&#8291;" \
#            "<img src=icon.svg>" \
#            "</center>" \
#            "<p>Version 31.4.159.265358<br/>" \
#            "Copyright &copy; Company Inc.</p>"
#     ?MB...about(window, "About Text Editor", text)
# about_action.t___.c__(show_about_dialog)
#
# window.s..
# app.exec_()