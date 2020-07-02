# #!coding:utf8
# ______ n..
# ______ __
# ______ s..
# ______ ___
#
# ___ browser path
# 	brws _ *nautilus
# 	__ ___.pl.. __ *win32
# 		brws _  *start
# 	____ ___.pl.. __ *darwin
# 		brws _ *open
# 	s__.P.. ? ?| s_o.._s__.P.. s_e.._s__.P..
# 	#Debug
# 	"""
# 	p = subprocess.Popen([brws, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 	stdout, stderr = p.communicate()
# 	if stderr:
# 		nuke.tprint(stderr, file=sys.stderr)
# 	if stdout:
# 		nuke.tprint(stdout)
# 	"""
#
# ___ main
# 	focusKnobs _ "file","vfield_file"
# 	nodes _ ?.sN..
# 	__ le. ? !_ 1
# 		?.m.. Please select only one node.
# 		r_
# 	___ knob __ f..
# 		__ ? __ n.. 0 .k..
# 			path _ n.. 0 ? .v..
# 			__ ? __ ""
# 				?.m.. *The path is empty.
# 				r_
# 			parentPath _ __.p__.d.. ?
# 			__ no. __.p__.e.. ?
# 				?.m.. *The path does not exist.
# 				r_
# 			b.. ?
# 			r_
# 	?.m.. *This is not a node using file Knob.
