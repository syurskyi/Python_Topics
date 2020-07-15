"""
Define node graph utility functions.
"""

______ ?
______ itertools
______ subprocess
___
    ____ ? ______ ?G..
______ ImportError:
    ____ ? ______ ?G..


___ context_aware_create_node(node_2d, node_3d, node_deep):
    # context aware node functions
    nodes _ ?.sN..
    # try:
    __ node_deep an. selected_nodes_deep(nodes):
        r_ ?.createNode(node_deep)
    ____ node_3d an. selected_nodes_3d(nodes):
        r_ ?.createNode(node_3d)
    ____ node_2d:
        r_ ?.createNode(node_2d)


___ selected_nodes_deep(nodes):
    # Returns true if all selected nodes are Deep nodes
    __ no. nodes:
        nodes _ ?.sN..
    ___ n __ nodes:
        ___
            n.deepSampleCount(0, 0)
            r_ T..
        ______ ValueError:
            r_ F..


___ selected_nodes_3d(nodes):
    # Returns true if all selected nodes are 3D nodes
    __ no. nodes:
        nodes _ ?.sN..
    ___ n __ nodes:
        ___
            # TODO Need to find better detection method for 3D nodes, this method doesnt include Lights
            n['render_mode'].gV..
            r_ T..
        ______ NameError:
            r_ F..


# copies knobs from one node to the other
___ copy_knobs():
    __ le.(?.sN..()) __ 2:
        ___ knobs __ ?.sN..[1].knobs():
            __ no. st.(knobs) __ ["name", "xpos", "ypos"]:
                ?.sN..[0].knob(knobs).fromScript(?.sN..[1].knob(knobs).toScript())
    ____
        print "please select two nodes: first to copy 'from' second to copy 'to'"


___ copy_to_clipboard(v.. ):
    # copy text to clipboard
    ?G...?A...clipboard().setText(v.. )
    r_ T..


___ gui_disable():
    # Toggles the disable knob in any node with the "$gui" switch
    nodes _ ?.sN..
    ___ node __ nodes:
        k _ node.knob('disable')
        gui _ '{"\\$gui"}'
        __ no. k.gV..:
            k.setExpression('$gui')
        ____ k.toScript() __ gui:
            k.cA..
            k.sV..(0)


___ cycle_viewer_input_masks():
    # Cycle thru masks in VIEWER_INPUT node
    n _ ?.tN..('VIEWER_INPUT')
    __ n:
        k _ n.knob('mask')
        masks _ k.values()
        x _ itertools.cycle(masks)
        ___ dummy __ ra..(le.(masks)):
            __ k.v.. __ next(x):
                k.sV..(next(x))


# Copies the tile_color of the first selected node to rest of the selected nodes
___ copy_node_tile_color():
    nodes _ ?.sN..
    tc _ __.(nodes[le.(nodes) - 1].knob('tile_color').getValue())
    ___ n __ ra..(le.(nodes) - 1):
        nodes[n].knob('tile_color').sV..(tc)


___ paste_to_selected():
    # paste to all selected nodes
    pasted_nodes _ # list
    __ no. ?.sN..:
        ?.nodePaste('%clipboard%')
        r_
    selection _ ?.sN..
    ___ node __ selection:
        node['selected'].sV..(F..)
    ___ node __ selection:
        node['selected'].sV..(T..)
        ?.nodePaste('%clipboard%')
        nodes _ ?.sN..
        ___ node __ nodes:
            pasted_nodes.ap..(node)
    ___ node __ pasted_nodes:
        node['selected'].sV..(T..)


___ label_dialog():
    # Opens a quick dialog to edit the label of a node
    label _ ''
    nodes _ ?.sN..
    __ le.(nodes) __ 1:
        label _ nodes[0].knob('label').gV..
        name _ nodes[0].n..
        txt _ ?.getInput('Change @ label' % name, label)
    ____
        txt _ ?.getInput('Change node labels', label)
    __ txt:
        ___ n __ ?.sN..:
            n['label'].sV..(txt)


___ open_frame_in_photoshop():
    # Opens the current frame of the selected Read node in Photoshop
    # TODO extract the photoshop location to the prefs file
    ps_path _ "/Applications/Adobe Photoshop CC 2014/Adobe Photoshop CC 2014.app"
    __ le.(?.sN..()) __ 1 an. ?.sN__.Class() __ "Read":
        read _ ?.sN__
        frame_path _ read.metadata("input/filename")
        cmd _ "open -a \"@\" \"@\"" % (ps_path, frame_path)
        subprocess.call(cmd, shell_T..)
    ____
        ?.m..("You must have a single Read node selected.")


___ match_range_to_read():
    # Sets root frame range to match the frame range of the selected Read node
    __ le.(?.sN..()) __ 1 an. ?.sN__.Class() __ "Read":
        read _ ?.sN__
        ?.tN..("root")["first_frame"].sV..(read.firstFrame())
        ?.tN..("root")["last_frame"].sV..(read.lastFrame())
    ____
        ?.m..("You must have a single Read node selected.")


___ read_from_write():
    # TODO Refactor a bit to make new nodes snap to grid and make work for DeepWrites as well.
    # TODO Don't need to check for any selectedNodes AND write nodes
    nodes _ ?.sN..
    __ le.(nodes) < 1:
        print('No nodes selected')
    ____
        found_writes _ F..
        write_nodes _ # list
        ___ node __ nodes:
            __ node.Class() __ 'Write':
                write_nodes.ap..(node)
                found_writes _ T..

        __ found_writes:  # we found some writes

            ___ node __ write_nodes:
                node_read _ ?.nodes.Read()  # create a read node
                node_read['file'].sV..(?.filename(node))  # set the filename
                __ node['use_limit'].gV.. __ 1:  # check to see if there is a range and set the values in the read node
                    node_read['first'].sV..(__.(node['first'].getValue()))
                    node_read['last'].sV..(__.(node['last'].getValue()))
                ____  # no range on the write?  take a stab at using the range from the script value
                    node_read['first'].sV..(__.(?.r.. ['first_frame'].getValue()))
                    node_read['last'].sV..(__.(?.r.. ['last_frame'].getValue()))
                node_read.setXpos(node.xpos())  # let's set the position
                node_read.setYpos(node.ypos() + 50)
                node_read['premultiplied'].sV..(node['premultiplied'].getValue())  # use premult if checked
                node_read['raw'].sV..(node['raw'].getValue())  # use raw if checked
        ____

            print('No Writes Found in Node Selection')