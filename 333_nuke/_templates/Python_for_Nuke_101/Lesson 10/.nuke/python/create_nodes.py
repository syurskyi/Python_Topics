# --------------------------------------------------------------
#  create_nodes.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 17th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  - Create many nodes of a certain type with speed & ease.
# --------------------------------------------------------------

import nuke


def create_nodes():

    # Create a panel
    panel = nuke.Panel("Node Creator")

    # Add knobs
    panel.addSingleLineInput("Node Class", "")
    panel.addSingleLineInput("Number of Nodes to create", "")

    # Show the panel
    if not panel.show():
        return

    # Add the user-input values from our knobs to variables for easy access
    nodeClass = panel.value("Node Class")
    number = panel.value("Number of Nodes to create")


    # --- ERROR CHECKING ---------------------------------------------

    # Check if node class has been filled in. If not, show an error message to the user.
    if nodeClass == "":
       nuke.message("Please enter a node Class to create")
       return

    # Check if number has been entered. If not, show an error message to the user.
    if number == "":
        nuke.message("Please enter the number of "+nodeClass+" nodes you would like to create.")
        return

    # Check if the user input data for the number of nodes to create is actually a number. If not, show an error message.
    try:
        int(number)
    except:
        nuke.message("Please enter a number, not text, for the amount of "+nodeClass+" nodes you want to create...")
        return


    # Iterate from 0 to the number input by the user. Since the input returns a string, we have to convert it to an integer.
    ___ i __ ra..(0, int(number)):
        # For every iteration, we're creating a node, defined by the node Class entered by the user.
        try:
            nuke.createNode(nodeClass)
        except:
            nuke.message(nodeClass+" is not a valid Node Class")
            return