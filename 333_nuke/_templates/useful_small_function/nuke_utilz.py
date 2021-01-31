

################################################################################
### _____ Statments ###########################################################

_____ __
_____ re
_____ ?
_____ glob
____ comp_utilz _____ dbinfo
____ comp_utilz _____ decorators

################################################################################
### Functions ##################################################################

# Universal Operations

___ check_selected
    nodes = ?.selectedNodes()
    __ le.(nodes) > 0:
        r_ T.., nodes[0]
    ____
        r_ False, N..

___ clear_selection
    ?.selectAll()
    ?.invertSelection()

___ select_nodes(nodes):
    ___ node __ nodes:
        node['selected'].sV.. T..

___ select_nodes_by_type(node_type):
    select_nodes(get_nodes_by_type(node_type))

___ select_all_nodes
    select_nodes(?.aN..())

___ get_nodes_by_type(node_type):
    r_ ?.aN..(node_type)

___ get_nodes_by_types(node_types=[]):
    nodes = []
    ___ node_type __ node_types:
        nodes.extend(get_nodes_by_type(node_type))
    r_ nodes

___ delete_nodes(nodes):
    ___ node __ nodes:
        ?.delete(node)

___ delete_nodes_by_type(node_type):
    delete_nodes(get_nodes_by_type(node_type))

___ delete_all_nodes
    delete_nodes(?.aN..())

___ is_disabled(node):
    __ type(node) __ str:
        node = ?.toNode(node)
    r_ node['disable'].value()

___ is_multi_view
    __ le.(?.views()) > 1:
        r_ T..

___ get_root_cut
    first_frame = in_(?.toNode('root')['first_frame'].value())
    last_frame = in_(?.toNode('root')['last_frame'].value())
    framerange = '%s-%s' % (first_frame, last_frame)
    exfrange = '%s to %s' % (first_frame, last_frame)
    length = last_frame - first_frame
    r_ first_frame, last_frame, framerange, exfrange, length

# Node Operations

___ get_coordinates(node):
    x = node['xpos'].value()
    y = node['ypos'].value()
    r_ x, y

___ connect_nodes(connect_to, connect_from, from_index):
    connect_to.connectInput(from_index, connect_from)

___ get_value(node, knob):
    r_ node[knob].value()

___ set_value(node, knob, value):
    node[knob].sV..(value)

___ align_node(node, base_x, base_y, x_buffer, y_buffer,
               x_align, y_align, x_mult, y_mult):
    x_shift = x_buffer*x_mult
    y_shift = y_buffer*y_mult
    xpos = in_(base_x+x_shift)+x_align
    yp__ = in_(base_y-y_shift)+y_align

    position(node, xpos, yp__)

___ auto_align_all_nodes
    ___ node __ ?.aN..
        ?.autoplace(node)

___ position(node, x, y):
    node.setXYpos(in_(x), in_(y))

___ batch_node_copypaste(basedir=__.getcwd()):
    _____ tempfile
    tmpNukeFile = tempfile.NamedTemporaryFile(suffix='.nk', dir=basedir)
    nukeFile = tmpNukeFile.name
    ?.nodeCopy(nukeFile)
    clear_selection()
    new_nodes = ?.nodePaste(nukeFile)
    r_ new_nodes

___ copy_root(from_nk, to_nk):
    ___
        ?.scriptSource(from_nk)
        ?.tprint(from_nk)
        knob_settings = ?.toNode('root').writeKnobs(?.TO_VALUE | ?.WRITE_ALL)
        ?.tprint(knob_settings)
        ?.scriptClear()
        ?.scriptSource(to_nk)
        name = ?.toNode('root')['name'].value()
        ?.toNode('root').readKnobs(knob_settings)
        ?.tprint('reseting name')
        ?.toNode('root')['name'].sV..(name)
        ?.tprint(to_nk)
        ?.scriptSaveAs(to_nk, 1)
        r_ T.., N..
    except Exception, e:
        r_ False, e

___ get_parent(node):
    __ type(node) __ str:
        node = ?.toNode(node)
    r_ ?.toNode('root.'+'.'.join(node.fullName().split('.')[:-1])) or ?.r__

# BuildHelper Functions

