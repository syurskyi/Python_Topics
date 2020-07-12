import nuke

def LabelShuffle():
	if nuke.selectedNodes() != []:
		selected = nuke.selectedNodes("Shuffle")
		if selected != []:
			for r in selected:
				inv = r.knob("in").value()
				r.knob("label").setValue(inv)
		else:
			nuke.message("Shuffle node(s) not found in selection")
	else:
		nuke.message("No nodes selected")