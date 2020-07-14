import os
node =nuke.selectedNode()

grp = nuke.Tab_Knob('parm', 'Parameters')
node.addKnob(grp)

k1 = nuke.Double_Knob('k1', 'Value 1')
node.addKnob(k1)

k2 = nuke.Boolean_Knob('cb', 'Chackbox')
k2.setFlag(nuke.STARTLINE)
node.addKnob(k2)

#k1.setFlag(nuke.INVISIBLE)
#k1.clearFlag(nuke.INVISIBLE)

gpr1 = nuke.Tab_Knob('grp1', 'Grp1', nuke.TABBEGINGROUP)
node.addKnob(gpr1)
k3 = nuke.Int_Knob('k3', 'Value')
node.addKnob(k3)
gpr2 = nuke.Tab_Knob('grp2', 'Grp1', nuke.TABENDGROUP)
node.addKnob(gpr2)
k34 = nuke.Int_Knob('k34', 'Value')
node.addKnob(k34)

# select Blur node
k = nuke.selectedNode()['size']
node.addKnob(k)
k.setLabel('SIZE')
#nuke.selectedNode().addKnob(k3)