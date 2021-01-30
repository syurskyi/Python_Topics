___ move_left
    """
    Move selected nodes to the left by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Left``
    """
    ______ ?
    ___ node __ ?.sN..
        node['xpos'].sV..(node['xpos'].gV..  -
                              ?.tN..('preferences')['GridWidth'].v.. ())

___ move_right
    """
    Move selected nodes to the right by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Right``
    """
    ______ ?
    ___ node __ ?.sN..
        node['xpos'].sV..(node['xpos'].gV..  +
                              ?.tN..('preferences')['GridWidth'].v.. ())

___ move_up
    """Move selected nodes up by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Up``
    """
    ______ ?
    ___ node __ ?.sN..
        node['ypos'].sV..(node['ypos'].gV..  -
                              ?.tN..('preferences')['GridHeight'].v.. ())

___ move_down
    """Move selected nodes down by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Down``
    """
    ______ ?
    ___ node __ ?.sN..
        node['ypos'].sV..(node['ypos'].gV..  +
                              ?.tN..('preferences')['GridHeight'].v.. ())
