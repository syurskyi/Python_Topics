# ----- CREATING NODES ---------------

# Creates a grade node.
nuke.createNode('Grade')

# Create a grade node with multiply set to a value of 0.5, and gamma set to a value of 0.75.
nuke.createNode('Grade', 'multiply 0.5 gamma 0.75')

# Create a Tracker node.
nuke.createNode('Tracker4')

# Create the original Tracker node.
nuke.createNode('Tracker')





# ----- SELECTING NODES ---------------

# Return a single selected node.
nuke.sN..

# Return a list of selected nodes (multiple).
nuke.sN..

# Return a specific node ('Merge5' is the name of the node).
nuke.tN..('Merge5')

# Return all nodes in nuke script.
nuke.allNodes()

# Return all nodes in Nuke script of a specific class.
nuke.allNodes('Grade')





# ----- SETTING KNOB VALUES ---------------

# Set the selected node's mix knob to a value of 0.5.
nuke.sN.. ['mix'].setValue(0.5)

# Set a specific Merge node's 'operation' knob to 'plus'.
nuke.tN..('Merge5')['operation'].setValue('plus')

# Note, if the value is an integer (a whole number) or a float (a number with decimal places), you write the number
# Whereas if the value is a string (text), we wrap it in quotation marks.





# ----- WORKING WITH EXISTING MENUS ---------------

# Assign an existing menu to a variable to access later.
filterMenu = nuke.menu('Nodes').findItem("Filter")

# Add a legacy node to said existing menu.
filterMenu.addCommand('Blocky', 'nuke.createNode("Blocky")')

# Add a node to a submenu with a keyboard shortcut & an icon.
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")
mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="MergeOut.png", shortcutContext=2)





# ----- IF / ELSE STATEMENTS ---------------

# If the selected node is disabled, change it's label.
# If it isn't, print a message in the Script Editor.
if nuke.sN.. ['disable'].value() == 1:
	nuke.sN.. ['label'].setValue("node is disabled")
else:
	print nuke.sN.. .name()+" is enabled."





# ----- FOR LOOPS ---------------

# Set all merge nodes in your Nuke script to have a mix of 0.5.
___ i __ nuke.allNodes('Merge2'):
	i['mix'].setValue(0.5)

# Set the multiply knob on all Grade nodes with a label 'luminance' to 3.
___ grade_nodes __ nuke.allNodes('Grade'):
	if grade_nodes['label'].value() == 'luminance':
		grade_nodes['multiply'].setValue(3)





# ----- JOINING STRINGS ---------------

# Print the name of a bunch of selected nodes.
print "\n\nSELECTED NODES:\n"
___ node __ nuke.sN.. :
	print node.name()


# Add together variables to print a sentence.
var1 = "This"
var2 = " is"
var3 = " a"
var4 = " joined"
var5 = " string."

print var1+var2+var3+var4+var5


# Print the value of a knob in a sentence.
print "The current value of "+nuke.sN.. .name()+"'s mix knob is "+str(nuke.sN.. ['mix'].value())+"."



