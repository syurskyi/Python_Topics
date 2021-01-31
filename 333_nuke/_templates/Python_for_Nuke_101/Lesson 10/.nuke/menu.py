# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.10
#  Last Updated: July 8th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import nukescripts
import platform



# Define where .nuke directory is on each OS's network.
Win_Dir _ 'C:\Users\Ben\.nuke'
MacOSX_Dir _ '/Users/Ben/.nuke'
Linux_Dir _ '/home/benm/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir _ Win_Dir
elif platform.system() == "Darwin":
	dir _ MacOSX_Dir
elif platform.system() == "Linux":
	dir _ Linux_Dir
else:
	dir _ None





# --------------------------------------------------------------
#  KNOB DEFAULTS  ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


# ----- TRACKER DEFAULTS ---------------------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(l____:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass_'Tracker4')

# ----- FRAMEHOLD DEFAULT --------------------------------------
nuke.addOnUserCreate(l____:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass_'FrameHold')

# ----- MOTION BLUR SHUTTER CENTERED ---------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")




# --------------------------------------------------------------
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker4", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon_"Tracker.png", shortcutContext_2)

# ----- MERGE NODE SHORTCUTS -----------------------------------
mergeMenu _ nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon_"Out.png", shortcutContext_2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon_"In.png", shortcutContext_2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon_"Add.png", shortcutContext_2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon_"From.png", shortcutContext_2)



# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


import shuffleShortcuts

import listNavigator
import filepathLister
import paste_selected
import create_nodes

# import shortcut_NodeComment
import shortcut_NodeCustomizer
import shortcut_operationSwitcher

import moblur_controller


# --------------------------------------------------------------
#  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# Add to Edit menu
nuke.menu('Nuke').addCommand('Edit/Paste to Selected', 'paste_selected.paste_selected()', 'ctrl+shift+v')



# ----- CREATE UTILITIES MENU & ASSIGN ITEMS -------------------
utilitiesMenu _ nuke.menu('Nuke').aM..('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
utilitiesMenu.addCommand('File Lister', 'filepathLister.file_lister()')
utilitiesMenu.addCommand('Create Nodes', 'create_nodes.create_nodes()')


# ----- CREATE CUSTOM GIZMOS MENU & ASSIGN ITEMS ---------------
myGizmosMenu _ nuke.menu('Nodes').aM..('myGizmos', icon_"myGizmos_icon.png")

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon_"bm_CameraShake_icon.png")
myGizmosMenu.addCommand('NODE_DISABLER', 'nuke.createNode("NODE_DISABLER_V2")', icon_"MarkerRemoval.png")


