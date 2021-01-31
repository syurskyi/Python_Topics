_____ ?
# create group
# nuke.collapseToGroup(False)
# nuke.createNode('Group', inpanel=False)
# nuke.nodes.Group()

_____ ?

grp = ?.nodes.Group()
grp.begin()
?.cN..('Tracker')
?.cN..('ColorCorrect')
grp.end()
# nuke.endGroup()
# nuke.root().begin()

with grp:
    ?.nodes.Input()
    ?.nodes.Output()

?.nodes.ColorCorrect()

# get nodes

grp.output()

?.aN..()

# to get list of Nodes in Group. Version1
grp.begin()
?.aN..()
grp.end

# to get list of Nodes in Group. Version2
?.aN..(group=grp)

# to get list of Nodes in Group. Version3
# nuke.selectedNodes() # need to select group

grp.begin()
?.selectedNodes()  # need to select group
grp.end

# get parent

n = ?.aN..(group=grp)[0]
n.name()
n.fullName()
n.fullName().split('.')[:-1]
'.'.join(n.fullName().split('.')[:-1])
?.toNode('.'.join(n.fullName().split('.')[:-1])) or ?.r__ 

########################################################################################################################

_____ ?
# create group
?.collapseToGroup F..
?.cN..('Group', inpanel=False)
grp = ?.nodes.Group()

# edit group
grp.begin()
?.cN..('Tracker')
?.cN..('ColorCorrect', inpanel=False)
grp.end()
 # or
#nuke.endGroup()
# or
#nuke.root().begin()

with grp:
    ?.nodes.Input()
    ?.nodes.Output()
?.nodes.ColorCorrect()

# get nodes
grp.output()

grp.begin()
?.aN..()
grp.end()

?.aN..(group=grp)

grp.begin()
?.selectedNodes()
grp.end()

# get parent

n = ?.aN..(group=grp)[0]
n = ?.aN..()[0]
?.toNode('.'.join(n.fullName().split('.')[:-1])) or ?.r__ 






