___ move_left():
    """
    Move selected nodes to the left by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Left``
    """
    ______ ?
    ___ node in ?.sN..():
        node['xpos'].setValue(node['xpos'].getValue() -
                              ?.tN..('preferences')['GridWidth'].value())

___ move_right():
    """
    Move selected nodes to the right by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Right``
    """
    ______ ?
    ___ node in ?.sN..():
        node['xpos'].setValue(node['xpos'].getValue() +
                              ?.tN..('preferences')['GridWidth'].value())

___ move_up():
    """Move selected nodes up by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Up``
    """
    ______ ?
    ___ node in ?.sN..():
        node['ypos'].setValue(node['ypos'].getValue() -
                              ?.tN..('preferences')['GridHeight'].value())

___ move_down():
    """Move selected nodes down by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Down``
    """
    ______ ?
    ___ node in ?.sN..():
        node['ypos'].setValue(node['ypos'].getValue() +
                              ?.tN..('preferences')['GridHeight'].value())
