______ ?
______ nukescripts
______ operator, math, os
______ string
______ random

# Get the grid size from the preferences. Used as the default unit of movement.
grid = (int(?.tN..('preferences').knob('GridWidth').value()), int(?.tN..('preferences').knob('GridHeight').value()))


___ unselect(nodes=None):
    # Unselect nodes
    __ not nodes:
        nodes = ?.allNodes(recurseGroups=True)
    __ not isinstance(nodes, list):
        r_
    _ = [n.setSelected(False) ___ n in nodes]


___ select(nodes):
    # Select specified nodes
    __ not isinstance(nodes, list):
        r_
    _ = [n.setSelected(True) ___ n in nodes]


___ get_parent(node):
    # return node's parent node, return nuke.root() if on the top level
    r_ ?.tN..('.'.j..(node.fullName().split('.')[:-1])) or ?.root()


___ get_topnode(node):

    # return the topnode of node
    r_ ?.tN..(?.tcl('return [value [topnode {0}].name]'.format(node.fullName())))


___ get_pos(node):
    # return 2d list of centered node positions
    __ node.Class() __ 'BackdropNode':
        r_ [node.xpos(), node.ypos()]
    ____
        r_ [node.xpos() + node.screenWidth()/2, node.ypos() + node.screenHeight()/2]


___ set_pos(node, posx, posy):
    # Set node's position given a centered position based on screen width
    # param: pos - 2dim list of int node positions
    __ node.Class() __ 'BackdropNode':
        r_ node.setXYpos(int(posx), int(posy))
    ____
        r_ node.setXYpos(int(posx - node.screenWidth()/2), int(posy - node.screenHeight()/2))


___ hide_panel():
    # Always hide control panels on node creation
    ?.tN..().showControlPanel()
    ?.tN..().hideControlPanel()
?.addOnUserCreate(hide_panel)


___ open_panels(nodes=None):
    # Open properties panels
    __ not nodes:
        nodes = ?.sN..()
    ignored = ['Viewer']
    __ le.(nodes) > 10:
        __ not ?.a..('Continuing will open {0} properties panels. \nAre you sure you want to continue?'.format(le.(nodes))):
            r_
    ___ node in nodes:
        __ node.Class() not in ignored:
            # if node.shown():
            #     if nclass in buggy:
            #         # There is a bug with node.shown() for some node classes, where .shown()
            #         # incorrectly returns true if it is hidden. Workaround by cutting node and undoing
            #         nuke.Undo().begin()
            #         nuke.delete(node)
            #         nuke.Undo().end()
            #         nuke.undo()
            #         node.setSelected(True)
            #     node.hideControlPanel()
            # else:
            node.showControlPanel()


___ close_panels(nodes=None):
    # Close all properties panels
    __ not nodes:
        nodes = ?.allNodes(recurseGroups=True)
    ___ node in nodes:
        node.hideControlPanel()


___ select_similar_position(axis=1):
    nodes = ?.sN..()
    __ not nodes:
        r_
    node = nodes[0]
    prev_selected = nodes[1:]
    threshold = 1
    unselect()
    select(prev_selected)
    __ axis:
        same_pos_nodes = {n:n.xpos() ___ n in ?.allNodes() __ abs(n.ypos()- node.ypos()) < threshold}
    ____
        same_pos_nodes = {n:n.ypos() ___ n in ?.allNodes() __ abs(n.xpos()- node.xpos()) < threshold}
    sorted_nodes = sorted(same_pos_nodes.i..(), key=operator.itemgetter(1))
    ___ n, pos in sorted_nodes:
        n.setSelected(True)


___ snap_to_grid():
    # Snap selected nodes to grid
    nodes = ?.sN..()
    ___ node in nodes:
        ?.autoplaceSnap(node)


