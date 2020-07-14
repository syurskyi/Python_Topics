

################################################################################
### Import Statments ###########################################################

import os
import re
import nuke
import glob
from comp_utilz import dbinfo
from comp_utilz import decorators

################################################################################
### Functions ##################################################################

# Universal Operations

def check_selected():
    nodes = nuke.selectedNodes()
    if len(nodes) > 0:
        return True, nodes[0]
    else:
        return False, None

def clear_selection():
    nuke.selectAll()
    nuke.invertSelection()

def select_nodes(nodes):
    for node in nodes:
        node['selected'].setValue(True)

def select_nodes_by_type(node_type):
    select_nodes(get_nodes_by_type(node_type))

def select_all_nodes():
    select_nodes(nuke.allNodes())

def get_nodes_by_type(node_type):
    return nuke.allNodes(node_type)

def get_nodes_by_types(node_types=[]):
    nodes = []
    for node_type in node_types:
        nodes.extend(get_nodes_by_type(node_type))
    return nodes

def delete_nodes(nodes):
    for node in nodes:
        nuke.delete(node)

def delete_nodes_by_type(node_type):
    delete_nodes(get_nodes_by_type(node_type))

def delete_all_nodes():
    delete_nodes(nuke.allNodes())

def is_disabled(node):
    if type(node) == str:
        node = nuke.toNode(node)
    return node['disable'].value()

def is_multi_view():
    if len(nuke.views()) > 1:
        return True

def get_root_cut():
    first_frame = int(nuke.toNode('root')['first_frame'].value())
    last_frame = int(nuke.toNode('root')['last_frame'].value())
    framerange = '%s-%s' % (first_frame, last_frame)
    exfrange = '%s to %s' % (first_frame, last_frame)
    length = last_frame - first_frame
    return first_frame, last_frame, framerange, exfrange, length

# Node Operations

def get_coordinates(node):
    x = node['xpos'].value()
    y = node['ypos'].value()
    return x, y

def connect_nodes(connect_to, connect_from, from_index):
    connect_to.connectInput(from_index, connect_from)

def get_value(node, knob):
    return node[knob].value()

def set_value(node, knob, value):
    node[knob].setValue(value)

def align_node(node, base_x, base_y, x_buffer, y_buffer,
               x_align, y_align, x_mult, y_mult):
    x_shift = x_buffer*x_mult
    y_shift = y_buffer*y_mult
    xpos = int(base_x+x_shift)+x_align
    ypos = int(base_y-y_shift)+y_align

    position(node, xpos, ypos)

def auto_align_all_nodes():
    for node in nuke.allNodes():
        nuke.autoplace(node)

def position(node, x, y):
    node.setXYpos(int(x), int(y))

def batch_node_copypaste(basedir=os.getcwd()):
    import tempfile
    tmpNukeFile = tempfile.NamedTemporaryFile(suffix='.nk', dir=basedir)
    nukeFile = tmpNukeFile.name
    nuke.nodeCopy(nukeFile)
    clear_selection()
    new_nodes = nuke.nodePaste(nukeFile)
    return new_nodes

def copy_root(from_nk, to_nk):
    try:
        nuke.scriptSource(from_nk)
        nuke.tprint(from_nk)
        knob_settings = nuke.toNode('root').writeKnobs(nuke.TO_VALUE | nuke.WRITE_ALL)
        nuke.tprint(knob_settings)
        nuke.scriptClear()
        nuke.scriptSource(to_nk)
        name = nuke.toNode('root')['name'].value()
        nuke.toNode('root').readKnobs(knob_settings)
        nuke.tprint('reseting name')
        nuke.toNode('root')['name'].setValue(name)
        nuke.tprint(to_nk)
        nuke.scriptSaveAs(to_nk, 1)
        return True, None
    except Exception, e:
        return False, e

def get_parent(node):
    if type(node) == str:
        node = nuke.toNode(node)
    return nuke.toNode('root.'+'.'.join(node.fullName().split('.')[:-1])) or nuke.root()

# BuildHelper Functions

