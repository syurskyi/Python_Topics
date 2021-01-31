# --------------------------------------------------------------
#  paste_selected.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Pastes previous-copied node to all the selected nodes.
# --------------------------------------------------------------

import nuke

def paste_selected():

    for i in nuke.sN.. :
        i.setSelected(True)
        nuke.nodePaste("%clipboard%")
