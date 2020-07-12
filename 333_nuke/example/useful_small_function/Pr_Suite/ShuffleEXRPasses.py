import nuke

def ShuffleEXRPasses():
	if nuke.selectedNodes() != []:
		selected = nuke.selectedNodes("Read")
		if selected:
			for read in selected:
				channelCollect = read.channels()
				store = []
				for channel in channelCollect:
					cut = channel.split(".")
					ind = cut[0]
					store.append(ind)
				channelSet = list(set(store))
				channelSet.remove("rgba")
				
				for separation in channelSet:
					shuffle = nuke.nodes.Shuffle(label = separation)
					shuffle.knob("in").setValue(separation)
					shuffle.setInput(0, read)
		else:
			nuke.message("Read node(s) not found in selection")
	else:
		nuke.message("No nodes selected")