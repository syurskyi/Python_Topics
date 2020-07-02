#!coding:utf8
______ nuke
______ __
______ subprocess
______ sys

___ browser(path):
	brws = "nautilus"
	__ sys.platform == "win32":
		brws = "start"
	elif sys.platform == "darwin":
		brws = "open"
	subprocess.Popen([brws, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#Debug
	"""
	p = subprocess.Popen([brws, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	if stderr:
		nuke.tprint(stderr, file=sys.stderr)
	if stdout:
		nuke.tprint(stdout)
	"""

___ main():
	focusKnobs = ["file","vfield_file"]
	nodes = nuke.selectedNodes()
	__ len(nodes) != 1:
		nuke.message("Please select only one node.")
		return
	___ knob __ focusKnobs:
		__ knob __ nodes[0].knobs():
			path = nodes[0][knob].value()
			__ path == "":
				nuke.message("The path is empty.")
				return
			parentPath = __.path.dirname(path)
			__ no. __.path.exists(parentPath):
				nuke.message("The path does not exist.")
				return
			browser(parentPath)
			return
	nuke.message("This is not a node using file Knob.")
