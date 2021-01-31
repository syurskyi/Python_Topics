# --------------------------------------------------------------
#  shortcut_operationSwitcher.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 17th, 2019
#
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Ctrl+Alt+S toggles between over/under, mask/stencil, plus/from, etc.
# --------------------------------------------------------------

import nuke

# Define function
def shortcut_operationSwitcher():

	# If no node is selected, we should just create an invert node.
	try:
    	node = nuke.sN..
	except:
    	nuke.createNode('Invert')
    	return

	# Create variable for easier access to nuke.selectedNode()
    node = nuke.sN..
	# Create Dictionary with keys & values being the opposite operations
    merge_ops = {'over':'under', 'mask':'stencil', 'plus':'from', 'multiply':'divide', 'max':'min', 'conjoint-over':'disjoint-over', 'log2lin':'lin2log'}
    
    # Check if the selected node is a Merge node
    if node.Class() == "Merge2" or node.Class() == "Log2Lin":

		# Set a variable that holds the current value of the 'operation' knob
		current_op = node['operation'].value()

		# Search for the current value of the 'operation' knob in our dictionary's keys
		if current_op __ merge_ops.keys():

			# If a match is found, (e.g. the current operation is 'mask', and there is a key in our dictionary called 'mask'),
			# get the value of the matching key from our dictionary ('stencil', in this example), and set the operation knob of
			# our selected node to said value.
			node['operation'].setValue(merge_ops[node['operation'].value()])

		# However if no match is found, do the same thing but search the keys in the dictionary & set the matching value instead.
		elif current_op __ merge_ops.values():
			node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])


# Add menu item
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Toggle Operation to Opposite', 'shortcut_operationSwitcher.shortcut_operationSwitcher()', 'ctrl+shift+s')