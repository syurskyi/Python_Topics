"""Handle all nodes in the DAG but skip all nodes of specified node classes.

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    skip (list of string): List of node classes to skip processing.

___________________________________________________________________________

Examples:

Standard:
    1) Will disable all nodes.

    mode: disable
    skip: ---

    ------------------------------------------------------------------------

    2) Will delete all Nodes except of Read nodes.

    mode: delete
    skip: Read

Advanced:
    1) Will disable all nodes:

    {
        "mode": "disable"
        "skip": []
    }

    ------------------------------------------------------------------------

    2) Will delete all Nodes except of Read nodes:

    {
        "mode": "delete"
        "skip": [
            "Read"
        ]
    }

"""

# Import third-party modules
import nuke  # pylint: disable=import-error

# Import local modules
from smartRescue.base_steps import NodeStep


class AllNodes(NodeStep):
    """Handle all nodes in the DAG."""

    def process(self):
        """Handle all nodes."""
        self.logger.info("%s all nodes, skip node classes: %s",
                         self.setup["mode"], ", ".join(self.setup["skip"]))
        for node in nuke.allNodes():
            if node.Class() in self.setup["skip"]:
                continue
            self.handle_node(node)
