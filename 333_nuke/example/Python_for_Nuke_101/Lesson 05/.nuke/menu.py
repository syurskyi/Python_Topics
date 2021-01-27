# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.5
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import nukescripts
import platform



# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\Ben\.nuke'
MacOSX_Dir = '/Users/Ben/.nuke'
Linux_Dir = '/home/benm/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None





# --------------------------------------------------------------
#  KNOB DEFAULTS  ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


# ----- TRACKER DEFAULTS ---------------------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

# ----- FRAMEHOLD DEFAULT --------------------------------------
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

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

nuke.menu('Nodes').addCommand("Transform/Tracker4", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)

# ----- MERGE NODE SHORTCUTS -----------------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Add.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="From.png", shortcutContext=2)



# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


import shuffleShortcuts

import listNavigator
import filepathLister
import paste_selected



# --------------------------------------------------------------
#  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# ----- CREATE UTILITIES MENU & ASSIGN ITEMS -------------------
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')



# ----- CREATE CUSTOM GIZMOS MENU & ASSIGN ITEMS ---------------
myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")

