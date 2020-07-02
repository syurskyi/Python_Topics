#!coding:utf8
import nuke
import os
import subprocess
import sys

def browser(path):
	brws = "nautilus"
	if sys.platform == "win32":
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

def main():
	focusKnobs = ["file","vfield_file"]
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("Please select only one node.")
		return
	for knob in focusKnobs:
		if knob in nodes[0].knobs():
			path = nodes[0][knob].value()
			if path == "":
				nuke.message("The path is empty.")
				return
			parentPath = os.path.dirname(path)
			if not os.path.exists(parentPath):
				nuke.message("The path does not exist.")
				return
			browser(parentPath)
			return
	nuke.message("This is not a node using file Knob.")
