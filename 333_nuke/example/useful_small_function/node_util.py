"""
Define node graph utility functions.
"""

import nuke
import itertools
import subprocess
try:
    from PySide import QtGui
except ImportError:
    from PySide2 import QtGui


def context_aware_create_node(node_2d, node_3d, node_deep):
    # context aware node functions
    nodes = nuke.selectedNodes()
    # try:
    if node_deep and selected_nodes_deep(nodes):
        return nuke.createNode(node_deep)
    elif node_3d and selected_nodes_3d(nodes):
        return nuke.createNode(node_3d)
    elif node_2d:
        return nuke.createNode(node_2d)


def selected_nodes_deep(nodes):
    # Returns true if all selected nodes are Deep nodes
    if not nodes:
        nodes = nuke.selectedNodes()
    for n in nodes:
        try:
            n.deepSampleCount(0, 0)
            return True
        except ValueError:
            return False


def selected_nodes_3d(nodes):
    # Returns true if all selected nodes are 3D nodes
    if not nodes:
        nodes = nuke.selectedNodes()
    for n in nodes:
        try:
            # TODO Need to find better detection method for 3D nodes, this method doesnt include Lights
            n['render_mode'].getValue()
            return True
        except NameError:
            return False


# copies knobs from one node to the other
def copy_knobs():
    if len(nuke.selectedNodes()) == 2:
        for knobs in nuke.selectedNodes()[1].knobs():
            if not str(knobs) in ["name", "xpos", "ypos"]:
                nuke.selectedNodes()[0].knob(knobs).fromScript(nuke.selectedNodes()[1].knob(knobs).toScript())
    else:
        print "please select two nodes: first to copy 'from' second to copy 'to'"


def copy_to_clipboard(value):
    # copy text to clipboard
    QtGui.QApplication.clipboard().setText(value)
    return True


def gui_disable():
    # Toggles the disable knob in any node with the "$gui" switch
    nodes = nuke.selectedNodes()
    for node in nodes:
        k = node.knob('disable')
        gui = '{"\\$gui"}'
        if not k.getValue():
            k.setExpression('$gui')
        elif k.toScript() == gui:
            k.clearAnimated()
            k.setValue(0)


def cycle_viewer_input_masks():
    # Cycle thru masks in VIEWER_INPUT node
    n = nuke.toNode('VIEWER_INPUT')
    if n:
        k = n.knob('mask')
        masks = k.values()
        x = itertools.cycle(masks)
        for dummy in range(len(masks)):
            if k.value() == next(x):
                k.setValue(next(x))


# Copies the tile_color of the first selected node to rest of the selected nodes
def copy_node_tile_color():
    nodes = nuke.selectedNodes()
    tc = int(nodes[len(nodes) - 1].knob('tile_color').getValue())
    for n in range(len(nodes) - 1):
        nodes[n].knob('tile_color').setValue(tc)


def paste_to_selected():
    # paste to all selected nodes
    pasted_nodes = []
    if not nuke.selectedNodes():
        nuke.nodePaste('%clipboard%')
        return
    selection = nuke.selectedNodes()
    for node in selection:
        node['selected'].setValue(False)
    for node in selection:
        node['selected'].setValue(True)
        nuke.nodePaste('%clipboard%')
        nodes = nuke.selectedNodes()
        for node in nodes:
            pasted_nodes.append(node)
    for node in pasted_nodes:
        node['selected'].setValue(True)


def label_dialog():
    # Opens a quick dialog to edit the label of a node
    label = ''
    nodes = nuke.selectedNodes()
    if len(nodes) == 1:
        label = nodes[0].knob('label').getValue()
        name = nodes[0].name()
        txt = nuke.getInput('Change %s label' % name, label)
    else:
        txt = nuke.getInput('Change node labels', label)
    if txt:
        for n in nuke.selectedNodes():
            n['label'].setValue(txt)


def open_frame_in_photoshop():
    # Opens the current frame of the selected Read node in Photoshop
    # TODO extract the photoshop location to the prefs file
    ps_path = "/Applications/Adobe Photoshop CC 2014/Adobe Photoshop CC 2014.app"
    if len(nuke.selectedNodes()) == 1 and nuke.selectedNode().Class() == "Read":
        read = nuke.selectedNode()
        frame_path = read.metadata("input/filename")
        cmd = "open -a \"%s\" \"%s\"" % (ps_path, frame_path)
        subprocess.call(cmd, shell=True)
    else:
        nuke.message("You must have a single Read node selected.")


def match_range_to_read():
    # Sets root frame range to match the frame range of the selected Read node
    if len(nuke.selectedNodes()) == 1 and nuke.selectedNode().Class() == "Read":
        read = nuke.selectedNode()
        nuke.toNode("root")["first_frame"].setValue(read.firstFrame())
        nuke.toNode("root")["last_frame"].setValue(read.lastFrame())
    else:
        nuke.message("You must have a single Read node selected.")


def read_from_write():
    # TODO Refactor a bit to make new nodes snap to grid and make work for DeepWrites as well.
    # TODO Don't need to check for any selectedNodes AND write nodes
    nodes = nuke.selectedNodes()
    if len(nodes) < 1:
        print('No nodes selected')
    else:
        found_writes = False
        write_nodes = []
        for node in nodes:
            if node.Class() == 'Write':
                write_nodes.append(node)
                found_writes = True

        if found_writes:  # we found some writes

            for node in write_nodes:
                node_read = nuke.nodes.Read()  # create a read node
                node_read['file'].setValue(nuke.filename(node))  # set the filename
                if node['use_limit'].getValue() == 1:  # check to see if there is a range and set the values in the read node
                    node_read['first'].setValue(int(node['first'].getValue()))
                    node_read['last'].setValue(int(node['last'].getValue()))
                else:  # no range on the write?  take a stab at using the range from the script value
                    node_read['first'].setValue(int(nuke.root()['first_frame'].getValue()))
                    node_read['last'].setValue(int(nuke.root()['last_frame'].getValue()))
                node_read.setXpos(node.xpos())  # let's set the position
                node_read.setYpos(node.ypos() + 50)
                node_read['premultiplied'].setValue(node['premultiplied'].getValue())  # use premult if checked
                node_read['raw'].setValue(node['raw'].getValue())  # use raw if checked
        else:

            print('No Writes Found in Node Selection')
