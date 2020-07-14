import nuke
import random


def autoBackdrop(name):
    '''
    Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    '''
    selNodes = nuke.selectedNodes()
    if not selNodes:
        return nuke.nodes.BackdropNode()

        # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom
    left, top, right, bottom = (-10, -80, 70, 10)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    n = nuke.nodes.BackdropNode(xpos=bdX,
                                bdwidth=bdW,
                                ypos=bdY,
                                bdheight=bdH,
                                tile_color=int((random.random() * (200 - 100))) + 10,
                                note_font_size=20,
                                label=name)

    # revert to previous selection
    n['selected'].setValue(False)
    for node in selNodes:
        node['selected'].setValue(False)

    return n


def shuffleLayer(node, layer):
    '''
    Shuffle a given layer into rgba
    args:
       node  - node to attach a Shuffle node to
       layer - layer to shuffle into rgba
    '''

    shuffleNode = nuke.nodes.Shuffle(label=knob, inputs=[punto])
    shuffleNode['in'].setValue(layer)
    shuffleNode['postage_stamp'].setValue(True)
    return nuke.nodes.Dot(inputs=[shuffleNode])

def autoComp