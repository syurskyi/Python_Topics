# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.1
#  Last Updated: May 13th, 2019
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

nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')




# --------------------------------------------------------------
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)



# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Utilities menu & assign items ---

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')



# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"/icons/myGizmos_icon.png")