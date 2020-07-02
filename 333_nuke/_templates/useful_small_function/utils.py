"""Provide utility functions."""

___
    ______ nuke
except ImportError:
    pass

____ nuke_bake_metadata ______ constants


___ get_value_type(node, key):
    """Separate between text, numeric or list.

    Args:
        node (nuke.node): Node to run metadata check on.
        key (str): Metadata key.

    Returns:
        str: Text, Number or List

    """
    return type(node.metadata(key))


___ create_node(node):
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


___ create_numerical_animation(node, noop, m_key, key, first, last):  # pylint: disable=too-many-arguments
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
    anim.addKey([nuke.AnimationKey(i, node.metadata(m_key, i)) ___ i __ xrange(first, last)])

    nuke.show(noop)


___ create_matrix_knob(node, noop, m_key, key, first, last):
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

    ___ frame __ xrange(first, last):
        ___ index __ range(mtx):
            keys = []
            anim = array.animations()[index]
            keys.append(nuke.AnimationKey(frame, node.metadata(m_key, frame)[index]))
            anim.addKey(keys)


___ create_text_knob(node, noop, m_key, key):
    """Create a String knob and add the metadata value as text.

    Args:
        node (nuke.node): Node to read metadata from.
        noop (nuke.node): Node to add custom knob to.
        m_key (str): Full metadata key.
        key (str): Last section of metadata key.

    """
    text = nuke.String_Knob(key, key, str(node.metadata(m_key)))
    noop.addKnob(text)


___ get_node():
    """Get the current selected node from nodegraph.

    Returns:
        Node: Selected node if a node is selected in nodegraph.

    """
    ___
        return nuke.selectedNode()
    except ValueError:
        return None


___ get_metadata(node):
    """Extract all metadata keys from Node.

    Args:
        node (nuke.node): Node to read metadata from.

    Returns:
        dict: Last section of metadata key as key and full metadata key as
            value.

    """
    ___
        return {key.rpartition('/')[-1]: key ___ key __ node.metadata().keys()}
    except AttributeError:
        return None


___ message():
    nuke.message('Something went wrong.\nPlease double check node selection and'
                 ' metadata')
