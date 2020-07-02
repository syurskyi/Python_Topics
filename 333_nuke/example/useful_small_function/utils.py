"""Provide utility functions."""

try:
    import nuke
except ImportError:
    pass

from nuke_bake_metadata import constants


def get_value_type(node, key):
    """Separate between text, numeric or list.

    Args:
        node (nuke.node): Node to run metadata check on.
        key (str): Metadata key.

    Returns:
        str: Text, Number or List

    """
    return type(node.metadata(key))


def create_node(node):
    """Create a NoOp node with specific color, position and label.

    Args:
        node (nuke.node): Node to place next to.

    Returns:
        Node: NoOp Node.

    """
    lab = 'baked metadata\nfrom {}'.format(node.name())
    noop = nuke.nodes.NoOp(hide_input=True,
                           xpos=node.xpos() + 100,
                           ypos=node.ypos(),
                           tile_color=constants.COLORS['noop'],
                           label=lab)
    return noop


def create_numerical_animation(node, noop, m_key, key, first, last):  # pylint: disable=too-many-arguments
    """Create a custom knob and add animation to it.

    Args:
        node (nuke.node): Node to read metadata from.
        noop (nuke.node): Node to add custom knob to.
        m_key (str): Full metadata key.
        key (str): Last section of metadata key.
        first (int): Frame number when animation should start.
        last (int): Frame number when animation should stop.

    """
    animation = nuke.Double_Knob(key)
    noop.addKnob(animation)
    animation.setAnimated()
    anim = animation.animations()[0]
    anim.addKey([nuke.AnimationKey(i, node.metadata(m_key, i)) for i in xrange(first, last)])

    nuke.show(noop)


def create_matrix_knob(node, noop, m_key, key, first, last):
    """Create a one dimensional Matrix based on the length of metadata.

    Args:
        node (nuke.node): Node to read metadata from.
        noop (nuke.node): Node to add custom knob to.
        m_key (str): Full metadata key.
        key (str): Last section of metadata key.
        first (int): Frame number when animation should start.
        last (int): Frame number when animation should stop.

    """
    mtx = len(node.metadata(m_key))
    array = nuke.IArray_Knob(key.replace(':', '_'), key, [mtx, 1])
    noop.addKnob(array)
    array.setAnimated()

    for frame in xrange(first, last):
        for index in range(mtx):
            keys = []
            anim = array.animations()[index]
            keys.append(nuke.AnimationKey(frame, node.metadata(m_key, frame)[index]))
            anim.addKey(keys)


def create_text_knob(node, noop, m_key, key):
    """Create a String knob and add the metadata value as text.

    Args:
        node (nuke.node): Node to read metadata from.
        noop (nuke.node): Node to add custom knob to.
        m_key (str): Full metadata key.
        key (str): Last section of metadata key.

    """
    text = nuke.String_Knob(key, key, str(node.metadata(m_key)))
    noop.addKnob(text)


def get_node():
    """Get the current selected node from nodegraph.

    Returns:
        Node: Selected node if a node is selected in nodegraph.

    """
    try:
        return nuke.selectedNode()
    except ValueError:
        return None


def get_metadata(node):
    """Extract all metadata keys from Node.

    Args:
        node (nuke.node): Node to read metadata from.

    Returns:
        dict: Last section of metadata key as key and full metadata key as
            value.

    """
    try:
        return {key.rpartition('/')[-1]: key for key in node.metadata().keys()}
    except AttributeError:
        return None


def message():
    nuke.message('Something went wrong.\nPlease double check node selection and'
                 ' metadata')