def find_upstream(node, class_list):
    '''
    Return the first node upstream that matches a class within
    a list of user-specified classes. Returns None if no match is found

    @param node: The node object from where to start looking upstream
    @param classList: A list of node classes to find a match for
    @return: Node or None.
    '''
    if node and node.Class() in class_list:
        return node
    else:
        for n in node.dependencies(nuke.INPUTS | nuke.HIDDEN_INPUTS):
            node = find_upstream(n, class_list)
            if node:
                return node

def get_upstream_value(class_list, inp, knb, exvalue):
    '''
    Return the value of a specific knob name in the first
    node upstream that matches the Classes in class_list.

    Returns exvalue if no match is found
    '''
    try:
        value = find_upstream(nuke.thisGroup().input(inp), class_list).knob(knb).value()
    except:
        value = exvalue

    return value

def get_parent_value(inp=0, knb=None, exvalue=50):
    '''
    Returns the value of a specific knob connected to the
    group to a member of that group
    '''
    try:
        value = nuke.thisGroup().input(inp).knob(knb).value()
    except:
        value = exvalue

    return value

def get_pv(inp=0, knb=None, exvalue=50, animchannel=0, holdframe=None):
    '''
    get the parent of the gizmo/group based on input nr
    the knob the anim channel for example 0 or 1 or 2 for an xyz knob
    if a holdframe is given it will use valueAt rather than value

    usage: getPV(inp=1, knb='translate', exvalue=10,
                    animchannel=1, holdframe=10)
    '''
    try:
        if holdframe is None:
            value = nuke.thisGroup().input(inp).knob(knb).value(animchannel)
            return value
        value = nuke.thisGroup().input(inp).knob(knb).valueAt(holdframe, animchannel)
    except AttributeError:
        value = exvalue

    return value

def find_downstream(node, node_class, name_pattern=None):
    '''
    Return the first node downstream that matches a class within
    a list of user-specified classes. Returns None if no match is found

    @param node: The node object from where to start looking downstream
    @param class_name: the class name string of a node to match
    @param name_pattern: optional re regex parttern of node name to match
    @return: Node or None.
    '''
    if node and node.Class() == node_class:
        if type(name_pattern) is str or type(name_pattern) is type(re.compile('')):
            if re.compile(name_pattern).match(node.name()):
                return node
            else:
                return None
        return node
    else:
        for n in node.dependent(nuke.INPUTS | nuke.HIDDEN_INPUTS):
            node = find_downstream(n, node_class, name_pattern=name_pattern)
            if node:
                return node

# Pipeline Task Functions

def get_parts_and_eye_index_for_basename(stereo_basename):
    parts = stereo_basename.split('.')
    eye_index = [i for i, item in enumerate(parts) if \
                 re.search('^[l|r]t$', item)]
    if eye_index and len(eye_index) == 1:
        eye_index = eye_index[0]
        return parts, eye_index

def p2p_module_db_eye_fetch():
    stereo_through_eye = dbinfo.get_dominant_eye()
    if not stereo_through_eye or stereo_through_eye not in ['lt', 'rt']:
        nuke.message("Cannot determine dominant eye from database value of:\n\n%s" % str(stereo_through_eye))
        return
    return stereo_through_eye

def p2p_module_get_current_eye(p2p_node):
    return p2p_node.knob('domEyeStatus').value().split()[2]

def p2p_module_eye_swap(p2p_node):
    cur_dom_eye = p2p_module_get_current_eye(p2p_node)
    if cur_dom_eye == 'lt':
        return 'rt'
    if cur_dom_eye == 'rt':
        return 'lt'

def p2p_module_get_write_name(p2p_node):
    cur_dom_eye = p2p_module_get_current_eye(p2p_node)
    if cur_dom_eye == 'lt':
        return 'rt_p2p'
    if cur_dom_eye == 'rt':
        return 'lt_p2p'

