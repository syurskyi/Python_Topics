# --------------------------------------------------------------
#  listNavigator.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  - List selected nodes alphabetically.
#  - Show details about the list in a message box.
# --------------------------------------------------------------

import nuke

def listNavigator():

	node_list _ []

	___ i __ nuke.sN.. :
	    node_list.append(i.name())

	node_list.sort()

	# Print all nodes in list
	print "NODES IN LIST:\n"

	___ i __ node_list:
	    print "- "+i

	nuke.message("There are "+st_(len(node_list))+" nodes in the list.\n\nThe first node in the list is "+node_list[0]+".\nThe last node in the list is "+node_list[-1]+"\n\nSee the script editor for all nodes in list, sorted alphabetically...")

