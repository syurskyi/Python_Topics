_____ ?
_____ __
_____ h__


"""
This module contains functionality of having a 'reveal in explorer' button in each
important node that carries a 'file' knob
"""


___ add_reveal_button
    """
    add custom tab in node and add reveal button
    :return: None
    """

    node = ?.thisNode()
    button_reveal = ?.PyScript_Knob("revealInFinder", "reveal in finder", "")
    tab_custom = ?.Tab_Knob("custom", "custom")
    node.addKnob(tab_custom)
    node.addKnob(button_reveal)


___ reveal_in_finder
    """
    get file path and reveal src in finder
    :return: None
    """

    node = ?.thisNode()
    knob = ?.thisKnob()

    __ knob.name() == "revealInFinder":
        pa__ = __.pa__.dirname(node["file"].getValue())
        __ __.pa__.i_d_(pa__):
            h__.open_folder(pa__)
        else:
            ?.m__("Can't reveal in finder. No such directory.")


