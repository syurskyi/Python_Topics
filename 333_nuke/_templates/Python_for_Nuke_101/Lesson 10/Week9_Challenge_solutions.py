"""
WEEK 09: CHALLENGE 01

Add the gizmo to the custom myGizmos menu we created in Lesson 02.

"""

# At the bottom of your menu.py lies the following code:

# ----- CREATE CUSTOM GIZMOS MENU & ASSIGN ITEMS ---------------
myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")


# To add NODE_DISABLER, we simply need to copy/paste the second line of code and change a few things, like so:

# ----- CREATE CUSTOM GIZMOS MENU & ASSIGN ITEMS ---------------
myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")
myGizmosMenu.addCommand('NODE_DISABLER', 'nuke.createNode("NODE_DISABLER")', icon="MarkerRemoval.png")

# The default "Marker Removal" icon in the 'Draw' menu looks to be a good fit for NODE_DISABLER, so we're re-purposing it!







"""
WEEK 09: CHALLENGE 02

Change NODE_DISABLER to work with expression-links, rather than knobChanged.

"""

# Remove the following knobChanged code from the addNodes button:
nuke.toNode('NODE_DISABLER').knob('knobChanged').setValue('disableNodesInList()')



# We need to find the disableNodesInList() function in the addNodes button...
# We actually don't need the code to be wrapped up as a function anymore, and we can just run the code straight up.
# Note the .setExpression() function a few lines down that's expression-linking the disable knobs.

# Loop through all the nodes in node_list.
for i in node_list:

    # Check if the node has a disable knob.
    if nuke.toNode(i).knob('disable'):

        # If it does, set an expression to link it to NODE_DISABLER's disable knob.
        nuke.toNode(i).knob('disable').setExpression('NODE_DISABLER.disable')

    # If the node does NOT have a disable knob, print an error message in the Script Editor.
    else:
        print " - "+i+" does not have a 'disable' knob. Ignoring..."

# ---------------------------------------------------------------------------------
#  YOU WILL NEED TO ADD THE ABOVE CODE SNIPPET TO THE addMoreNodes BUTTON AS WELL!
# ---------------------------------------------------------------------------------



# Lastly, we need to break the expression link if the Clear List button is checked.
# Add the following snippet to the top of the clearList button's code:

# Before we clear node_list, we should remove the expression links from the linked nodes.
for i in node_list:
    nuke.toNode(i).knob('disable').clearAnimated()







"""
WEEK 09: CHALLENGE 03

Bonus Points: Add a new tab containing buttons that automatically add nodes from a certain Class into node_list.

"""

# "Manage User Knobs > Add > Tab" allows you to add a new tab.
# We need to add a new Python Script Button to this tab, and then we can
# add all nodes in our Nuke script with a 'Defocus' Class to node_list with the following code:

for i in nuke.allNodes("Defocus"):
    if i.name() not in node_list:
        node_list.append(i.name())

        # Don't forget to add the expression link as well!
        i.knob('disable').setExpression('NODE_DISABLER.disable')

print node_list

# Turn the list into a single string, and add
# a line break, a bullet point and a space in between each item.
node_list_cleaned = '\n• '.j..(node_list)

# Set the value of the text knob.
nuke.thisNode()['txtknob_node_list'].setValue("• "+node_list_cleaned)

print node_list



# ----- This requires node_list to be defined first, and therefore, "Add Nodes To List" must be pressed first -------
# This means we should disable the Defocus button by default, by running the following in the Script editor:

# NOTE: addDefocus is what I've named the new button...
nuke.toNode('NODE_DISABLER').knob('addDefocus').setEnabled(False)


# We also need our addNodes button to re-enable said button, so let's add the following code underneath
# all the other code in addNodes:
nuke.thisNode.knob('addDefocus').setEnabled(True)


# Voila!







# ---------------------------------------------------------------------------------
#
#  I've added a NODE_DISABLER_V2 gizmo into the .nuke/gizmos directory, included
#  with this week's lesson. Import it into nuke and take a look at how it's working
#  if you get stuck!
#
#  I've also added a bunch of extra Node Class buttons as a bonus, with fancy
#  colour options for you to pick apart and learn from :)
#
#
#  It's important to note that this isn't the perfect, bullet-proof node.
#  Funny things will happen if the user (for whatever silly reason) decides they
#  want two of these nodes in their Nuke script.
#
#  Also, if linked nodes get deleted, they won't be deleted from the NODE LIST:
#  printed on the NODE_DISABLER node itself.
#
#  The lesson here is there is always more work that can be done to make a Gizmo,
#  Python Script, etc. more functional, more user-friendly, and more bullet-proof...
#  This example would get way too long and confusing if we tried to account for
#  everything!
#
# ---------------------------------------------------------------------------------
