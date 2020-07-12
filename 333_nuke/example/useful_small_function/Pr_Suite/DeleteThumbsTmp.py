import nuke

def DeleteThumbsTmp():
	all = nuke.allNodes("Read")
	if all:
		for read in all:
			file = read["file"].value()
			last = file.split('/')[-1]
			if last == "Thumbs.db" or last[-4:] == ".tmp":
				nuke.delete(read)
	else:
		nuke.message("No read nodes found")