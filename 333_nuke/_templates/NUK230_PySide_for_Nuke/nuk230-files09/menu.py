import nuke
import toolbox

menu = nuke.menu("Nuke")
fxphd = menu.addMenu("FXPHD")
fxphd.addCommand("Hotbox","toolbox.start()","n")