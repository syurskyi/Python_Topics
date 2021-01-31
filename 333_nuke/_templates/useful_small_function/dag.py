______ ?
______ n_s_
______ operator, math, __
______ string
______ random

# Get the grid size from the preferences. Used as the default unit of movement.
grid _ (in_(?.tN..('preferences').knob('GridWidth').v.. ()), in_(?.tN..('preferences').knob('GridHeight').v.. ()))


___ unselect(n___N..):
    # Unselect nodes
    __ no. n__:
        n__ _ ?.aN..(recurseGroups_T..)
    __ no. isinstance(n__, list):
        r_
    _ _ [n.sS.. F.. ___ n __ n__]


___ select(n__):
    # Select specified nodes
    __ no. isinstance(n__, list):
        r_
    _ _ [n.sS.. T.. ___ n __ n__]


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


___ open_panels(n___N..):
    # Open properties panels
    __ no. n__:
        n__ _ ?.sN..()
    ignored _ ['Viewer']
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


___ close_panels(n___N..):
    # Close all properties panels
    __ no. n__:
        n__ _ ?.aN..(recurseGroups_T..)
    ___ node __ n__:
        node.hideControlPanel()


___ select_similar_position(axis_1):
    n__ _ ?.sN..()
    __ no. n__:
        r_
    node _ n__[0]
    prev_selected _ n__[1:]
    threshold _ 1
    unselect()
    select(prev_selected)
    __ axis:
        same_pos_nodes _ {n:n.xpos() ___ n __ ?.aN..() __ abs(n.yp__()- node.yp__()) < threshold}
    ____
        same_pos_nodes _ {n:n.yp__() ___ n __ ?.aN..() __ abs(n.xpos()- node.xpos()) < threshold}
    sorted_nodes _ sorted(same_pos_nodes.i..(), key_operator.itemgetter(1))
    ___ n, pos __ sorted_nodes:
        n.sS.. T..


___ snap_to_grid
    # Snap selected nodes to grid
    n__ _ ?.sN..()
    ___ node __ n__:
        ?.autoplaceSnap(node)


___ auto_place
    # autoplace all selected
    n__ _ ?.sN..()

    # Sort by file knob value if the nodes have one
    filenodes _ {n: n['file'].gV..  ___ n __ n__ __ 'file' __ n.knobs()}
    __ filenodes:
        sorted_filenodes _ sorted(filenodes.i..(), key_operator.itemgetter(1))
        filenodes_pos _ {n: [n.xpos(), n.yp__()] ___ n __ n__ __ 'file' __ n.knobs()}
        ypos_sort _ sorted(filenodes_pos.i..(), key_l___ (k, v): v[1])
        xpos_sort _ sorted(filenodes_pos.i..(), key_l___ (k, v): v[0])
        start_pos _ [xpos_sort[0][1][0], ypos_sort[0][1][1]]
        ___ node, filepath __ sorted_filenodes:
            node.setXYpos(start_pos[0], start_pos[1])
            start_pos _ (start_pos[0] + grid[0]*2, start_pos[1])

    # Normal autoplace for nodes without file knob
    normal_nodes _ [n ___ n __ n__ __ 'file' no. __ n.knobs()]
    unselect()
    _ _ [n.sS.. T.. ___ n __ normal_nodes]
    ?.autoplace_all()
    _ _ [n.sS.. T.. ___ n __ n__]


___ move(xvel, yvel):
    # Move selected nodes by specified number of grid lengths in x and y
    yvel *_ 3
    n__ _ ?.sN..()
    ___ node __ n__:
        node.setXYpos(in_(node.xpos() + grid[0] * xvel), in_(node.yp__() + grid[1] * yvel))


___ get_closest_node(node):
    # Return the closest node to node
    distances _ {}
    ___ n __ ?.aN..
        __ n.n..  __ node.n.. :
            c___
        distance _ math.sqrt(
            math.pow( (node.xpos() - n.xpos()), 2 ) + math.pow( (node.yp__() - n.yp__()), 2 )
        )
        distances[n.n.. ] _ distance
    r_ ?.tN..(min(distances, key_distances.get))


