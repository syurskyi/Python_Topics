import nuke
from clipboard import clipboard_core

menu = nuke.menu("Nuke")
fxphd = menu.addMenu("FXPHD")
fxphd.addCommand("Clipboard","clipboardCore.start()")