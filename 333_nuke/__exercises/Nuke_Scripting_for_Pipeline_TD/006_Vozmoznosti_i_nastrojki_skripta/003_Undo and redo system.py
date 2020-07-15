nuke.Undo.begin('My Script')
for i in range(15):
    nuke.createNode('Blur', inpanel=False)
nuke.Undo.end()

nuke.Undo.begin('My Script1')
for i in range(15):
    nuke.nodes.Blur()
nuke.Undo.end()

undo = nuke.Undo()
undo.begin('My Action')
for i in range(15):
    nuke.nodes.Blur()
undo.end()
undo.undo()
#nuke.undo()
undo.redo()

with nuke.Undo():
    for i in range(15):
        nuke.nodes.Blur()