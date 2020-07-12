# add inside exists tab

gpr_start _ ?.T_K..('pr', 'Prefs', ?.TAB..)
k _ ?.String_Knob('prefs', 'Preferences')
gpr_end _ ?.T_K..('', '', ?.TABENDGROUP)

node.aK..(gpr_start)
node.aK..(k)
node.aK..(gpr_end)

gpr_start.sF..(?.INVISIBLE)
k.sF..(?.INVISIBLE)