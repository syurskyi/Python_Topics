import nuke
# create group
# nuke.collapseToGroup(False)
# nuke.createNode('Group', inpanel=False)
# nuke.nodes.Group()

import nuke

grp = nuke.nodes.Group()
grp.begin()
nuke.createNode('Tracker')
nuke.createNode('ColorCorrect')
grp.end()
# nuke.endGroup()
# nuke.root().begin()

with grp:
    nuke.nodes.Input()
    nuke.nodes.Output()

nuke.nodes.ColorCorrect()

# get nodes

grp.output()

nuke.allNodes()

# to get list of Nodes in Group. Version1
grp.begin()
nuke.allNodes()
grp.end

# to get list of Nodes in Group. Version2
nuke.allNodes(group=grp)

# to get list of Nodes in Group. Version3
# nuke.selectedNodes() # need to select group

grp.begin()
nuke.selectedNodes()  # need to select group
grp.end

# get parent

n = nuke.allNodes(group=grp)[0]
n.name()
n.fullName()
n.fullName().split('.')[:-1]
'.'.join(n.fullName().split('.')[:-1])
nuke.toNode('.'.join(n.fullName().split('.')[:-1])) or nuke.root()

########################################################################################################################

import nuke
# create group
nuke.collapseToGroup(False)
nuke.createNode('Group', inpanel=False)
grp = nuke.nodes.Group()

# edit group
grp.begin()
nuke.createNode('Tracker')
nuke.createNode('ColorCorrect', inpanel=False)
grp.end()
 # or
#nuke.endGroup()
# or
#nuke.root().begin()

with grp:
    nuke.nodes.Input()
    nuke.nodes.Output()
nuke.nodes.ColorCorrect()

# get nodes
grp.output()

grp.begin()
nuke.allNodes()
grp.end()

nuke.allNodes(group=grp)

grp.begin()
nuke.selectedNodes()
grp.end()

# get parent

n = nuke.allNodes(group=grp)[0]
n = nuke.allNodes()[0]
nuke.toNode('.'.join(n.fullName().split('.')[:-1])) or nuke.root()






