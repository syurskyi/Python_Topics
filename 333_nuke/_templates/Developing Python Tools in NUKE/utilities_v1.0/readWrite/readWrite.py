_____ ?


"""
This module contains functionality to create a read node from a selected write node
"""


___ create_read_from_write
    """
    create a read node from a selected write node
    :return: None
    """

    sel = ?.selectedNode()

    __ sel.Class() == "Write":
        read = ?.createNode("Read")
        read.setXpos(int(sel["xpos"].getValue()))
        read.setYpos(int(sel["ypos"].getValue()+50))
        read["file"].setValue(sel["file"].getValue())
        read["first"].setValue(int(?.r__ ["first_frame"].getValue()))
        read["last"].setValue(int(?.r__ ["last_frame"].getValue()))
        read["origfirst"].setValue(int(?.r__ ["first_frame"].getValue()))
        read["origlast"].setValue(int(?.r__ ["last_frame"].getValue()))
        read["colorspace"].setValue(int(sel["colorspace"].getValue()))
