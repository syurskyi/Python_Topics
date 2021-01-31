_____ ?
_____ random


___ autoBackdrop(name):
    '''
    Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    '''
    selNodes _ ?.sN..
    __ no. selNodes:
        r_ ?.n__.BackdropNode()

        # Calculate bounds for the backdrop node.
    bdX _ min([node.xpos() ___ node __ selNodes])
    bdY _ min([node.yp__() ___ node __ selNodes])
    bdW _ max([node.xpos() + node.screenWidth() ___ node __ selNodes]) - bdX
    bdH _ max([node.yp__() + node.screenHeight() ___ node __ selNodes]) - bdY

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom
    left, top, right, bottom _ (-10, -80, 70, 10)
    bdX +_ left
    bdY +_ top
    bdW +_ (right - left)
    bdH +_ (bottom - top)

    n _ ?.n__.BackdropNode(xpos_bdX,
                                bdwidth_bdW,
                                yp___bdY,
                                bdheight_bdH,
                                tile_color_in_((random.random() * (200 - 100))) + 10,
                                note_font_size_20,
                                label_name)

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

    shuffleNode _ ?.n__.Shuffle(label_knob, inputs_[punto])
    shuffleNode['in'].sV..(layer)
    shuffleNode['postage_stamp'].sV.. T..
    r_ ?.n__.Dot(inputs_[shuffleNode])

___ autoComp