___ connect_to_closest(direction_0):
    # Connect next available input of all selected nodes to the closest node
    ___ node __ ?.sN..
        closest _ get_closest_node(node)
        __ direction:
            closest.setInput(0, node)
        ____
            node.cI..(0, closest)


___ paste_to_selected
    n__ _ ?.sN..()
    all_nodes _ ?.aN..()
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

    n__ _ ?.sN..()

    __ le.(n__) < 2:
        r_

    horizontally _ ['left', 'right']
    vertically _ ['up', 'down']

    __ direction __ horizontally:
        align _ 0
    ____ direction __ vertically:
        align _ 1
    ____
        print 'Error: invalid direction specified: {0}'.f..(direction)
        r_

    positions _ {n: get_pos(n) ___ n __ n__}
    sorted_positions _ sorted(positions.i..(), key_l___ (k, v): v[align])
    __ direction __ ['down', 'right']:
        sorted_positions.reverse()
    target _ sorted_positions[0]
    target_pos _ target[1]

    offset _ 0

    other_axis _ abs(1 - align)

    sorted_other_axis _ sorted(positions.i..(), key_l___ (k, v): v[other_axis])

    ?.Undo().begin()
    ___ i __ ra__(le.(sorted_other_axis)):
        node _ sorted_other_axis[i][0]
        pos _ sorted_other_axis[i][1]
        __ i __ 0: 
            distance _ 0
            overlapping _ F..
            prev_pos _ pos
        ____
            prev_pos _ sorted_other_axis[i-1][1]
            # Compare current node position to previous node position.
            # If difference is < overlap threshold, nodes are overlapping.
            distance _ abs(pos[other_axis] + grid[other_axis] * offset - prev_pos[other_axis])
            overlap_threshold _ [in_(node.screenWidth() * 1.1), in_(node.screenHeight() * 1.1)]
            overlapping _ distance < overlap_threshold[other_axis]

        __ overlapping:
            offset +_ 1

        new_pos _ pos
        new_pos[other_axis] _ in_(pos[other_axis] + grid[other_axis] * offset)

        # Set value into sorted_other_axis also so we access the right value on the next loop
        sorted_other_axis[i][1][other_axis] _ new_pos[other_axis]
        
        __ align:
            set_pos(node, new_pos[other_axis], target_pos[align])
        ____
            set_pos(node, target_pos[align], new_pos[other_axis])
        i +_ 1
    ?.Undo().end()


___ scale(axis, scale, pivot_'max'):
    # Scale selected nodes by factor of xscale, yscale
    # param: axis - one of 0 or 1 - x or y scale
    # param: float scale - factor to scale. 1 will do nothing. 2 will scale up 1 grid unit.
    # param: str pivot - where to scale from. One of min | max | center
    pivots _ ['min', 'max', 'center']
    __ pivot no. __ pivots:
        r_
    n__ _ ?.sN..()
    __ le.(n__) < 2:
        r_

    positions _ {n: get_pos(n) ___ n __ n__}
    sort _ sorted(positions.i..(), key_l___ (k, v): v[axis])

    minpos _ sort[0][1][axis]
    maxpos _ sort[-1][1][axis]

    __ pivot __ 'max':
        pivot_pos _ maxpos
    ____ pivot __ 'min':
        pivot_pos _ minpos
    ____ pivot __ 'center':
        pivot_pos _ (minpos - maxpos)/2 + minpos

    ?.Undo().begin()
    ___ node, pos __ positions.iteritems
        __ axis:
            new_pos _ (pos[1] - pivot_pos) * scale + pivot_pos
            set_pos(node, pos[0], new_pos)
            __ node.C..  __ 'BackdropNode':
                bdpos _ ((pos[1] + node['bdheight'].gV..()) - pivot_pos) * scale + pivot_pos - node.yp__()
                print pos[1]
                print new_pos
                print bdpos
                __ scale > 0:
                    node['bdheight'].sV..(bdpos)
                ____
                    node.setXYpos(pos[0], in_(new_pos-abs(bdpos)))
        ____
            new_pos _ (pos[0] - pivot_pos) * scale + pivot_pos
            set_pos(node, new_pos, pos[1])
            __ node.C..  __ 'BackdropNode':
                bdpos _ ((pos[0] + node['bdwidth'].gV..()) - pivot_pos) * scale + pivot_pos - node.xpos()
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
    parent _ get_parent(node)
    parent.begin()
    node.sS.. T..
    args _ node.writeKnobs( ?.WRITE_ALL | ?.WRITE_USER_KNOB_DEFS |
                            ?.WRITE_NON_DEFAULT_ONLY | ?.TO_SCRIPT)
    decloned_node _ ?.cN..(node.C.. , knobs_args, __.._F..)
    copy_inputs(node, decloned_node)
    ?.delete(node)
    parent.end()
    r_ decloned_node


