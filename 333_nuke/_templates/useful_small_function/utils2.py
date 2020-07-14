"""Utility functions for position, cender and edges of nodes."""

import nuke


def get_center_x(node):
    """Return the horizontal center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        int: Horizontal center of the node.

    """
    return node.xpos() + node.screenWidth() / 2.0


def get_center_y(node):
    """Return the vertical center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        int: Horizontal center of the node.

    """
    return node.ypos() + node.screenHeight() / 2.0


def get_center(node):
    """Return the center of a node.

    Args:
        node (nuke.Node): Node to get center position of.

    Returns:
        :obj:`tuple` of :obj`int`: Center of the node.

    """
    return get_center_x(node), get_center_y(node)


def find_highest(nodes):
    """Find highest node in given nodes

    Args:
        nodes(list of nuke.Node): Nodes to search through for highest node.

    Returns:
        nuke.Node: The highest node in the DAG.

    """
    return min(nodes, key=lambda node: get_center_y(node))


def find_lowest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    return max(nodes, key=lambda node: get_center_y(node))


def find_leftest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    return min(nodes, key=lambda node: get_center_x(node))


def find_rightest(nodes):
    """Find the lowest node in the DAG of given nodes.

    Args:
        nodes (list of nuke.Node): Nodes to get lowest node from.

    Returns:
        nuke.Node: The lowest node.

    """
    return max(nodes, key=lambda node: get_center_x(node))


def get_node_bounds(node):
    """Return the left, top, right and bottom edge of a Node in the DAG.

    Args:
        node (nuke.Node): Node to get bounds of.

    Returns:
        :obj:`tuple` of :obj:`int`: Left, top, right and bottom edge of a Node
            in the DAG.

    """
    node_edge_left = node.xpos()
    node_edge_top = node.ypos()
    if node.Class() == "BackdropNode":
        # The node's screenWidth and screenHeight don't update immediately
        # after a node has been created. To allow to run tests, calculate the
        # right and bottom edge of Backdrop nodes directly from width and
        # height.
        node_edge_right = node_edge_left + node["bdwidth"].value()
        node_edge_bottom = node_edge_top + node["bdheight"].value()
    else:
        node_edge_right = node_edge_left + node.screenWidth()
        node_edge_bottom = node_edge_top + node.screenHeight()
    return node_edge_left, node_edge_top, node_edge_right, node_edge_bottom


def is_inside_backdrops(node, backdrops=None):
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
    if backdrops is None:
        backdrops = nuke.allNodes(filter="BackdropNode")

    node_center_x, node_center_y = get_center(node)

    for backdrop in backdrops:
        edge_left, edge_top, edge_right, edge_bottom = get_node_bounds(
            backdrop
        )
        if (
            edge_left <= node_center_x <= edge_right
            and edge_top <= node_center_y <= edge_bottom
        ):
            return True

    return False


def get_overlapping_backdrops(
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
    if backdrops is None:
        backdrops = nuke.allNodes(filter="BackdropNode")

    position_x, position_y = position

    overlapping_backdrops = set()
    for backdrop in backdrops:
        bd_x, bd_y, bd_r, bd_t = get_node_bounds(backdrop)
        if horizontal:
            if bd_y <= position_y <= bd_t:
                overlapping_backdrops.add(backdrop)
        if vertical:
            if bd_x <= position_x <= bd_r:
                overlapping_backdrops.add(backdrop)

    return overlapping_backdrops


def get_surrounding_backdrops(nodes, backdrops=None):
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
    backdrops = backdrops or nuke.allNodes(filter="BackdropNode")

    surrounding_backdrops = []
    for backdrop in backdrops:
        if any([is_inside_backdrops(node, [backdrop]) for node in nodes]):
            surrounding_backdrops.append(backdrop)

    return surrounding_backdrops


def get_grid_preferences():
    """Return the width and height of the grid set in preferences.

    Returns:
        :obj:`tuple` of :obj:`int`: The grid size in width and height.

    """
    pref_node = nuke.toNode("preferences")
    grid_height = int(pref_node["GridHeight"].value())
    grid_width = int(pref_node["GridWidth"].value())
    return grid_width, grid_height


def get_closest_grid_offset(offset):
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
    return offset_x, offset_y
