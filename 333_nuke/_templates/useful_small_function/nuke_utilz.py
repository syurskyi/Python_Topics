

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
    n__ _ ?.sN..
    __ le.(n__) > 0:
        r_ T.., n__[0]
    ____
        r_ F.., N..

___ clear_selection
    ?.selectAll()
    ?.invertSelection()

___ select_nodes(n__):
    ___ node __ n__:
        node['selected'].sV.. T..

___ select_nodes_by_type(node_type):
    select_nodes(get_nodes_by_type(node_type))

___ select_all_nodes
    select_nodes(?.aN..())

___ get_nodes_by_type(node_type):
    r_ ?.aN..(node_type)

___ get_nodes_by_types(node_types_[]):
    n__ _ []
    ___ node_type __ node_types:
        n__.extend(get_nodes_by_type(node_type))
    r_ n__

___ delete_nodes(n__):
    ___ node __ n__:
        ?.delete(node)

___ delete_nodes_by_type(node_type):
    delete_nodes(get_nodes_by_type(node_type))

___ delete_all_nodes
    delete_nodes(?.aN..())

___ is_disabled(node):
    __ type(node) __ st_:
        node _ ?.tN..(node)
    r_ node['disable'].value()

___ is_multi_view
    __ le.(?.views()) > 1:
        r_ T..

___ get_root_cut
    first_frame _ in_(?.tN..('root')['first_frame'].value())
    last_frame _ in_(?.tN..('root')['last_frame'].value())
    framerange _ '%s-%s' % (first_frame, last_frame)
    exfrange _ '%s to %s' % (first_frame, last_frame)
    length _ last_frame - first_frame
    r_ first_frame, last_frame, framerange, exfrange, length

# Node Operations

___ get_coordinates(node):
    x _ node['xpos'].value()
    y _ node['ypos'].value()
    r_ x, y

___ connect_nodes(connect_to, connect_from, from_index):
    connect_to.cI..(from_index, connect_from)

___ get_value(node, knob):
    r_ node[knob].value()

___ set_value(node, knob, value):
    node[knob].sV..(value)

___ align_node(node, base_x, base_y, x_buffer, y_buffer,
               x_align, y_align, x_mult, y_mult):
    x_shift _ x_buffer*x_mult
    y_shift _ y_buffer*y_mult
    xpos _ in_(base_x+x_shift)+x_align
    yp__ _ in_(base_y-y_shift)+y_align

    position(node, xpos, yp__)

___ auto_align_all_nodes
    ___ node __ ?.aN..
        ?.autoplace(node)

___ position(node, x, y):
    node.setXYpos(in_(x), in_(y))

___ batch_node_copypaste(basedir___.getcwd()):
    _____ tempfile
    tmpNukeFile _ tempfile.NamedTemporaryFile(suffix_'.nk', dir_basedir)
    nukeFile _ tmpNukeFile.name
    ?.nodeCopy(nukeFile)
    clear_selection()
    new_nodes _ ?.nodePaste(nukeFile)
    r_ new_nodes

___ copy_root(from_nk, to_nk):
    ___
        ?.scriptSource(from_nk)
        ?.tprint(from_nk)
        knob_settings _ ?.tN..('root').writeKnobs(?.TO_VALUE | ?.WRITE_ALL)
        ?.tprint(knob_settings)
        ?.scriptClear()
        ?.scriptSource(to_nk)
        name _ ?.tN..('root')['name'].value()
        ?.tN..('root').readKnobs(knob_settings)
        ?.tprint('reseting name')
        ?.tN..('root')['name'].sV..(name)
        ?.tprint(to_nk)
        ?.scriptSaveAs(to_nk, 1)
        r_ T.., N..
    except Exception, e:
        r_ F.., e

___ get_parent(node):
    __ type(node) __ st_:
        node _ ?.tN..(node)
    r_ ?.tN..('root.'+'.'.j..(node.fullName().sp__('.')[:-1])) or ?.r__

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
            node _ find_upstream(n, class_list)
            __ node:
                r_ node

___ get_upstream_value(class_list, inp, knb, exvalue):
    '''
    Return the value of a specific knob name in the first
    node upstream that matches the Classes in class_list.

    Returns exvalue if no match is found
    '''
    ___
        value _ find_upstream(?.thisGroup().input(inp), class_list).knob(knb).value()
    ______
        value _ exvalue

    r_ value

___ get_parent_value(inp_0, knb_N.., exvalue_50):
    '''
    Returns the value of a specific knob connected to the
    group to a member of that group
    '''
    ___
        value _ ?.thisGroup().input(inp).knob(knb).value()
    ______
        value _ exvalue

    r_ value

___ get_pv(inp_0, knb_N.., exvalue_50, animchannel_0, holdframe_N..):
    '''
    get the parent of the gizmo/group based on input nr
    the knob the anim channel for example 0 or 1 or 2 for an xyz knob
    if a holdframe is given it will use valueAt rather than value

    usage: getPV(inp=1, knb='translate', exvalue=10,
                    animchannel=1, holdframe=10)
    '''
    ___
        __ holdframe __ N..:
            value _ ?.thisGroup().input(inp).knob(knb).value(animchannel)
            r_ value
        value _ ?.thisGroup().input(inp).knob(knb).valueAt(holdframe, animchannel)
    except AttributeError:
        value _ exvalue

    r_ value

