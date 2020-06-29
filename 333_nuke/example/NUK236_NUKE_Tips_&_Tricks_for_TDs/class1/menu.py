import nuke
import timelog
import timelog_viewer

timelog.Timelog().start_thread()

def preset_nodes(val):

    preset_node = nuke.toNode("PRESETS")

    if not preset_node:
        nuke.message("No preset node found!")
        return

    target_preset = preset_node["preset%s" % val]
    is_postage_stamp = preset_node["ps%s" % val].value()
    target_node = nuke.toNode(target_preset.value())

    if is_postage_stamp:
        _input = nuke.createNode("PostageStamp")
    else:
        _input = nuke.createNode("Dot")
        _input['note_font_color'].setValue(4278190335)
        _input['note_font_size'].setValue(15)

    _input['label'].setValue(target_node.name())
    _input.setInput(0, target_node)
    _input['hide_input'].setValue(True)


menu = nuke.menu("Nuke")
preset_menu = menu.addMenu("Preset")
timelog_menu = menu.addMenu("Timelog")
timelog_menu.addCommand("Timelog Viewer", "timelog_viewer.Panel('Timelog Viewer').showModalDialog()")

for i in range(1,10):
    preset_menu.addCommand("Preset %s" % i, "preset_nodes(%s)" % i, "alt+%s" % i)
