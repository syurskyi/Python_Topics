import nuke
import nukescripts


"""
This module contains functionality to jump directly to the first/last node
and to connect the viewer with the first/last node
"""


def get_edge_node(which):
    """
    get most top or bottom node
    :param which: String first or last node
    :return: node most top or bottom node
    """

    edge_node = None

    for node in nuke.allNodes():

        if node.Class() != "Viewer":

            if edge_node is None:
                edge_node = node

            if which == "top":
                if node.ypos() < edge_node.ypos():
                    edge_node = node

            if which == "bottom":
                if node.ypos() > edge_node.ypos():
                    edge_node = node

    return edge_node


def view_edge_node(which):
    """
    connect viewer to first/last node
    :param which: String first or last node
    :return: None
    """

    viewer_port = 8
    edge_node = get_edge_node(which)
    sel = nuke.selectedNodes()

    if edge_node is None:
        return

    nukescripts.clear_selection_recursive()
    edge_node.setSelected(True)
    nukescripts.connect_selected_to_viewer(viewer_port)
    edge_node.setSelected(False)

    for node in sel:
        node.setSelected(True)

    for node in nuke.allNodes("Viewer"):
        node.setSelected(False)


def jump_to_edge_node(which):
    """
    jump to most top or most bottom node
    :param which: String first or last node
    :return: None
    """

    edge_node = get_edge_node(which)

    if edge_node is None:
        return

    nuke.zoom(1, [float(edge_node.xpos()), float(edge_node.ypos())])