def update_p2p_module(p2p_node, write_name, eye):
    one_view_knob = find_downstream(p2p_node, 'OneView', 'OneView_p2p(\d?)').knob('view')
    dom_eye_status_knob = p2p_node.knob('domEyeStatus')
    write_node = find_downstream(p2p_node, 'Write', write_name+'(\d?)')
    if eye == 'lt':
        nuke.Undo().begin('Make P2P Dominant Eye lt')
        with p2p_node:
            nuke.toNode('eyeSwapMaster').knob('which').setValue(0)
        with nuke.root():
            one_view_knob.setValue('rt')
            write_node.knob('views').setValue('rt')
            write_node.knob('tile_color').setValue(11401983)
            write_node.knob('heroview').setValue('lt')
            write_node.setName('rt_p2p')
            nuke.root().knob('hero_view').setValue('lt')
            dom_eye_status_knob.setValue('<font color="Crimson"><b> lt </b></font color>')
        nuke.Undo().end()
    if eye == 'rt':
        nuke.Undo().begin('Make P2P Dominant Eye rt')
        with p2p_node:
            nuke.toNode('eyeSwapMaster').knob('which').setValue(1)
        with nuke.root():
            one_view_knob.setValue('lt')
            write_node.knob('views').setValue('lt')
            write_node.knob('tile_color').setValue(4278190335)
            write_node.knob('heroview').setValue('rt')
            write_node.setName('lt_p2p')
            nuke.root().knob('hero_view').setValue('rt')
            dom_eye_status_knob.setValue('<font color="DeepSkyBlue"><b> rt </b></font color>')
        nuke.Undo().end()

def p2p_symlinks():
    node = nuke.thisNode()
    dest_path = node.knob('file').evaluate()
    source_path = nuke.tcl("value [topnode %s].file" % node.name())
    import os
    dest_base = os.path.basename(dest_path)
    parts, eye_token = get_parts_and_eye_index_for_basename(dest_base)
    if eye_token:
        base_dir = '.'.join(parts[:eye_token])
        link_path = os.path.join(os.environ.get('SHOTDIR'),
                                 os.environ.get('p2ps'), base_dir, dest_base)
    if not link_path:
        nuke.tprint('***ERROR*** cannot determine path for symlinks')
        return
    dest_path = link_path
    if '.rt.' in dest_path:
        source_path = source_path.replace('.rt.', '.lt.')
        dest_path = dest_path.replace('.rt.', '.lt.')
    elif '.lt.' in dest_path:
        source_path = source_path.replace('.lt.', '.rt.')
        dest_path = dest_path.replace('.lt.', '.rt.')
    if not os.path.exists(dest_path):
        os.symlink(source_path, dest_path)
    dest_movie = re.sub('\.[0-9]*\.exr', '.mov', dest_path)
    dest_movie = dest_movie.replace('.SRC.', '.RAW.')
    if not os.path.exists(dest_movie):
        parts, eye_index = get_parts_and_eye_index_for_basename(source_path)
        if eye_index:
            eye_index = eye_index + 1
            source_movie = '.'.join(parts[:eye_index])
            source_movie += '.RAW.q98.2k.mov'
            if os.path.exists(source_movie):
                os.symlink(source_movie, dest_movie)

def set_read_disparity(shot=None, show=None):
    try:
        disparity_path = dbinfo.get_disparity(shot, show)
        disparity = re.sub(".[0-9]*-[0-9]*.", ".%d.", disparity_path)
        nuke.thisNode().knob('file').setValue(disparity)
    except:
        pass


@decorators.CacheDecorator
def path_wildcard(input_string):
    """
    Given a full input file path, this function will use glob to expand any wildcards up to the directory and then
    return the entry together with the filename. This can be useful to call in a read node's path knob. The result
    is cached with the CacheDecorator to prevent it from being triggered on every frame.

    :param input_string: file path with wildcard(s)
    :return: path with wildcards expanded to first valid result
    """
    evaluated_string = nuke.tcl('set wildcard_results ' + input_string)
    directory = os.path.dirname(evaluated_string)
    glob_results = glob.glob(directory)

    if glob_results:
        return os.path.join(glob_results[0], os.path.basename(evaluated_string))
    else:
        return evaluated_string

