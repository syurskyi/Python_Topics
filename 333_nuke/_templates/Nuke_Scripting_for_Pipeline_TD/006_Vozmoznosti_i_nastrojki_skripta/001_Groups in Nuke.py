_____ ?
# create group
# nuke.collapseToGroup(False)
# nuke.createNode('Group', inpanel=False)
# nuke.nodes.Group()

_____ ?

grp _ ?.n__.Group()
grp.begin()
?.cN..('Tracker')
?.cN..('ColorCorrect')
grp.end()
# nuke.endGroup()
# nuke.root().begin()

with grp:
    ?.n__.Input()
    ?.n__.Output()

?.n__.ColorCorrect()

# get nodes

grp.output()

?.aN..()

# to get list of Nodes in Group. Version1
grp.begin()
?.aN..()
grp.end

# to get list of Nodes in Group. Version2
?.aN..(group_grp)

# to get list of Nodes in Group. Version3
# nuke.selectedNodes() # need to select group

grp.begin()
?.sN..   # need to select group
grp.end

# get parent

n _ ?.aN..(group_grp)[0]
n.n..
n.fullName()
n.fullName().sp__('.')[:-1]
'.'.j..(n.fullName().sp__('.')[:-1])
?.tN..('.'.j..(n.fullName().sp__('.')[:-1])) or ?.r__

########################################################################################################################

_____ ?
# create group
?.collapseToGroup F..
?.cN..('Group', __.._F..)
grp _ ?.n__.Group()

# edit group
grp.begin()
?.cN..('Tracker')
?.cN..('ColorCorrect', __.._F..)
grp.end()
 # or
#nuke.endGroup()
# or
#nuke.root().begin()

with grp:
    ?.n__.Input()
    ?.n__.Output()
?.n__.ColorCorrect()

# get nodes
grp.output()

grp.begin()
?.aN..()
grp.end()

?.aN..(group_grp)

grp.begin()
?.sN..
grp.end()

# get parent

n _ ?.aN..(group_grp)[0]
n _ ?.aN..()[0]
?.tN..('.'.j..(n.fullName().sp__('.')[:-1])) or ?.r__






