# --------------------------------------------------------------
#  moblur_controller.py
#  Version: 1.1.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: July 1st, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  - Creates a NoOp node which allows the user to control 
#    motionblur on all nodes globally.
# --------------------------------------------------------------

import nuke

# Define function.
def moblur_controller():

	# Check if the Nuke script already has a GLOBAL_MOTIONBLUR_CONTROLLER NoOp node.
	___ x __ nuke.allNodes('NoOp'):
		if x.name() == "GLOBAL_MOTIONBLUR_CONTROLLER":
			nuke.message("You already have one of those in your script!")
			return

	# Create a list to hold nodes.
	node_list = []

	# Loop through all nodes, and the ones that have a motionblur or samples knob, add them to node_list.
	___ n __ nuke.allNodes():
		if n.knob('motionblur') or n.knob('samples'):
			node_list.append(n)

	# Create a NoOp node, and set it's name.
	NoOp = nuke.createNode('NoOp')
	NoOp['name'].setValue("GLOBAL_MOTIONBLUR_CONTROLLER")

	# Make the node black, and the text bold.
	NoOp['tile_color'].setValue(255)
	NoOp['note_font'].setValue("Bold")

	# Add knobs to the NoOp node. One for motionblur samples, one for the shutter, and a third to disable all motionblur.
	NoOp.addKnob(nuke.Int_Knob('global_motionblur', "motionblur"))
	NoOp.addKnob(nuke.Double_Knob('global_shutter', "shutter"))
	NoOp.addKnob(nuke.Boolean_Knob('global_disable_moblur', "disable motionblur"))
	NoOp['global_disable_moblur'].setFlag(nuke.STARTLINE)

	# Set default values of out knobs
	NoOp['global_motionblur'].setValue(1)
	NoOp['global_shutter'].setValue(0.5)

	# Loop through all the nodes in node_list.
	___ node __ node_list:
		# If the node has a motionblur knob
		if node.knob('motionblur'):
			# Set an expression that links said motionblur knob to our global moblur NoOp's motionblur knob value.
			# There is a TCL if/else statement here saying, "If the disable_moblur knob is not checked,
			#      set the value to the GLOBAL_MOTIONBLUR_CONTROLLER's global_motionblur knob.
			#      Otherwise, set the value to 0."
			node['motionblur'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 0')
			# Same thing here -- setting an expression to link the value to the new global_shutter knob on our NoOp node.
			node['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

		# If the node doesn't have a motionblur knob, but it does have a samples knob, we still want to add the same expression.
		# The only difference here is that the samples knob is always 1 by default, so we should match that with our code.
		elif node.knob('samples'):
			node['samples'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 1')
			node['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')



	# Define function to use in addOnCreate(), for when new nodes with motionblur knobs are created AFTER our NoOp node is created.
	# We're adding the expressions to the knobs exactly the same way we are when we create the NoOp node to begin with.
	def addExpr():

		tn = nuke.thisNode()

		if tn.knob('motionblur'):
			tn['motionblur'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 0')
			tn['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

		elif tn.knob('samples'):
			tn['samples'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 1')
			tn['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

	# Any time a new node is created, the addExpr() function will run.
	# If a node without motionblur, samples and/or shutter knobs is created, this addOnCreate() will be ignored.
	nuke.addOnCreate(addExpr)



	# Define another function to use in nuke.addOnDestroy(), so when the NoOp node gets deleted,
	# all expression-links are removed and node values are set back to their defaults.
	def deleteExpressions():

		___ node __ nuke.allNodes():
			if node.knob('motionblur'):
				node['motionblur'].clearAnimated()
				node['motionblur'].setValue(0)				
				node['shutter'].clearAnimated()
				node['shutter'].setValue(0.5)

			elif node.knob('samples'):
				node['samples'].clearAnimated()
				node['samples'].setValue(1)				
				node['shutter'].clearAnimated()
				node['shutter'].setValue(0.5)

			nuke.removeOnCreate(addExpr)


	# Like addOnCreate, except it runs when the node is deleted.
	# The argument it takes is a the name of a function to run...
	nuke.addOnDestroy(deleteExpressions, nodeClass="NoOp")




# Add to menu
nuke.menu('Nuke').addCommand('Utilities/Global Motionblur Controller', 'moblur_controller.moblur_controller()')
