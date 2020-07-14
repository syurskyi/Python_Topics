def move_left():
    """
    Move selected nodes to the left by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Left``
    """
    import nuke
    for node in nuke.selectedNodes():
        node['xpos'].setValue(node['xpos'].getValue() -
                              nuke.toNode('preferences')['GridWidth'].value())

def move_right():
    """
    Move selected nodes to the right by 1x the ``GridWidth``

    Shortcut: ``Ctrl+Shift+Right``
    """
    import nuke
    for node in nuke.selectedNodes():
        node['xpos'].setValue(node['xpos'].getValue() +
                              nuke.toNode('preferences')['GridWidth'].value())

def move_up():
    """Move selected nodes up by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Up``
    """
    import nuke
    for node in nuke.selectedNodes():
        node['ypos'].setValue(node['ypos'].getValue() -
                              nuke.toNode('preferences')['GridHeight'].value())

def move_down():
    """Move selected nodes down by 1x the ``GridHeight``

    Shortcut: ``Ctrl+Shift+Down``
    """
    import nuke
    for node in nuke.selectedNodes():
        node['ypos'].setValue(node['ypos'].getValue() +
                              nuke.toNode('preferences')['GridHeight'].value())
