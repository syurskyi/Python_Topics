______ ?
______ n_s_
______ operator, math, __
______ string
______ random

# Get the grid size from the preferences. Used as the default unit of movement.
grid = (in_(?.tN..('preferences').knob('GridWidth').v.. ()), in_(?.tN..('preferences').knob('GridHeight').v.. ()))


___ unselect(n__=N..):
    # Unselect nodes
    __ no. n__:
        n__ = ?.aN..(recurseGroups=T..)
    __ no. isinstance(n__, list):
        r_
    _ = [n.sS.. F.. ___ n __ n__]


___ select(n__):
    # Select specified nodes
    __ no. isinstance(n__, list):
        r_
    _ = [n.sS.. T.. ___ n __ n__]


___ get_parent(node):
    # return node's parent node, return nuke.root() if on the top level
    r_ ?.tN..('.'.j..(node.fullName().s..('.')[:-1])) or ?.r..


___ get_topnode(node):

    # return the topnode of node
    r_ ?.tN..(?.tcl('return [value [topnode {0}].name]'.f..(node.fullName())))


___ get_pos(node):
    # return 2d list of centered node positions
    __ node.C..  __ 'BackdropNode':
        r_ [node.xpos(), node.yp__()]
    ____
        r_ [node.xpos() + node.screenWidth()/2, node.yp__() + node.screenHeight()/2]


___ set_pos(node, posx, posy):
    # Set node's position given a centered position based on screen width
    # param: pos - 2dim list of int node positions
    __ node.C..  __ 'BackdropNode':
        r_ node.setXYpos(in_(posx), in_(posy))
    ____
        r_ node.setXYpos(in_(posx - node.screenWidth()/2), in_(posy - node.screenHeight()/2))


___ hide_panel
    # Always hide control panels on node creation
    ?.tN..().showControlPanel()
    ?.tN..().hideControlPanel()
?.aOUC..(hide_panel)


___ open_panels(n__=N..):
    # Open properties panels
    __ no. n__:
        n__ = ?.sN..()
    ignored = ['Viewer']
    __ le.(n__) > 10:
        __ no. ?.a..('Continuing will open {0} properties panels. \nAre you sure you want to continue?'.f..(le.(n__))):
            r_
    ___ node __ n__:
        __ node.C..  no. __ ignored:
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


___ close_panels(n__=N..):
    # Close all properties panels
    __ no. n__:
        n__ = ?.aN..(recurseGroups=T..)
    ___ node __ n__:
        node.hideControlPanel()


___ select_similar_position(axis=1):
    n__ = ?.sN..()
    __ no. n__:
        r_
    node = n__[0]
    prev_selected = n__[1:]
    threshold = 1
    unselect()
    select(prev_selected)
    __ axis:
        same_pos_nodes = {n:n.xpos() ___ n __ ?.aN..() __ abs(n.yp__()- node.yp__()) < threshold}
    ____
        same_pos_nodes = {n:n.yp__() ___ n __ ?.aN..() __ abs(n.xpos()- node.xpos()) < threshold}
    sorted_nodes = sorted(same_pos_nodes.i..(), key=operator.itemgetter(1))
    ___ n, pos __ sorted_nodes:
        n.sS.. T..


___ snap_to_grid
    # Snap selected nodes to grid
    n__ = ?.sN..()
    ___ node __ n__:
        ?.autoplaceSnap(node)


___ auto_place
    # autoplace all selected
    n__ = ?.sN..()

    # Sort by file knob value if the nodes have one
    filenodes = {n: n['file'].gV..  ___ n __ n__ __ 'file' __ n.knobs()}
    __ filenodes:
        sorted_filenodes = sorted(filenodes.i..(), key=operator.itemgetter(1))
        filenodes_pos = {n: [n.xpos(), n.yp__()] ___ n __ n__ __ 'file' __ n.knobs()}
        ypos_sort = sorted(filenodes_pos.i..(), key=l___ (k, v): v[1])
        xpos_sort = sorted(filenodes_pos.i..(), key=l___ (k, v): v[0])
        start_pos = [xpos_sort[0][1][0], ypos_sort[0][1][1]]
        ___ node, filepath __ sorted_filenodes:
            node.setXYpos(start_pos[0], start_pos[1])
            start_pos = (start_pos[0] + grid[0]*2, start_pos[1])

    # Normal autoplace for nodes without file knob
    normal_nodes = [n ___ n __ n__ __ 'file' no. __ n.knobs()]
    unselect()
    _ = [n.sS.. T.. ___ n __ normal_nodes]
    ?.autoplace_all()
    _ = [n.sS.. T.. ___ n __ n__]


