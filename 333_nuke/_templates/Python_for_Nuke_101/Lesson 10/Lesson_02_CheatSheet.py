# ----- SETTING KNOB DEFAULTS ---------------

# Set shutter offset to "centered".
nuke.knobDefault('Tracker4.shutteroffset', "centered")

# Set dynamic label on Tracker to display the value of the "transform" and "reference_frame" knobs.
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")

# Any time a Tracker node is created, set the "reference_frame" knob to the value of the current frame.
nuke.addOnUserCreate(l____:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass_'Tracker4')





# ----- ADDING CUSTOM MENUS --------------------------

# Create Utilities menu & assign items
utilitiesMenu _ nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

# Create Custom Gizmos menu. Remember, it won't appear until there's a menu item...
myGizmosMenu _ nuke.menu('Nodes').addMenu('myGizmos', icon_dir+"/icons/myGizmos_icon.png")





# ----- MENU TYPES --------------------------

# Top menu-bar, where File, Edit, etc. lives
nuke.menu('Nuke')

# Gizmos menu on the side
nuke.menu('Nodes')

# Right-click menu in the Viewer
nuke.menu('Viewer')

# Right-click menu in the Node Graph
nuke.menu('Node Graph')

# Right-click menu on a knob & in the curve editor
nuke.menu('Animation')

# Run the following to see others
help(nuke.menu)





# ----- KEYBOARD SHORTCUTS --------------------------

# Add a custom keyboard shortcut to a node
nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon_"Tracker.png", shortcutContext_2)

# In English, the syntax reads,
# nuke.menu('<Name of Menu>').addCommand("<Node Class>/<Node Label>", "nuke.createNode(<Node Class>)", "<Your Keyboard Shortcut>", icon="<Filename of Icon>", shortcutContext=2)

# --- Shortcut contexts:

# Context = Window
shortcutContext_0
# Context = Application
shortcutContext_1
# Context = Node Graph
shortcutContext_2


