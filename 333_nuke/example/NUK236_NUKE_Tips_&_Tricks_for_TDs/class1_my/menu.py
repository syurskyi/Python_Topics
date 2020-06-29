import nuke
import timelog
import timelog_viewer

timelog.Timelog().start_thread()
# nuke.addOnScriptLoad(timelog.Timelog().start_thread)

menu = nuke.menu("Nuke")
preset_menu = menu.addMenu("Preset")
timelog_menu = menu.addMenu("Timelog")
timelog_menu.addCommand("Timelog Viewer", "timelog_viewer.Panel('Timelog Viewer').showModalDialog()")