___ declone_nodes(n__):
    # A better declone than the buggy default nukescripts.misc.declone()
    unselect()
    decloned_nodes _ list()
    ___ node __ n__:
        decloned_nodes.ap..(declone(node))
    __ decloned_nodes:
        # Restore selection
        _ _ [n.sS.. T.. ___ n __ decloned_nodes]


___ export_selected_nodes
    pa__ _ ?.getFilename("Export Selected To:")
    __ no. pa__:
        r_
    ?.nodeCopy(pa__)
    root _ ?.r..
    rootstring _ root.writeKnobs(?.TO_SCRIPT | ?.WRITE_USER_KNOB_DEFS)
    rootstring _ "%s\nfirst_frame %d\nlast_frame %d" % (rootstring, root['first_frame'].v.. (), root['last_frame'].v.. ())
    rootstring _ "%s\nproxy_format \"%s\"" % (rootstring, root['proxy_format'].toScript())
    rootstring _ "Root {\n%s\n}" % rootstring
    noroot _ open(pa__).read()
    with open(pa__, "w+") __ f:
        f.w..((rootstring + "\n" + noroot))



#--------------------------------------------------------------
# Nuke Node Dependency Utilities
__ ?.NUKE_VERSION_MAJOR > 11:
    connection_filter _ ?.INPUTS | ?.HIDDEN_INPUTS | ?.EXPRESSIONS | ?.LINKINPUTS
____
    connection_filter _ ?.INPUTS | ?.HIDDEN_INPUTS | ?.EXPRESSIONS