___ find_upstream(node, class_list):
    '''
    Return the first node upstream that matches a class within
    a list of user-specified classes. Returns None if no match is found

    @param node: The node object from where to start looking upstream
    @param classList: A list of node classes to find a match for
    @return: Node or None.
    '''
    __ node and node.C..  __ class_list:
        r_ node
    ____
        ___ n __ node.dependencies(?.INPUTS | ?.HIDDEN_INPUTS):
            node = find_upstream(n, class_list)
            __ node:
                r_ node

___ get_upstream_value(class_list, inp, knb, exvalue):
    '''
    Return the value of a specific knob name in the first
    node upstream that matches the Classes in class_list.

    Returns exvalue if no match is found
    '''
    ___
        value = find_upstream(?.thisGroup().input(inp), class_list).knob(knb).value()
    ______
        value = exvalue

    r_ value

___ get_parent_value(inp=0, knb=N.., exvalue=50):
    '''
    Returns the value of a specific knob connected to the
    group to a member of that group
    '''
    ___
        value = ?.thisGroup().input(inp).knob(knb).value()
    ______
        value = exvalue

    r_ value

___ get_pv(inp=0, knb=N.., exvalue=50, animchannel=0, holdframe=N..):
    '''
    get the parent of the gizmo/group based on input nr
    the knob the anim channel for example 0 or 1 or 2 for an xyz knob
    if a holdframe is given it will use valueAt rather than value

    usage: getPV(inp=1, knb='translate', exvalue=10,
                    animchannel=1, holdframe=10)
    '''
    ___
        __ holdframe __ N..:
            value = ?.thisGroup().input(inp).knob(knb).value(animchannel)
            r_ value
        value = ?.thisGroup().input(inp).knob(knb).valueAt(holdframe, animchannel)
    except AttributeError:
        value = exvalue

    r_ value

___ find_downstream(node, node_class, name_pattern=N..):
    '''
    Return the first node downstream that matches a class within
    a list of user-specified classes. Returns None if no match is found

    @param node: The node object from where to start looking downstream
    @param class_name: the class name string of a node to match
    @param name_pattern: optional re regex parttern of node name to match
    @return: Node or None.
    '''
    __ node and node.C..  __ node_class:
        __ type(name_pattern) __ str or type(name_pattern) __ type(re.compile('')):
            __ re.compile(name_pattern).match(node.name()):
                r_ node
            ____
                r_ N..
        r_ node
    ____
        ___ n __ node.dependent(?.INPUTS | ?.HIDDEN_INPUTS):
            node = find_downstream(n, node_class, name_pattern=name_pattern)
            __ node:
                r_ node

# Pipeline Task Functions

___ get_parts_and_eye_index_for_basename(stereo_basename):
    parts = stereo_basename.split('.')
    eye_index = [i ___ i, item __ enumerate(parts) __ \
                 re.search('^[l|r]t$', item)]
    __ eye_index and le.(eye_index) __ 1:
        eye_index = eye_index[0]
        r_ parts, eye_index

___ p2p_module_db_eye_fetch
    stereo_through_eye = dbinfo.get_dominant_eye()
    __ no. stereo_through_eye or stereo_through_eye no. __ ['lt', 'rt']:
        ?.m__("Cannot determine dominant eye from database value of:\n\n%s" % str(stereo_through_eye))
        r_
    r_ stereo_through_eye

___ p2p_module_get_current_eye(p2p_node):
    r_ p2p_node.knob('domEyeStatus').value().split()[2]

___ p2p_module_eye_swap(p2p_node):
    cur_dom_eye = p2p_module_get_current_eye(p2p_node)
    __ cur_dom_eye __ 'lt':
        r_ 'rt'
    __ cur_dom_eye __ 'rt':
        r_ 'lt'

___ p2p_module_get_write_name(p2p_node):
    cur_dom_eye = p2p_module_get_current_eye(p2p_node)
    __ cur_dom_eye __ 'lt':
        r_ 'rt_p2p'
    __ cur_dom_eye __ 'rt':
        r_ 'lt_p2p'

