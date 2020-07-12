import nuke

def RedShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		red = nuke.nodes.Shuffle(tile_color="0xff0000ff", red="red", green="red", blue="red", alpha="red")
		try:
			red.setInput(0, connect)
		except ValueError:
			pass

def GreenShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		green = nuke.nodes.Shuffle(tile_color="0xff00ff", red="green", green="green", blue="green", alpha="green")
		try:
			green.setInput(0, connect)
		except ValueError:
			pass

def BlueShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		blue = nuke.nodes.Shuffle(tile_color="0xffff", red="blue", green="blue", blue="blue", alpha="blue")
		try:
			blue.setInput(0, connect)
		except ValueError:
			pass

def AlphaShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		alpha = nuke.nodes.Shuffle(tile_color="0xffffffff", red="alpha", green="alpha", blue="alpha", alpha="alpha")
		try:
			alpha.setInput(0, connect)
		except ValueError:
			pass