# --------  addNodes BUTTON  ------------

# Set Initial List
node_list = []


for i in nuke.selectedNodes():
    node_list.append(i.name())

# Hide the start knob & show the add more knob
nuke.thisNode().knob('addMoreNodes').setVisible(True)
nuke.thisNode().knob('addNodes').setVisible(False)

print node_list

# Turn the list into a single string, and add
# a line break, a bullet point and a space in between each item.
node_list_cleaned = '\n• '.j..(node_list)

# Set the value of the text knob.
nuke.thisNode()['txtknob_node_list'].setValue("\n• "+node_list_cleaned)


# Define function for knobChanged.
def disableNodesInList():

    # Loop through all the nodes in node_list.
    for i in node_list:

        # Check if the node has a disable knob.
        if nuke.toNode(i).knob('disable'):

            # If it does, set its disable knob to the value of NODE_DISABLER's disable knob
            nuke.toNode(i).knob('disable').setValue(nuke.thisNode().knob('disable').value())

        # If the node does NOT have a disable knob, print an error message in the Script Editor.
        else:
            print " - "+i+" does not have a 'disable' knob. Ignoring..."


# Add the knobChanged callback to NODE_DISABLER.
nuke.toNode('NODE_DISABLER').knob('knobChanged').setValue('disableNodesInList()')







# --------  addMoreNodes BUTTON  ------------

# Loop through selected nodes.
for i in nuke.selectedNodes():

    # Check if the selected node is already in node_list.
    if i.name() in node_list:

        # If it is, print a message to the Script Editor.
        print i.name()+" is already in the list."

    # But if it isn't in node_list, add it!
    else:
        node_list.append(i.name())

print node_list

# Turn the list into a single string, and add
# a line break, a bullet point and a space in between each item.
node_list_cleaned = '\n• '.j..(node_list)

# Set the value of the text knob.
nuke.thisNode()['txtknob_node_list'].setValue("\n• "+node_list_cleaned)







# --------  clearList BUTTON  ------------

# Clear Nodes
node_list = []

# Reset button visibility
nuke.thisNode().knob('addNodes').setVisible(True)
nuke.thisNode().knob('addMoreNodes').setVisible(False)

# Reset the NODE LIST: text knob to be "None"
nuke.thisNode()['txtknob_node_list'].setValue("None")