___ update_p2p_module(p2p_node, write_name, eye):
    one_view_knob = find_downstream(p2p_node, 'OneView', 'OneView_p2p(\d?)').knob('view')
    dom_eye_status_knob = p2p_node.knob('domEyeStatus')
    write_node = find_downstream(p2p_node, 'Write', write_name+'(\d?)')
    __ eye __ 'lt':
        ?.Undo().begin('Make P2P Dominant Eye lt')
        with p2p_node:
            ?.toNode('eyeSwapMaster').knob('which').sV..(0)
        with ?.root
            one_view_knob.sV..('rt')
            write_node.knob('views').sV..('rt')
            write_node.knob('tile_color').sV..(11401983)
            write_node.knob('heroview').sV..('lt')
            write_node.setName('rt_p2p')
            ?.r__ .knob('hero_view').sV..('lt')
            dom_eye_status_knob.sV..('<font color="Crimson"><b> lt </b></font color>')
        ?.Undo().end()
    __ eye __ 'rt':
        ?.Undo().begin('Make P2P Dominant Eye rt')
        with p2p_node:
            ?.toNode('eyeSwapMaster').knob('which').sV..(1)
        with ?.root
            one_view_knob.sV..('lt')
            write_node.knob('views').sV..('lt')
            write_node.knob('tile_color').sV..(4278190335)
            write_node.knob('heroview').sV..('rt')
            write_node.setName('lt_p2p')
            ?.r__ .knob('hero_view').sV..('rt')
            dom_eye_status_knob.sV..('<font color="DeepSkyBlue"><b> rt </b></font color>')
        ?.Undo().end()

___ p2p_symlinks
    node = ?.tN..
    dest_path = node.knob('file').evaluate()
    source_path = ?.tcl("value [topnode %s].file" % node.name())
    _____ __
    dest_base = __.pa__.b__(dest_path)
    parts, eye_token = get_parts_and_eye_index_for_basename(dest_base)
    __ eye_token:
        base_dir = '.'.join(parts[:eye_token])
        link_path = __.pa__.join(__.environ.get('SHOTDIR'),
                                 __.environ.get('p2ps'), base_dir, dest_base)
    __ no. link_path:
        ?.tprint('***ERROR*** cannot determine path for symlinks')
        r_
    dest_path = link_path
    __ '.rt.' __ dest_path:
        source_path = source_path.replace('.rt.', '.lt.')
        dest_path = dest_path.replace('.rt.', '.lt.')
    elif '.lt.' __ dest_path:
        source_path = source_path.replace('.lt.', '.rt.')
        dest_path = dest_path.replace('.lt.', '.rt.')
    __ no. __.pa__.exists(dest_path):
        __.symlink(source_path, dest_path)
    dest_movie = re.sub('\.[0-9]*\.exr', '.mov', dest_path)
    dest_movie = dest_movie.replace('.SRC.', '.RAW.')
    __ no. __.pa__.exists(dest_movie):
        parts, eye_index = get_parts_and_eye_index_for_basename(source_path)
        __ eye_index:
            eye_index = eye_index + 1
            source_movie = '.'.join(parts[:eye_index])
            source_movie += '.RAW.q98.2k.mov'
            __ __.pa__.exists(source_movie):
                __.symlink(source_movie, dest_movie)

___ set_read_disparity(shot=N.., show=N..):
    ___
        disparity_path = dbinfo.get_disparity(shot, show)
        disparity = re.sub(".[0-9]*-[0-9]*.", ".%d.", disparity_path)
        ?.tN.. .knob('file').sV..(disparity)
    ______
        pass


@decorators.CacheDecorator
___ path_wildcard(input_string):
    """
    Given a full input file path, this function will use glob to expand any wildcards up to the directory and then
    return the entry together with the filename. This can be useful to call in a read node's path knob. The result
    is cached with the CacheDecorator to prevent it from being triggered on every frame.

    :param input_string: file path with wildcard(s)
    :return: path with wildcards expanded to first valid result
    """
    evaluated_string = ?.tcl('set wildcard_results ' + input_string)
    directory = __.pa__.d..(evaluated_string)
    glob_results = glob.glob(directory)

    __ glob_results:
        r_ __.pa__.join(glob_results[0], __.pa__.b__(evaluated_string))
    ____
        r_ evaluated_string

