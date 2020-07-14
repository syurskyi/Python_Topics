import nuke

nuke.allNodes()
nuke.allNodes('ColorCorrect')

nuke.selectedNodes('ColorCorrect')


nodes = nuke.allNodes()
print[x for x in nodes if x.Class()=='Transform']

nuke.toNode('ColorCorrect1')

nuke.activeViewer()

nuke.activeViewer().node()