_____ ?
_____ random


___ autoBackdrop(name):
    '''
    Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    '''
    selNodes = ?.sN..
    __ no. selNodes:
        r_ ?.n__.BackdropNode()

        # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() ___ node __ selNodes])
    bdY = min([node.yp__() ___ node __ selNodes])
    bdW = max([node.xpos() + node.screenWidth() ___ node __ selNodes]) - bdX
    bdH = max([node.yp__() + node.screenHeight() ___ node __ selNodes]) - bdY

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom
    left, top, right, bottom = (-10, -80, 70, 10)
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    n = ?.n__.BackdropNode(xpos=bdX,
                                bdwidth=bdW,
                                yp__=bdY,
                                bdheight=bdH,
                                tile_color=in_((random.random() * (200 - 100))) + 10,
                                note_font_size=20,
                                label=name)

    # revert to previous selection
    n['selected'].sV.. F..
    ___ node __ selNodes:
        node['selected'].sV.. F..

    r_ n


___ shuffleLayer(node, layer):
    '''
    Shuffle a given layer into rgba
    args:
       node  - node to attach a Shuffle node to
       layer - layer to shuffle into rgba
    '''

    shuffleNode = ?.n__.Shuffle(label=knob, inputs=[punto])
    shuffleNode['in'].sV..(layer)
    shuffleNode['postage_stamp'].sV.. T..
    r_ ?.n__.Dot(inputs=[shuffleNode])

___ autoComp