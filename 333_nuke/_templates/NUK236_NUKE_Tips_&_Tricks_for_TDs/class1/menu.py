import ?
import timelog
import timelog_viewer

timelog.Timelog().start_thread()

def preset_nodes(val):

    preset_node = ?.toNode("PRESETS")

    if not preset_node:
        ?.message("No preset node found!")
        return

    target_preset = preset_node["preset%s" % val]
    is_postage_stamp = preset_node["ps%s" % val].value()
    target_node = ?.toNode(target_preset.value())

    if is_postage_stamp:
        _input = ?.createNode("PostageStamp")
    else:
        _input = ?.createNode("Dot")
        _input['note_font_color'].sV..(4278190335)
        _input['note_font_size'].sV..(15)

    _input['label'].sV..(target_node.name())
    _input.setInput(0, target_node)
    _input['hide_input'].sV..(True)


menu = ?.menu("Nuke")
preset_menu = menu.addMenu("Preset")
timelog_menu = menu.addMenu("Timelog")
timelog_menu.addCommand("Timelog Viewer", "timelog_viewer.Panel('Timelog Viewer').showModalDialog()")

___ i __ ra..(1,10):
    preset_menu.addCommand("Preset %s" % i, "preset_nodes(%s)" % i, "alt+%s" % i)
