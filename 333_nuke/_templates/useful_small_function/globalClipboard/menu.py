# COSA TOOLS MENU

___ call_clipboard_help
    ?.m..("Please use global copy and paste buttons below")

___ call_global_clipboard_copy
    ______ global_clipboard
    global_clipboard.global_clipboard().copy()

___ call_global_clipboard_paste
    ______ global_clipboard_paste
    global_clipboard_paste.main()

clipboard _ ?.m__("Nodes").aM..("Global Clipboard", icon_"globalClipboard.png")

clipboard.aC..("Global Clipboard", 'call_clipboard_help()', icon_"globalClipboard.png")
clipboard.aC..('X_Copy', 'call_global_clipboard_copy()', shortcut_'Ctrl+Shift+C')
clipboard.aC..('X_Paste', 'call_global_clipboard_paste()', shortcut_'Alt+Shift+X')