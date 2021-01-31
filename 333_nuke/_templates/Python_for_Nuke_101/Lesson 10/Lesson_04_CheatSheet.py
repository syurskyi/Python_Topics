# ----- CREATING NODES / CHANGING KNOBS / SETTING INPUTS ---------------

# Creates a Shuffle node.
nuke.createNode('Shuffle')

# Creates a Shuffle node with all channels set to 'green'.
myShuffle = nuke.createNode("Shuffle")

myShuffle['red'].setValue('green')
myShuffle['green'].setValue('green')
myShuffle['blue'].setValue('green')
myShuffle['alpha'].setValue('green')

# Displaying a selected node's mix knob's value in the node's label (TCL).
nuke.selectedNode()['label'].setValue("Mix: [value mix]")



# Set the input of a selected node to a node named 'Grade4.'
nuke.selectedNode().setInput(0, nuke.toNode('Grade4'))

# Connect the mask input of all Blur nodes to a selected node.
for i in nuke.allNodes('Blur'):
    i.setInput(1, nuke.selectedNode())



# Move a node called 'Blur15' in the node graph to the right of a selected node.
nuke.selectedNode()['xpos'].setValue(nuke.toNode('Blur15')['xpos'].value()+150)
nuke.selectedNode()['ypos'].setValue(nuke.toNode('Blur15')['ypos'].value())

# Same thing, but a little cleaner with variables.
node_to_align_to = nuke.toNode('Blur15')
node_xPos = node_to_align_to['xpos'].value()
node_yPos = node_to_align_to['ypos'].value()
 
selected_xPos_knob = nuke.selectedNode()['xpos']
selected_yPos_knob = nuke.selectedNode()['ypos']

selected_xPos_knob.setValue(node_xPos+150)
selected_yPos_knob.setValue(node_yPos)





# ----- FUNCTIONS ---------------

# Defining a function.
def theNameOfYourFunction():

# Defining a function with arguments.
def theNameOfYourFunction(arg1, arg2, arg3):

# Create a simple addition calculator using arguments .
def simple_addition_calc(value1, value2):

    print str(value1)+" + "+str(value2)+" = "+str(value1+value2)

simple_addition_calc(5, 12)


# Adding menu items for our shuffleShortcuts.py functions
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "shuffleShortcuts.createCustomShuffle('alpha', 'rgba', 'alpha', 1, 1, 1)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)





# ----- SETTING A NODE'S TILE_COLOR KNOB IN A PAINLESS WAY ---------------

# Multiplying Nuke's slider values by 255 to convert them to 8-bit, then converting that to a hexidecimal colour value.
myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (0*255,1*255,0*255,1),16))



# Function that does the above.
def hex_color_to_rgb(red, green, blue):
    return int('%02x%02x%02x%02x' % (red*255,green*255,blue*255,255),16)

# You would then set the tile_color like so:
nuke.selectedNode()['tile_color'].setValue(hex_color_to_rgb(1,0.6,0))



# Function that converts a web-based hex colour, which can be easily-googled,
# to a nuke-friendly format.
# https://www.google.com/search?q=hex+color+picker

def hex_color_to_int(hexValue):
    return int(hexValue+'00', 16)