___ find_root_nodes(node, results_# list, remove_roots_with_inputs=True):
    # Find all root nodes of node. 
    # If remove_roots_with_inputs: remove root nodes with an input (like Roto etc)
    ___ dependency __ node.dependencies
        __ no. dependency.dependencies
            results.ap..(dependency)
        ____
            find_root_nodes(dependency, results)
    __ remove_roots_with_inputs:
        results _ [res ___ res __ results __ res.maxInputs() __ 0]
    r_ results


___ upstream(node, max_depth_-1, deps_set(# list)):
    __ max_depth !_ 0:
       new_deps _ set([n ___ n __ ?.dependencies(node, what_connection_filter) __ n no. __ deps])
       deps |_ new_deps
       ___ dep __ new_deps:
          upstream(dep, max_depth-1, deps)
    r_ deps


___ connected(n__, upstream_T.., downstream_T..):
    # return all upstream and/or downstream nodes of node
    # based on nuke.overrides.selectConnectedNodes()
    all_deps _ set()
    deps_list _ n__
    evaluate_all _ T..
    w__ deps_list:
        deps _ # list
        __ upstream:
            deps +_ ?.dependencies(deps_list, connection_filter)
        __ downstream:
            deps +_ ?.dependentNodes(connection_filter, deps_list, evaluate_all)
        evaluate_all _ F..
        deps_list _ [d ___ d __ deps __ d no. __ all_deps and no. all_deps.add(d)]
    r_ all_deps

___ select_upstream(n__):
    # Select all upstream dependencies of node
    deps _ [n ___ n __ connected(n__, upstream_T.., downstream_F..)]
    select(deps)
    r_ deps

___ select_downstream(n__):
    # Select all downstream dependencies of node
    deps _ [n ___ n __ connected(n__, upstream_F.., downstream_T..)]
    select(deps)
    r_ deps

___ select_connected(n__):
    # Select all nodes connected to node
    deps _ [n ___ n __ connected(n__, upstream_T.., downstream_T..)]
    select(deps)
    r_ deps

___ select_unused(n__):
    # select all nodes that are not upstream or downstream of :param: nodes
    # Backdrops and dot nodes with a label are omitted.
    connected_nodes _ [n ___ n __ connected(n__, upstream_T.., downstream_T..)]
    unused_nodes _ [n ___ n __ ?.aN..() __ n no. __ connected_nodes and n.C..  !_ 'BackdropNode' and no. (n.C..  __ 'Dot' and n['label'].gV..())]
    unselect()
    select(unused_nodes)
    r_ unused_nodes






# DAG Positions
# Inspired by Simon Bjork's sb_dagPosition.py https://www.bjorkvisuals.com/tools/the-foundrys-nuke/python
# Using built-in nukescripts.bookmarks module now instead.
___ save_dag_pos(preset):
    # Save current dag zoom and position as a preset on the active viewer
    zoom _ ?.zoom()
    pos _ ?.center()
    viewer _ ?.aV..
    __ no. viewer:
        ?.m__('Error: please create a viewer to store the dag positions on...')
        r_
    ____
        viewer _ viewer.node()
    __ 'dagpos' no. __ viewer.knobs
        viewer.aK..(?.String_Knob('dagpos', 'dagpos', '0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0:0,0,0'))
        dagpos_knob _ viewer['dagpos']
        dagpos_knob.setFlag(?.STARTLINE)
        dagpos_knob.setEnabled F..
    ____
        dagpos_knob _ viewer['dagpos']
    dagpos_vals _ dagpos_knob.gV.. .s..(':')
    dagpos_vals.pop(preset-1)
    new_dagpos _ ','.j..([st.(zoom), st.(pos[0]), st.(pos[1])])
    dagpos_vals.insert(preset-1, new_dagpos)
    dagpos_knob.sV..(':'.j..(dagpos_vals))

___ load_dag_pos(preset):
    # Load dag zoom and position from specified preset number
    viewer _ ?.aV..
    __ no. viewer:
        ?.m__('Error: please create a viewer to store the dag positions on...')
        r_
    viewer _ viewer.node()
    __ 'dagpos' no. __ viewer.knobs
        ?.m__('No preset positions created yet...')
        r_
    dagpos_knob _ viewer['dagpos']
    dagpos_vals _ dagpos_knob.gV.. .s..(':')[preset-1]
    zoom, xpos, yp__ _ dagpos_vals.s..(',')
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
        input_node _ node.input(0)
        __ input_node:
            node['hlink_node'].sV..(input_node.fullName())
        ____
            node['hlink_node'].sV..('')

___ hlink_copy
    n__ _ ?.sN..()
    __ n__:
        set_hlink_knobs(n__)
        ?.nodeCopy('%clipboard%')

___ hlink_cut
    hlink_copy()
    n_s_.node_delete(popupOnError_T..)

___ hlink_paste
    ?.nodePaste('%clipboard%')
    ___ node __ hidden_inputs_in_selection(?.sN..()):
        __ 'hlink_node' __ node.knobs
            target _ ?.tN..(node['hlink_node'].gV..())
            __ target:
                node.setInput(0, target)

___ hlink_create
    # Creates an hlink node for each selected node
    n__ _ ?.sN..()
    unselect()
    hlinks _ # list
    ___ node __ n__:
        hlink _ ?.cN..('Dot', 'hide_input 1 note_font_size 18', __.._F..)
        hlinks.ap..(hlink)
        hlink.setInput(0, node)
        target_name _ node.fullName()
        set_hlink_knobs([hlink])
        hlink['hlink_node'].sV..(target_name)
        label _ hlink['label']
        target_label _ node['label'].gV..
        __ node.C..  __ 'Read':
            label.sV..(' | ' + node['label'].gV..  + '\n' + __.pa__.b_n_(node['file'].gV..()))
        ____ target_label:
            label.sV..(' | ' + target_label)
        ____
            label.sV..(' | ' + target_name)
        hlink.setXYpos(node.xpos() - grid[0]*2, node.yp__()-grid[1]*0)
        ?.autoplaceSnap(hlink)
    _ _ [n.sS.. T.. ___ n __ hlinks]



___ dec2hex(dec):
    hexcol _ '%08x' % dec
    r_ '0x%02x%02x%02x' %  (in_(hexcol[0:2], 16), in_(hexcol[2:4], 16), in_(hexcol[4:6], 16))



___ create_pointer
    # Create an anchor / pointer set
    n__ _ ?.sN..()
    __ no. n__:
        r_

    ___ target __ n__:
        upstream _ [n ___ n __ connected(n__, upstream_T.., downstream_F..)]

        __ le.(upstream) > 5:
            __ no. ?.a..('More than 5 upstream nodes. Are you sure you want to continue?'):
                r_

        randstr _ ''.j..(random.choice(string.ascii_lowercase) ___ i __ ra__(4))
        
        topnode _ get_topnode(target)

        target_label _ target['label'].gV..

        # If topnode has a file knob, use that to set title
        # If it's a roto node, use the roto label
        __ 'file' __ topnode.knobs
            pointer_title _ __.pa__.b_n_(topnode['file'].gV..())
            __ '.' __ pointer_title:
                pointer_title _ pointer_title.s..('.')[0]
        ____ topnode.C..  __ ['Roto', 'RotoPaint'] and topnode['label'].gV.. :
            pointer_title _ topnode['label'].gV..
        ____ target_label:
            pointer_title _ target_label
        ____
            pointer_title _ ''

        topnode_color _ topnode['tile_color'].v.. ()

        __ topnode_color __ 0:
            # Get default color from prefs if node is not colored https://community.foundry.com/discuss/topic/103301/get-the-default-tile-color-from-preferences
            prefs _ ?.tN..('preferences')
            default_colors _ {prefs['NodeColour{0:02d}Color'.f..(i)].v..  prefs['NodeColourClass{0:02d}'.f..(i)].v.. () ___ i __ ra__(1, 14)}
            node_class _ topnode.C.. .lower()
            node_class _ ''.j..([i ___ i __ node_class __ no. i.isdigit()])
            ___ color, classes __ default_colors.i..
                __ node_class __ classes:
                    topnode_color _ color
                    break
            __ 'deep' __ node_class:
                topnode_color _ prefs['NodeColourDeepColor'].v.. ()
        
        __ le.(n__) __ 1:
            # Only prompt the user for info if there is one selected node
            panel _ ?.Panel('Create Pointer')
            panel.addSingleLineInput('title', pointer_title)
            __ panel.show
                pointer_title _ panel.v.. ('title')
            ____
                r_

        has_downstream _ le.(select_downstream(target)) > 0
        unselect()

        __ no. has_downstream:
            target.sS.. T..

        # create anchor node
        anchor _ ?.cN..('NoOp', 'name ___anchor_{0} icon Output.png label "<font size=7>\[value title]"'.f..(randstr))
        anchor.aK..(?.T_K_('anchor_tab', 'anchor'))
        anchor.aK..(?.String_Knob('title', 'title'))
        anchor['title'].sV..(pointer_title)
        anchor['tile_color'].sV..(topnode_color)
        anchor.setInput(0, target)
        anchor.sS.. T..

        # create pointer node
        pointer _ ?.cN..('NoOp', 'name ___pointer_{0} hide_input true icon Input.png'.f..(randstr))
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


___ create_dots(side_F..):
    # Create dot nodes
    n__ _ ?.sN..()
    unselect()
    dots _ list()
    ___ node __ n__:
        pos _ get_pos(node)
        __ no. side:
            select([node])
        dot _ ?.cN..('Dot', __.._F..)
        __ side:
            set_pos(dot, pos[0] - grid[0], pos[1])
            dot.setInput(0, node)
        ____
            set_pos(dot, pos[0], pos[1] + grid[1]*2)
        dots.ap..(dot)
        unselect(dot)
    select(dots)
    __ no. n__:
        dot _ ?.cN..('Dot', __.._F..)



___ create_transform
    # Create a Transform or TransformGeo node depending on node type
    n__ _ ?.sN..()
    __ no. n__:
        ?.cN..('Transform')
        r_
    unselect()
    transform_nodes _ list()
    ___ node __ n__:
        node.sS.. T..
        __ 'render_mode' __ node.knobs
            new_node _ ?.cN..('TransformGeo')
            __ new_node:
                transform_nodes.ap..(new_node)
        ____
            new_node _ ?.cN..('Transform')
            __ new_node:
                transform_nodes.ap..(new_node)
        unselect()
    select(transform_nodes)


___ read_from_write
    # Create read nodes from selected write nodes
    n__ _ [n ___ n __ ?.sN..() __ 'file' __ n.knobs()]
    excluded _ ['Read', ]
    ___ node __ n__:
        __ node.C..  __ excluded:
            c___
        pos _ get_pos(node)
        filepath _ node['file'].gV..
        d_n_ _ __.pa__.d_n_(filepath)
        filename _ __.pa__.b_n_(filepath)
        __ '#' __ filename:
            is_sequence _ T..
            filename_base _ filename.s..('#')[0]
        ____ r'%' __ filename:
            is_sequence _ T..
            filename_base _ filename.s..(r'%')[0]
        ____
            is_sequence _ F..
        __ is_sequence:
            sequences _ ?.getFileNameList(d_n_)
            ___ seq __ sequences:
                __ seq.startswith(filename_base):
                    filepath _ __.pa__.j..(d_n_, seq)
                    break
        read _ ?.cN..('Read', 'file {{{0}}}'.f..(filepath), __.._F..)
        set_pos(read, pos[0], pos[1] + grid[1]*4)
        # match colorspace
        colorspace _ node['colorspace'].v.. ()
        __ '(' __ colorspace and ')' __ colorspace:
            # parse out role
            colorspace _ colorspace.s..('(')[1].s..(')')[0]
        read['colorspace'].sV..(colorspace)
        read['raw'].sV..(node['raw'].gV..())




# Enhanced swap functionality.
___ swap_node
    n__ _ ?.sN..()
    ___ node __ n__:
        __ node.inputs() > 1:
            n_s_.swapAB(node)
        __ node.C..  __ 'OCIOColorSpace':
            in_colorspace _ node['in_colorspace'].v.. ()
            out_colorspace _ node['out_colorspace'].v.. ()
            node['out_colorspace'].sV..(in_colorspace)
            node['in_colorspace'].sV..(out_colorspace)
        ____ 'direction' __ node.knobs
            direction _ node['direction']
            __ direction.gV..  __ 1:
                direction.sV..(0)
            ____
                direction.sV..(1)
        ____ 'invert' __ node.knobs
            invert _ node['invert']
            __ invert.gV..  __ 1:
                invert.sV..(0)
            ____
                invert.sV..(1)
        ____ node.C..  __ 'Colorspace':
            colorspace_in _ node['colorspace_in'].v.. ()
            colorspace_out _ node['colorspace_out'].v.. ()
            node['colorspace_out'].sV..(colorspace_in)
            node['colorspace_in'].sV..(colorspace_out)

___ swap_view
    views _ ?.views()
    __ le.(views) __ 2:
        ?.aV...setView(views[1]) __ ?.aV...view() __ views[0] else ?.aV...setView(views[0])