import os
node =?.sN__

grp = ?.Tab_Knob('parm', 'Parameters')
node.addKnob(grp)

k1 = ?.Double_Knob('k1', 'Value 1')
node.addKnob(k1)

k2 = ?.Boolean_Knob('cb', 'Chackbox')
k2.setFlag(?.STARTLINE)
node.addKnob(k2)

#k1.setFlag(nuke.INVISIBLE)
#k1.clearFlag(nuke.INVISIBLE)

gpr1 = ?.Tab_Knob('grp1', 'Grp1', ?.TABBEGINGROUP)
node.addKnob(gpr1)
k3 = ?.Int_Knob('k3', 'Value')
node.addKnob(k3)
gpr2 = ?.Tab_Knob('grp2', 'Grp1', ?.TABENDGROUP)
node.addKnob(gpr2)
k34 = ?.Int_Knob('k34', 'Value')
node.addKnob(k34)

# select Blur node
k = ?.sN__['size']
node.addKnob(k)
k.setLabel('SIZE')
#nuke.selectedNode().addKnob(k3)