___ move(xvel, yvel):
    # Move selected nodes by specified number of grid lengths in x and y
    yvel *= 3
    n__ = ?.sN..()
    ___ node __ n__:
        node.setXYpos(in_(node.xpos() + grid[0] * xvel), in_(node.yp__() + grid[1] * yvel))


___ get_closest_node(node):
    # Return the closest node to node
    distances = {}
    ___ n __ ?.aN..
        __ n.n..  __ node.n.. :
            c___
        distance = math.sqrt( 
            math.pow( (node.xpos() - n.xpos()), 2 ) + math.pow( (node.yp__() - n.yp__()), 2 )
        )
        distances[n.n.. ] = distance
    r_ ?.tN..(min(distances, key=distances.get))


___ connect_to_closest(direction=0):
    # Connect next available input of all selected nodes to the closest node
    ___ node __ ?.sN..
        closest = get_closest_node(node)
        __ direction:
            closest.setInput(0, node)
        ____
            node.cI..(0, closest)


___ paste_to_selected
    n__ = ?.sN..()
    all_nodes = ?.aN..()
    unselect()
    ___ node __ n__:
        node.sS.. T..
        ?.nodePaste('%clipboard')
        unselect()
    __ no. n__:
        ?.nodePaste('%clipboard')
    # Select pasted nodes
    select(all_nodes)
    ?.invertSelection()
    

___ align(direction):
    # Align nodes to the farthest outlier in the specified direction.
    # param: direction - one of: left | right | up | down

    n__ = ?.sN..()

    __ le.(n__) < 2:
        r_

    horizontally = ['left', 'right']
    vertically = ['up', 'down']

    __ direction __ horizontally:
        align = 0
    ____ direction __ vertically:
        align = 1
    ____
        print 'Error: invalid direction specified: {0}'.f..(direction)
        r_

    positions = {n: get_pos(n) ___ n __ n__}
    sorted_positions = sorted(positions.i..(), key=l___ (k, v): v[align])
    __ direction __ ['down', 'right']:
        sorted_positions.reverse()
    target = sorted_positions[0]
    target_pos = target[1]

    offset = 0

    other_axis = abs(1 - align)

    sorted_other_axis = sorted(positions.i..(), key=l___ (k, v): v[other_axis])

    ?.Undo().begin()
    ___ i __ ra__(le.(sorted_other_axis)):
        node = sorted_other_axis[i][0]
        pos = sorted_other_axis[i][1]
        __ i __ 0: 
            distance = 0
            overlapping = F..
            prev_pos = pos
        ____
            prev_pos = sorted_other_axis[i-1][1]
            # Compare current node position to previous node position.
            # If difference is < overlap threshold, nodes are overlapping.
            distance = abs(pos[other_axis] + grid[other_axis] * offset - prev_pos[other_axis])
            overlap_threshold = [in_(node.screenWidth() * 1.1), in_(node.screenHeight() * 1.1)]
            overlapping = distance < overlap_threshold[other_axis]

        __ overlapping:
            offset += 1

        new_pos = pos
        new_pos[other_axis] = in_(pos[other_axis] + grid[other_axis] * offset)

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
    __ pivot no. __ pivots:
        r_
    n__ = ?.sN..()
    __ le.(n__) < 2:
        r_

    positions = {n: get_pos(n) ___ n __ n__}
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
    ___ node, pos __ positions.iteritems
        __ axis:
            new_pos = (pos[1] - pivot_pos) * scale + pivot_pos
            set_pos(node, pos[0], new_pos)
            __ node.C..  __ 'BackdropNode':
                bdpos = ((pos[1] + node['bdheight'].gV..()) - pivot_pos) * scale + pivot_pos - node.yp__()
                print pos[1]
                print new_pos
                print bdpos
                __ scale > 0:
                    node['bdheight'].sV..(bdpos)
                ____
                    node.setXYpos(pos[0], in_(new_pos-abs(bdpos)))
        ____
            new_pos = (pos[0] - pivot_pos) * scale + pivot_pos
            set_pos(node, new_pos, pos[1])
            __ node.C..  __ 'BackdropNode':
                bdpos = ((pos[0] + node['bdwidth'].gV..()) - pivot_pos) * scale + pivot_pos - node.xpos()
                __ scale > 0:
                    node['bdwidth'].sV..(bdpos)
                ____
                    node.setXYpos(in_(new_pos-abs(bdpos)), in_(node.yp__()))
    ?.Undo().end()



