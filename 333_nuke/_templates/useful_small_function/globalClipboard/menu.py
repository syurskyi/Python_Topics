# COSA TOOLS MENU

___ call_clipboard_help():
    ?.message("Please use global copy and paste buttons below")

___ call_global_clipboard_copy():
    ______ global_clipboard
    global_clipboard.global_clipboard().copy()

___ call_global_clipboard_paste():
    ______ global_clipboard_paste
    global_clipboard_paste.main()

clipboard = ?.menu("Nodes").addMenu("Global Clipboard", icon="globalClipboard.png")

clipboard.addCommand("Global Clipboard", 'call_clipboard_help()', icon="globalClipboard.png")
clipboard.addCommand('X_Copy', 'call_global_clipboard_copy()', shortcut='Ctrl+Shift+C')
clipboard.addCommand('X_Paste', 'call_global_clipboard_paste()', shortcut='Alt+Shift+X')