___ auto_place():
    # autoplace all selected
    nodes = ?.sN..()

    # Sort by file knob value if the nodes have one
    filenodes = {n: n['file'].getValue() ___ n in nodes __ 'file' in n.knobs()}
    __ filenodes:
        sorted_filenodes = sorted(filenodes.i..(), key=operator.itemgetter(1))
        filenodes_pos = {n: [n.xpos(), n.ypos()] ___ n in nodes __ 'file' in n.knobs()}
        ypos_sort = sorted(filenodes_pos.i..(), key=l___ (k, v): v[1])
        xpos_sort = sorted(filenodes_pos.i..(), key=l___ (k, v): v[0])
        start_pos = [xpos_sort[0][1][0], ypos_sort[0][1][1]]
        ___ node, filepath in sorted_filenodes:
            node.setXYpos(start_pos[0], start_pos[1])
            start_pos = (start_pos[0] + grid[0]*2, start_pos[1])

    # Normal autoplace for nodes without file knob
    normal_nodes = [n ___ n in nodes __ 'file' not in n.knobs()]
    unselect()
    _ = [n.setSelected(True) ___ n in normal_nodes]
    ?.autoplace_all()
    _ = [n.setSelected(True) ___ n in nodes]


___ move(xvel, yvel):
    # Move selected nodes by specified number of grid lengths in x and y
    yvel *= 3
    nodes = ?.sN..()
    ___ node in nodes:
        node.setXYpos(int(node.xpos() + grid[0] * xvel), int(node.ypos() + grid[1] * yvel))


___ get_closest_node(node):
    # Return the closest node to node
    distances = {}
    ___ n in ?.allNodes():
        __ n.name() __ node.name():
            c___
        distance = math.sqrt( 
            math.pow( (node.xpos() - n.xpos()), 2 ) + math.pow( (node.ypos() - n.ypos()), 2 )
        )
        distances[n.name()] = distance
    r_ ?.tN..(min(distances, key=distances.get))


___ connect_to_closest(direction=0):
    # Connect next available input of all selected nodes to the closest node
    ___ node in ?.sN..():
        closest = get_closest_node(node)
        __ direction:
            closest.setInput(0, node)
        ____
            node.connectInput(0, closest)


___ paste_to_selected():
    nodes = ?.sN..()
    all_nodes = ?.allNodes()
    unselect()
    ___ node in nodes:
        node.setSelected(True)
        ?.nodePaste('%clipboard')
        unselect()
    __ not nodes:
        ?.nodePaste('%clipboard')
    # Select pasted nodes
    select(all_nodes)
    ?.invertSelection()
    

___ align(direction):
    # Align nodes to the farthest outlier in the specified direction.
    # param: direction - one of: left | right | up | down

    nodes = ?.sN..()

    __ le.(nodes) < 2:
        r_

    horizontally = ['left', 'right']
    vertically = ['up', 'down']

    __ direction in horizontally:
        align = 0
    ____ direction in vertically:
        align = 1
    ____
        print 'Error: invalid direction specified: {0}'.format(direction)
        r_

    positions = {n: get_pos(n) ___ n in nodes}
    sorted_positions = sorted(positions.i..(), key=l___ (k, v): v[align])
    __ direction in ['down', 'right']:
        sorted_positions.reverse()
    target = sorted_positions[0]
    target_pos = target[1]

    offset = 0

    other_axis = abs(1 - align)

    sorted_other_axis = sorted(positions.i..(), key=l___ (k, v): v[other_axis])

    ?.Undo().begin()
    ___ i in ra__(le.(sorted_other_axis)):
        node = sorted_other_axis[i][0]
        pos = sorted_other_axis[i][1]
        __ i __ 0: 
            distance = 0
            overlapping = False
            prev_pos = pos
        ____
            prev_pos = sorted_other_axis[i-1][1]
            # Compare current node position to previous node position.
            # If difference is < overlap threshold, nodes are overlapping.
            distance = abs(pos[other_axis] + grid[other_axis] * offset - prev_pos[other_axis])
            overlap_threshold = [int(node.screenWidth() * 1.1), int(node.screenHeight() * 1.1)]
            overlapping = distance < overlap_threshold[other_axis]

        __ overlapping:
            offset += 1

        new_pos = pos
        new_pos[other_axis] = int(pos[other_axis] + grid[other_axis] * offset)

        # Set value into sorted_other_axis also so we access the right value on the next loop
        sorted_other_axis[i][1][other_axis] = new_pos[other_axis]
        
        __ align:
            set_pos(node, new_pos[other_axis], target_pos[align])
        ____
            set_pos(node, target_pos[align], new_pos[other_axis])
        i += 1
    ?.Undo().end()


