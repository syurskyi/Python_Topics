"""
WEEK 08: CHALLENGE 01

If you try to create two GLOBAL_MOTIONBLUR_CONTROLLER nodes, things bug out. Before it’s created, add a check to see if it already exists.

"""

# Add the following code to the moblur_controller.py file, right after the moblur_controller() function is defined.

	# Check if the Nuke script already has a GLOBAL_MOTIONBLUR_CONTROLLER NoOp node.
	for x in nuke.allNodes('NoOp'):
		if x.name() == "GLOBAL_MOTIONBLUR_CONTROLLER":
			nuke.message("You already have one of those in your script!")
			return





"""
WEEK 08: CHALLENGE 02

If you delete any node in your script, the addOnDestroy() function removes all expressions entirely. Figure out how to fix this.
Hint: Go back to Lesson 02.

"""

# Add a second argument to the .addOnDestroy() function, that references the NoOp node's Class.

nuke.addOnDestroy(deleteExpressions, nodeClass="NoOp")





# You may have noticed that if you create the GLOBAL_MOTIONBLUR_CONTROLLER, delete some of the nodes
#   connected to it, and then delete the GLOBAL_MOTIONBLUR_CONTROLLER, a few nodes keep their expression
#   link. This is undesirable, so we have to change our deleteExpressions() function code from this:

	def deleteExpressions():

		for node in node_list:
			if node.knob('motionblur'):
				node['motionblur'].clearAnimated()
				node['motionblur'].setValue(0)	
				# ...

# To this:

		def deleteExpressions():

		for node in nuke.allNodes():
			if node in node_list:
				if node.knob('motionblur'):
					node['motionblur'].clearAnimated()
					node['motionblur'].setValue(0)
					# ...

"""
Why this is the case is: if you delete a node from Nuke, the node remains in the node_list list.

Then, when the nuke.addOnDestroy() function runs the deleteExpressions() function, it loops through
all the niodes in node_list, and when it gets to a node that no longer exists in the Nuke script,
it gets confused and doesn't know what to do, so it exists the function.


Instead of looping through node_list, we should first loop through nuke.allNodes() and see which
nodes exist in node_list, and THEN go ahead and delete the expressions.

It's a subtle difference, but a necessary change to make our tool function correctly!!
"""





"""
WEEK 08: CHALLENGE 03

If you add nodes after creating the GLOBAL_MOTIONBLUR_CONTROLLER, they’re not linked. Find a way to link them after the fact.

"""

# This is done via, you guessed it, nuke.addOnCreate()!
# before our deleteExpressions() function, we need to create a new function that adds the same expressions to the same knobs.

	def addExpr():
		tn = nuke.thisNode()
		if tn.knob('motionblur'):
			tn['motionblur'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 0')
			tn['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')
		elif tn.knob('samples'):
			tn['samples'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 1')
			tn['shutter'].sE..('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

	nuke.addOnCreate(addExpr)

"""
Adding this functionality also means our fix from our deleteExpressions() function will no longer work. Why?
Because our new nodes wont be in the node_list list. In this case, it's easier to just remove the check
against node_list, like so:
"""

	def deleteExpressions():

		for node in nuke.allNodes():
			if node.knob('motionblur'):
				node['motionblur'].clearAnimated()
				node['motionblur'].setValue(0)
				# ...



####   The moblur_controller.py file has been updated to reflect these changes. Go and take a look!
