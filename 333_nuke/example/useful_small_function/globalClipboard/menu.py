# COSA TOOLS MENU

def call_clipboard_help():
    nuke.message("Please use global copy and paste buttons below")

def call_global_clipboard_copy():
    import global_clipboard
    global_clipboard.global_clipboard().copy()

def call_global_clipboard_paste():
    import global_clipboard_paste
    global_clipboard_paste.main()

clipboard = nuke.menu("Nodes").addMenu("Global Clipboard", icon="globalClipboard.png")

clipboard.addCommand("Global Clipboard", 'call_clipboard_help()', icon="globalClipboard.png")
clipboard.addCommand('X_Copy', 'call_global_clipboard_copy()', shortcut='Ctrl+Shift+C')
clipboard.addCommand('X_Paste', 'call_global_clipboard_paste()', shortcut='Alt+Shift+X')