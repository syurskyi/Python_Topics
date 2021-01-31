# ----- DIFFERENT FUNCTIONS THAT OPEN DIALOG BOXES FOR USER INPUT ---------------

# Get a user-input number
inputBox = nuke.getInput("Number + 5", "Enter your number here")

# Add 5 to our number
number = float(inputBox)+5

# Convert that number to a string, and show it in a message.
nuke.message(str(inputBox)+" + 5 = "+str(number))



# ------  Others  ------

nuke.ask("I am a question!") # pops open a window that asks a question, with a yes and a no button.
# Clicking “Yes” returns the value True, and clicking “No” returns the value False.
# We would deal with the true and false responses the same way we dealt with the “Cancel” button returning None in our comment shortcut function.

nuke.getColor("Window Name") # opens a colour picker window.
# It returns some funky hex values, which we can convert the same way we did when we created our shuffleShortcuts.py Python Script.

nuke.getFilename("Get File", '*.nk *.py') # opens the same sort of window that File > Open would.
# As always, the first argument names the window, and the second (optionally) allows you to add filters to only look for certain filetypes.
# Each new filter starts with a *, and is separated from the previous filter by a space.

nuke.getClipname(“Get Sequence”) # is similar to nuke.getFilename(), except it searches for image sequences.
# Just like the window that pops up when you create a Read node.

nuke.getFramesAndViews("Get Frame Range", '1001-1050') # let’s you define a frame range.
# If your script is set up for stereo, it also gives an option for which views to use (or returns ‘main’ if not).
# It’s worth noting that this returns a list rather than a single value...





# ----- CUSTOM PANELS ---------------

# Create a panel called 'My Panel'.
panel = nuke.Panel("My Panel")

# Show the panel, with some error checking (must be inside a function).
# If the cancel button is pressed, the window will close and nothing will happen.
if not panel.show():
	return



# Add a single line input knob to the panel.
panel.addSingleLineInput("Label", "Default Text")

# Add a dropdown list knob with 3 items.
panel.addEnumerationPulldown("Label", 'Item1 Item2 Item3')

# Add a checkbox knob, which is checked by default.
panel.addBooleanCheckBox("Label", True)

# Learn about more knob types here:
# https://learn.foundry.com/nuke/developers/113/ndkdevguide/knobs-and-handles/knobtypes.html





# ----- USING EXISTING DATA TO POPULATE KNOBS ---------------

# Set the value of a selected node's mix knob with a pop-up, using the existing value as the default.
oldValue = nuke.selectedNode()['mix'].value()
newValue = nuke.getInput('Mix Value', str(oldValue))
nuke.selectedNode()['mix'].setValue(float(newValue))



# --- Create an EnumerationPulldown knob, and populate it with a list of selected nodes.

# Create a panel called 'My Panel'.
panel = nuke.Panel("My Panel")

# Create a new list.
node_list = []

# Put all selected nodes' names in 'node_list'.
for i in nuke.selectedNodes():
    node_list.append(i.name())

# Sort list alphabetically.
node_list.sort()

# Join the list into a string with spaces in between each item, so the EnumerationPulldown has data it expects.
node_list_string = " ".join(node_list)

# Add a dropdown list knob with all the selected nodes.
panel.addEnumerationPulldown("Label", node_list_string)

# Show the panel
panel.show()