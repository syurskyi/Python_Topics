import nuke

def NodeGraphGrid():
	show_value = nuke.toNode("preferences").knob("show_grid").value()
	show = nuke.toNode("preferences").knob("show_grid")
	snap_value = nuke.toNode("preferences").knob("SnapToGrid").value()
	snap = nuke.toNode("preferences").knob("SnapToGrid")

	if show_value == 1 & snap_value == 1:
		show.setValue(0)
		snap.setValue(0)
	else:
		show.setValue(1)
		snap.setValue(1)