___ scale(axis, scale, pivot='max'):
    # Scale selected nodes by factor of xscale, yscale
    # param: axis - one of 0 or 1 - x or y scale
    # param: float scale - factor to scale. 1 will do nothing. 2 will scale up 1 grid unit.
    # param: str pivot - where to scale from. One of min | max | center
    pivots = ['min', 'max', 'center']
    __ pivot not in pivots:
        r_
    nodes = ?.sN..()
    __ le.(nodes) < 2:
        r_

    positions = {n: get_pos(n) ___ n in nodes}
    sort = sorted(positions.i..(), key=l___ (k, v): v[axis])

    minpos = sort[0][1][axis]
    maxpos = sort[-1][1][axis]

    __ pivot __ 'max':
        pivot_pos = maxpos
    ____ pivot __ 'min':
        pivot_pos = minpos
    ____ pivot __ 'center':
        pivot_pos = (minpos - maxpos)/2 + minpos

    ?.Undo().begin()
    ___ node, pos in positions.iteritems():
        __ axis:
            new_pos = (pos[1] - pivot_pos) * scale + pivot_pos
            set_pos(node, pos[0], new_pos)
            __ node.Class() __ 'BackdropNode':
                bdpos = ((pos[1] + node['bdheight'].getValue()) - pivot_pos) * scale + pivot_pos - node.ypos()
                print pos[1]
                print new_pos
                print bdpos
                __ scale > 0:
                    node['bdheight'].setValue(bdpos)
                ____
                    node.setXYpos(pos[0], int(new_pos-abs(bdpos)))
        ____
            new_pos = (pos[0] - pivot_pos) * scale + pivot_pos
            set_pos(node, new_pos, pos[1])
            __ node.Class() __ 'BackdropNode':
                bdpos = ((pos[0] + node['bdwidth'].getValue()) - pivot_pos) * scale + pivot_pos - node.xpos()
                __ scale > 0:
                    node['bdwidth'].setValue(bdpos)
                ____
                    node.setXYpos(int(new_pos-abs(bdpos)), int(node.ypos()))
    ?.Undo().end()



___ copy_inputs(src, dst):
    # copy input connections from src node to dst node
    # number of inputs must be the same between nodes
    ___ j in ra__(dst.inputs()):
        dst.setInput(j, None)
    ___ i in ra__(src.inputs()):
        dst.setInput(i, src.input(i))


___ declone(node):
    # Declone a single node
    __ not node.clones():
        r_
    parent = get_parent(node)
    parent.begin()
    node.setSelected(True)
    args = node.writeKnobs( ?.WRITE_ALL | ?.WRITE_USER_KNOB_DEFS |
                            ?.WRITE_NON_DEFAULT_ONLY | ?.TO_SCRIPT)
    decloned_node = ?.createNode(node.Class(), knobs=args, inpanel=False)
    copy_inputs(node, decloned_node)
    ?.delete(node)
    parent.end()
    r_ decloned_node


___ declone_nodes(nodes):
    # A better declone than the buggy default nukescripts.misc.declone()
    unselect()
    decloned_nodes = list()
    ___ node in nodes:
        decloned_nodes.append(declone(node))
    __ decloned_nodes:
        # Restore selection
        _ = [n.setSelected(True) ___ n in decloned_nodes]