___ find_downstream(node, node_class, name_pattern_N..):
    '''
    Return the first node downstream that matches a class within
    a list of user-specified classes. Returns None if no match is found

    @param node: The node object from where to start looking downstream
    @param class_name: the class name string of a node to match
    @param name_pattern: optional re regex parttern of node name to match
    @return: Node or None.
    '''
    __ node and node.C..  __ node_class:
        __ type(name_pattern) __ st_ or type(name_pattern) __ type(re.compile('')):
            __ re.compile(name_pattern).match(node.name()):
                r_ node
            ____
                r_ N..
        r_ node
    ____
        ___ n __ node.dependent(?.INPUTS | ?.HIDDEN_INPUTS):
            node _ find_downstream(n, node_class, name_pattern_name_pattern)
            __ node:
                r_ node

# Pipeline Task Functions

___ get_parts_and_eye_index_for_basename(stereo_basename):
    parts _ stereo_basename.sp__('.')
    eye_index _ [i ___ i, item __ enumerate(parts) __ \
                 re.search('^[l|r]t$', item)]
    __ eye_index and le.(eye_index) __ 1:
        eye_index _ eye_index[0]
        r_ parts, eye_index

___ p2p_module_db_eye_fetch
    stereo_through_eye _ dbinfo.get_dominant_eye()
    __ no. stereo_through_eye or stereo_through_eye no. __ ['lt', 'rt']:
        ?.m__("Cannot determine dominant eye from database value of:\n\n%s" % st_(stereo_through_eye))
        r_
    r_ stereo_through_eye

___ p2p_module_get_current_eye(p2p_node):
    r_ p2p_node.knob('domEyeStatus').value().sp__()[2]

___ p2p_module_eye_swap(p2p_node):
    cur_dom_eye _ p2p_module_get_current_eye(p2p_node)
    __ cur_dom_eye __ 'lt':
        r_ 'rt'
    __ cur_dom_eye __ 'rt':
        r_ 'lt'

___ p2p_module_get_write_name(p2p_node):
    cur_dom_eye _ p2p_module_get_current_eye(p2p_node)
    __ cur_dom_eye __ 'lt':
        r_ 'rt_p2p'
    __ cur_dom_eye __ 'rt':
        r_ 'lt_p2p'

___ update_p2p_module(p2p_node, write_name, eye):
    one_view_knob _ find_downstream(p2p_node, 'OneView', 'OneView_p2p(\d?)').knob('view')
    dom_eye_status_knob _ p2p_node.knob('domEyeStatus')
    write_node _ find_downstream(p2p_node, 'Write', write_name+'(\d?)')
    __ eye __ 'lt':
        ?.Undo().begin('Make P2P Dominant Eye lt')
        with p2p_node:
            ?.tN..('eyeSwapMaster').knob('which').sV..(0)
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
            ?.tN..('eyeSwapMaster').knob('which').sV..(1)
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
    node _ ?.tN..
    dest_path _ node.knob('file').e..
    source_path _ ?.tcl("value [topnode %s].file" % node.name())
    _____ __
    dest_base _ __.pa__.b__(dest_path)
    parts, eye_token _ get_parts_and_eye_index_for_basename(dest_base)
    __ eye_token:
        base_dir _ '.'.j..(parts[:eye_token])
        link_path _ __.pa__.j..(__.environ.get('SHOTDIR'),
                                 __.environ.get('p2ps'), base_dir, dest_base)
    __ no. link_path:
        ?.tprint('***ERROR*** cannot determine path for symlinks')
        r_
    dest_path _ link_path
    __ '.rt.' __ dest_path:
        source_path _ source_path.replace('.rt.', '.lt.')
        dest_path _ dest_path.replace('.rt.', '.lt.')
    elif '.lt.' __ dest_path:
        source_path _ source_path.replace('.lt.', '.rt.')
        dest_path _ dest_path.replace('.lt.', '.rt.')
    __ no. __.pa__.e..(dest_path):
        __.symlink(source_path, dest_path)
    dest_movie _ re.sub('\.[0-9]*\.exr', '.mov', dest_path)
    dest_movie _ dest_movie.replace('.SRC.', '.RAW.')
    __ no. __.pa__.e..(dest_movie):
        parts, eye_index _ get_parts_and_eye_index_for_basename(source_path)
        __ eye_index:
            eye_index _ eye_index + 1
            source_movie _ '.'.j..(parts[:eye_index])
            source_movie +_ '.RAW.q98.2k.mov'
            __ __.pa__.e..(source_movie):
                __.symlink(source_movie, dest_movie)

___ set_read_disparity(shot_N.., show_N..):
    ___
        disparity_path _ dbinfo.get_disparity(shot, show)
        disparity _ re.sub(".[0-9]*-[0-9]*.", ".%d.", disparity_path)
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
    evaluated_string _ ?.tcl('set wildcard_results ' + input_string)
    directory _ __.pa__.d..(evaluated_string)
    glob_results _ glob.glob(directory)

    __ glob_results:
        r_ __.pa__.j..(glob_results[0], __.pa__.b__(evaluated_string))
    ____
        r_ evaluated_string

