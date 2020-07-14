import nuke
import os

import nukescripts

nukescripts.autoBackdrop()

def clearNodeSelection():
  for n in nuke.selectedNodes():
    # n['selected'].setValue(False)
    n.setSelected(False)

nukescripts.clear_selection_recursive()
nukescripts.declone(node)
nukescripts.declone(nuke.selectedNode())
nukescripts.swapAB(nuke.selectedNode())
nukescripts.color_nodes()
nukescripts.search_replace()

nukescripts.getNukeUserFolder()

# nukescripts.findNextNodeName('Read')
# nuke.nodes.Read()
# nuke.nodes.Read(name=nukescripts.findNextNodeName('Read'))

# nuke.createNode('Read')
# t = nuke.toNode('Read3')
# t.setSelected(1)



