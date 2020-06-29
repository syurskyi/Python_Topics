# add inside exists tab

gpr_start = ?.Tab_Knob('pr', 'Prefs', ?.TABBEGINGROUP)
k = ?.String_Knob('prefs', 'Preferences')
gpr_end = ?.Tab_Knob('', '', ?.TABENDGROUP)

node.addKnob(gpr_start)
node.addKnob(k)
node.addKnob(gpr_end)

gpr_start.setFlag(?.INVISIBLE)
k.setFlag(?.INVISIBLE)