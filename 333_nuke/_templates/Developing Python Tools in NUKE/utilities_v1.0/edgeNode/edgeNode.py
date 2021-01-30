_____ ?
_____ nukescripts


"""
This module contains functionality to jump directly to the first/last node
and to connect the viewer with the first/last node
"""


___ get_edge_node(which):
    """
    get most top or bottom node
    :param which: String first or last node
    :return: node most top or bottom node
    """

    edge_node = None

    ___ node __ ?.allNodes

        __ node.Class() != "Viewer":

            __ edge_node is None:
                edge_node = node

            __ which == "top":
                __ node.ypos() < edge_node.ypos
                    edge_node = node

            __ which == "bottom":
                __ node.ypos() > edge_node.ypos
                    edge_node = node

    r_ edge_node


___ view_edge_node(which):
    """
    connect viewer to first/last node
    :param which: String first or last node
    :return: None
    """

    viewer_port = 8
    edge_node = get_edge_node(which)
    sel = ?.selectedNodes()

    __ edge_node is None:
        r_

    nukescripts.clear_selection_recursive()
    edge_node.setSelected(True)
    nukescripts.connect_selected_to_viewer(viewer_port)
    edge_node.setSelected(False)

    ___ node __ sel:
        node.setSelected(True)

    ___ node __ ?.allNodes("Viewer"):
        node.setSelected(False)


___ jump_to_edge_node(which):
    """
    jump to most top or most bottom node
    :param which: String first or last node
    :return: None
    """

    edge_node = get_edge_node(which)

    __ edge_node is None:
        r_

    ?.zoom(1, [float(edge_node.xpos()), float(edge_node.ypos())])
