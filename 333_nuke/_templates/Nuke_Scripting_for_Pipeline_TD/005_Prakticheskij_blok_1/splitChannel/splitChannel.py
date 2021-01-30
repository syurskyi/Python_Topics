_____ ?
_____ random


___ autoBackdrop(name):
    '''
    Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    '''
    selNodes = ?.selectedNodes()
    __ no. selNodes:
        r_ ?.nodes.BackdropNode()

        # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() ___ node __ selNodes])
    bdY = min([node.ypos() ___ node __ selNodes])
    bdW = max([node.xpos() + node.screenWidth() ___ node __ selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() ___ node __ selNodes]) - bdY

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom
    left, top, right, bottom = (-10, -80, 70, 10)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    n = ?.nodes.BackdropNode(xpos=bdX,
                                bdwidth=bdW,
                                ypos=bdY,
                                bdheight=bdH,
                                tile_color=int((random.random() * (200 - 100))) + 10,
                                note_font_size=20,
                                label=name)

    # revert to previous selection
    n['selected'].setValue(False)
    ___ node __ selNodes:
        node['selected'].setValue(False)

    r_ n


___ shuffleLayer(node, layer):
    '''
    Shuffle a given layer into rgba
    args:
       node  - node to attach a Shuffle node to
       layer - layer to shuffle into rgba
    '''

    shuffleNode = ?.nodes.Shuffle(label=knob, inputs=[punto])
    shuffleNode['in'].setValue(layer)
    shuffleNode['postage_stamp'].setValue(True)
    r_ ?.nodes.Dot(inputs=[shuffleNode])

___ autoComp