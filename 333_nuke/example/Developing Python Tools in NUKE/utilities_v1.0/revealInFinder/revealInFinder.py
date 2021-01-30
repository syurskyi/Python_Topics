import nuke
import os
import helper


"""
This module contains functionality of having a 'reveal in explorer' button in each
important node that carries a 'file' knob
"""


def add_reveal_button():
    """
    add custom tab in node and add reveal button
    :return: None
    """

    node = nuke.thisNode()
    button_reveal = nuke.PyScript_Knob("revealInFinder", "reveal in finder", "")
    tab_custom = nuke.Tab_Knob("custom", "custom")
    node.addKnob(tab_custom)
    node.addKnob(button_reveal)


def reveal_in_finder():
    """
    get file path and reveal src in finder
    :return: None
    """

    node = nuke.thisNode()
    knob = nuke.thisKnob()

    if knob.name() == "revealInFinder":
        path = os.path.dirname(node["file"].getValue())
        if os.path.isdir(path):
            helper.open_folder(path)
        else:
            nuke.message("Can't reveal in finder. No such directory.")


