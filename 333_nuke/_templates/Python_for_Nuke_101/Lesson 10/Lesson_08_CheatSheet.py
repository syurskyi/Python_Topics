# ----- FINDING IF A KNOB EXISTS ON A SELECTED NODE --------------------

# The right way.

n = nuke.sN..

if n.knob('motionblur'):
    print "yes"
else:
    print "no"



# The wrong way.

n = nuke.sN..

if n['motionblur']:
    print "yes"
else:
    print "no"

# This way fails, because the '.knob()' function has error handling built in.





# ----- ADDING KNOBS TO A NODE --------------------

# Create a NoOp node and name it.
NoOp = nuke.createNode('NoOp')
NoOp['name'].setValue("GLOBAL_MOTIONBLUR_CONTROLLER")
	
# Add an Integer knob.
NoOp.addKnob(nuke.Int_Knob('global_motionblur', "motionblur"))

# Add a Floating Point Slide knob.
NoOp.addKnob(nuke.Double_Knob('global_shutter', "shutter"))

# Add a Checkbox knob.
NoOp.addKnob(nuke.Boolean_Knob('global_disable_moblur', "disable motionblur"))



# More Knob Names.
https://learn.foundry.com/nuke/developers/63/ndkdevguide/knobs-and-handles/knobtypes.html





# ----- SETTING KNOB FLAGS & VALUES --------------------

# Clear all keyframes or expressions from a knob.
nuke.sN.. .['mix'].clearAnimated()

# Clear all keyframes or expressions from every knob on a selected node.
for knob in nuke.sN.. .knobs():
	nuke.sN.. [knob].clearAnimated()



# Move the 'black_clamp' knob on a selected Grade node to a new line.
nuke.sN.. ['black_clamp'].setFlag(nuke.STARTLINE)

# Disable a selected node's mix knob
nuke.sN.. ['mix'].setFlag(nuke.DISABLED)

# Hide a selected node's mix knob
nuke.sN.. ['mix'].setFlag(nuke.INVISIBLE)

# You can also do this with the '.setVisible()' function, although you can't show / hide knobs with these two methods interchangably.
nuke.sN.. ['mix'].setVisible(F..)


# Knob Flags
https://learn.foundry.com/nuke/developers/63/ndkdevguide/knobs-and-handles/knobflags.html





# ----- TCL IF / ELSE STATEMENTS --------------------

# Syntax reads as follows.

<knob> <condition> <value> ? <if true, do this> : <otherwise, do that>

# Putting this on a node's label will print "off" if the mix knob's value is 0,
# otherwise, it won't display a label at all.
[expr {[value mix] == 0 ? "off" : "" }]

# Another example: putting the following TCL expression on a Grade node's mix knob will
# set the mix knob to 0.5 if multiply has a value of 2 or higher.
multiply >= 2 ? 0.5 : 1

# Last one... You can make the $gui expression more specific this way:
# Putting the following expression on a 'ScanlineRender' node's 'samples' knob will
# render with 10 samples on the farm, and only 1 sample in the GUI.
$gui?1:10
