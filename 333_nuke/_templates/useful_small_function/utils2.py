"""Utility functions for position, cender and edges of nodes."""

______ ?


___ get_center_x(node):
    """Return the horizontal center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        int: Horizontal center of the node.

    """
    r_ node.xpos() + node.screenWidth() / 2.0


___ get_center_y(node):
    """Return the vertical center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        int: Horizontal center of the node.

    """
    r_ node.ypos() + node.screenHeight() / 2.0


___ get_center(node):
    """Return the center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        :obj:`tuple` of :obj`int`: Center of the node.

    """
    r_ get_center_x(node), get_center_y(node)


___ find_highest(nodes):
    """Find highest node in given nodes

    Args:
        nodes(list of nuke.Node): Nodes to search through for highest node.

    Returns:
        nuke.Node: The highest node in the DAG.

    """
    r_ min(nodes, key=l___ node: get_center_y(node))


___ find_lowest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    r_ max(nodes, key=l___ node: get_center_y(node))


___ find_leftest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    r_ min(nodes, key=l___ node: get_center_x(node))


___ find_rightest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    r_ max(nodes, key=l___ node: get_center_x(node))


___ get_node_bounds(node):
    """Return the left, top, right and bottom edge of a Node in the DAG.

    Args:
        node (nuke.Node): Node to get bounds of.

    Returns:
        :obj:`tuple` of :obj:`int`: Left, top, right and bottom edge of a Node
            in the DAG.

    """
    node_edge_left = node.xpos()
    node_edge_top = node.ypos()
    __ node.Class() __ "BackdropNode":
        # The node's screenWidth and screenHeight don't update immediately
        # after a node has been created. To allow to run tests, calculate the
        # right and bottom edge of Backdrop nodes directly from width and
        # height.
        node_edge_right = node_edge_left + node["bdwidth"].v.. ()
        node_edge_bottom = node_edge_top + node["bdheight"].v.. ()
    ____
        node_edge_right = node_edge_left + node.screenWidth()
        node_edge_bottom = node_edge_top + node.screenHeight()
    r_ node_edge_left, node_edge_top, node_edge_right, node_edge_bottom


___ is_inside_backdrops(node, backdrops=None):
    """Whether given node is inside given Backdrop nodes.

    Args:
        node (nuke.Node): Node to check if it is inside a BackdropNode.
        backdrops (:obj:`list` of :obj:`nuke.BackdropNode`, optional): Backdrop
            nodes that may surround given node.  An empty list is considered a
            selection. If None, all Backdrop nodes will be considered.

    Returns:
        bool: True if the node is surrounded by a BackdropNode.

    """
    # Keep an empty list.
    __ backdrops is None:
        backdrops = ?.allNodes(filter="BackdropNode")

    node_center_x, node_center_y = get_center(node)

    ___ backdrop __ backdrops:
        edge_left, edge_top, edge_right, edge_bottom = get_node_bounds(
            backdrop
        )
        __ (
            edge_left <= node_center_x <= edge_right
            and edge_top <= node_center_y <= edge_bottom
        ):
            r_ True

    r_ False


___ get_overlapping_backdrops(
    position, backdrops=None, horizontal=True, vertical=False
):
    """Find backdrops overlapping with given ypos in DAG.

    Notes:
        The result will include backdrops surrounding

    Args:
        position (:obj:`tuple` of :obj:`int`): x and y position in DAG.
        backdrops (list): Nodes to check if they overlap with given position.
            If None is given, all nodes will be checked against. If an empty
            list is given, return False.
        horizontal (bool, optional): If True, find backdrops overlapping
            horizontally.
        vertical (bool, optional): If True, find backdrops overlapping
            vertically.

    Returns:
        set: Overlapping backdrop nodes.

    """
    # Keep an empty list.
    __ backdrops is None:
        backdrops = ?.allNodes(filter="BackdropNode")

    position_x, position_y = position

    overlapping_backdrops = set()
    ___ backdrop __ backdrops:
        bd_x, bd_y, bd_r, bd_t = get_node_bounds(backdrop)
        __ horizontal:
            __ bd_y <= position_y <= bd_t:
                overlapping_backdrops.add(backdrop)
        __ vertical:
            __ bd_x <= position_x <= bd_r:
                overlapping_backdrops.add(backdrop)

    r_ overlapping_backdrops


___ get_surrounding_backdrops(nodes, backdrops=None):
    """Get all BackdropNodes surrounding given nodes.

    Args:
        nodes (:obj:`list` of :obj:`nuke.Node`): Nodes to get surrounding
            BackdropNodes of.
        backdrops (:obj:`list` of :obj:`nuke.BackdropNode`, optional): Backdrop
            nodes that might surround given node.

    Returns:
        :obj:`list` of :obj:`nuke.BackdropNode`: BackdropNodes that surround
            given nodes.

    """
    backdrops = backdrops or ?.allNodes(filter="BackdropNode")

    surrounding_backdrops = # list
    ___ backdrop __ backdrops:
        __ any([is_inside_backdrops(node, [backdrop]) ___ node __ nodes]):
            surrounding_backdrops.ap..(backdrop)

    r_ surrounding_backdrops


___ get_grid_preferences():
    """Return the width and height of the grid set in preferences.

    Returns:
        :obj:`tuple` of :obj:`int`: The grid size in width and height.

    """
    pref_node = ?.tN..("preferences")
    grid_height = int(pref_node["GridHeight"].v.. ())
    grid_width = int(pref_node["GridWidth"].v.. ())
    r_ grid_width, grid_height


___ get_closest_grid_offset(offset):
    """Return the closest product of the grid setting.

    Args:
        offset (:obj:`tuple` of :obj:`int`): Offset in x and y direction.

    Returns:
        :obj:`tuple` of :obj:`int`: The width and height snapped to grid.

    """
    grid_width, grid_height = get_grid_preferences()
    # Set offset to closest on DAG grid.
    offset_x = int(round(float(offset[0]) / grid_width)) * grid_width
    offset_y = int(round(float(offset[1]) / grid_height)) * grid_height
    r_ offset_x, offset_y
