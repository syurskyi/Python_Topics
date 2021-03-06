"""Handle all nodes of the configured node classes in the DAG.

This processes recursively, meaning we include also all nodes being nested
inside Group nodes.

Keep in mind that some node classes are versioned inside Nuke, e.g. Merge2,
Camera2, Tracker4, etc. If in doubt about the node class, create a node and
press 'I' to show the node info window. In this window you can also see the
node class of the selected node.

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    node_classes (list of str): Node classes to include handle.

___________________________________________________________________________

Examples:

Standard:
    1) This will delete all Viewer nodes:

    mode: delete
    node classes: Viewer

    ------------------------------------------------------------------------

    2) This will disable all 'Reformat' and 'Write' nodes in the DAG:

    mode: disable
    node classes:
        Reformat
        Write

    3) This will disconnect all 'Defocus' nodes from the stream.

    mode: disconnect
    node classes:
        Defocus

Advanced:
    1) This will delete all Viewer nodes:

    {
        "mode": "delete",
        "node_classes": [
          "Viewer"
        ]
    }

    ---------------------------------------------------------------------------

    2) This will disable all 'Reformat' and 'Write' nodes in the DAG:

    {
        "mode": "disable",
        "node_classes": [
          "Reformat",
          "Write"
        ]
    }

    ---------------------------------------------------------------------------

    3) This will disconnect all 'Defocus' nodes from the stream.

    {
        "mode": "disconnect",
        "node_classes": [
          "Defocus"
        ]
    }

"""

# Import third-party modules
import nuke  # pylint: disable=import-error

# Import local modules
from smartRescue.base_steps import NodeStep


class NodesByClass(NodeStep):
    """Handle all nodes of the configured node classes in the DAG."""

    def process(self):
        """Handle all nodes of the listed node classes."""
        for node_class in self.setup["node_classes"]:
            for node in nuke.allNodes(recurseGroups=True):
                class_name = node.Class()
                if class_name != node_class:
                    continue

                self.logger.info("%s '%s' because its node class (%s) is "
                                 "included in %s", self.setup["mode"],
                                 node.name(), class_name,
                                 self.setup["node_classes"])

                self.handle_node(node)
