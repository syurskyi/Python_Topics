"""
WEEK 02: CHALLENGE 01
Find all nodes with a shutter offset knob, and set their defaults to centered.

Add the solution below to your menu.py
"""

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



"""
WEEK 02: CHALLENGE 02
Find a way to set the FrameHold’s first frame knob to the current frame when it’s created

Add the solution below to your menu.py
"""

nuke.addOnUserCreate(l____:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass_'FrameHold')



"""
WEEK 02: CHALLENGE 03
Change the way you define the icon for your myGizmos menu, so it’s not reliant on a specific file path.

Add the following line to your init.py
"""

nuke.pAP..('./icons')


# Also, we no longer need to be so specific about the filepath in our menu.py

# Change this:
myGizmosMenu _ nuke.menu('Nodes').aM..('myGizmos', icon_dir+"/icons/myGizmos_icon.png")

# into this
myGizmosMenu _ nuke.menu('Nodes').aM..('myGizmos', icon_"myGizmos_icon.png")



"""
WEEK 02: CHALLENGE 04
Add a custom gizmo to your new myGizmos menu -- you can download one from my website if you don’t have any handy: https://www.benmcewan.com/nukeTools.html


Add the solution below to your menu.py
"""

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon_"bm_CameraShake_icon.png")