___ export_selected_nodes():
    pa__ = ?.getFilename("Export Selected To:")
    __ not pa__:
        r_
    ?.nodeCopy(pa__)
    root = ?.root()
    rootstring = root.writeKnobs(?.TO_SCRIPT | ?.WRITE_USER_KNOB_DEFS)
    rootstring = "%s\nfirst_frame %d\nlast_frame %d" % (rootstring, root['first_frame'].value(), root['last_frame'].value())
    rootstring = "%s\nproxy_format \"%s\"" % (rootstring, root['proxy_format'].toScript())
    rootstring = "Root {\n%s\n}" % rootstring
    noroot = open(pa__).read()
    with open(pa__, "w+") __ f:
        f.w..((rootstring + "\n" + noroot))



#--------------------------------------------------------------
# Nuke Node Dependency Utilities
__ ?.NUKE_VERSION_MAJOR > 11:
    connection_filter = ?.INPUTS | ?.HIDDEN_INPUTS | ?.EXPRESSIONS | ?.LINKINPUTS
____
    connection_filter = ?.INPUTS | ?.HIDDEN_INPUTS | ?.EXPRESSIONS

___ find_root_nodes(node, results=# list, remove_roots_with_inputs=True):
    # Find all root nodes of node. 
    # If remove_roots_with_inputs: remove root nodes with an input (like Roto etc)
    ___ dependency in node.dependencies():
        __ not dependency.dependencies():
            results.append(dependency)
        ____
            find_root_nodes(dependency, results)
    __ remove_roots_with_inputs:
        results = [res ___ res in results __ res.maxInputs() __ 0]
    r_ results


___ upstream(node, max_depth=-1, deps=set(# list)):
    __ max_depth != 0:
       new_deps = set([n ___ n in ?.dependencies(node, what=connection_filter) __ n not in deps])
       deps |= new_deps
       ___ dep in new_deps:
          upstream(dep, max_depth-1, deps)
    r_ deps


___ connected(nodes, upstream=True, downstream=True):
    # return all upstream and/or downstream nodes of node
    # based on nuke.overrides.selectConnectedNodes()
    all_deps = set()
    deps_list = nodes
    evaluate_all = True
    w__ deps_list:
        deps = # list
        __ upstream:
            deps += ?.dependencies(deps_list, connection_filter)
        __ downstream:
            deps += ?.dependentNodes(connection_filter, deps_list, evaluate_all)
        evaluate_all = False
        deps_list = [d ___ d in deps __ d not in all_deps and not all_deps.add(d)]
    r_ all_deps

___ select_upstream(nodes):
    # Select all upstream dependencies of node
    deps = [n ___ n in connected(nodes, upstream=True, downstream=False)]
    select(deps)
    r_ deps

___ select_downstream(nodes):
    # Select all downstream dependencies of node
    deps = [n ___ n in connected(nodes, upstream=False, downstream=True)]
    select(deps)
    r_ deps

___ select_connected(nodes):
    # Select all nodes connected to node
    deps = [n ___ n in connected(nodes, upstream=True, downstream=True)]
    select(deps)
    r_ deps

___ select_unused(nodes):
    # select all nodes that are not upstream or downstream of :param: nodes
    # Backdrops and dot nodes with a label are omitted.
    connected_nodes = [n ___ n in connected(nodes, upstream=True, downstream=True)]
    unused_nodes = [n ___ n in ?.allNodes() __ n not in connected_nodes and n.Class() != 'BackdropNode' and not (n.Class() __ 'Dot' and n['label'].getValue())]
    unselect()
    select(unused_nodes)
    r_ unused_nodes






# DAG Positions
# Inspired by Simon Bjork's sb_dagPosition.py https://www.bjorkvisuals.com/tools/the-foundrys-nuke/python
# Using built-in nukescripts.bookmarks module now instead.
___ save_dag_pos(preset):
    # Save current dag zoom and position as a preset on the active viewer
    zoom = ?.zoom()
    pos = ?.center()
    viewer = ?.activeViewer()
    __ not viewer:
        ?.message('Error: please create a viewer to store the dag positions on...')
        r_
    ____
        viewer = viewer.node()
    __ 'dagpos' not in viewer.knobs():
        viewer.addKnob(?.String_Knob('dagpos', 'dagpos', '0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0'))
        dagpos_knob = viewer['dagpos']
        dagpos_knob.setFlag(?.STARTLINE)
        dagpos_knob.setEnabled(False)
    ____
        dagpos_knob = viewer['dagpos']
    dagpos_vals = dagpos_knob.getValue().split(':')
    dagpos_vals.pop(preset-1)
    new_dagpos = ','.j..([st.(zoom), st.(pos[0]), st.(pos[1])])
    dagpos_vals.insert(preset-1, new_dagpos)
    dagpos_knob.setValue(':'.j..(dagpos_vals))

___ load_dag_pos(preset):
    # Load dag zoom and position from specified preset number
    viewer = ?.activeViewer()
    __ not viewer:
        ?.message('Error: please create a viewer to store the dag positions on...')
        r_
    viewer = viewer.node()
    __ 'dagpos' not in viewer.knobs():
        ?.message('No preset positions created yet...')
        r_
    dagpos_knob = viewer['dagpos']
    dagpos_vals = dagpos_knob.getValue().split(':')[preset-1]
    zoom, xpos, ypos = dagpos_vals.split(',')
    ?.zoom(float(zoom), [float(xpos), float(ypos)])




#----------------------------------------------------------------------------------
# Hidden Input Link Nodes
# This is no longer used in favor of the anchor / pointer workflow

___ hidden_inputs_in_selection(nodes):
    r_ [n ___ n in nodes __ 'hide_input' in n.knobs() and n['hide_input'].getValue()]

___ set_hlink_knobs(nodes):
    # Add knob to track what node this node is connected to
    ___ node in hidden_inputs_in_selection(nodes):
        __ not 'hlink_node' in node.knobs():
            node.addKnob(?.String_Knob('hlink_node', 'hlink_node'))
        input_node = node.input(0)
        __ input_node:
            node['hlink_node'].setValue(input_node.fullName())
        ____
            node['hlink_node'].setValue('')

___ hlink_copy():
    nodes = ?.sN..()
    __ nodes:
        set_hlink_knobs(nodes)
        ?.nodeCopy('%clipboard%')

___ hlink_cut():
    hlink_copy()
    nukescripts.node_delete(popupOnError=True)

___ hlink_paste():
    ?.nodePaste('%clipboard%')
    ___ node in hidden_inputs_in_selection(?.sN..()):
        __ 'hlink_node' in node.knobs():
            target = ?.tN..(node['hlink_node'].getValue())
            __ target:
                node.setInput(0, target)

___ hlink_create():
    # Creates an hlink node for each selected node
    nodes = ?.sN..()
    unselect()
    hlinks = # list
    ___ node in nodes:
        hlink = ?.createNode('Dot', 'hide_input 1 note_font_size 18', inpanel=False)
        hlinks.append(hlink)
        hlink.setInput(0, node)
        target_name = node.fullName()
        set_hlink_knobs([hlink])
        hlink['hlink_node'].setValue(target_name)
        label = hlink['label']
        target_label = node['label'].getValue()
        __ node.Class() __ 'Read':
            label.setValue(' | ' + node['label'].getValue() + '\n' + os.pa__.b_n_(node['file'].getValue()))
        ____ target_label:
            label.setValue(' | ' + target_label)
        ____
            label.setValue(' | ' + target_name)
        hlink.setXYpos(node.xpos() - grid[0]*2, node.ypos()-grid[1]*0)
        ?.autoplaceSnap(hlink)
    _ = [n.setSelected(True) ___ n in hlinks]



___ dec2hex(dec):
    hexcol = '%08x' % dec
    r_ '0x%02x%02x%02x' %  (int(hexcol[0:2], 16), int(hexcol[2:4], 16), int(hexcol[4:6], 16))



___ create_pointer():
    # Create an anchor / pointer set
    nodes = ?.sN..()
    __ not nodes:
        r_

    ___ target in nodes:
        upstream = [n ___ n in connected(nodes, upstream=True, downstream=False)]

        __ le.(upstream) > 5:
            __ not ?.a..('More than 5 upstream nodes. Are you sure you want to continue?'):
                r_

        randstr = ''.j..(random.choice(string.ascii_lowercase) ___ i in ra__(4))
        
        topnode = get_topnode(target)

        target_label = target['label'].getValue()

        # If topnode has a file knob, use that to set title
        # If it's a roto node, use the roto label
        __ 'file' in topnode.knobs():
            pointer_title = os.pa__.b_n_(topnode['file'].getValue())
            __ '.' in pointer_title:
                pointer_title = pointer_title.split('.')[0]
        ____ topnode.Class() in ['Roto', 'RotoPaint'] and topnode['label'].getValue():
            pointer_title = topnode['label'].getValue()
        ____ target_label:
            pointer_title = target_label
        ____
            pointer_title = ''

        topnode_color = topnode['tile_color'].value()

        __ topnode_color __ 0:
            # Get default color from prefs if node is not colored https://community.foundry.com/discuss/topic/103301/get-the-default-tile-color-from-preferences
            prefs = ?.tN..('preferences')
            default_colors = {prefs['NodeColour{0:02d}Color'.format(i)].value(): prefs['NodeColourClass{0:02d}'.format(i)].value() ___ i in ra__(1, 14)}
            node_class = topnode.Class().lower()
            node_class = ''.j..([i ___ i in node_class __ not i.isdigit()])
            ___ color, classes in default_colors.i..():
                __ node_class in classes:
                    topnode_color = color
                    break
            __ 'deep' in node_class:
                topnode_color = prefs['NodeColourDeepColor'].value()
        
        __ le.(nodes) __ 1:
            # Only prompt the user for info if there is one selected node
            panel = ?.Panel('Create Pointer')
            panel.addSingleLineInput('title', pointer_title)
            __ panel.show():
                pointer_title = panel.value('title')
            ____
                r_

        has_downstream = le.(select_downstream(target)) > 0
        unselect()

        __ not has_downstream:
            target.setSelected(True)

        # create anchor node
        anchor = ?.createNode('NoOp', 'name ___anchor_{0} icon Output.png label "<font size=7>\[value title]"'.format(randstr))
        anchor.addKnob(?.Tab_Knob('anchor_tab', 'anchor'))
        anchor.addKnob(?.String_Knob('title', 'title'))
        anchor['title'].setValue(pointer_title)
        anchor['tile_color'].setValue(topnode_color)
        anchor.setInput(0, target)
        anchor.setSelected(True)

        # create pointer node
        pointer = ?.createNode('NoOp', 'name ___pointer_{0} hide_input true icon Input.png'.format(randstr))
        pointer.addKnob(?.Tab_Knob('pointer_tab', 'pointer'))
        pointer.addKnob(?.String_Knob('target', 'target'))
        pointer['target'].setValue(anchor.fullName())
        pointer['label'].setValue('<font size=7> [if {[exists input.title]} {return [value input.title]}]')
        pointer.addKnob(?.PyScript_Knob('connect_to_target', 'connect'))
        pointer['connect_to_target'].setFlag(?.STARTLINE)
        pointer.addKnob(?.PyScript_Knob('zoom_to_target', 'zoom'))
        pointer.addKnob(?.PyScript_Knob('set_target', 'set target'))
        pointer['connect_to_target'].setValue('''n = nuke.thisNode()
t = n['target'].getValue()
if nuke.exists(t):
    tn = nuke.toNode(t)
    n.setInput(0, tn)''')
        pointer['zoom_to_target'].setValue('''t = nuke.thisNode()['target'].getValue()
if nuke.exists(t):
    tn = nuke.toNode(t)
    nuke.zoom(2.0, [tn.xpos(), tn.ypos()])''')
        pointer['set_target'].setValue('''n = nuke.thisNode()
sn = nuke.selectedNodes()
if sn:
    t = sn[-1]
n['target'].setValue(t.fullName())''')
        # set autolabel node to execute connect python script button.
        # it's a hack but it works to automatically reconnect the input without using knobChanged callbacks!
        # FYI, onCreate callback can not connect input 0 due to a nuke bug
        pointer['autolabel'].setValue('nuke.thisNode()["connect_to_target"].execute()')
        pointer.setXYpos(anchor.xpos(), anchor.ypos()+120)
        pointer['tile_color'].setValue(topnode_color)


___ create_dots(side=False):
    # Create dot nodes
    nodes = ?.sN..()
    unselect()
    dots = list()
    ___ node in nodes:
        pos = get_pos(node)
        __ not side:
            select([node])
        dot = ?.createNode('Dot', inpanel=False)
        __ side:
            set_pos(dot, pos[0] - grid[0], pos[1])
            dot.setInput(0, node)
        ____
            set_pos(dot, pos[0], pos[1] + grid[1]*2)
        dots.append(dot)
        unselect(dot)
    select(dots)
    __ not nodes:
        dot = ?.createNode('Dot', inpanel=False)



___ create_transform():
    # Create a Transform or TransformGeo node depending on node type
    nodes = ?.sN..()
    __ not nodes:
        ?.createNode('Transform')
        r_
    unselect()
    transform_nodes = list()
    ___ node in nodes:
        node.setSelected(True)
        __ 'render_mode' in node.knobs():
            new_node = ?.createNode('TransformGeo')
            __ new_node:
                transform_nodes.append(new_node)
        ____
            new_node = ?.createNode('Transform')
            __ new_node:
                transform_nodes.append(new_node)
        unselect()
    select(transform_nodes)


___ read_from_write():
    # Create read nodes from selected write nodes
    nodes = [n ___ n in ?.sN..() __ 'file' in n.knobs()]
    excluded = ['Read', ]
    ___ node in nodes:
        __ node.Class() in excluded:
            c___
        pos = get_pos(node)
        filepath = node['file'].getValue()
        d_n_ = os.pa__.d_n_(filepath)
        filename = os.pa__.b_n_(filepath)
        __ '#' in filename:
            is_sequence = True
            filename_base = filename.split('#')[0]
        ____ r'%' in filename:
            is_sequence = True
            filename_base = filename.split(r'%')[0]
        ____
            is_sequence = False
        __ is_sequence:
            sequences = ?.getFileNameList(d_n_)
            ___ seq in sequences:
                __ seq.startswith(filename_base):
                    filepath = os.pa__.j..(d_n_, seq)
                    break
        read = ?.createNode('Read', 'file {{{0}}}'.format(filepath), inpanel=False)
        set_pos(read, pos[0], pos[1] + grid[1]*4)
        # match colorspace
        colorspace = node['colorspace'].value()
        __ '(' in colorspace and ')' in colorspace:
            # parse out role
            colorspace = colorspace.split('(')[1].split(')')[0]
        read['colorspace'].setValue(colorspace)
        read['raw'].setValue(node['raw'].getValue())




# Enhanced swap functionality.
___ swap_node():
    nodes = ?.sN..()
    ___ node in nodes:
        __ node.inputs() > 1:
            nukescripts.swapAB(node)
        __ node.Class() __ 'OCIOColorSpace':
            in_colorspace = node['in_colorspace'].value()
            out_colorspace = node['out_colorspace'].value()
            node['out_colorspace'].setValue(in_colorspace)
            node['in_colorspace'].setValue(out_colorspace)
        ____ 'direction' in node.knobs():
            direction = node['direction']
            __ direction.getValue() __ 1:
                direction.setValue(0)
            ____
                direction.setValue(1)
        ____ 'invert' in node.knobs():
            invert = node['invert']
            __ invert.getValue() __ 1:
                invert.setValue(0)
            ____
                invert.setValue(1)
        ____ node.Class() __ 'Colorspace':
            colorspace_in = node['colorspace_in'].value()
            colorspace_out = node['colorspace_out'].value()
            node['colorspace_out'].setValue(colorspace_in)
            node['colorspace_in'].setValue(colorspace_out)

___ swap_view():
    views = ?.views()
    __ le.(views) __ 2:
        ?.activeViewer().setView(views[1]) __ ?.activeViewer().view() __ views[0] else ?.activeViewer().setView(views[0])