___ copy_inputs(src, dst):
    # copy input connections from src node to dst node
    # number of inputs must be the same between nodes
    ___ j __ ra__(dst.inputs()):
        dst.setInput(j, N..)
    ___ i __ ra__(src.inputs()):
        dst.setInput(i, src.input(i))


___ declone(node):
    # Declone a single node
    __ no. node.clones
        r_
    parent = get_parent(node)
    parent.begin()
    node.sS.. T..
    args = node.writeKnobs( ?.WRITE_ALL | ?.WRITE_USER_KNOB_DEFS |
                            ?.WRITE_NON_DEFAULT_ONLY | ?.TO_SCRIPT)
    decloned_node = ?.cN..(node.C.. , knobs=args, __.._F..)
    copy_inputs(node, decloned_node)
    ?.delete(node)
    parent.end()
    r_ decloned_node


___ declone_nodes(n__):
    # A better declone than the buggy default nukescripts.misc.declone()
    unselect()
    decloned_nodes = list()
    ___ node __ n__:
        decloned_nodes.ap..(declone(node))
    __ decloned_nodes:
        # Restore selection
        _ = [n.sS.. T.. ___ n __ decloned_nodes]


___ export_selected_nodes
    pa__ = ?.getFilename("Export Selected To:")
    __ no. pa__:
        r_
    ?.nodeCopy(pa__)
    root = ?.r..
    rootstring = root.writeKnobs(?.TO_SCRIPT | ?.WRITE_USER_KNOB_DEFS)
    rootstring = "%s\nfirst_frame %d\nlast_frame %d" % (rootstring, root['first_frame'].v.. (), root['last_frame'].v.. ())
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
    ___ dependency __ node.dependencies
        __ no. dependency.dependencies
            results.ap..(dependency)
        ____
            find_root_nodes(dependency, results)
    __ remove_roots_with_inputs:
        results = [res ___ res __ results __ res.maxInputs() __ 0]
    r_ results


