# ----- PYTHON SCRIPT BUTTONS --------------------

# Reference the same node the code will be added to.
nuke.thisNode()

# Reference the same knob the code will be added to.
nuke.thisKnob()



# ----- PYTHON SCRIPT BUTTONS --------------------

# For all examples of Python Script Buttons from Lesson 09, please refer to the 'py_for_buttons.py' file included in the download.
# Otherwise, I've included a few other fun examples below...

# Script for a Python Script Button which randomly sets the 'tile_color' knob of all 'Grade' nodes
import random

___ i __ nuke.allNodes('Grade'):
    i['tile_color'].setValue(int(random.random()*1000000000000000))



# Script for a Python Script Button which opens a website
import webbrowser
webbrowser.open('https://benmcewan.com')





# ----- KNOB VISIBILITY --------------------

# Hide the mix knob on a node called 'Grade5'
nuke.tN..('Grade5')['mix'].setVisible(F..)

# ...and show it again
nuke.tN..('Grade5')['mix'].setVisible(True)


# Script for a Python Script Button, which hides all the knobs on the node

___ i __ nuke.thisNode().knobs():
    nuke.thisNode()[i].setVisible(F..)


# Remove knobChanged from a node
# To remove it, we actually have to add a blank value to the node's hidden knobChanged knob
nuke.tN..('NODE_DISABLER').knob('knobChanged').setValue("")





# Pretty short Cheat Sheet this week, as the rest has been covered in previous Lessons & Cheat Sheets.

