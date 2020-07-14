# add inside exists tab

gpr_start = nuke.Tab_Knob('pr', 'Prefs', nuke.TABBEGINGROUP)
k = nuke.String_Knob('prefs', 'Preferences')
gpr_end = nuke.Tab_Knob('', '', nuke.TABENDGROUP)

node.addKnob(gpr_start)
node.addKnob(k)
node.addKnob(gpr_end)

gpr_start.setFlag(nuke.INVISIBLE)
k.setFlag(nuke.INVISIBLE)