___ upstream(node, max_depth=-1, deps=set(# list)):
    __ max_depth != 0:
       new_deps = set([n ___ n __ ?.dependencies(node, what=connection_filter) __ n no. __ deps])
       deps |= new_deps
       ___ dep __ new_deps:
          upstream(dep, max_depth-1, deps)
    r_ deps


___ connected(n__, upstream=T.., downstream=T..):
    # return all upstream and/or downstream nodes of node
    # based on nuke.overrides.selectConnectedNodes()
    all_deps = set()
    deps_list = n__
    evaluate_all = T..
    w__ deps_list:
        deps = # list
        __ upstream:
            deps += ?.dependencies(deps_list, connection_filter)
        __ downstream:
            deps += ?.dependentNodes(connection_filter, deps_list, evaluate_all)
        evaluate_all = F..
        deps_list = [d ___ d __ deps __ d no. __ all_deps and no. all_deps.add(d)]
    r_ all_deps

___ select_upstream(n__):
    # Select all upstream dependencies of node
    deps = [n ___ n __ connected(n__, upstream=T.., downstream=F..)]
    select(deps)
    r_ deps

___ select_downstream(n__):
    # Select all downstream dependencies of node
    deps = [n ___ n __ connected(n__, upstream=F.., downstream=T..)]
    select(deps)
    r_ deps

___ select_connected(n__):
    # Select all nodes connected to node
    deps = [n ___ n __ connected(n__, upstream=T.., downstream=T..)]
    select(deps)
    r_ deps

___ select_unused(n__):
    # select all nodes that are not upstream or downstream of :param: nodes
    # Backdrops and dot nodes with a label are omitted.
    connected_nodes = [n ___ n __ connected(n__, upstream=T.., downstream=T..)]
    unused_nodes = [n ___ n __ ?.aN..() __ n no. __ connected_nodes and n.C..  != 'BackdropNode' and no. (n.C..  __ 'Dot' and n['label'].gV..())]
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
    __ no. viewer:
        ?.m__('Error: please create a viewer to store the dag positions on...')
        r_
    ____
        viewer = viewer.node()
    __ 'dagpos' no. __ viewer.knobs
        viewer.aK..(?.String_Knob('dagpos', 'dagpos', '0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0'))
        dagpos_knob = viewer['dagpos']
        dagpos_knob.setFlag(?.STARTLINE)
        dagpos_knob.setEnabled F..
    ____
        dagpos_knob = viewer['dagpos']
    dagpos_vals = dagpos_knob.gV.. .s..(':')
    dagpos_vals.pop(preset-1)
    new_dagpos = ','.j..([st.(zoom), st.(pos[0]), st.(pos[1])])
    dagpos_vals.insert(preset-1, new_dagpos)
    dagpos_knob.sV..(':'.j..(dagpos_vals))

___ load_dag_pos(preset):
    # Load dag zoom and position from specified preset number
    viewer = ?.activeViewer()
    __ no. viewer:
        ?.m__('Error: please create a viewer to store the dag positions on...')
        r_
    viewer = viewer.node()
    __ 'dagpos' no. __ viewer.knobs
        ?.m__('No preset positions created yet...')
        r_
    dagpos_knob = viewer['dagpos']
    dagpos_vals = dagpos_knob.gV.. .s..(':')[preset-1]
    zoom, xpos, yp__ = dagpos_vals.s..(',')
    ?.zoom(fl..(zoom), [fl..(xpos), fl..(yp__)])




#----------------------------------------------------------------------------------
# Hidden Input Link Nodes
# This is no longer used in favor of the anchor / pointer workflow

___ hidden_inputs_in_selection(n__):
    r_ [n ___ n __ n__ __ 'hide_input' __ n.knobs() and n['hide_input'].gV.. ]

___ set_hlink_knobs(n__):
    # Add knob to track what node this node is connected to
    ___ node __ hidden_inputs_in_selection(n__):
        __ no. 'hlink_node' __ node.knobs
            node.aK..(?.String_Knob('hlink_node', 'hlink_node'))
        input_node = node.input(0)
        __ input_node:
            node['hlink_node'].sV..(input_node.fullName())
        ____
            node['hlink_node'].sV..('')

___ hlink_copy
    n__ = ?.sN..()
    __ n__:
        set_hlink_knobs(n__)
        ?.nodeCopy('%clipboard%')

___ hlink_cut
    hlink_copy()
    n_s_.node_delete(popupOnError=T..)

___ hlink_paste
    ?.nodePaste('%clipboard%')
    ___ node __ hidden_inputs_in_selection(?.sN..()):
        __ 'hlink_node' __ node.knobs
            target = ?.tN..(node['hlink_node'].gV..())
            __ target:
                node.setInput(0, target)

___ hlink_create
    # Creates an hlink node for each selected node
    n__ = ?.sN..()
    unselect()
    hlinks = # list
    ___ node __ n__:
        hlink = ?.cN..('Dot', 'hide_input 1 note_font_size 18', __.._F..)
        hlinks.ap..(hlink)
        hlink.setInput(0, node)
        target_name = node.fullName()
        set_hlink_knobs([hlink])
        hlink['hlink_node'].sV..(target_name)
        label = hlink['label']
        target_label = node['label'].gV..
        __ node.C..  __ 'Read':
            label.sV..(' | ' + node['label'].gV..  + '\n' + __.pa__.b_n_(node['file'].gV..()))
        ____ target_label:
            label.sV..(' | ' + target_label)
        ____
            label.sV..(' | ' + target_name)
        hlink.setXYpos(node.xpos() - grid[0]*2, node.yp__()-grid[1]*0)
        ?.autoplaceSnap(hlink)
    _ = [n.sS.. T.. ___ n __ hlinks]



___ dec2hex(dec):
    hexcol = '%08x' % dec
    r_ '0x%02x%02x%02x' %  (in_(hexcol[0:2], 16), in_(hexcol[2:4], 16), in_(hexcol[4:6], 16))



___ create_pointer
    # Create an anchor / pointer set
    n__ = ?.sN..()
    __ no. n__:
        r_

    ___ target __ n__:
        upstream = [n ___ n __ connected(n__, upstream=T.., downstream=F..)]

        __ le.(upstream) > 5:
            __ no. ?.a..('More than 5 upstream nodes. Are you sure you want to continue?'):
                r_

        randstr = ''.j..(random.choice(string.ascii_lowercase) ___ i __ ra__(4))
        
        topnode = get_topnode(target)

        target_label = target['label'].gV..

        # If topnode has a file knob, use that to set title
        # If it's a roto node, use the roto label
        __ 'file' __ topnode.knobs
            pointer_title = __.pa__.b_n_(topnode['file'].gV..())
            __ '.' __ pointer_title:
                pointer_title = pointer_title.s..('.')[0]
        ____ topnode.C..  __ ['Roto', 'RotoPaint'] and topnode['label'].gV.. :
            pointer_title = topnode['label'].gV..
        ____ target_label:
            pointer_title = target_label
        ____
            pointer_title = ''

        topnode_color = topnode['tile_color'].v.. ()

        __ topnode_color __ 0:
            # Get default color from prefs if node is not colored https://community.foundry.com/discuss/topic/103301/get-the-default-tile-color-from-preferences
            prefs = ?.tN..('preferences')
            default_colors = {prefs['NodeColour{0:02d}Color'.f..(i)].v..  prefs['NodeColourClass{0:02d}'.f..(i)].v.. () ___ i __ ra__(1, 14)}
            node_class = topnode.C.. .lower()
            node_class = ''.j..([i ___ i __ node_class __ no. i.isdigit()])
            ___ color, classes __ default_colors.i..
                __ node_class __ classes:
                    topnode_color = color
                    break
            __ 'deep' __ node_class:
                topnode_color = prefs['NodeColourDeepColor'].v.. ()
        
        __ le.(n__) __ 1:
            # Only prompt the user for info if there is one selected node
            panel = ?.Panel('Create Pointer')
            panel.addSingleLineInput('title', pointer_title)
            __ panel.show
                pointer_title = panel.v.. ('title')
            ____
                r_

        has_downstream = le.(select_downstream(target)) > 0
        unselect()

        __ no. has_downstream:
            target.sS.. T..

        # create anchor node
        anchor = ?.cN..('NoOp', 'name ___anchor_{0} icon Output.png label "<font size=7>\[value title]"'.f..(randstr))
        anchor.aK..(?.T_K_('anchor_tab', 'anchor'))
        anchor.aK..(?.String_Knob('title', 'title'))
        anchor['title'].sV..(pointer_title)
        anchor['tile_color'].sV..(topnode_color)
        anchor.setInput(0, target)
        anchor.sS.. T..

        # create pointer node
        pointer = ?.cN..('NoOp', 'name ___pointer_{0} hide_input true icon Input.png'.f..(randstr))
        pointer.aK..(?.T_K_('pointer_tab', 'pointer'))
        pointer.aK..(?.String_Knob('target', 'target'))
        pointer['target'].sV..(anchor.fullName())
        pointer['label'].sV..('<font size=7> [if {[exists input.title]} {return [value input.title]}]')
        pointer.aK..(?.PS_K..('connect_to_target', 'connect'))
        pointer['connect_to_target'].setFlag(?.STARTLINE)
        pointer.aK..(?.PS_K..('zoom_to_target', 'zoom'))
        pointer.aK..(?.PS_K..('set_target', 'set target'))
        pointer['connect_to_target'].sV..('''n = nuke.thisNode()
t = n['target'].getValue()
if nuke.exists(t):
    tn = nuke.toNode(t)
    n.setInput(0, tn)''')
        pointer['zoom_to_target'].sV..('''t = nuke.thisNode()['target'].getValue()
if nuke.exists(t):
    tn = nuke.toNode(t)
    nuke.zoom(2.0, [tn.xpos(), tn.ypos()])''')
        pointer['set_target'].sV..('''n = nuke.thisNode()
sn = nuke.selectedNodes()
if sn:
    t = sn[-1]
n['target'].setValue(t.fullName())''')
        # set autolabel node to execute connect python script button.
        # it's a hack but it works to automatically reconnect the input without using knobChanged callbacks!
        # FYI, onCreate callback can not connect input 0 due to a nuke bug
        pointer['autolabel'].sV..('nuke.thisNode()["connect_to_target"].execute()')
        pointer.setXYpos(anchor.xpos(), anchor.yp__()+120)
        pointer['tile_color'].sV..(topnode_color)


___ create_dots(side=F..):
    # Create dot nodes
    n__ = ?.sN..()
    unselect()
    dots = list()
    ___ node __ n__:
        pos = get_pos(node)
        __ no. side:
            select([node])
        dot = ?.cN..('Dot', __.._F..)
        __ side:
            set_pos(dot, pos[0] - grid[0], pos[1])
            dot.setInput(0, node)
        ____
            set_pos(dot, pos[0], pos[1] + grid[1]*2)
        dots.ap..(dot)
        unselect(dot)
    select(dots)
    __ no. n__:
        dot = ?.cN..('Dot', __.._F..)



___ create_transform
    # Create a Transform or TransformGeo node depending on node type
    n__ = ?.sN..()
    __ no. n__:
        ?.cN..('Transform')
        r_
    unselect()
    transform_nodes = list()
    ___ node __ n__:
        node.sS.. T..
        __ 'render_mode' __ node.knobs
            new_node = ?.cN..('TransformGeo')
            __ new_node:
                transform_nodes.ap..(new_node)
        ____
            new_node = ?.cN..('Transform')
            __ new_node:
                transform_nodes.ap..(new_node)
        unselect()
    select(transform_nodes)


___ read_from_write
    # Create read nodes from selected write nodes
    n__ = [n ___ n __ ?.sN..() __ 'file' __ n.knobs()]
    excluded = ['Read', ]
    ___ node __ n__:
        __ node.C..  __ excluded:
            c___
        pos = get_pos(node)
        filepath = node['file'].gV..
        d_n_ = __.pa__.d_n_(filepath)
        filename = __.pa__.b_n_(filepath)
        __ '#' __ filename:
            is_sequence = T..
            filename_base = filename.s..('#')[0]
        ____ r'%' __ filename:
            is_sequence = T..
            filename_base = filename.s..(r'%')[0]
        ____
            is_sequence = F..
        __ is_sequence:
            sequences = ?.getFileNameList(d_n_)
            ___ seq __ sequences:
                __ seq.startswith(filename_base):
                    filepath = __.pa__.j..(d_n_, seq)
                    break
        read = ?.cN..('Read', 'file {{{0}}}'.f..(filepath), __.._F..)
        set_pos(read, pos[0], pos[1] + grid[1]*4)
        # match colorspace
        colorspace = node['colorspace'].v.. ()
        __ '(' __ colorspace and ')' __ colorspace:
            # parse out role
            colorspace = colorspace.s..('(')[1].s..(')')[0]
        read['colorspace'].sV..(colorspace)
        read['raw'].sV..(node['raw'].gV..())




# Enhanced swap functionality.
___ swap_node
    n__ = ?.sN..()
    ___ node __ n__:
        __ node.inputs() > 1:
            n_s_.swapAB(node)
        __ node.C..  __ 'OCIOColorSpace':
            in_colorspace = node['in_colorspace'].v.. ()
            out_colorspace = node['out_colorspace'].v.. ()
            node['out_colorspace'].sV..(in_colorspace)
            node['in_colorspace'].sV..(out_colorspace)
        ____ 'direction' __ node.knobs
            direction = node['direction']
            __ direction.gV..  __ 1:
                direction.sV..(0)
            ____
                direction.sV..(1)
        ____ 'invert' __ node.knobs
            invert = node['invert']
            __ invert.gV..  __ 1:
                invert.sV..(0)
            ____
                invert.sV..(1)
        ____ node.C..  __ 'Colorspace':
            colorspace_in = node['colorspace_in'].v.. ()
            colorspace_out = node['colorspace_out'].v.. ()
            node['colorspace_out'].sV..(colorspace_in)
            node['colorspace_in'].sV..(colorspace_out)

___ swap_view
    views = ?.views()
    __ le.(views) __ 2:
        ?.activeViewer().setView(views[1]) __ ?.activeViewer().view() __ views[0] else ?.activeViewer().setView(views[0])