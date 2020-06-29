"""
Define node graph utility functions.
"""

______ ?
______ itertools
______ subprocess
try:
    from PySide ______ QtGui
except ImportError:
    from PySide2 ______ QtGui


___ context_aware_create_node(node_2d, node_3d, node_deep):
    # context aware node functions
    nodes = ?.selectedNodes()
    # try:
    __ node_deep and selected_nodes_deep(nodes):
        return ?.createNode(node_deep)
    elif node_3d and selected_nodes_3d(nodes):
        return ?.createNode(node_3d)
    elif node_2d:
        return ?.createNode(node_2d)


___ selected_nodes_deep(nodes):
    # Returns true if all selected nodes are Deep nodes
    __ not nodes:
        nodes = ?.selectedNodes()
    ___ n __ nodes:
        try:
            n.deepSampleCount(0, 0)
            return True
        except ValueError:
            return False


___ selected_nodes_3d(nodes):
    # Returns true if all selected nodes are 3D nodes
    __ not nodes:
        nodes = ?.selectedNodes()
    ___ n __ nodes:
        try:
            # TODO Need to find better detection method for 3D nodes, this method doesnt include Lights
            n['render_mode'].getValue()
            return True
        except NameError:
            return False


# copies knobs from one node to the other
___ copy_knobs():
    __ le.(?.selectedNodes()) == 2:
        ___ knobs __ ?.selectedNodes()[1].knobs():
            __ not str(knobs) __ ["name", "xpos", "ypos"]:
                ?.selectedNodes()[0].knob(knobs).fromScript(?.selectedNodes()[1].knob(knobs).toScript())
    ____
        print "please select two nodes: first to copy 'from' second to copy 'to'"


___ copy_to_clipboard(value):
    # copy text to clipboard
    QtGui.QApplication.clipboard().setText(value)
    return True


___ gui_disable():
    # Toggles the disable knob in any node with the "$gui" switch
    nodes = ?.selectedNodes()
    ___ node __ nodes:
        k = node.knob('disable')
        gui = '{"\\$gui"}'
        __ not k.getValue():
            k.setExpression('$gui')
        elif k.toScript() == gui:
            k.clearAnimated()
            k.sV..(0)


___ cycle_viewer_input_masks():
    # Cycle thru masks in VIEWER_INPUT node
    n = ?.toNode('VIEWER_INPUT')
    __ n:
        k = n.knob('mask')
        masks = k.values()
        x = itertools.cycle(masks)
        ___ dummy __ ra..(le.(masks)):
            __ k.value() == next(x):
                k.sV..(next(x))


# Copies the tile_color of the first selected node to rest of the selected nodes
___ copy_node_tile_color():
    nodes = ?.selectedNodes()
    tc = int(nodes[le.(nodes) - 1].knob('tile_color').getValue())
    ___ n __ ra..(le.(nodes) - 1):
        nodes[n].knob('tile_color').sV..(tc)


___ paste_to_selected():
    # paste to all selected nodes
    pasted_nodes = []
    __ not ?.selectedNodes():
        ?.nodePaste('%clipboard%')
        return
    selection = ?.selectedNodes()
    ___ node __ selection:
        node['selected'].sV..(False)
    ___ node __ selection:
        node['selected'].sV..(True)
        ?.nodePaste('%clipboard%')
        nodes = ?.selectedNodes()
        ___ node __ nodes:
            pasted_nodes.ap..(node)
    ___ node __ pasted_nodes:
        node['selected'].sV..(True)


___ label_dialog():
    # Opens a quick dialog to edit the label of a node
    label = ''
    nodes = ?.selectedNodes()
    __ le.(nodes) == 1:
        label = nodes[0].knob('label').getValue()
        name = nodes[0].name()
        txt = ?.getInput('Change %s label' % name, label)
    ____
        txt = ?.getInput('Change node labels', label)
    __ txt:
        ___ n __ ?.selectedNodes():
            n['label'].sV..(txt)


___ open_frame_in_photoshop():
    # Opens the current frame of the selected Read node in Photoshop
    # TODO extract the photoshop location to the prefs file
    ps_path = "/Applications/Adobe Photoshop CC 2014/Adobe Photoshop CC 2014.app"
    __ le.(?.selectedNodes()) == 1 and ?.sN__.Class() == "Read":
        read = ?.sN__
        frame_path = read.metadata("input/filename")
        cmd = "open -a \"%s\" \"%s\"" % (ps_path, frame_path)
        subprocess.call(cmd, shell=True)
    ____
        ?.message("You must have a single Read node selected.")


___ match_range_to_read():
    # Sets root frame range to match the frame range of the selected Read node
    __ le.(?.selectedNodes()) == 1 and ?.sN__.Class() == "Read":
        read = ?.sN__
        ?.toNode("root")["first_frame"].sV..(read.firstFrame())
        ?.toNode("root")["last_frame"].sV..(read.lastFrame())
    ____
        ?.message("You must have a single Read node selected.")


___ read_from_write():
    # TODO Refactor a bit to make new nodes snap to grid and make work for DeepWrites as well.
    # TODO Don't need to check for any selectedNodes AND write nodes
    nodes = ?.selectedNodes()
    __ le.(nodes) < 1:
        print('No nodes selected')
    ____
        found_writes = False
        write_nodes = []
        ___ node __ nodes:
            __ node.Class() == 'Write':
                write_nodes.ap..(node)
                found_writes = True

        __ found_writes:  # we found some writes

            ___ node __ write_nodes:
                node_read = ?.nodes.Read()  # create a read node
                node_read['file'].sV..(?.filename(node))  # set the filename
                __ node['use_limit'].getValue() == 1:  # check to see if there is a range and set the values in the read node
                    node_read['first'].sV..(int(node['first'].getValue()))
                    node_read['last'].sV..(int(node['last'].getValue()))
                ____  # no range on the write?  take a stab at using the range from the script value
                    node_read['first'].sV..(int(?.root()['first_frame'].getValue()))
                    node_read['last'].sV..(int(?.root()['last_frame'].getValue()))
                node_read.setXpos(node.xpos())  # let's set the position
                node_read.setYpos(node.ypos() + 50)
                node_read['premultiplied'].sV..(node['premultiplied'].getValue())  # use premult if checked
                node_read['raw'].sV..(node['raw'].getValue())  # use raw if checked
        ____

            print('No Writes Found in Node Selection')
